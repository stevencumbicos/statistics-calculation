import numpy as np
import math
import pandas as pd
import statistics as stat
import statistics as s


# def mean_median_mode(data):
#     print("----------------")
#     print("Media: ", np.mean(data))
#     print("Mediana: ", np.median(data))
#     print("Moda: ", stat.mode(data))


def mean(data):
    print("Media: ", np.mean(data))
    # return

def median(data):
    print("Mediana: ", np.median(data))

def mode(data):
    print("Moda: ", stat.mode(data))


# standard variance
# and → standard population variance
def standard_variance(data):
    print("----------------")
    print("Varianza Población: ", np.var(data))
    print("Desviación Estándar (población): ", np.std(data))
    print("----------------")


# sample variance
# and → sample standard variance
def sample_variance(data):
    print("Varianza Muestral: ", np.var(data, ddof=1))
    de_muestra = np.var(data, ddof = 1)
    de_muestra = sqrt=de_muestra**(1 / 2)
    print("Desviación Estándar Muestral: " + str(de_muestra))
    print("----------------")

def average_deviation(data):
    print("----------------")
    print("----------------")
    print("----------------")
    lista = [0]
    a = abs(data + lista)
    print(a)
    

    # promedio = mean(data)
    # average = (12 - promedio)
    # print(average)


def deciles(data):
    data = np.array(data)
    deciles = np.percentile(data, np.arange(10,100,10))
    print(f"Deciles con Numpy:")
    # print(f"Deciles: {deciles}")
    dictionary = {
        "10%" : deciles[0],
        "20%" : deciles[1],
        "30%" : deciles[2],
        "40%" : deciles[3],
        "50%" : deciles[4],
        "60%" : deciles[5],
        "70%" : deciles[6],
        "80%" : deciles[7],
        "90%" : deciles[8]
    }
    for key, value in dictionary.items():
        print(key, "→", value)
    print("----------------")

def deci(data):
    decil = s.quantiles(data, n=10)
    print("Deciles (versión → Statictis y Excel):")
    # print("Deciles con statictics:" + str(decil))

    dictionary = {
        "10%" : decil[0],
        "20%" : decil[1],
        "30%" : decil[2],
        "40%" : decil[3],
        "50%" : decil[4],
        "60%" : decil[5],
        "70%" : decil[6],
        "80%" : decil[7],
        "90%" : decil[8]
    }

    for key, value in dictionary.items():
        print(key, "→", value)
    print("----------------")

def run():
    # data = [25,28,30,30,35,35,36,37,37,38,40,40,40,40,40,40,41,43,48,50] 

    data = [12,13,12,14,15]

    # data = [56,58,64,67,68,73,78,83,84,88,89,90,91,92,93,93,94,95,97,99]
    data.sort()
    print(f"Los datos ordenados: ", data)
    # mean_median_mode(data)
    mean(data)
    median(data)
    mode(data)
    standard_variance(data)
    sample_variance(data)
    deciles(data)
    deci(data)
    average_deviation(data)

if __name__ == "__main__":
    run()