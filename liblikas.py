import matplotlib.pyplot as plt
import numpy as np

plt.figure(facecolor="lightblue")


x1=np.linspace(-9,-1,400)
y1=-1/8*(x1+9)**2+8
plt.plot(x1,y1,markersize=5,color="lightgreen")

x6=np.linspace(1,9,400)
y6=-1/8*(x6-9)**2+8
plt.plot(x6,y6,color="lightgreen")

x3=np.linspace(-9,-8,400)
y3=7*(x3+8)**2+1
plt.plot(x3,y3,color="lightgreen")

x8=np.linspace(8,9,400)
y8=7*(x8-8)**2+1
plt.plot(x8,y8,color="lightgreen")

x4=np.linspace(-8,-1,400)
y4=1/49*(x4+1)**2
plt.plot(x4,y4,color="lightgreen")

x5=np.linspace(1,8,400)
y5=1/49*(x5-1)**2
plt.plot(x5,y5,color="lightgreen")

x7=np.linspace(-8,-1,400)
y7=-4/49*(x7+1)**2
plt.plot(x7,y7,color="pink")


x9=np.linspace(1,8,400)
y9=-4/49*(x9-1)**2
plt.plot(x9,y9,color="pink")

x10=np.linspace(-8,-2,400)
y10=1/3*(x10+5)**2-7
plt.plot(x10,y10,color="pink")

x11=np.linspace(2,8,400)
y11=1/3*(x11-5)**2-7
plt.plot(x11,y11,color="pink")

x12=np.linspace(-2,-1,400)
y12=-2*(x12+1)**2-2
plt.plot(x12,y12,color="pink")


x13=np.linspace(1,2,400)
y13=-2*(x13-1)**2-2
plt.plot(x13,y13,color="pink")


x14=np.linspace(-1,1,400)
y14=-4*x14**2+2
plt.plot(x14,y14,color="brown")

x15=np.linspace(-1,1,100)
y15=4*x15**2-6
plt.plot(x15,y15,color="brown")

x16=np.linspace(-2,0,100)
y16=-1.5*x16+2
plt.plot(x16,y16,color="black")


x17=np.linspace(0,2,400)
y17=1.5*x17+2
plt.fill(x17,y17,color="black")
plt.title("LIBLIKAS")
plt.show()





