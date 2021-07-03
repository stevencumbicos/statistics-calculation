from pandas.core.frame import DataFrame
import numpy as np
import math
import pandas as pd
import statistics as stat

def mean(data):
    print("MEDIA: ", np.mean(data))

def median(data):
    print("MEDIANA: ", np.median(data))

def mode(data):
    print("MODA: ", stat.mode(data))


# population variance
# and → population standar deviation
def population_variance(data):
    print("---------------------------------------")
    print("DESVIACIÓN ESTÁNDAR (POBLACIÓN): ", round(np.std(data),2))
    print("DESVIACIÓN ESTÁNDAR (POBLACIÓN): ", round(np.std(data),2))
    print("---------------------------------------")

# sample variance
# and → sample standard deviation
def sample_variance(data):
    print("VARIANZA MUESTRAL: ", round(np.var(data, ddof=1),2))
    de_muestra = np.var(data, ddof = 1) 
    de_muestra = sqrt= round(de_muestra**(1 / 2),2)
    print("DESVIACIÓN ESTÁNDAR MUESTRAL: " + str(de_muestra))
    print("---------------------------------------")

# Average deviation
def average_deviation(data):
    print("DESVIACIÓN MEDIA:")
    print(f"Datos de la lista ordenados: {data}")
    print("---------------------------------------------------------------------------------------------")
    mode_var = np.mean(data)
    average_var = []
    average_var = [round(abs(value_data - mode_var),2) for value_data in data]
    for i, _ in enumerate(average_var):
        print("• La desviación media de [{0}] es {1}".format(data[i],average_var[i]))
    print("---------------------------------------")


def deciles_numpy(data):
    data = np.array(data)
    deciles = np.percentile(data, np.arange(10,100,10))
    print(f"DECILES (versión → Numpy):")
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
        print(key, "→", round(value,2))
    print("---------------------------------------")



def deciles_statistics(data):
    decil = stat.quantiles(data, n = 10)
    print("DECILES (versión → Statictis y Excel):")
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
    print("---------------------------------------------------------------------------------------------")



def quartiles_numpy(data):
    print("CUARTILES (versión → Numpy)")
    print("Mínimo: ", np.quantile(data,0))
    print("Cuartil 1 (25%): ", np.quantile(data,0.25)) 
    print("Cuartil 2 (50%): ", np.quantile(data,0.50)) 
    print("Cuartil 3 (75%): ", np.quantile(data,0.70)) 
    print("Máximo: ", np.quantile(data,1))
    print("---------------------------------------")


def quartiles_pandas(data):
    print("CUARTILES (versión → Pandas)")
    data_1 = {"A" : data}
    df = pd.DataFrame(data_1)
    print("Estadísticas: ", round(df["A"].describe()),2)
    grafica=df.boxplot()
    print("---------------------------------------")


def run():
    data = [25,28,30,30,35,35,36,37,37,38,40,40,40,40,40,40,41,43,48,50] 
    data.sort()
    print(f"Los datos ordenados: ", data)
    mean(data)
    median(data)
    mode(data)
    population_variance(data)
    sample_variance(data)
    deciles_numpy(data)
    deciles_statistics(data)
    average_deviation(data)
    quartiles_numpy(data)
    quartiles_pandas(data)

if __name__ == "__main__":
    run()