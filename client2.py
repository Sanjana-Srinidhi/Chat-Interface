import socket
import sys
import time
x=socket.socket()
h_name= input(str(" Enter the hostname of the server: "))
port=8080
x.connect((h_name,port))
print("Connected to chat server")
while 1: 
   incoming_message=x.recv(10000);
   incoming_message=incoming_message.decode()
   print(" Server :", incoming_message)
   message= input(str("Type the message to the server: "))
   message=message.encode()
   x.send(message)
   print("Message sent")