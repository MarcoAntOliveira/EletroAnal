from DyMat import DyMatFile
import matplotlib.pyplot as plt

res_file = "/home/marco/projects/9semestre/eletroanal/build/LimitadorTensao_res.mat"
mat = DyMatFile(res_file)

# Tempo
time = mat.abscissa('R1.n.v')[0]  # eixo do tempo

# Tensões
vin  = mat.data('fonte.p.v')[0]
vout = mat.data('R1.n.v')[0]

# Plot
plt.figure(figsize=(10,5))
plt.plot(time, vin, label='Entrada: fonte.p.v')
plt.plot(time, vout, label='Saída: R1.n.v')
plt.xlabel('Tempo [s]')
plt.ylabel('Tensão [V]')
plt.title('Limitador de Tensão com Diodos Antiparalelo')
plt.legend()
plt.grid(True)
plt.show()
