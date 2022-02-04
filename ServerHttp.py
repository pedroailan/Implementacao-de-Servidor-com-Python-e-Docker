from socket import *

host = '0.0.0.0'
porta = 12000

servidor = socket (AF_INET, SOCK_STREAM)
servidor.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
servidor.bind((host, porta))
servidor.listen(1)

print('Ouvindo em: ')
print(host + ':%s ...' % porta)

def enviarRequisicao(requisicao):
	diretorio = 'responses/index.html'
	if "filosofos: gregos" in requisicao:
		diretorio = 'responses/gregos.html'
	elif "filosofos: romanos" in requisicao:
		diretorio = 'responses/romanos.html'
	elif "clima: tropical" in requisicao:
		diretorio = 'responses/clima_tropical.html'
	elif "clima: semiarido" in requisicao:
		diretorio = 'responses/clima_semiarido.html'
	elif "civilizacao: egipcia" in requisicao:
		diretorio = 'responses/civilizacao_egipcia.html'
	elif "civilizacao: maia" in requisicao:
		diretorio = 'responses/civilizacao_maia.html'

	arquivo = open(diretorio)
	conteudo = arquivo.read()
	arquivo.close()

	response = 'HTTP/1.1 200 OK\n\n' + conteudo
	conexao.sendall(response.encode())
	

while True:
	try:
		conexao, endereco = servidor.accept()
		receive = conexao.recv(1024).decode()
		print("\nRecebido: \n" + receive)
		enviarRequisicao(receive)
		conexao.close()	
	except Exception as E:
		print(E)

		
	