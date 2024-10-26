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
print(df.describe())