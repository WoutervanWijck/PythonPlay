import numpy as np
import pandas as pd
Testing = 'dit is gewoon even testen'
print(Testing)

df = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df)

df2 = pd.DataFrame(df, columns=['Kolom 1', 'Kolom 2', 'Kolom 3'])
print(df2)