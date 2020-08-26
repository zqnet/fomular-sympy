import sympy as S

x = S.Symbol('x')
y = S.Symbol('y')
z = S.Symbol('z')
a = S.Symbol('a')
b = S.Symbol('b')
c = S.Symbol('c')
fx = -4*x**2+2*x+1
# 解一元二次方程
print(S.solve(fx,x))
# 平方根
print(S.sqrt(2)*S.sqrt(3))
# 去括号
print(S.expand((a+b)**2))
# 方程组
print(S.solve([x+y-1,x-y-3]),[x,y])
# 求和式
i=S.Symbol('i',integer = True)
fx=S.summation(x,(i,1,5))+10*x-15
print(S.solve(fx,x))
# 解一元二次方程
print(S.solve(x**2-2,x))
f = S.solve(x*S.log(4,3)-2,x)
print(f)
#print(S.log(S.E))
#print(S.log(1000,10))
print(S.expand_log(S.log(x*y),force=True))
#约分
fx=(x**2+3*x+2)/(x**2+x)
print(S.cancel(fx))

#三角函数
print(S.solve([S.sin(x-y),S.cos(x+y)],[x,y]))

#求定积分
print(S.integrate(2*x,(x,0,1)))

#求不定积分
print(S.integrate((S.E**x+2*x),x))

#计算结果以小数方式显示
print("exp is e sqrt x")
print(S.exp(2).evalf())

#无穷大的表示方式
print(1+S.oo)

#求平方根
print(S.sqrt(4))

#求n次方根
print(S.root(8,3))

#求阶乘
print(S.factorial(4))

#求三角函数
print(S.sin(S.pi/2))

#支持多元表达式
f=2*x+y
print(f.evalf(subs={x:1,y:2}))

#解方程组
print(S.solve([x+y-1,x-y-3],[x,y]))

#计算求和式 ：x从1到100
print(S.summation(2*x,(x,1,100)))

#解求和的方程
i=S.Symbol('i',integer = True)
print(S.solve(S.summation(x,(i,1,5))+10*x-15,x))

#求极限  x->0
print(S.limit(S.sin(x)/x,x,0))

#求导 diff
print(S.diff(x**2+2*x+1,x))

#变量替换
expr=x+1
print(expr.subs(x,2))

#合并
print(S.together(1/x+1/y+1/z))

#######sympy 表达式变换和化简###########

#化简
print(S.simplify(S.sin(x)**2 + S.cos(x)**2))
print(S.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

#分解--表达式进行部分分式分解，它将一个有理函数变为数个分子及分母次数较小的有理函数
print("分解")
print(S.apart(1/((x+2)*(x+1)),x))

#三角函数
print(S.sin(x+y).expand(trig=True))

#化简-去括号
f=(a-b+c)*(a+b-c)
print(S.expand(f))

#因式分解
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
