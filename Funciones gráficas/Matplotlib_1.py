import matplotlib.pyplot as plt
import numpy as np

# Configuración general
plt.figure(figsize=(7,5))
plt.suptitle("Graficadora", fontsize = 20)

# Grafica #1
x = np.arange(0,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(3,3,1)
plt.plot(y1, label = "Seno" ,color= "#7B3131", linestyle = "--")
plt.plot(y2, label = "Coseno" ,color = "#483B9F" )
#plt.xlabel("Distancia")
#plt.ylabel("Tiempo")
plt.title("Funciones sen/cos")
#plt.legend()

# Gráfica #2 - Histograma
datos = [2,3,5,2,5,1,5,2,6]
plt.subplot(3,3,9)
plt.hist(datos, orientation="horizontal", color = "#0186B2", edgecolor = "black")
plt.title("Histograma")

# Gráfica #3 - Torta
dic = {"Electrónica" : 3, "Eléctrica" : 3, "Mecatrónica" : 1}
plt.subplot(3,3,5)
plt.pie(list(dic.values()), labels= list(dic.keys()), startangle= 45)
plt.title("Torta")

# Gráfica #4 - Barras
plt.subplot(3,3,4)
plt.bar(list(dic.keys()), list(dic.values()))
plt.title("Barra")


plt.tight_layout()
plt.show()