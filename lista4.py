import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Dados do problema
IDSS = 8e-3     # 8 mA
Vp = -4.0       # Vp = -4 V
VDD = 16.0      # VDD = 16 V

R1 = 2.1e6      # 2.1 MΩ
R2 = 270e3      # 270 kΩ
RD = 2.4e3      # 2.4 kΩ
RS = 1.5e3      # 1.5 kΩ

# Tensão do gate pelo divisor
VG = VDD * (R2 / (R1 + R2))

# Equação do JFET
def eq(ID):
    VS = ID * RS
    VGS = VG - VS
    return ID - IDSS * (1 - VGS / Vp)**2

# Resolver IDQ numericamente
IDQ = fsolve(eq, 2e-3)[0]  # chute inicial 2mA
VSQ = IDQ * RS
VGSQ = VG - VSQ
VDQ = VDD - IDQ * RD
VDSQ = VDQ - VSQ

print(f"IDQ = {IDQ*1e3:.2f} mA")
print(f"VGSQ = {VGSQ:.2f} V")
print(f"VS = {VSQ:.2f} V")
print(f"VD = {VDQ:.2f} V")
print(f"VDS = {VDSQ:.2f} V")

# Plot da curva ID x VGS
VGS_vals = np.linspace(-6, 1, 200)
ID_vals = IDSS * (1 - VGS_vals/Vp)**2
ID_vals[VGS_vals < Vp] = 0  # abaixo do cutoff, corrente é 0

# Reta de carga da fonte: ID = (VG - VGS)/RS
ID_reta = (VG - VGS_vals)/RS

plt.figure(figsize=(8,6))
plt.plot(VGS_vals, ID_vals*1e3, label="Curva do JFET")
plt.plot(VGS_vals, ID_reta*1e3, label="Reta de carga (fonte)")
plt.scatter([VGSQ], [IDQ*1e3], color="red", zorder=5, label="Ponto Q")

# Mostrar valores do ponto Q no gráfico
plt.text(VGSQ+0.2, IDQ*1e3,
         f"IDQ = {IDQ*1e3:.2f} mA\nVGSQ = {VGSQ:.2f} V",
         fontsize=10, color="red", bbox=dict(facecolor="white", alpha=0.7))

plt.xlabel("VGS (V)")
plt.ylabel("ID (mA)")
plt.title("Curva ID vs VGS com reta de carga e Ponto Q")
plt.legend()
plt.grid(True)
plt.savefig("curva_jfet.png")
plt.show()
