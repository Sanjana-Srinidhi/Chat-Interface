import socket
import sys
import time    
x=socket.socket()
h_name= socket.gethostname() #gets the name of the host
print("Server will start on host:", h_name)
port= 8080
x.bind((h_name, port))
print('Server binded to host and port successfully')
print('Server waiting for incoming connections...')
x.listen(1)#n number of people will connect to the server
connection,address= x.accept()
print(address, " client has connected to the server and is now online.")
while 1: 
   display_mess= input(str("Type a message to the client: "))
   display_mess=display_mess.encode()
   connection.send(display_mess)
   print("Message sent.")
   in_message=connection.recv(10000);
   in_message=in_message.decode()
   print(" Client:", in_message)
