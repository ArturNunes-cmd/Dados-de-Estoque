import matplotlib.pyplot as plt

dias = [1,2,3,4,5,6,7]
estoque = [100,95,110,105,120,115,130]

plt.plot(dias, estoque)

plt.plot(dias, estoque)

plt.title("Estoque ao longo dos dias", fontsize=15)

plt.xlabel("Dias")

plt.ylabel("Estoque")

plt.legend()

plt.show()




