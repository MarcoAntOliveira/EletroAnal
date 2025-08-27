from DyMat import DyMatFile
import matplotlib.pyplot as plt

# Caminho absoluto
res_file = "/home/marco/projects/9semestre/eletroanal/build/LimitadorTensao_res.mat"
mat = DyMatFile(res_file)

# Exemplo: pegar tempo e variáveis
time = mat.abscissa('R1.i')[0]
v_fonte = mat.data('fonte.p.v')[0]
i_diodo = mat.data('D1.i')[0]

plt.plot(time, v_fonte, label='Tensão da Fonte')
plt.plot(time, i_diodo, label='Corrente no Diodo')
plt.legend()
plt.show()

