import pandas as pd
import random

students = {
    'name': ['Bob','John','Anna','Michael','Mary','Nik','Olya','Linda','Kamala','Jack'],
    'Math': [random.randint(3,5) for i in range(10)],
    'Geography': [random.randint(3,5) for i in range(10)],
    'English': [random.randint(3,5) for i in range(10)],
    'Russian': [random.randint(3,5) for i in range(10)],
    'Reading': [random.randint(3,5) for i in range(10)]
}

df = pd.DataFrame(students)
print(df.head())

subjects = df.columns[1:5].tolist() #Список предметов

#Расчет средних значений
print("\n")
for subject in subjects:
    print(f"Средняя оценка по {subject} = {df[subject].mean()}")

#Расчет медиан
print("\n")
for subject in subjects:
    print(f"Медианная оценка по {subject} = {df[subject].median()}")

#Расчет средне-квадр. отклонений
print("\n")
for subject in subjects:
    print(f"Ср. квадр. отклонение по {subject} = {df[subject].std()}")

#Расчет Q1 и Q2 по математике
Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f"\nКвартили по Math:\nQ1 = {Q1_math}\nQ3 = {Q3_math}\nIQR = {IQR}")