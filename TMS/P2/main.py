import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import resource
import time

time_start = time.perf_counter()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)




l_0 = 32.6
l_f = 34.3
D_0 = 4.984   #in mm, D_0; Dieser Wert ist mit Unsicherheit behaftet. Versuchen Sie diesen Wert, falls die Ergebnisse nicht zufriedenstellend sind(  ----- ).

A_0 = (np.pi*(D_0/2)**2)*10**(-3*2)  #in m^2

D_f = 3.688 




df = pd.read_excel("CTM Lab. M12-2024.xlsx")
L = df.columns[0]
F = df.columns[1]

with plt.style.context('Solarize_Light2'):
    plt.plot(df[L],df[F],color = 'blue')
plt.title('F-Δl curve (machine’s curve)',fontsize = 18)
plt.xlabel('Δl (mm)',fontsize = 12)
plt.ylabel('F (N)',fontsize = 12)
plt.xlim(0,df[L].iloc[-1]+1)
plt.ylim(0,max(df[F])+5000)
plt.show()

l_f = l_0 +df[L].iloc[-1]-2.2
A_f = (np.pi*(D_f/2)**2)*10**(-3*2)  #in m^2
#el = ((df[L].iloc[-1]-l_0)/l_0)*100
el = ((l_f-l_0)/l_0)*100
ra = ((A_0-A_f)/A_0)*100







df['e']= df[L]/l_0  #Keine Einheit
df['sigma']= (df[F]/A_0)*10**-6  #in MPa
max_sig = max(df['sigma'])
max_e = df.loc[df['sigma'] == max_sig, 'e'].iloc[0]
#print(max_sig,A_0)
########## Steigung[E]
index = df[(df['e'] > 0.025) & (df['e'] < 0.1)]['e'].index

with plt.style.context('Solarize_Light2'):
    plt.plot(df['e'],df['sigma'],color ='blue',label = 'Engineering stress-engineering strain')
    plt.plot(max_e,max_sig,'o', color = 'black', label = 'Ultimate Tensile Strength (UTS).')  
plt.title('σ-e curve (engineering curve)',fontsize = 18)
plt.xlabel('e',fontsize = 12)
plt.ylabel('σ (MPa)',fontsize = 12)
plt.xlim(0,df['e'].iloc[-1]+df['e'].iloc[-1]/6)
plt.ylim(0,max(df['sigma'])+max(df['sigma'])/6)
plt.annotate(f"≈{int(max_sig)+1} MPa", xy=(max_e,max_sig), xytext=(0.15,1050),
             arrowprops=dict(arrowstyle='-'),
             fontsize=8, color='black')
plt.legend(loc = 'upper left')
plt.show()





E1 ,cov = np.polyfit(df['e'][index[0]:index[-1]],df['sigma'][index[0]:index[-1]],1,cov=True)




E = E1[0]
error_s = np.sqrt(cov[0][0])

def sig__(x,c):
    return E*x + c
sig_02 = 0.2/100
cc = -sig_02*E 
y = sig__(df['e'],cc)

sum = 0
rou = 1
inde = []
error = []
for i in range(len(df['e'])):
    if np.round(df['sigma'][i],rou) == np.round(y[i],rou):
        error.append(np.abs(df['sigma'][i]-y[i]))
        sum += 1
        inde.append(i)
        
        #print("AFfffffffffffffffffffffffff_________________________+++++++++++++")
    else:
        continue
        #print("no",np.round(y[i],rou),np.round(df['sigma'][i],rou))

funny = sig__(df['e'],E1[1])
with plt.style.context('Solarize_Light2'):
    plt.plot(df['e'],df['sigma'],color ='blue',label = 'Engineering stress-engineering strain')
    plt.plot(df['e'],funny, '--', color = 'red',label = 'Modulus of elasticity (E) [Slope]',alpha = 0.7)  
    plt.text(0.15, 1100, f"y = {int(E1[0])}*x + {int(E1[1])}", fontsize=8, color='black')
plt.title('σ-e curve (engineering curve)',fontsize = 18)
plt.xlabel('e',fontsize = 12)
plt.ylabel('σ (MPa)',fontsize = 12)
plt.xlim(0,df['e'].iloc[-1]+df['e'].iloc[-1]/6)
plt.ylim(0,max(df['sigma'])+max(df['sigma'])/6)
plt.legend(loc = 'upper left')
plt.show()
'''
print(sum)
print(inde)
print(error)
print(E)
'''
sig02 = y[inde[1]]  # Antworttttttttttttt

with plt.style.context('Solarize_Light2'):
    plt.plot(df['e'],df['sigma'],color ='blue',label = 'Engineering stress-engineering strain')
    plt.plot(df['e'],y, color = 'red', label = 'Yiels Strength at 0.2% (σ_0.2%) line')  
    plt.plot(df['e'].iloc[inde[1]],y[inde[1]],'o', color = 'black', label = 'Yiels Strength at 0.2% (σ_0.2%)')  
plt.title('σ-e curve (engineering curve)',fontsize = 18)
plt.xlabel('e',fontsize = 12)
plt.ylabel('σ (MPa)',fontsize = 12)
plt.xlim(0,df['e'].iloc[-1]+df['e'].iloc[-1]/6)
plt.ylim(0,max(df['sigma'])+max(df['sigma'])/6)
plt.legend(loc = 'upper left')
plt.annotate(f"≈{int(sig02)+1} MPa", xy=(df['e'].iloc[inde[1]],y[inde[1]]), xytext=(0.15,1000),
             arrowprops=dict(arrowstyle='-'),
             fontsize=8, color='black')
plt.show()

Ur = (1/2)*((sig02**2)/E)

Ur2 = np.trapz(df['sigma'][:inde[1]],df['e'][:inde[1]])


MT = np.trapz(df['sigma'],df['e'])

with plt.style.context('Solarize_Light2'):
    plt.plot(df['e'],df['sigma'],color ='blue',label = 'Engineering stress-engineering strain')
    plt.plot(df['e'].iloc[inde[1]],y[inde[1]],'o', color = 'black', label = 'Yiels Strength at 0.2% (σ_0.2%)')  
    plt.fill_between(df['e'][0:inde[1]],df['sigma'][0:inde[1]], color='lightblue', alpha=0.5, label = 'Modulus of resilience (Ur)')

plt.title('σ-e curve (engineering curve)',fontsize = 18)
plt.xlabel('e',fontsize = 12)
plt.ylabel('σ (MPa)',fontsize = 12)
plt.xlim(0,df['e'].iloc[-1]+df['e'].iloc[-1]/6)
plt.ylim(0,max(df['sigma'])+max(df['sigma'])/6)
plt.legend(loc = 'upper left')
plt.annotate(f"≈{int(sig02)+1} MPa", xy=(df['e'].iloc[inde[1]],y[inde[1]]), xytext=(0.15,1000),
             arrowprops=dict(arrowstyle='-'),
             fontsize=8, color='black')
plt.show()
with plt.style.context('Solarize_Light2'):
    plt.plot(df['e'],df['sigma'],color ='blue',label = 'Engineering stress-engineering strain')
    plt.fill_between(df['e'],df['sigma'], color='lightblue', alpha=0.5, label = 'Modulus of toughness (MT)')

plt.title('σ-e curve (engineering curve)',fontsize = 18)
plt.xlabel('e',fontsize = 12)
plt.ylabel('σ (MPa)',fontsize = 12)
plt.xlim(0,df['e'].iloc[-1]+df['e'].iloc[-1]/6)
plt.ylim(0,max(df['sigma'])+max(df['sigma'])/6)
plt.legend(loc = 'upper left')

plt.show()


sigma_max = df['sigma'].max() #Eine Auflosung 5
df['e_R'] = np.log(1+df['e'])
df['sigma_R'] = df['sigma']*np.log(1+df['e'])  #in MPa
print(df)
 
with plt.style.context('Solarize_Light2'):
    plt.plot(df['e'],df['sigma'],color = 'blue',label = 'Engineering stress-engineering strain')
    plt.plot(df['e_R'],df['sigma_R'], color = 'green', label = 'True stress-true strain')  
plt.title('σ-e curve',fontsize = 18)
plt.xlabel('e',fontsize = 12)
plt.ylabel('σ (MPa)',fontsize = 12)
plt.xlim(0,df['e'].iloc[-1]+df['e'].iloc[-1]/6)
plt.ylim(0,max(df['sigma'])+max(df['sigma'])/6)
plt.legend(loc = 'upper left')

plt.show()
print(f"Modulus of elasticity (E) = {E} ± {error_s} MPa\nYiels Strength at 0.2% (σ0.2%) = {sig02} ± {min(error)} MPa\nUltimate Tensile Strength (UTS) = {max_sig} MPa\nReduction in area (%RA) in % = {ra} %\nElongation at break (%EL) in % = {el} %\nModulus of resilience (formula) = {Ur} J/M^3\nModulus of resilience (Graphical method) = {Ur2} J/M^3\nModulus of toughness (MT) = {MT} J/M^3 ")



#print(df)

t = (time.perf_counter() - time_start)

memb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%5.1f secs %5.1f MByte" % (time_start,memb))


