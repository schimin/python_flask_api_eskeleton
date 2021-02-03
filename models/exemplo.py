from flask_restful import Resource, request
from decorators import check_token
import messages
import helper
from flask import g

class Pessoa(Resource):
    @check_token
    def __init__(self):
        self.dados = request.json

    @check_token
    def get(self, cnpj_cpf):
      pass
