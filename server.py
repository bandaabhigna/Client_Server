#this is the server code

import socket
import select
import sys
import random
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port=1357
server.bind((ip,port))
n=20

print "started listening on ",ip,":",port
server.listen(3)

Q=["Q1  What is the full form of TCP? : (a)Transmission control protocol  (b)traffic control protocol",   "Q2 What is the full form of UDP? : (a)user drain protocol  (b)user datagram protocol",   "Q3 What is the full form of ARP? : (a)address resolution protocol  (b)address resolver protocol",  "Q4 What is the full form of DHCP? : (a)datagram host configuration protocol  (b)Dynamic host configuration protocol",   "Q5 What is the full form of DNS? : (a)domain name system  (b)domain name server",   "Q6 What is the full form of PPP? : (a)peer to peer protocol  (b)point to point protocol",   "Q7 What is the full form of LAN? : (a)local address network  (b)local area network",   "Q8 What is the full form of IP? : (a)internet protocol  (b)internet permission",   "Q9 What is the full form of OSI? : (a)open system interconnection  (b)open server internet",   "Q10 What is the full form of WAN? : (a)wide area network  (b)wide address network",   "Q11 What is the full form of FTMA? : (a)file transfer address managenent  (b) file transfer access management",   "Q12 What is the full form of ADSL? : (a)asymmetric digital subscriber line  (b)asymmetric data system language",   "Q13 What is the full form of FTP? : (a)file transfer protocol  (b)file transmit protocol",   "Q14 What is the full form of SMTP? : (a)system main transmit protocol (b)simple mail transfer protocol",   "Q15 What is the full form of HTTP? : (a)hypertext transfer protocol  (b)high text transfer protocol",   "Q16 What is the full form of CN? : (a)computer network  (b)communication network",   "Q17 What is the full form of SR? : (a)system recurssion  (b)selective repeat",   "Q18  What is the full form of RIP? : (a)routing information protocol  (b)routing internet protocol",   "Q19 What is the full form of OSPF? : (a)open shortest path first  (b)open server path first",   "Q20 What is the full form of BGP? : (a)border gain protocol  (b)border gataeway protocol"]

A=['a','b','a','b','a','b','b','a','a','a','a','a','a','b','a','a','b','a','a','b']

clientlist= []
portlist=[]
bz=[0]
no=[0]


random.shuffle(Q)
def clienthandler():
    client,addr=server.accept()
    clientlist.append(client)
    portlist.append(addr[1])
    count=0
    print "got a connection from ",addr[0],":",addr[1]
    while count<5:
        if(len(clientlist)==3 and bz[0]==0) :
            broadcast(Q[no[0]])
            no[0]=no[0]+1
        data=client.recv(1024)
        if(data[0:2]=="bz" and bz[0]!=1 ):
            bz[0]=1
            ans=client.recv(1024)
            if (len(A[Q[no[0]-1]])==2 and ans[0:2]==A[Q[no[0]-1]]) or (len(A[Qlist[no[0]-1]])==1 and ans[0:1]==A[Q[no[0]-1]]):
                count=count+1
                print "score of ",addr[0],",",addr[1],"is ",count
                bz[0]=0
                if count==5:
                    print "game is won by",addr[0],":",addr[1]
                    for client in clientlist:
                        client.close()
                        break
            else:
                print "Wrong Answer"
                bz[0]=0
        elif(data=="disconnect"):
            client.send("bye")
            client.close()
            break
        else:
            print "sorry you are not the winner"

        
        
            
        

def broadcast(message):
    for client in clientlist:
        client.send(message)


for i in range(3):
    Thread(target=clienthandler).start()

server.close()
