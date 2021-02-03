from models.seguranca import SegurancaModel, SegurancaQuery
from itsdangerous import URLSafeSerializer
from flask import g
import json


class Seguranca():
    """def __init__(self):
        self.auth_s = URLSafeSerializer("Chave Secret@ Grupo Forvs", "auth")"""


    def check(self, token):
        #from itsdangerous import URLSafeSerializer
        import base64
        from flask import jsonify

        try:
            print(token)
            #auth_s = URLSafeSerializer("Chave Secret@ Grupo Forvs", "auth")
            #token1 = auth_s.dumps({"id": 5, "name": "itsdangerous"})

            # https://www.base64encode.org/
        
            base64_bytes                = token.encode('ascii')
            message_bytes               = base64.b64decode(base64_bytes)
            message                     = message_bytes.decode('ascii')

            #print('resources seguranca check 1 ', message)
            res                         = json.loads(message)

            print('resources seguranca check 2 ', res)
            g.global_cdempresa          = res['cd_empresa']
            g.global_cdfilial           = res['cd_filial']
            g.apiintegracao             = res['apiintegracao']
            g.apiintegracao_cfg_receb   = res['apiintegracao_cfg_receb']
            g.apiintegracao_cfg_envia   = res['apiintegracao_cfg_envia']

            # METODO TESTE SQL, NÃO COMITA, E FAZ ROLLBACK ('S','N')
            g.global_sql_test         = 'N'

            # INICIALIZA AVISO GLOBAL DE EMAIL
            g.dados_email = []
            """res = auth_s.loads(token)
            print('Resource - Segurança 1: ', token)
            print('Resource - Segurança 2: ', res)
            print('Resource - Segurança 3: ', res['nome'])

            g.global_cdempresa = res['cd_empresa']
            g.global_cdfilial = res['cd_filial']

            print('global_cdempresa: ', g.global_cdempresa)"""

            if res:
                print('res if ', res)

                
                sm = SegurancaQuery()
                result = sm.getParametros(res['apiintegracao'], res['apiintegracao_cfg_receb'], res['cd_empresa'], res['cd_filial'])
                print('result', result)
                return result

        except Exception as e:
            print('Segurança Exception 1')
            # Just print(e) is cleaner and more likely what you want,
            # but if you insist on printing message specifically whenever possible...
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
        except:
            print('Segurança Erro')
            return False
        else:
            print('Segurança Sucesso')
            return True

