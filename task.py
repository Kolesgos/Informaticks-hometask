import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
from math import ceil

def Ep1():
    for i in range(5):
        file = open(f'dead_moroz/00{i+1}.dat', 'r')
        X = []; Y = []
        for j in range(int(file.readline())):
            x, y = map(float, file.readline().split())
            X.append(x)
            Y.append(y)
        fig, axs = plt.subplots()
        axs.scatter(X, Y, s = 17-4*i)
        axs.axis('equal')
        fig.savefig(f'00{i+1}.pdf')  
        fig.show()
        file.close()

def Ep2():
    file = open('frames.dat', 'r')
    data = list(file.read().split('\n'))
    fig, axs = plt.subplots(ceil(len(data)//6), 3, figsize=(11, 11), sharey=True)
    for i in range(len(data)//2):
        X = list(map(float,data[i*2].split()))
        Y = list(map(float,data[i*2+1].split()))
        axs[i//3][i - i//3*3].set_ylim([-12, 12])
        axs[i//3][i - i//3*3].set_xlim(min(X), max(X))
        axs[i//3][i - i//3*3].plot(X, Y)
        axs[i//3][i - i//3*3].set_title(f"Frame{i}")
        axs[i//3][i - i//3*3].grid()
        axs[i//3][i - i//3*3].xaxis.set_ticks([i for i in range(0, int(max(list(map(float,data[i*2].split()))))+1, 2)])
        axs[i//3][i - i//3*3].yaxis.set_ticks([i-12 for i in range(0, 24, 2)])
    fig.savefig(f'Frames.pdf')      
    fig.show()
    
def Ep3():
    preps = []
    group = []
    marks_per_preps = []    
    marks_per_group = [] 
    for i in csv.reader(open("students.csv", encoding='utf-8'), delimiter = ";"):
        if (i[0] in preps):
            marks_per_preps[preps.index(i[0])][int(i[2])] += 1
        else:
            marks_per_preps.append([0 for i in range(11)])
            preps.append(i[0])
        if (i[1] in group):
            marks_per_group[group.index(i[1])][int(i[2])] += 1
        else:
            marks_per_group.append([0 for i in range(11)]) 
            group.append(i[1])
            
    fig, ax = plt.subplots(2, 1, figsize=(6, 9), sharey=True)
    
    bottom = [0 for i in range(len(preps))]
    for i in range(11):
        if ([j[i] for j in marks_per_preps] != [0 for i in marks_per_preps]):
            n = i
            break
    for i in range(n, 11):
        ax[0].bar(preps, [j[i] for j in marks_per_preps], label=str(i), bottom = bottom)
        for k in range(len(preps)):
            bottom[k] += [j[i] for j in marks_per_preps][k]
    ax[0].legend()
    
    bottom = [0 for i in range(len(group))]
    for i in range(11):
        if ([j[i] for j in marks_per_group] != [0 for i in marks_per_group]):
            n = i
            break
    for i in range(n, 11):
        ax[1].bar(group, [j[i] for j in marks_per_group], label=str(i), bottom = bottom)
        for k in range(len(group)):
            bottom[k] += [j[i] for j in marks_per_group][k]
    ax[0].legend(loc = 'upper right')
    ax[0].set_title("Marks per prep")
    ax[1].legend(loc = 'upper right')
    ax[1].set_title("Marks per group")
    fig.savefig('Marks.pdf')
    
def main():
    n = int(input("Введите номер эпизода:\n"))
    if (0 < n < 4):
        exec(f"Ep{n}()")
    else:
        print("Такой эпизод еще не снят:)")
        main()
main()