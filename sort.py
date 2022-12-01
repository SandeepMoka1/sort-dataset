import numpy as np

Data = []
Data = np.genfromtxt("/sort/data.txt", dtype=int,encoding=None, delimiter=",")

print("Original array")
print(Data)
print("Sorted array")
print(sorted(Data))
