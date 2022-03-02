from pandas.core.frame import DataFrame
import numpy as np
import math
import pandas as pd
import statistics as stat

def mean(data):
    print("---------------------------------------------------------------------------------------------")
    print("MEDIA: ", round(np.mean(data),2))

def median(data):
    print("---------------------------------------------------------------------------------------------")
    print("MEDIANA: ", round(np.median(data),2))
    print("---------------------------------------------------------------------------------------------")

def mode(data):
    print("MODA: ", round(stat.mode(data),2))


# population variance
# and → population standar deviation
def population_variance(data):
    print("---------------------------------------------------------------------------------------------")
    print("VARIANZA POBLACIÓN: ", round(np.var(data),2))
    print("DESVIACIÓN ESTÁNDAR (POBLACIÓN): ", round(np.std(data),2))
    print("---------------------------------------------------------------------------------------------")

# sample variance
# and → sample standard deviation
def sample_variance(data):
    print("VARIANZA MUESTRAL: ", round(np.var(data, ddof=1),2))
    de_muestra = np.var(data, ddof = 1) 
    de_muestra = sqrt= round(de_muestra**(1 / 2),2)
    print("DESVIACIÓN ESTÁNDAR MUESTRAL: " + str(de_muestra))
    print("---------------------------------------------------------------------------------------------")

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
    print("---------------------------------------------------------------------------------------------")


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
    print("---------------------------------------------------------------------------------------------")


def deciles_statistics(data):
    decil = stat.quantiles(data, n = 10)
    print("DECILES (versión → Statictis y Excel):")
    dictionary = {
        "10%" : round(decil[0],2),
        "30%" : round(decil[2],2),
        "40%" : round(decil[3],2),
        "50%" : round(decil[4],2),
        "60%" : round(decil[5],2),
        "70%" : round(decil[6],2),
        "80%" : round(decil[7],2),
        "90%" : round(decil[8],2)
    }

    for key, value in dictionary.items():
        print(key, "→", value)
    print("---------------------------------------------------------------------------------------------")


def quartiles_numpy(data):
    print("CUARTILES (versión → Numpy)")
    print("Mínimo: ", np.quantile(data,0))
    print("Cuartil 1 (25%): ", round(np.quantile(data,0.25),2)) 
    print("Cuartil 2 (50%): ", round(np.quantile(data,0.50),2)) 
    print("Cuartil 3 (75%): ", round(np.quantile(data,0.70),2)) 
    print("Máximo: ", np.quantile(data,1))
    print("---------------------------------------------------------------------------------------------")


def quartiles_pandas(data):
    print("CUARTILES (versión → Pandas)")
    data_1 = {"A" : data}
    df = pd.DataFrame(data_1)
    print("Estadísticas: ", round(df["A"].describe()),2)
    grafica = df.boxplot()
    print("---------------------------------------------------------------------------------------------")


def run():
    data = [1.3, 7.0, 3.6, 4.1, 5.0, 3.4, 6.3, 8.2, 7.3, 5.3, 3.5, 5.0, 6.5, 2.3, 6.5, 7.7, 9.0, 8.1, 7.0, 6.5, 4.0, 5.0, 6.0, 7.0] 
    print(f"Unsorted data: ", data)
    data.sort()
    print(f"Ordered data: ", data)
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
