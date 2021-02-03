# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

jwt = JWTManager(app)

# LISTA DE RESOURCES
api.add_resource(Order, '/v1/order')
api.add_resource(Pessoa, '/v1/pessoa', '/v1/pessoa/<cnpj_cpf>')
api.add_resource(PedidoVenda, '/v1/pedidovenda', '/v1/pedidovenda/<int:cd_pedidovenda>')
api.add_resource(OrdemFaturamento, '/v1/ordemfaturamento', '/v1/ordemfaturamento/<int:cd_pedidovenda>')

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

#EXCESSOES DE TOKEN E MENSAGENS
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired.',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'The token has been revoked.',
        'error': 'token_revoked'

    }), 401


if __name__ == '__main__': 
    app.run(host='0.0.0.0')
