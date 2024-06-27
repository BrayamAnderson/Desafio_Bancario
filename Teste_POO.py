class pessoa:
    def __init__(self,nome,ano):
        self.nome = nome 
        self.ano = ano

    def cinco(self):
        return self.ano - 5
    
    @property
    def ano(self):
        return self._ano 
    
    @ano.setter
    def ano(self,value):
        if value > 0:
            self._ano = value
        else:
            print("O valor não pode ser negativo")

    

p1 = pessoa("Brayam",-5)
print(p1.cinco())


import time
import random

print("""Suas opções
      
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA

Qual a sua jogada ?
      """)

for acao in range(1,3):

    acao = int(input())
    print("\n")
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print('PO !!')

    lista = ["Pedra", "Papel" , "Tesoura" ]

    nmr_aleatorio = random.choice(lista)


    if acao == 0:

        if nmr_aleatorio == "Pedra":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Pedra")
            print("""
                DEU EMPATE!!
                """)

        elif nmr_aleatorio == "Papel":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Pedra")
            print("""
                O COMPUTADOR VENCEU!!
                """)
            
        elif nmr_aleatorio == "Tesoura":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Pedra")
            print("""
                VOCE VENCEU!!
                """)
            

    elif acao == 1:
        if nmr_aleatorio == "Pedra":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Papel")
            print("""
                VOCE VENCEU!!
                """)

        elif nmr_aleatorio == "Papel":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Papel")
            print("""
                DEU EMPATE!!
                """)
            
        elif nmr_aleatorio == "Tesoura":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Papel")
            print("""
                O COMPUTADOR VENCEU!!
                """)

    elif acao == 2:
        if nmr_aleatorio == "Pedra":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Tesoura")
            print("""
                O COMPUTADOR VENCEU!!
                """)

        elif nmr_aleatorio == "Papel":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Tesoura")
            print("""
                VOCE VENCEU!!
                """)
            
        elif nmr_aleatorio == "Tesoura":
            print("-" *20)
            print(f"Computador jogou {nmr_aleatorio}")
            print("Voce jogou Tesoura")
            print("""
                DEU EMPATE!!
                """)


    else:
        print("Escolha entre as opções listadas")