# Universidade Ferderal de Minas Gerais
# DCC023 - Redes de Computadores 2017/1
# Trabalho Pratico 0

# Codigo por Alison de Oliveira Souza - 2012049316
# Servidor

# Para executar basta rodar python serv.py

import socket
import sys
import struct

# Definicao da porta e endereco. Inicializacao do socket e contador global.
HOST = ''
PORT = 51515
contador = 0;
contador_global = 0;
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

# Abertura passiva.
tcp.bind(orig)
tcp.listen(1)


while True:
	contador = contador_global;
	# Abertura completa, aguardando conexao de algum cliente.
	con, cliente = tcp.accept()
	# Definindo timeout de 5 segundos.
	con.settimeout(5)
	print 'Conectado por', cliente
	
	# Recebendo mensagem (+ ou -).
	msg = con.recv(1)
	if msg == '+':
		if contador == 999:
			contador = 0
		else:
			contador += 1
	elif msg == '-':
		if contador == 0:
			contador = 999
		else:
			contador -= 1
	else:
		print >> sys.stderr, 'Mensagem invalida. Conexao encerrada com', cliente
		con.close()
		continue

	# Enviando os 4 bytes codificados via pack.
	con.send(struct.pack('>i', contador))

	# Recebendo os 3 caracteres de confirmacao do cliente.
	confirm1 = con.recv(1)
	confirm2 = con.recv(1)
	confirm3 = con.recv(1)
	confirmacao = confirm1 + confirm2 + confirm3
	
	# Verificando se a mensagem do cliente confere com o contador.
	if int(confirmacao) == contador:
		contador_global = contador
		print 'Contador global atualizado: ', contador_global
	else:
		print >> sys.stderr, 'Mensagem do cliente nao condiz com contador.'
		print 'Contador global nao foi atualizado. Valor atual: ', contador_global
	print 'Finalizando conexao do cliente', cliente
	con.close()
