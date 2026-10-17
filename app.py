import jwt
def read(token):
    return jwt.decode(token, algorithms=["none"])
