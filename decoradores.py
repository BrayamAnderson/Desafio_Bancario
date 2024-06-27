# def MeuGerador():
#     texto = "Python"
#     for i in range(len(texto)):
#         yield texto[i]

# for fe in MeuGerador():
#     print(fe)


from datetime import datetime
import pytz ##importar biblioteca de fuso horario

data_atual = datetime.now()

data_texto = f"{data_atual.day}/{data_atual.month}/{data_atual.year}" ## Outra forma de conseguir a data
data_em_texto = data_atual.strftime('%d/%m/%y as %H:%M') ## Melhor forma de coneguir data e hora
print(data_texto)
print("-="*10)
print(data_em_texto)
print("-="*10)

data_fuso = datetime.now(pytz.timezone("Europe/Oslo"))
print(data_fuso)