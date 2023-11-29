
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

# make data:

y = [4.8, 5.5, 3.5, 4.6, -6.5, 6.6, 2.6, 3.0, 4.0, -10, -11, 5] #siia klientide arvud 12 kuu kaupay
x = 0.5 + np.arange(len(y)) #8 peab vastama listi pikusele?
# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=0.5, edgecolor="white", linewidth=0.7, label="Kliendid")

ax.set(xlim=(0, 12), xticks=np.arange(1, 13),
       ylim=(0, max(y)+1), yticks=np.arange(0, max(y))) #y np.arange on hallide kriipsude kogus, vasak korgus
ax.set_xticklabels(['zero','two','four','six', "a", 'zero','two','four','six', "a", "e", "h"])#peab olema sama kogus kui on y vaartuseid
for i, v in enumerate(y):
    plt.text(i +0.5, v, str(v), color='black', ha='center', va='bottom')
    
print(np.average(y))

plt.legend()
plt.title("Klientide muutus") #pealkiri
plt.xlabel("aastad") #x vaarttuste pealkiri
plt.ylabel("klientide arv")
plt.show()