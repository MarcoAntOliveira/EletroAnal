import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 1e3       # 1 kΩ
C = 1e-6      # 1 µF
f = 1000      # 1 kHz sinal de entrada
T = 1/f
t = np.linspace(1, 3*T, 1000)
vin = np.sign(np.sin(2*np.pi*f*t))  # onda quadrada +/-1 V

# Simulação aproximada de clamp
vout = []
vc = 0
for v in vin: 
    # Diodo ideal: se tensão de saída < 0V, capacitor carrega
# --- Clampeador positivo (negativos presos em 0): desloca para cima
    if v + vc < 0:          # saída tenderia a ficar < 0
        vc = -v             # diodo conduz e "zera" a saída

    # --- Clampeador negativo (diodo invertido: positivos presos em 0): desloca para baixo
    if v + vc > 0:          # saída tenderia a ficar > 0
        vc = -v             # diodo conduz e "zera" a saída


plt.figure(figsize=(10,4))
# plt.plot(t, vin, label="Entrada $v_i$")
plt.plot(t, vout, label="Saída $v_o$")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.grid(True)
plt.show()
