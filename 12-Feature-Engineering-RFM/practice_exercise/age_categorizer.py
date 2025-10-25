'''
 Age Categorizer.
 In a DataFrame with an 'age' column,
 create a new column 'age_group' ('Young', 'Adult', 'Senior')
 using a function with .apply.
 Focus: Creating categorical features.
'''

import pandas as pd
import numpy as np


def categorize_age(age):
    if age <= 19:
        return 'Young'
    elif 20 <= age <= 59:
        return 'Adult'
    else:
        return 'Senior'


data = {
    'user': ['Miguel', 'Sofia', 'Davi', 'Helena', 'Artur', 'Manuela', 'Pedro', 'Laura'],
    'age': [15, 25, 68, 42, 9, 81, 18, 59]
}

df = pd.DataFrame(data)

# Apply the function to the 'age' column to create the new 'age_group' column
df['age_group'] = df['age'].apply(categorize_age)

print(df)