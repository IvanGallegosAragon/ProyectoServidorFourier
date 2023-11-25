import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import argparse


#Variables simbolicas
n = sym.Symbol("n")
t = sym.Symbol("t")
#Coeficientes
a0 = 1
bn = ((1 - sym.cos(np.pi * n)) / (np.pi * n)) #Función simbolica
#Serie de Fourier
serie = a0 / 2
#Variable insertada desde CLI
parse = argparse.ArgumentParser()
parse.add_argument("--x",type=int,default=1,help="Ingresa el numero de armonicos enteros")
#Obtención del argumento del CLI de la forma:
#python Fourier.py --x=<Numero de Armonicos enteros>
armonicos = parse.parse_args()
armonicos = armonicos.x
if armonicos != 0:
  for i in range(1,armonicos + 1):
    #Sigma y evaluaciónes de los cueficientes conforme a las n impares de la sigma
    if i % 2 != 0:
      serie +=  (bn * sym.sin(2 * n * t)).subs(n,i) #Evaluación con subs
#Variable tiempo convirtiendo la expresion de sympy en una evaluable para un t desglosado en matrices
fserie = sym.lambdify(t,serie) #Conversion de funcion simbolica a función evaluable
v_tiempo = np.linspace(-3,3,100000) #Varaible tiempo acotada en los limites de [-3,3] usando una matriz lineal de len 100,000
fserieG = fserie(v_tiempo) #Función concreta de la serie de Fourier de n terminos
#Label
plt.plot(v_tiempo,fserieG)
plt.title(f"Serie de fuerier para f(x) = {{ 1 : 0 < t < pi/2 , 0 : pi/2 < t < pi }} con {armonicos} armonicos")
#Salva el plot en un png
plt.savefig("Plot.png")