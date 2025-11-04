# 📊 Visualizações de Dados com Matplotlib

Este projeto apresenta **gráficos gerados com a biblioteca Matplotlib**, explorando diferentes tipos de visualização para análise de dados simples, como estoque, produtos e categorias de vendas.

---

## 🚀 Tipos de Gráficos

### 📈 1. Gráfico de Linha — Evolução do Estoque
Mostra a variação do estoque ao longo dos dias.

```python
plt.plot(dias, estoque)
plt.title("Estoque ao longo dos dias", fontsize=15)
plt.xlabel("Dias")
plt.ylabel("Estoque")
plt.legend()
plt.show()
