import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("ResVsRad.txt", skiprows=1)

# Data de x,y
x = data[:, 0]
y = data[:, 1]

# Error de x,y
# xerr = np.array()
# yerr = np.array()

print(x, y)  # Verificar si se está leyendo el documento .txt de forma correcta.

# Fit de la data

B, A = np.polyfit(x, y, deg=1)
fit = (B * x) + A

print(A, B, fit)

# Plotting

fig, ax = plt.subplots()
ax.scatter(x, y, color="black")
ax.plot(x, fit, color="black")
fig.set_size_inches(8, 6)
plt.grid(True)

# Labels

ax.set_title("Radiación vs. Temperatura", fontsize=15)
ax.set_xlabel("$T_k^4-T_{rm}^4$ ($K^4$)", fontsize=12)
ax.set_ylabel("Rad (mV)", fontsize=12)

# Fit Equation

fig.text(0.3, 0.25, f"$y = {B:.2f}x + {A:.2f}$", fontsize=12, color="black")

# Descripción de al Figura

# txt = """
#     Figura 1.1. Radiación vs. Temperatura; se muestra la relación entre la radiación
#     incidente en el sensor y la resta de la cuarta potencia de la temperatura medida
#     por el termistor del cubo con la cuarta potencia de la temperatura ambiente. Una
#     relación lineal entre las variables es aparente, por lo que, se sugiere que estas
#     dos son directamento proporcionales.
# """

# fig.text(
#     0.5,
#     0.03,
#     txt,
#     ha="center",
# )

# Figure Size
# fig.set_size_inches(10, 10, forward=True)

# Cifras de los ejes
# ax.xaxis.set_major_formatter('{x:9<5.1f}')

# Tick Settings

ax.tick_params(axis="both", which="major", labelsize=12)
ax.tick_params(axis="both", which="minor", labelsize=10)

# Barra de Error

# ax.errorbar(x, y, xerr, yerr, fmt="o", lindewidth=2, capsize=6)

plt.savefig("RadVsTemp.png")
plt.show()

