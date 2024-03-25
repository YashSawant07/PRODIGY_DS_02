import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("C:\\Users\\YASH\\Desktop\\text.csv")
print(data)

print(data.info)

print(data.describe())

# to check for missing values of data
print(data.isnull().sum())

data.dropna(subset=["Embarked"],inplace= True)
data["Cabin"].fillna("Unknown", inplace=True)
data["Age"].fillna(data["Age"].mean(), inplace= True)

print(data.isnull().sum())

print(data.duplicated().sum())

# create a box plot of Age vs survived
sns.boxplot(x='Cabin', y='Age', data=data)
plt.show()

plt.figure(figsize=(6,3))
sns.scatterplot(data=data, x="Age", y="Fare", hue="Survived")
plt.title("Scatter plot of Age vs Fire")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend(title= "Survived")
plt.show()

# this plot shows number of survival gender wise
plt.figure(figsize=(6,3))
sns.countplot(data=data, x="Sex", hue="Survived")
plt.title("Survival by gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title= "Survived", loc="upper right")
plt.show()
