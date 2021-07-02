import numpy as np
import math
import pandas as pd
import statistics as stat

def run():
    # data = [42, 47, 53, 47, 50, 45, 46, 48, 41, 49, 45, 40, 54]
    # data = [5,6,15,4,2]
    data = [25,28,30,30,35,35,36,37,37,38,40,40,40,40,40,40,41,43,48,50]
    data.sort()
    print(f"Los datos ordenados: ", data)

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
    de_muestra = sqrt=de_muestra**(1/2)
    print("Desviación Estándar (muestra): " + str(de_muestra))

    print("----------------")


    data = np.array([data])
    deciles = np.percentile(data, np.arange(10,100,10))
    print(f"Deciles: {deciles}")

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
        print(key, "-", value)

    print("----------------")



if __name__ == "__main__":
    run()