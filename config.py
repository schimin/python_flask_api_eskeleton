from datetime import timedelta
import socket
import os


# HABILITA MOSTRAR MAIS DE UMA LINHA DE ERRO DE RESPOSTA DA API
BUNDLE_ERRORS = True

""" CONFIGURAÇÕES DE ENVIROMENT """
# 'development' ou 'production', 'test'
ENVIRONMENT = os.getenv('FLASK_ENV')
if not ENVIRONMENT:
    ENVIRONMENT = 'development'

if ENVIRONMENT == 'development':
    TESTING = True
    DEBUG = True
    ENV = 'development'
    SERVER_NAME = 'localhost:6060'
    print('Ambiente de Desenvolvimento', SERVER_NAME)

if ENVIRONMENT == 'production':
    TESTING = False
    DEBUG = False
    ENV = 'production'
    SERVER_NAME = 'ip:porta'
    print('Ambiente de Produção', SERVER_NAME)

if ENVIRONMENT == 'testing':
    TESTING = True
    DEBUG = False
    ENV = 'testing'
    SERVER_NAME = 'ip:porta'
    print('Ambiente de Teste', SERVER_NAME)


print('ENV', ENV)
