import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
f = 1000      # 1 kHz
T = 1/f
t = np.linspace(0, 2*T, 2000)   # tempo: 2 períodos

# Onda quadrada ±16 V
vin = 16 * np.sign(np.sin(2*np.pi*f*t))

# Mantém só a parte negativa (zera o resto)
vin_neg = np.where(vin < 0, vin, 0)

plt.figure(figsize=(10,4))
plt.xlim(0, 2*T)
plt.ylim(-20, 5)
plt.plot(t, vin_neg, label="Parte negativa da onda quadrada", color="red")

plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)
plt.savefig("6")
plt.show()
