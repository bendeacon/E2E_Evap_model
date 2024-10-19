import pandas as pd
import numpy as np

df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])

# df.filter(items=['mouse'])

value_list = ["mouse"]
boolean_series = df.index.isin(value_list)
filtered_df = df[boolean_series]


print(filtered_df)