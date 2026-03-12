 import matplotlib.pyplot as plt

FRR_list = [sum(d >= t for d in alice)/len(alice) for t in thresholds]
FAR_list = [sum(d < t for d in eve)/len(eve) for t in thresholds]

plt.plot(thresholds, FRR_list, marker='o', label='FRR')
plt.plot(thresholds, FAR_list, marker='x', label='FAR')
plt.xlabel('Threshold')
plt.ylabel('Rate')
plt.title('FAR vs FRR')
plt.legend()
plt.grid(True)
plt.show()
alice = [0.27,0.079,0.27,0.36,0.25]
eve = [1.2,0.77,0.88,0.39,0.51]

thresholds = [0.25,0.3,0.35,0.4,0.45,0.5,0.55]

for t in thresholds:
    FRR = sum(d >= t for d in alice) / len(alice)
    FAR = sum(d < t for d in eve) / len(eve)
    
    print("----------------")
    print("Threshold:", t)
    print("FRR:", FRR)
    print("FAR:", FAR)
