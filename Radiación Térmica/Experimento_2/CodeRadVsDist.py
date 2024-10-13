import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
    "/Users/jessielvelez/env/Laboratorio Intermedio/Radiación Térmica/Experimento_2/RadVsDist.txt",
    skiprows=1,
)

# Data de x,y
pos = data[:, 0]
rad = data[:, 1]
invsqpos = 1/(pos**2)

# Error de x,y
# xerr = np.array()
# yerr = np.array()

print('Valores de Posición:')
for i in pos:
    
    print(i)  # Verificar si se está leyendo el documento .txt de forma correcta.
    
print('Valores de Radiación:')
for i in rad:
     
    print(i)  # Verificar si se está leyendo el documento .txt de forma correcta.

print('Valores de Inverso Cuadrado de Posición:')    
for i in invsqpos:
    
    print(i)  # Verificar si se está leyendo el documento .txt de forma correcta.

# Fit de la data

# B, A = np.polyfit(x, y, deg=1)
# fit = (B * x) + A

# print(A, B, fit)

# FIGURE 1
# Plotting de Rad vs x

fig, ax = plt.subplots()
ax.scatter(pos, rad, color="black")
# ax.plot(x, fit, color="black")
fig.set_size_inches(8, 6)
plt.grid(True)

# Labels

ax.set_title("Radiación vs. Distancia del Sensor", fontsize=15)
ax.set_ylabel("Rad (mV)", fontsize=12)
ax.set_xlabel("x (cm)", fontsize=12)

# Fit Equation

#fig.text(0.3, 0.15, f"$y = {B:.2f}x + {A:.2f}$", fontsize=12, color="black")

# Figure Size
# fig.set_size_inches(10, 10, forward=True)

# Cifras de los ejes
# ax.xaxis.set_major_formatter('{x:9<5.1f}')

# Tick Settings

ax.tick_params(axis="both", which="major", labelsize=12)
ax.tick_params(axis="both", which="minor", labelsize=10)

# Barra de Error

# ax.errorbar(x, y, xerr, yerr, fmt="o", lindewidth=2, capsize=6)


# Saving Figure

plt.savefig("RadVsPos.png")
plt.show()

#Fit de Rad vs InvSq
a,b = np.polyfit(invsqpos, rad, 1)

def fit(x,a,b):
    
    y = a*(x)+b
    
    return y

fit = fit(invsqpos,a,b)

# FIGURE 2
# Plotting de Rad vs 1/x^2

fig2, ax2 = plt.subplots()
ax2.scatter(invsqpos, rad, color="black")
ax2.plot(invsqpos, fit, color="black")
fig2.set_size_inches(8, 6)
plt.grid(True)

# Labels

ax2.set_title("Radiación vs. Inverso Cuadrado de Distancia", fontsize=15)
ax2.set_ylabel("Rad (mV)", fontsize=12)
ax2.set_xlabel("$1/x^2$ ($cm^{-2}$)", fontsize=12)

# Tick Settings

ax2.tick_params(axis="both", which="major", labelsize=12)
ax2.tick_params(axis="both", which="minor", labelsize=10)

# Saving Figure

plt.savefig("RadVsInvSqPos.png")
plt.show()


'''
CÁLCULOS DE ERROR PARA EL INVERSO DEL CUADRADO DE LA POSICIÓN
'''

errx = 0.1
errxrel = (0.1/pos) * 100
errx2rel = 2*(errxrel) #Error de el inverso cuadrado

print('Error de Inverso Cuadrado de Posición:')    
for i in errx2rel:
    
    print(i)  # Verificar si se está leyendo el documento .txt de forma correcta.


