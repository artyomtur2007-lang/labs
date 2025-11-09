import numpy as np
a=input("Введите длины участков через пробел:")
c=a.split()
parts=np.array(c,dtype=float)
b=input("Введите значения скоростей через пробел:")
d=b.split()
speeds=np.array(d,dtype=float)
k=int(input('Введите номер участка въезда'))
p=int(input('Введите номер участка съезда'))
if len(parts)!=len(speeds) or k<1 or k>p or k-1>len(parts):
    print('Неверный ввод')
else:
    dist=sum(parts[k-1:p])
    tot_time=0
    for i in range(k-1,p):
        tot_time+=parts[i]/speeds[i]
    av_speed=dist/tot_time
    print(f"длина пути с k по p участок: {dist},время в пути: {tot_time},средняя скорость: {av_speed}")