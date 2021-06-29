import numpy as np

def run():
    data = [18, 20, 21, 23, 25, 28, 32, 35, 39]
    print("Media: ", np.mean(data))
    print("Mediana: ", np.median(data))
    print("Desviación Estándar: ", np.std(data))
    print("Varianza: ", np.var(data))




if __name__ == "__main__":
    run()