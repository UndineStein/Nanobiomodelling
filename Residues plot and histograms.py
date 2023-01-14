import matplotlib.pyplot as plt
import numpy as np

ro = []
t = []
z = []
t1 = []
Ic = []
Icm = []

tau_1 = 0 
tau_2 = 0
tau_3 = 0
tau_4 = 0
tau_5 = 0
tau_6 = 0
tau_7 = 0
tau_8 = 0
tau_9 = 0

Ic_1 = [] 
Ic_2 = [] 
Ic_3 = []
Ic_4 = []
Ic_5 = []
Ic_6 = []
Ic_7 = []
Ic_8 = []
Ic_9 = []

with open("residues_COM.dat", 'r') as f:
    lines = f.readlines()
    l = len(lines)

    
    for i in range(l):
        t.append(float(lines[i].split()[0])/100)
        z.append(float(lines[i].split()[4]))
        ro.append(np.sqrt((float(lines[i].split()[2]))**2+
                          (float(lines[i].split()[3]))**2+
                          (float(lines[i].split()[4]))**2))

with open("ionic_current.dat", 'r') as f:
    strings = f.readlines()
    l1 = len(strings)
    
    for i in range(l1-1):
        t1.append(float(strings[i].split()[0])/100)
        Ic.append(float(strings[i].split()[1]))
        Icm.append(float(strings[i].split()[2]))

t = t[1::11]

for j in range(1,10):
    exec(f'z_{j} = z[j::11]') 
    exec(f'ro_{j} = ro[j::11]')  
 #   exec(f'Ic_{j} = Ic[j::11]')
    # h = 0.7 D = 1.5  
    for i in range(32199):
        r = eval(f'ro_{j}[i]')
        zet = eval(f'z_{j}[i]')
        if r < 1.5/2 and np.abs(zet) < 0.7:
           # eval(f'ind_{j}.append(i)')
            exec(f'tau_{j} = tau_{j} + 1')
            exec(f'Ic_{j}.append(Ic[i])')

a = np.array([tau_1, tau_2, tau_3, tau_4, tau_5,tau_6,tau_7,tau_8,tau_9])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['tau_1', 'tau_2', 'tau_3', 'tau_4', 'tau_5',
         'tau_6', 'tau_7', 'tau_8', 'tau_9']
ax.bar(langs,a)















































