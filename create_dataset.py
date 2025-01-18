import pandas as pd
from catboost import CatBoostClassifier
from catboost.datasets import titanic

# Загружаем датасет
data = titanic()
data.to_csv('titanic.csv', index=False)