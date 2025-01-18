import pandas as pd
from catboost import CatBoostClassifier
from catboost.datasets import titanic

# Загружаем датасет
data, _ = titanic()
data.to_csv('titanic.csv', index=False)

