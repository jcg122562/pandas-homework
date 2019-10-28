import pandas as pd


# uncomment these two lines so you can see all the records when you print or write instead of dot dot dot ...
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# filename where to print the output for my reference
f = open("data/output.txt", "w+")


def pretty_write(name, to_write):
    f.write(f'{name}:\r')
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
pretty_write("2.6 info()", insurance.info())

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





