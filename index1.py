import matplotlib.pyplot as plt

produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam'] 
Quantidades = [50, 75, 30, 60]

plt.bar(produtos, Quantidades, color=['#7dafff', '#9be7a1', '#ff9999', '#c9a0dc'])

plt.title("Comparação de Produtos", fontsize=15)

plt.xlabel("Produtos")

plt.ylabel("Quantidades")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()
