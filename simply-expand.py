import sympy as S
x = S.Symbol('x')
y = S.Symbol('y')
z = S.Symbol('z')
a = S.Symbol('a')
b = S.Symbol('b')
c = S.Symbol('c')
#化简
print(S.simplify(S.sin(x)**2 + S.cos(x)**2))  #等同于下式（化简表达式中的三角函数）
print(S.trigsimp(S.sin(x)**2 + S.cos(x)**2))

print(S.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))  #等同于下式（约分）
print(S.cancel((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))
#分解--表达式进行部分分式分解，它将一个有理函数变为数个分子及分母次数较小的有理函数
print("====分式分解======")
print(S.apart(1/((x+2)*(x+1)),x))

#三角函数
print(S.sin(x+y).expand(trig=True))

#化简-去括号
print("====去括号======")
f=(a-b+c)*(a+b-c)
print(S.expand(f))

#因式分解
print("====因式分解（去括号逆过程）======")
print(S.factor(a**2 - b**2 + 2*b*c - c**2))

#通分运算 ratsimp()对表达式中的分母进行通分运算，即将表达式转换为分子除分母的形式
print(S.ratsimp(x/(x+y)+y/(x-y)))
print(S.ratsimp(x/a+x/b))

#分母有理化
#radsimp()对表达式的分母进行有理化，结果中的分母部分不含无理数.
print(S.ratsimp(1/(S.sqrt(5))))

#fraction()返回包含表达式的分子与分母的元组， 用它可以获得ratsimp()通分之后的分子或分母
print(S.fraction(S.ratsimp(1/x+1/y)))

#化简三角函数
#trigsimp()化简表达式中的三角函数，通过method参数可以选择化简算法.
print(S.trigsimp(S.sin(x)**2+S.cos(x)**2+2*S.cos(x)))

print(((x+y)**2).expand())#展开
print(((x+y)**2).subs(x,1))#subs(old,new)
print(((x+y)**2).subs(x,y))
print(S.apart(1/((x+2)*(x+1)),x))#分离整式
print(S.apart((x+1)/(x-1),x))
print(S.together(1/x+1/y+1/z))#合并
print(S.together(S.apart((x+1)/(x-1),x),x))