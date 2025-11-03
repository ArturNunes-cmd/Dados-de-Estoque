import matplotlib.pyplot as plt

categorias = ['Eletrônicos', 'Vestuário', 'Alimentos'] 
valores = [15000, 8000, 5000]

explode = [0.05,0,0]

fig1, ax1 = plt.subplots()
ax1.pie(valores, 
        explode=explode, 
        labels=categorias,
        autopct='%1.1f%%',
        shadow=True, 
        startangle=90,
        wedgeprops={"edgecolor":"black", 'linewidth': 1, 'antialiased': True})
ax1.axis('equal')

plt.title("Proporção de Categorias")

plt.legend(valores, title="Categorias", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()