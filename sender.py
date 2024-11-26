import socket

import numpy as np
import pyaudio
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Параметры AES
key = b"uJg7J\xc4\xb2z\x1dF\xdd%E'\x8fR"
iv = b"\xa2\x88\xfd\xd4\xea\x92\xc5L\xf8B\x17\x1cE\xa3\x93\x17"

# Настройки для захвата и передачи аудио
RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1

# Создаем объект шифрования AES
cipher = AES.new(key, AES.MODE_CBC, iv)

# Настройка сокета
server_ip = "127.0.0.1"
server_port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Настройка микрофона
p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

print("Start speaking...")

while True:
    # Чтение аудио с микрофона
    audio_data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)

    # Шифрование
    encrypted_data = cipher.encrypt(pad(audio_data.tobytes(), AES.block_size))

    # Отправка зашифрованных данных
    sock.sendto(encrypted_data, (server_ip, server_port))
