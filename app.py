# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

# LISTA DE RESOURCES
api.add_resource(Order, '/v1/order')
api.add_resource(Pessoa, '/v1/pessoa', '/v1/pessoa/<cnpj_cpf>')
api.add_resource(PedidoVenda, '/v1/pedidovenda', '/v1/pedidovenda/<int:cd_pedidovenda>')
api.add_resource(OrdemFaturamento, '/v1/ordemfaturamento', '/v1/ordemfaturamento/<int:cd_pedidovenda>')

if __name__ == '__main__': 
    app.run(host='0.0.0.0')
