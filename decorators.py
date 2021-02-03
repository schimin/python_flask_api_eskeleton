from flask import Flask, Response, request, abort
from functools import wraps
from resources.seguranca import Seguranca
import messages

def check_token(f):
    """ DECORATOR PARA VERIFICAR SE TOKEN É VALIDO E SE ESTÁ REGISTRADO NO ERP."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401, description=messages.MSG_ERRO_AUTHORIZATION)
        headers = request.headers
        sm = Seguranca()
        res = sm.check(headers['Authorization'])
        print("decorator: ", res)
        if not res:
            print('erro check token ')
            abort(403, description=messages.MSG_ERRO_TOKEN)
        return f(*args, **kwargs)
    return wrapper
