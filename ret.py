import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 1e3
C = 1e-6
f = 1000
T = 1/f

t0  = np.linspace(0, T/2, 1000)
t1 = np.linspace(T/2, T, 1000)
t2 = np.linspace(T, 3*T/2, 1000)
t3 = np.linspace(3*T/2, 2*T, 1000)

# Arrays de zeros separados
zeros0 = np.zeros_like(t0)
zeros2 = np.zeros_like(t2)
zeros3 = np.zeros_like(t3)

V = 20
vcc = -0.318*V

vout1 =20 * np.sin(2*np.pi*f*t1)  # onda senoidal 1
tcc = (np.arcsin(vcc/20))/(2*np.pi*f)
print(tcc)

plt.figure(figsize=(10,4))
plt.xlim(0, 2*T)
plt.ylim(-20, 20)


plt.plot(t0, zeros0, label="$1$")
plt.plot(t1, vout1, label="$2$")
plt.plot(t2, zeros0, label="$3$")
plt.plot(t3, vout1, label="$4$")
plt.axhline(y=vcc, color='b', linestyle='--', label='Vcc - 6.36V')
plt.plot([tcc], [vcc], 'ro')  # ponto vermelho
plt.annotate(f'Pico: {vcc:.2f}V', xy=(tcc, vcc), xytext=(tcc+0.0002, vcc+1),
             arrowprops=dict(facecolor='black', shrink=0.05))





plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)
plt.savefig("letraa")
plt.show()
