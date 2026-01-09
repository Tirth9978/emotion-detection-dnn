import pandas as pd

test = pd.read_csv("test.csv")
training = pd.read_csv("training.csv")
validation = pd.read_csv("validation.csv")

print(test["label"].value_counts())

test.head(), training.head(),validation.head()