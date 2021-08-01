import JWT
import base64
from playsound import playsound
import os

fileDirectory = "demo.jpeg"
mysecret = "mysecret"

def encodeFile(dir,secret):
    file =  open(dir,'rb').read()
    encoded = str(base64.encodestring(file))
    encoded = (encoded[2:] + encoded[:-1]).replace("\\n",'')

    arr = dir.split(".")
    extension = arr[-1]
    del arr[-1]

    _dir = ""
    for i in arr:
        _dir += i 
        if i != arr[-1]:
            _dir += "."
    
    _dir += ".secret"

    token = JWT.encode(encoded,secret,extension)

    if token:
        fileOutput = open(_dir,"w+")
        fileOutput.write(str(token))
        fileOutput.close()
    os.remove(dir)

def decodeFile(dir,secret):
    file = open(dir,"rb").read()
    payload = JWT.decode(file,secret)

    if payload["response"] == "ok":
        extension = payload["extension"]
        encoded = payload["encoded"]
        arr = dir.split(".")
        del arr[-1]
    
        _dir = ""
        for i in arr:
            _dir += i 
            if i != arr[-1]:
                _dir += "."
        
        _dir += "."+extension

        fileOutput = open(_dir,"wb")
        encoded = bytes(encoded,"utf-8")
        decoded = base64.decodestring(encoded)
        fileOutput.write(decoded)
        fileOutput.close()

        os.remove(dir)
        return True
    else:
        return False

#encodeFile("demo.jpg",mysecret)
#decodeFile("demo.secret",mysecret)
