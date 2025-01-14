import matplotlib.pyplot as plt
import math
import numpy as np

nums = np.random.randint(0,100,20)
sqrt = [math.sqrt(num) for num in nums]

diagrama = plt.subplot()
diagrama.scatter(nums,sqrt)
diagrama.set_title("Diagrama de dispersión")
plt.xlabel("Números random")
plt.ylabel("Raíz cuadrada")
plt.show()
