import numpy as np
import math
import statistics as stat

def run():
    # data = [18, 20, 21, 23, 25, 28, 32, 35, 39]
    data = [52,55,58]
    print("----------------")

    print("Media: ", np.mean(data))
    print("Mediana: ", np.median(data))
    print("Moda: ", stat.mode(data))

    print("----------------")

    print("Varianza Población: ", np.var(data))
    print("Desviación Estándar (población): ", np.std(data))

    print("----------------")

    print("Varianza Muestra: ", np.var(data, ddof=1))
    de_muestra = np.var(data, ddof=1)
    de_muestra = sqrt = de_muestra**(1/2)
    print("Desviación Estándar (muestra): " + str(de_muestra))

    print("----------------")


if __name__ == "__main__":
    run()