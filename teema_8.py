import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,10,1)
y=2*x**2-4*x+5
plt.figure(facecolor="yellow")
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('y=2*x**2-4*x+5')
plt.title('Graafik')
plt.grid()
plt.savefig('graafik.png')
plt.show()

x=np.linspace(-10,10,100)
y=2*x**2-4*x+5
plt.figure(facecolor="yellow")
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('y=2*x**2-4*x+5')
plt.title('Graafik')
plt.grid()
plt.savefig('graafik.png')
plt.show()


x=[1,2,3,4,5]
y=[10,20,25,30,35]
plt.plot(x,y,linestyle="--",marker="D",markersize=5,color="lightgreen")
plt.xlabel('X-telg')  #telg-axis
plt.ylabel('Y-telg')
plt.title('Lihtne graafik')
plt.show()

plt.scatter(x,y)
plt.plot(x, y, color='pink', marker="D",label="Punktidest diagramm")
plt.show()

plt.bar(x,y,color='lightpink',label="Tulpdiagramm")
plt.legend()
plt.show()

# histogramm
# sektordiagramm
x=["A=20%","B=30%"]
y=["C=40%","D=45%"]
y=np.array([50,25,25,15])
mylabels=["20%","30%","45%","50%"]
plt.pie(y,labels="mylabels")
plt.show()

plt.hist(x,y,color='lightpink',label="Histogramm")
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# 1. Failist lugemine
linnad = []
rahvaarvud = []

with open("rahvaarv.txt", encoding="utf-8") as f:
    for rida in f:
        osad = rida.strip().split()
        linn = " ".join(osad[:-1])
        arv = int(osad[-1])
        linnad.append(linn)
        rahvaarvud.append(arv)

# 2. NumPy array töötluseks
arvud_np = np.array(rahvaarvud)

# 3. Statistika
koguarv = arvud_np.sum()
keskmine = arvud_np.mean()
suurim = arvud_np.max()
väikseim = arvud_np.min()
suurima_linn = linnad[np.argmax(arvud_np)]
väikseima_linn = linnad[np.argmin(arvud_np)]

# 4. Tulemuste printimine
print(f"Koguarv: {koguarv}")
print(f"Keskmine: {keskmine:.1f}")
print(f"Suurim: {suurima_linn} ({suurim})")
print(f"Väikseim: {väikseima_linn} ({väikseim})")

# 5. Tulpdiagramm
plt.figure(figsize=(10, 6))
plt.bar(linnad, rahvaarvud, color="skyblue")
plt.title("Eesti linnade rahvaarv")
plt.xlabel("Linn")
plt.ylabel("Elanike arv")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




