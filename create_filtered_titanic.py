from create_dataset import data
# Создаем новый датасет с нужными признаками
filtered_data = data[['Pclass', 'Sex', 'Age']]
filtered_data.to_csv('filtered_titanic.csv', index=False)