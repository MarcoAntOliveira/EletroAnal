import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
Vcc = 18.0
Rc = 2200.0
Re = 1100.0

# Parâmetros do modelo (ajuste estes para "encaixar" no gráfico desejado)
beta = 200.0    # ganho DC aproximado
VA = 100.0      # tensão de Early (quanto maior -> curvas mais planas)
turn_on_scale = 0.5  # escala (V) da transição da região de saturação para ativa

# Eixo VCE
Vce = np.linspace(0, 18, 800)

# Valores de corrente de base (como no exercício)
Ib_values = [0, 5e-6, 10e-6, 15e-6, 20e-6, 25e-6, 30e-6]

def ic_model(Ib, Vce, beta=beta, VA=VA, scale=turn_on_scale):
    """
    Modelo simplificado:
      Ic(Vce) = beta*Ib*(1 + Vce/VA) * (1 - exp(-Vce/scale))
    - (1 + Vce/VA) => efeito Early (leve inclinação com VCE)
    - (1 - exp(-Vce/scale)) => transição suave da região saturação -> ativa
    """
    I_plateau = beta * Ib
    I_active = I_plateau * (1 + Vce / VA)     # inclinação por Early effect
    soft_start = 1.0 - np.exp(-Vce / scale)   # garante Ic ~ 0 para Vce~0, sobe rápido
    Ic = I_active * soft_start
    return Ic

# Reta de carga (inclui correção de Re considerando Ib)
R_load = Rc + (1.0 + 1.0/beta) * Re
Ic_load = (Vcc - Vce) / R_load
Ic_load = np.clip(Ic_load, 0, None)  # não ter correntes negativas

# Plot
plt.figure(figsize=(9,6))
for Ib in Ib_values:
    Ic = ic_model(Ib, Vce)
    line, = plt.plot(Vce, Ic*1e3, label=f"Ib = {Ib*1e6:.0f} µA")  # mA
    # encontra ponto de interseção com a reta de carga
    idx = np.argmin(np.abs(Ic - Ic_load))
    Vq = Vce[idx]
    Iq = Ic[idx]
    plt.plot(Vq, Iq*1e3, 'o', color=line.get_color(), markersize=5)
    # imprime no terminal as coordenadas de ponto Q
    print(f"Ib={Ib*1e6:>2.0f} µA -> Q: VCE={Vq:.3f} V, IC={Iq*1e3:.3f} mA")

# plota a reta de carga
plt.plot(Vce, Ic_load*1e3, 'k--', linewidth=2, label="Reta de carga")

plt.xlabel("VCE (V)")
plt.ylabel("IC (mA)")
plt.title("Curvas características do transistor (modelo simplificado) + Reta de carga")
plt.grid(True)
plt.legend()
plt.xlim(0, 18)
plt.ylim(0, 7.0)
plt.tight_layout()
plt.savefig("curvas_transistor.png")
plt.show()
