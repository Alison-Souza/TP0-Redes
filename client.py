import socket
import sys
import struct

HOST = '127.0.0.1'
PORT = 51515
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.settimeout(5)
dest = (HOST, PORT)
tcp.connect(dest)

#TESTE DO TIMEOUT DO SERVIDOR
#while True:
#	continue

if sys.argv[1] == 'dec':
	tcp.send ('-')
	msg = tcp.recv(4)
#Verificar se recebeu corretamente. Se nao, stderr
	(msg,) = struct.unpack('>i', msg)	
	print msg
#Aqui tem que enviar como 3 caracteres ascii (sprintf)
	msg = str(msg)
	tcp.send(msg[0])
	if(int(msg) > 9):
		tcp.send(msg[1])
		if(int(msg) > 99):
			tcp.send(msg[2])
elif sys.argv[1] == 'inc':
	tcp.send ('+')
	msg = tcp.recv(4)
#Verificar se recebeu corretamente. Se nao, stderr
	(msg,) = struct.unpack('>i', msg)
	print msg
#Aqui tem que enviar como 3 caracteres ascii (sprintf)
	msg = str(msg)
	tcp.send(msg[0])
	if(int(msg) > 9):
		tcp.send(msg[1])
		if(int(msg) > 99):
			tcp.send(msg[2])
else:
#Colocar o erro em stderr
	print >> sys.stderr, 'Argumento invalido!\n'
tcp.close()
