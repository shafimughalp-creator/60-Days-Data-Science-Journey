
# **Q18.** Write np.where() code to create a passed column:
# - True if attendance >= 75
# - False otherwise

import pandas as pd 
import numpy as np


data = pd.DataFrame({
    "attendance" : [60,65,70,75,80,85,90]
})

check_attendance = np.where(data["attendance"]>= 75  ,"True" , "False")
print(check_attendance)

