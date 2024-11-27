import hashlib, asyncio, random, jwt, os

secretkey = 1 #os.getenv('SEC_TOKEN')

async def text_to_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def generatetoken(userid):
    payload = {'userid': userid}
    token = jwt.encode(payload, secretkey, algorithm='HS256')
                       
    return token