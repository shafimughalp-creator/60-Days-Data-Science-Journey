
# Day 2 – Statistics Basics with NumPy

Concepts Covered:
- Mean
- Standard Deviation
- Variance
- Outlier Detection

Example Dataset:
[100, 105, 98, 102, 500]

Observation:
500 is an outlier; it’s very far from other numbers. This increases the standard deviation.

Code:
```python
import numpy as np

DATASET = np.array([100,105,98,102,500])
print("Standard Deviation:", np.std(DATASET))

