import jwt

def encode(encodedFile,secret,extension):
    try:
        payload = {
            'encoded': str(encodedFile),
            'extension': extension
        }
        return jwt.encode(
            payload,
            secret,
            algorithm='HS256'
        )
    except Exception as e:
        print(e)
        return False


def decode(encodedFile,secret):
    try:
        payload = jwt.decode(encodedFile, secret,algorithms="HS256")
        return {
            "response":"ok",
            "encoded":payload["encoded"],
            "extension":payload["extension"]
            }
    except jwt.ExpiredSignatureError:
        return {
            "response":"err",
            "value":"Signature expired."
            }
    except jwt.InvalidTokenError:
        return {
            "response":"err",
            "value":"Invalid Token."
            }