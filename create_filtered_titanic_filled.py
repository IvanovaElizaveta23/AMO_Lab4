from create_filtered_titanic import filtered_data

# Заполнение пропусков средним значением
mean_age = filtered_data['Age'].mean()
filtered_data.loc[:, 'Age'] = filtered_data['Age'].fillna(mean_age)
