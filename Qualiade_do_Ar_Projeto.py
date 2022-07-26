from google.colab import drive
drive.mount('/content/drive')  #Linkando o Colab com o Drive

import pandas as pd  #Manipular database
import matplotlib.pyplot as plt  #Visualização de dados
from sklearn.model_selection import train_test_split  #Divisor database
from sklearn.naive_bayes import GaussianNB  #Classificador 
from sklearn import metrics  #Acurácia dos resultados
import time
import random


database = pd.read_excel('/content/drive/MyDrive/AirQuality/DataAirQualityUCI.xlsx')
database.info()  #Visão geral das categorias
database.head(15)  #Primeirs 15 linhas formatadas

colors = ['steelblue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'lightcoral']
dataclass = []

qtd = [0, 0, 0, 0]
dataclass = list(database['CO(GT)'].values)  #Guarda em uma lista os valores da classe seleconada

plotclass = ['0.0-3.0', '3.1-6.0', '6.1-9.0', '9.1-12.0']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=3: 
        qtd[0]+=1;
    elif x > 3 and x<=6:
        qtd[1]+=1;
    elif x > 6 and x<=9:
        qtd[2]+=1;
    elif x > 9 and x<=12:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('CO(GT)')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['NMHC(GT)'].values)  #Guarda em uma lista os valores da classe seleconada

plotclass = ['0-300', '301-600', '601-900', '901-1200']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=300: 
        qtd[0]+=1;
    elif x > 300 and x<=600:
        qtd[1]+=1;
    elif x > 600 and x<=900:
        qtd[2]+=1;
    elif x > 900 and x<=1200:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('NMHC(GT)')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['C6H6(GT)'].values)  #Guarda em uma lista os valores da classe seleconada

plotclass = ['00.00-15.00', '15.01-30.00', '30.1-45.00', '45.01-60.00']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=15: 
        qtd[0]+=1;
    elif x > 15 and x<=30:
        qtd[1]+=1;
    elif x > 30 and x<=45:
        qtd[2]+=1;
    elif x > 45 and x<=60:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('C6H6(GT)')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['NOx(GT)'].values)  #Guarda em uma lista os valores da classe seleconada

plotclass = ['0-400', '401-800', '801-1200', '1201-1600']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=400: 
        qtd[0]+=1;
    elif x > 400 and x<=800:
        qtd[1]+=1;
    elif x > 800 and x<=1200:
        qtd[2]+=1;
    elif x > 1200 and x<=1600:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('NOx(GT)')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['NO2(GT)'].values)  #Guarda em uma lista os valores da classe seleconada
plotclass = ['0-100', '101-200', '201-300', '301-400']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=100: 
        qtd[0]+=1;
    elif x > 100 and x<=200:
        qtd[1]+=1;
    elif x > 200 and x<=300:
        qtd[2]+=1;
    elif x > 300 and x<=400:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('NO2(GT)')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['T'].values)  #Guarda em uma lista os valores da classe seleconada

plotclass = ['00.00-12.00', '12.01-24.00', '24.01-36.00', '36.01-48.00']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=12: 
        qtd[0]+=1;
    elif x > 12 and x<=24:
        qtd[1]+=1;
    elif x > 24 and x<=36:
        qtd[2]+=1;
    elif x > 36 and x<=48:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('Temperature')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['RH'].values)  #Guarda em uma lista os valores da classe seleconada

plotclass = ['00.00-25.00', '25.01-50.00', '50.01-75.00', '75.01-100.00']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=25: 
        qtd[0]+=1;
    elif x > 25 and x<=50:
        qtd[1]+=1;
    elif x > 50 and x<=75:
        qtd[2]+=1;
    elif x > 75 and x<=100:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('Relative Humidity')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()

qtd = [0, 0, 0, 0]
dataclass = list(database['AH'].values)  #Guarda em uma lista os valores da classe seleconada
plotclass = ['0.00-0.50', '0.51-1.00', '1.01-1.50', '1.51-2.00']
print(len(dataclass))
for x in dataclass:
    if x >= 0 and x<=0.5: 
        qtd[0]+=1;
    elif x > 0.5 and x<=1:
        qtd[1]+=1;
    elif x > 1 and x<=1.5:
        qtd[2]+=1;
    elif x > 1.5 and x<=2:
        qtd[3]+=1;

#Plotando o gráfico
plt.figure(figsize=(7, 7))
plt.bar(plotclass, qtd, color=colors)
plt.title('Absolute Humidity')
plt.xlabel("Result Class")
plt.ylabel("Count")
plt.show()


x = database.iloc[:, 3:]  #Atributos (menos a hora e data de verificação)
y = database.iloc[:, 0]  #Resultados 
#print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = int(time.time()))

model = GaussianNB()
model.fit(x_train, y_train)
y_predicted = model.predict(x_test)

#Verificando o desemplenho do modelo
accu = metrics.accuracy_score(y_test, y_predicted)  #Accuracy
prec = metrics.precision_score(y_test,y_predicted, average="weighted", zero_division=0)  #Precision
recall = metrics.precision_score(y_test, y_predicted, average="weighted", zero_division=0)  #Recall
f1_score = metrics.f1_score(y_test, y_predicted, average="weighted")  #F1 Score
print('Desempenho do modelo:\n\tAccuracy: ', accu, '\n\tPrecision:', prec, '\n\tRecall:   ', recall, '\n\tF1_score: ', f1_score, '\n')


#Testando para uma amostra considerada limpa [co = 0.9, nmhc = 61, c6h6 = 2.5, nox = 56, no2 = 62, t = 11.5, rh = 60, ah = 0.65]
co = float(input("Digite a concentração de CO (mg/m^3): "))
nmhc = int(input("Digite a concentração de NMHC (microg/m^3): "))
c6h6 = float(input("Digite a concentração de C6H6 (microg/m^3): "))
nox = float(input("Digite a concentração de NOX (ppb): "))
no2 = float(input("Digite a concentração de NO2 (mg/m^3): "))
t = float(input("Digite a temperatura (ºC): "))
rh = float(input("Digite a humidade relativa (%): "))
ah = float(input("Digite a humidade absoluta: "))

res = model.predict([[co, nmhc, c6h6, nox, no2, t, rh, ah]])
if res==1: print('\nSua amostra de ar é considerada poluída\n')
if res==0: print('\nSua amostra de ar é considerada limpa\n')

#Testando para uma amostra considerada poluída [co = 6.9, nmhc = 401, c6h6 = 22.1, nox = 250, no2 = 140, t = 9.7, rh = 50.8, ah = 0.5]
co = float(input("Digite a concentração de CO (mg/m^3): "))
nmhc = int(input("Digite a concentração de NMHC (microg/m^3): "))
c6h6 = float(input("Digite a concentração de C6H6 (microg/m^3): "))
nox = float(input("Digite a concentração de NOX (ppb): "))
no2 = float(input("Digite a concentração de NO2 (mg/m^3): "))
t = float(input("Digite a temperatura (ºC): "))
rh = float(input("Digite a humidade relativa (%): "))
ah = float(input("Digite a humidade absoluta: "))

res = model.predict([[co, nmhc, c6h6, nox, no2, t, rh, ah]])
if res==1: print('\nSua amostra de ar é considerada poluída\n')
if res==0: print('\nSua amostra de ar é considerada limpa\n')