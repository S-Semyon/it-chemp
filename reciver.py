import socket

import numpy as np
import pyaudio
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Параметры AES
key = b"uJg7J\xc4\xb2z\x1dF\xdd%E'\x8fR"
iv = b"\xa2\x88\xfd\xd4\xea\x92\xc5L\xf8B\x17\x1cE\xa3\x93\x17"

# Настройки для захвата и воспроизведения аудио
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
sock.bind((server_ip, server_port))

# Настройка воспроизведения
p = pyaudio.PyAudio()
stream_out = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK
)

print("Waiting for audio data...")

while True:
    # Получаем зашифрованные данные
    encrypted_data, addr = sock.recvfrom(2048)

    try:
        # Сначала расшифровываем данные, затем удаляем паддинг
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Преобразование в аудиоформат и воспроизведение
        audio_data = np.frombuffer(decrypted_data, dtype=np.int16)
        stream_out.write(audio_data.tobytes())

    except ValueError as e:
        print(f"Ошибка при расшифровке: {e}")
