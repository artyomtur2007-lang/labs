from scipy import integrate
d=float(input('Введите нижний предел: '))
b=float(input('Введите верхний предел: '))
#определенный интеграл
def f(x):
    return x**3
result_1=integrate.quad(f,d,b)[0]
#двойной интеграл

def g(a,c):
    return a*c**2
r=int(input('Введите нижний предел с: '))
t=int(input('Введите верхний предел с: '))
y=int(input('Введите нижний предел a: '))
u=int(input('Введите верхний предел а: '))
result_2=integrate.dblquad(g,r,t,lambda a:y,lambda a:u)[0]
print('Результат интегрирования первой функции: ',result_1)
print('Результат интегрирования второй функции: ',result_2)