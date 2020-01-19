# -*- coding: utf-8 -*-


import sklearn.neural_network as sk
import sklearn.neural_network.multilayer_perceptron as mlp
import numpy as np
import pandas as pd

file_xls = pd.read_excel("datos.xlsx","sheet1")
numero=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[20],[12],[25],[47],[50],[32],[100],[11],[13],[77],[81],[78],[66],[45],[59],[19],[26],[27],[28]])

raiz=np.array([1.000,1.414,1.732,2.000,2.236,2.449,2.646,2.828,3.001,4.721,3.464,5.001,6.855,7.071,5.656,10.000,3.316,3.605,8.774,9.000,8.831,8.124,6.708,7.681,4.358,5.099,5.196,5.291])
print(type(raiz))


while True:
  perc=mlp.MLPRegressor(hidden_layer_sizes=(5,4,3,2),solver='lbfgs' )
  perc.fit(numero,raiz)
  print(perc.score(numero,raiz))
  if perc.score(numero,raiz) >0.999:
    break
print(file_xls)

while True:
 number=int(input()) 
 if number> -1:
    print "numero: ", number 
    print "raiz: ", perc.predict(np.array([[number]]))
 else:
   break