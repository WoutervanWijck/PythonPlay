import numpy as np
import pandas as pd
Testing3 = 'dit is gewoon even testen'
print(Testing3)

df = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df)

df2 = pd.DataFrame(df, columns=['Kolom 1', 'Kolom 2', 'Kolom 3'])
df3 = df2.copy()
df2.insert(0, "Kolom 0", [10, 11, 12])

print(df2)
print(df3)
tag = 'dit is een tag'
new = 'we gaan nu proberen dit in VS Code te krijgen'

branc = 'We gaan kijken of dit te mergen valt'