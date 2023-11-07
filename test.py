
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data:

y = [4.8, 5.5, 3.5, 4.6, -6.5, 6.6, 2.6, 3.0, 4.0] #siia klientide arvud 12 kuu kaupay
x = 0.5 + np.arange(len(y)) #8 peab vastama listi pikusele?
# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=0.5, edgecolor="white", linewidth=0.7, label="Kliendid")

ax.set(xlim=(0, 12), xticks=np.arange(1, 13),
       ylim=(0, max(y)+1), yticks=np.arange(1, max(y))) #y np.arange on hallide kriipsude kogus, vasak korgus

plt.legend()
plt.title("Klientide kasv") #pealkiri
plt.xlabel("kuud") #x vaarttuste pealkiri
plt.show()