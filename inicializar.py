from datetime import datetime
from rfid import read_rfid
import json

vAgora = datetime.now()
vSegundos = vAgora.strftime('%S')
vUltaDataHora = datetime.now()

with open('configuracao.json', 'r') as f:
    data = json.loads(str(f.read()).strip("'<>() ").replace('\'', '\"')) 

if data!="":
    vPorta = data['rfid']['porta']
    vVelocidade = data['rfid']['velocidade']
    vArquivoSaida = data['rfid']['ArquivoSaida']

while True:
    try:
        vAgora = datetime.now()
        #--------------------------------------------------------------------------------
        if (vSegundos != vAgora.strftime('%S')):
            #atualizada data e hora
            vSegundos = vAgora.strftime('%S')

            #Aguarda RFID   
            VCartao = read_rfid(porta=vPorta, velocidade=vVelocidade)
            print(VCartao)
            #--------------------------------------------------------------------------------
            #Gravar arquivo de saída
            with open(vArquivoSaida, 'r') as f:
                vSaidasCB = json.loads(str(f.read()).strip("'<>() ").replace('\'', '\"')) 

            vSaidasCB["rfid"]["ultimocartao"] = VCartao


            #Trata passagem de cartão repetidas vezes
            vDiffSeg = datetime.now()-vUltaDataHora
            vUltaDataHora = datetime.now()

            print (vDiffSeg.seconds)
            #Verifica se o de agora for diferente do ativo e tiver mais de 2 segundos ativa cartão
            if VCartao != vSaidasCB["rfid"]["cartaoativo"] and VCartao!=0 and vDiffSeg.seconds > 2:
                vSaidasCB["rfid"]["cartaoativo"] = VCartao

            with open(vArquivoSaida, 'w') as json_file:
                json.dump(vSaidasCB, json_file)
    except:
        print("erro RFID " + vAgora.strftime('%H:%M:%S'))