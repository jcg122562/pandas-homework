import pandas as pd
import numpy as np


# uncomment these two lines so you can see all the records when you print or write instead of dot dot dot ...
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


def pretty_print(name, to_print):
    print(f'{name} ')
    print(f'{to_print}\n\n')


# filename where to print the output for my reference
f = open("data/output.txt", "w+")


def pretty_write(name, to_write):
    f.write(f'{name}:\r')
    f.write(f'{to_write}\n\n')


def pretty_write2(name, to_write):
    f.write(f'{name} ')
    f.write(f'{to_write}\n\n')


# read the file
insurance = pd.read_csv(filepath_or_buffer='data/insurance.csv',
                        sep=',',
                        header=0)  # header starts in first line
# to_string
pretty_print("2.1 to_string()", insurance.to_string())
pretty_write("2.1 to_string()", insurance.to_string())

# columns
pretty_print("2.2 columns", insurance.columns)
pretty_write("2.2 columns", insurance.columns)

# index
pretty_print("2.3 index", insurance.index)
pretty_write("2.3 index", insurance.index)

# dtypes
pretty_print("2.4 dtypes", insurance.dtypes)
pretty_write("2.4 dtypes", insurance.dtypes)

# shape
pretty_print("2.5 shape", insurance.shape)
pretty_write("2.5 shape", insurance.shape)

# info()

pretty_print("2.6 info()", insurance.info())
pretty_write("2.6 info()", insurance.info(buf=f))

# describe()
pretty_print("2.7 describe()", insurance.describe())
pretty_write("2.7 describe()", insurance.describe())

# print only the column age
pretty_print("3. column age", insurance['age'])
pretty_write("3. column age", insurance['age'])

# print only the columns age, children, and charges
pretty_print("4. columns age, children and charges", insurance[['age', 'children', 'charges']])
pretty_write("4. columns age, children and charges", insurance[['age', 'children', 'charges']])

# print only the first 5 lines and only columns age, children, and charges
pretty_print("5. 1st 5 lines & columns age, children and charges", insurance.loc[[0, 1, 2, 3, 4],
                                                                                 ['age', 'children', 'charges']])
pretty_write("5. 1st 5 lines & columns age, children and charges", insurance.loc[[0, 1, 2, 3, 4],
                                                                                 ['age', 'children', 'charges']])

# print average of charges
pretty_print("6.1 average of charges", round(insurance['charges'].mean(), 2))
pretty_print("6.2 mininum of charges", round(insurance['charges'].min(), 2))
pretty_print("6.3 maximum of charges", round(insurance['charges'].max(), 2))
pretty_write("6.1 average of charges", round(insurance['charges'].mean(), 2))
pretty_write("6.2 mininum of charges", round(insurance['charges'].min(), 2))
pretty_write("6.3 maximum of charges", round(insurance['charges'].max(), 2))

# print age and sex of the person that paid 10797.3362.  Was he/she a smoker

data1 = insurance[insurance['charges'] == 10797.3362]
print(f'7.1 The age of the person is', data1['age'].to_string(index=False))
print(f'7.2 The person is a', data1['sex'].to_string(index=False))
print(f'7.3 Is the person a smoker? ', data1['smoker'].to_string(index=False))

pretty_write2(f'7.1 The age of the person is ', data1['age'].to_string(index=False))
pretty_write2(f'7.2 The person is a', data1['sex'].to_string(index=False))
pretty_write2(f'7.3 Is the person a smoker? ', data1['smoker'].to_string(index=False))

# what is the age of the person who paid the maximum charge?
max_c = insurance[insurance['charges'] == insurance['charges'].max()]

print(f'8. The age of the person that paid the maximum charge is ', max_c['age'].to_string(index=False))
pretty_write2(f'8. The age of the person that paid the maximum charge is ', max_c['age'].to_string(index=False))

# How many insured people do we have for each region?
# note:  Per line, there is the main insured plus the number of children in the children column.
# so the total insured per line is the main insured plus the children

insurance['InsuredPerRow'] = 1 + insurance['children']  # needs to sum the self insured plus the children count
pretty_print("9. New Data frame ", insurance.to_string())
pretty_write("9. New Data frame ", insurance.to_string())

insurance.rename(columns={'InsuredPerRow': 'Insured'}, inplace=True)  # rename the InsuredPerRow to Insured
pretty_print("9. Insured by Region ", insurance.groupby(['region']).agg({'Insured': 'sum'}))
pretty_write("9. Insured by Region ", insurance.groupby(['region']).agg({'Insured': 'sum'}))

# then drop the newly created column to have the original dataframe
insurance.drop('Insured', axis=1, inplace= True)

# How many insured people are children?
pretty_print("10. Insured children total is ", insurance['children'].sum())
pretty_write("10. Insured children total is ", insurance['children'].sum())

# correlation

pretty_print("11. Correlation ", insurance.corr().to_string())
pretty_write("11. Correlation ", insurance.corr().to_string())


# correlation analysis
# 12. 0 Using the Corr() it seems my assumptions are correct:
# 12.1 There is a correlation between age and charges.  The higher the age, the higher the insurance charge
# 12.2 The BMI has more correlation to Charges compared with the number of children.


# pretty_print("4. columns age, children and charges", insurance[['bmi', 'children', 'charges']].to_string())
# pretty_print("11. Correlation ", insurance[['bmi', 'children', 'charges']].corr().to_string())
