import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
E = 20       # Tensão da fonte (V)
R = 1e3      # Resistor (Ohms)

# Parâmetros do diodo (modelo Shockley aproximado)
Is = 1e-12   # Corrente de saturação (A)
n = 1.7      # Fator de idealidade
Vt = 25.8e-3 # Tensão térmica a 300K (V)

# Faixa de tensão no diodo
Vd = np.linspace(0, E, 1000)

# Curva do diodo
Id_diodo = Is * (np.exp(Vd / (n*Vt)) - 1)

# Reta de carga: Id = (E - Vd)/R
Id_reta = (E - Vd) / R

# Encontrar ponto de operação (interseção)
# Diferença entre as curvas
diff = np.abs(Id_diodo - Id_reta)
idx = np.argmin(diff)  # índice da menor diferença
Vq, Iq = Vd[idx], Id_diodo[idx]

# Plotagem
plt.figure(figsize=(8,6))
plt.plot(Vd, Id_diodo, label="Curva do diodo", linewidth=2)
plt.plot(Vd, Id_reta, label="Reta de carga", linewidth=2)
plt.plot(Vq, Iq, 'ro', label=f'Ponto Q: Vd={Vq:.2f} V, Id={Iq*1e3:.2f} mA')

plt.title("Curva característica do diodo e reta de carga")
plt.xlabel("Tensão no diodo Vd (V)")
plt.ylabel("Corrente Id (A)")
plt.ylim(0, 0.03)  # até 30 mA (ajustável)
plt.grid(True)
plt.legend()
plt.show()