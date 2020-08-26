import sympy as S

x = S.Symbol('x')
y = S.Symbol('y')
z = S.Symbol('z')
a = S.Symbol('a')
b = S.Symbol('b')
c = S.Symbol('c')
m = S.Symbol('m')
n = S.Symbol('n')

#print(S.solve([-3+4-m,-n-2-1],[m,n]))
#print(S.solve([3*x+5*y-a-2,2*x+3*y-a,x+y-8],[x,y,a]))
print(S.solve(x**2+x-12,x))