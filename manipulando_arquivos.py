# arquivo = arquivo = open('C:/Users/braya/Documents/Investimento/DIO/Python estrutura de dados/texto.txt', 'w')
# arquivo.write("Meu Pau")


# arquivo = open('C:/Users/braya/Documents/Investimento/DIO/Python estrutura de dados/texto.txt', 'r')
# print(arquivo.read())
# arquivo.close()


# with open('arquivo.txt' , 'w', encoding='utf-8') as arquivo:

# arquivo_path = 'C:/Users/braya/Documents/Investimento/DIO/Python estrutura de dados/texto.txt'

# # Verificando se o caminho do arquivo está correto
# print(f"Tentando abrir o arquivo: {arquivo_path}")

# try:
#     with open(arquivo_path, 'r') as arquivo:
#         print("Arquivo aberto com sucesso!")
#         conteudo = arquivo.read()
#         print("Conteúdo do arquivo:")
#         print(conteudo)
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# except PermissionError:
#     print("Erro: Permissão negada para ler o arquivo.")
# except Exception as e:
#     print(f"Erro ao ler o arquivo: {e}")

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, saldo_inicial):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo_inicial

    def fazer_chamada(self,destinatario,duracao):
        dest = destinatario
        minutos = duracao * 0.10
        saldo_final = self.saldo - minutos

        if saldo_final < 0:
            return "Saldo insuficiente para fazer a chamada."
        else:
            return f"Chamada para {dest} realizada com sucesso. Saldo: ${saldo_final:.2f}"
    



# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioTelefone(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))

