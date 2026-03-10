
# 9️⃣ Visualizing Distribution (Optional but Powerful)

import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.normal( 50 , 10 , 1000 )

plt.hist(data)

plt.title("Normal Distribution Example ")

plt.show()

# This produces a bell curve histogram.