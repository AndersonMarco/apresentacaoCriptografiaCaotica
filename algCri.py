def alloc(n):
    i=0
    ret=[]
    while(i<n):
        ret.append(None)
        i=i+1

    return ret

v=[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]

s=[1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,
   1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
   0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0,
   1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1,
   1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1,
   0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
   1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1,
   0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]

c=alloc(len(v))
a1=0
a2=0
a3=0
for i in range(43):
    a1=a1+((2**i)*s[i])

for i in range(43):
    a2=a2+((2**i)*s[i+43])

for i in range(42):
    a3=a3+((2**i)*s[i+86])

lambda1=2**64

b=49191317529892137642
p=28*lambda1
o=10*lambda1

w=2000

#============calcula o numero de iteracoes necessarias============
#============necessario para criar os vetores que=================
#============guardam a evolucao das variveis x,y,z================
ite=w*len(v)
x=alloc(ite+1)
y=alloc(ite+1)
z=alloc(ite+1)
#======================fim==================

dt=184467440737095516

x[0]=(3*lambda1)+a1
y[0]=(5*lambda1)+a2
z[0]=(7*lambda1)+a3

for n in range(ite):
    x[n+1]=x[n]+((dt*((o*(y[n]-x[n]))>>64))>>64)
    y[n+1]=y[n]+((dt*(((x[n]*(p-z[n]))>>64)-y[n]))>>64)
    z[n+1]=z[n]+((dt*(((x[n]*y[n])>>64)-((b*z[n])>>64)))>>64)

for j in range(len(c)):
    c[j]=v[j]^(x[j*w]&1)

#============imprime o valor c[j] na tela=========================
for cj in c:
    print str(cj)+",",
#======================fim==================
