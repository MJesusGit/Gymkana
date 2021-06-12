#!/usr/bin/python3
#-*-coding: utf-8; mode:python-*-

import socket
import hashlib
import struct
import base64
import threading
import urllib
import sys

#Maria Jesús Dueñas Recuero.
def main():
    code0=yimkana0() 
    code1=yimkana1(code0)
    code2=yimkana2(code1)
    code3=yimkana3(code2)
    code4=yimkana4(code3)
    code5=yimkana5(code4)
  

def yimkana0():
    address=('node1',2000)
    sock_0=socket.socket()
    sock_0.connect(address)
    print(sock_0.recv(1024).decode()) 

    sock_0.send('mjesus.duenas1'.encode())

    code1=(sock_0.recv(36).decode())
    print(code1)
    print(sock_0.recv(1024).decode())
    sock_0.close()

    return code1

def yimkana1(code0):
    dest=('node1',3000)
    address=('',57276)
    
    sock_1_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    
    sock_1_server.bind(address)
    sock_1_server.sendto(f'57276  {code0}'.encode(),dest)
    
    identifier=''
    solution1=(sock_1_server.recv(1024).decode())
    for n in range (len(solution1)):
        if (n>4) and (n<42):
            identifier+=solution1[n]
        if(n>41):
            break
   
    print(solution1)
    
    sock_1_server.close()
    return identifier

def yimkana2(code1):
    dest=('node1',4000)
    read=True
    flag1="that's" 
    flag2= "all"
    message=''
    totalMessage=''
    solution_2=''
    concatenar=False
    
    sock_2_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock_2_server.connect(dest)
      
    while read:
        message=sock_2_server.recv(1024).decode()
        totalMessage=totalMessage+message
        eachWord=totalMessage.split()
        wordCounter=0
        for i in  range (len(eachWord)):
            wordCounter=wordCounter+1
            if((flag1==eachWord[i]) and (flag2==eachWord[i+1])):
                solution2=wordCounter-1
                read=False
                break
    
    identifier=code1
    amountWords=solution2
    sent="{0} {1}".format(identifier,amountWords) 
    sent=str(sent)
  
    sock_2_server.send(sent.encode())
   
  
    code3=''
    while True:
       solution_2=(sock_2_server.recv(1024).decode()) 
       totalMessage+=solution_2
       if not solution_2:
            break
    
    for n in range (len(totalMessage)):
        if (concatenar==True):
            code3+=totalMessage[n]
    
        if(totalMessage[n]==':'):
            concatenar=True
        if((concatenar== True) and (totalMessage[n]=='\n')):
            break
    
    print(totalMessage)        
       
    sock_2_server.close()
    return code3

def yimkana3(code2):
    destination=('node1',5001) 
    read=True 
    complete=''
    sum=0
    keyWord= ' '
    totalMessage='' 
    catchCode=False 
    code4=''

    sock3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock3.connect(destination)   
    
    while read:
        message=sock3.recv(1024).decode()
        complete=complete+message
        completeMessageChallenge=complete.split(" ")
        sum=0
        for word in completeMessageChallenge:
            if(word.isdigit()):
                sum=sum+int(word)
            if(word.isdigit()==False):
                keyWord=word
            if(sum>1300):
                read=False
                break    

    answer=f"{keyWord} {code2}"
    sock3.send(answer.encode())
   
    while True:
       solution_3=(sock3.recv(1024).decode()) 
       totalMessage+=solution_3
       if not solution_3:
            break
   
    print(totalMessage)
    for n in range (len(totalMessage)):
        if((catchCode== True) and (totalMessage[n]=='\n')):
            break
   
        if (catchCode==True):
            code4+=totalMessage[n]
    
        if(totalMessage[n]==':'):
            catchCode=True
       
    return code4

def yimkana4 (code3):
    destination=('node1',10000)
    read=True
    completeMessage=b''
    message=b''
    quantityBytes=b''
    toReceive=1000
    totalMessage=''
    catchCode=False
    code5=''

    sock4=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock4.connect(destination)  
    sock4.send(code3.encode())

    while read:
        message=sock4.recv(1)
       
        if(message==b':'):
            read=False
            break
        quantityBytes=b''.join([quantityBytes,message])
    
    quantityBytes=int(quantityBytes.decode('ascii'))
    count=quantityBytes
    print(quantityBytes)

    read=True
    while read:
        message=sock4.recv(toReceive)
        count-=len(message)
        
        completeMessage=b''.join([completeMessage,message])
       
        if (count<=len(message)):
            message=sock4.recv(count)
            completeMessage=b''.join([completeMessage,message])
            read=False
            break

    md5=hashlib.md5(completeMessage)
    md5=md5.digest()
    sock4.send(md5)

    while True:
        solution4=(sock4.recv(1000).decode('utf-8')) 
        totalMessage+=solution4
        if not solution4:
           break
        print(solution4)

    for n in range (len(totalMessage)):
        if((catchCode== True) and (totalMessage[n]=='\n')):
            break
   
        if (catchCode==True):
            code5+=totalMessage[n]
    
        if(totalMessage[n]==':'):
            catchCode=True
    
    sys.stdout.flush
    return code5

# Copyright (C) 2009-2020  David Villa Alises
def sum16(data):
    if len(data) % 2:
        data = b'\0' + data

    return sum(struct.unpack('!%sH' % (len(data) // 2), data))

def cksum(data):
    sum_as_16b_words  = sum16(data)
    sum_1s_complement = sum16(struct.pack('!L', sum_as_16b_words))
    _1s_complement    = ~sum_1s_complement & 0xffff
    return _1s_complement

def yimkana5(code5):
    destination=('node1',7001)
    address=('',57277)
    catchCode=False
    code6=''

    sock5=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock5.bind(address)
   
  
    payload=base64.b64encode(bytes(code5,'utf-8'))
    data=struct.pack(f'!3s?hH {len(payload)}s',b'WYP',0,0,0,payload)

    data=struct.pack(f'!3s?hH {len(payload)}s',b'WYP',0,0,cksum(data),payload)
    sock5.sendto(data,destination)

    info= sock5.recv(2500)
   
    reply=struct.unpack(f'!3s?hH{(len(info)-8)}s',info)

    solution5=reply[4].decode()
    solution5=str((base64.b64decode(solution5)).decode())
    print(solution5)

    for n in range (len(solution5)):
        if((catchCode== True) and (solution5[n]=='\n')):
            break
   
        if (catchCode==True):
            code6+=solution5[n]
    
        if(solution5[n]==':'):
            catchCode=True
            
    return code6


if __name__=='__main__':
    main()
    

