import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return 12.7380965*np.exp(-0.253777499*x)
x = np.linspace(0,500,500)
y = f(x)
fig8, ax8 = plt.subplots()
ax8.plot(y,x)

# DAta for Plotting0000
t = [-28.135, -26.09, -24.2, -22.19, -20.04, -15.1, -10.1, -4.97, 0, 5.02, 10.106, 15.07, 20.15, 22.18, 24.2, 26.16, 28.16]
c = [-7.3, -2.41, -0.97, -0.37, -0.16, -0.03, -0.01, 0, 0, 0, 0, 0.2, 0.11, 0.26, 0.68, 1.94, 5.29]
##print(len(t)==len(c))
# Data for plotting1111
tension_v = [0, 0.935, 1.98, 2.93, 4.01, 4.96]
corriente_ma = [0, 0.42, 0.84, 1.33, 1.82, 2.26]

ttension_v = [0, 0.98, 1.99, 2.95, 4.04, 4.97]
tcorriente_ma = [0, 0.05, 0.1, 0.15, 0.2, 0.26]

# Data for plotting2222
tiempo = [20, 40, 60, 80, 100, 120, 140]
resistencia = [382, 313, 235, 178, 138, 110, 91]


fig, ax = plt.subplots()
ax.plot(t , c)

ax.set(xlabel='Tension (V)', ylabel='Corriente(mA)',
    title='I/V ( 21)(IF) )')
ax.set_xlim([-30, 30])
ax.set_ylim([-8, 8])
ax.grid()
fig.savefig('21IF.png')

fig1, ax2 = plt.subplots()

ax2.plot(tension_v , corriente_ma,label = 'Sense caputxó')
ax2.plot(ttension_v , tcorriente_ma,label = 'Amb el caputxó')

ax2.set(xlabel='Corriente(mA) ', ylabel='Tension (V)',
    title='Tension/Corriente ( 27)(IF) )')
ax2.set_xlim([0, 5])
ax2.set_ylim([0, 0.5])
ax2.legend()
ax2.grid()
#fig1.savefig('27IF.png')

fig2, ax3 = plt.subplots()
ax3.plot(tiempo , resistencia)

ax3.set(xlabel='Variacions de temperatura (C°) ', ylabel='Resistència (Ω)',
    title='Tension/Corriente')
ax3.grid()

##fig.savefig("f27.png")
##plt.legend()
##plt.show()
