import numpy as np
import matplotlib.pyplot as plt

# 1. Failist lugemine
maed = []
kõrgused = []

with open("maed.txt", encoding="utf-8") as f:
    for rida in f:
        k = rida.strip().split()
        mae = " ".join(k[:-1])
        arv = int(k[-1])
        maed.append(mae)
        kõrgused.append(arv)

# 2. NumPy array töötluseks
kõrgused_np = np.array(kõrgused)

# 3. Statistika
summa = kõrgused_np.sum()
keskmine = kõrgused_np.mean()
suurim = kõrgused_np.max()
väikseim = kõrgused_np.min()
suurima_mae = maed[np.argmax(kõrgused_np)]
väikseima_mae = maed[np.argmin(kõrgused_np)]

# 4. Tulemuste printimine
print(f"Koguarv: {summa}")
print(f"Keskmine: {keskmine:.1f}")
print(f"Suurim: {suurima_mae} ({suurim})")
print(f"Väikseim: {väikseima_mae} ({väikseim})")


# 5. Tulpdiagramm
plt.figure(figsize=(10, 6))
plt.bar(maed, kõrgused, color="lightpink")
plt.title("Kõrgeimad mäed maailmas")
plt.xlabel("Maed")
plt.ylabel("Kõrgus")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik.png")
plt.show()

maed_np=np.array(maed)
sort_indx=np.argsort(kõrgused_np)
sort_m=maed_np[sort_indx]
sort_kõr=kõrgused_np[sort_indx]

plt.figure(figsize=(10, 6))
plt.bar(sort_m,sort_kõr,color="salmon")
plt.title("Kõrgeimad mäed sorteeritud")
plt.xlabel("Maed")
plt.ylabel("Kõrgus")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik.png")
plt.show()






