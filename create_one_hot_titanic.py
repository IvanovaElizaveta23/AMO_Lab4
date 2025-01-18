from create_filtered_titanic import filtered_data
import pandas as pd

# One-hot encoding для 'Sex'
one_hot_data = pd.get_dummies(filtered_data, columns=['Sex'], drop_first=True)
one_hot_data.to_csv('one_hot_titanic.csv', index=False)