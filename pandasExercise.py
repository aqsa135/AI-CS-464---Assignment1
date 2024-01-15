# Aqsa Noreen
# 9/6/2023
# CS-462
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    df = pd.read_csv('breast-cancer.csv')
    return df

def most_common_classification(df):
    return df['classification'].value_counts().index[0]

def most_common_age_menopause(df):
    df_recur = df[df['classification'] == 'recurrence-events']
    return df_recur['age'].mode()[0], df_recur['menopause'].mode()[0]

def plot_recurrences_by_age(df):
    df_recur = df[df['classification'] == 'recurrence-events']
    age_groups = df_recur.groupby('age')['classification'].count()
    age_groups.plot(kind='bar')
    plt.title('Recurrences by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Recurrences')

df = read_data()

common_class = most_common_classification(df)
print("Most common classification:", common_class)

common_age, common_menopause = most_common_age_menopause(df)
print("Most common age:", common_age)
print("Most common menopause:", common_menopause)

plot_recurrences_by_age(df)


