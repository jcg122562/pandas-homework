import pandas as pd
import matplotlib.pyplot as plt
import os

# uncomment these two lines so you can see all the records when you print or write instead of dot dot dot ...
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

def pretty_print(name, to_print):
    print(f'{name} ')
    print(f'{to_print}\n\n')


# filename where to print the output for my reference
f = open("data/my_output.txt", "w+")

# read / load  the file
df = pd.read_csv(filepath_or_buffer='data/tweets.csv',
                 sep=',',
                 header=0)  # header starts in first line

# 1. General information

pretty_print("Columns ", df.columns)
pretty_print("index ", df.index)
pretty_print("dtypes ", df.dtypes)
pretty_print("shape ", df.shape)
pretty_print("info ", df.info())
pretty_print("describe ", df.describe())
pretty_print("null check", df.isnull())
pretty_print("length", len(df))  # output total records

# 2 Print 'handle', 'text', 'is_retweet', 'time', 'lang', 'retweet_count', 'favorite_count' columns

# There is no need to clean other columns as I will not be using them.  I can drop them however, for now, I will just
# select the columns that I need to use.

# Add ActualDate in the last column
df['actual_date'] = df['time'].str[:10]
# Change data type of actual_date
df['actual_date'] = pd.to_datetime(df['actual_date'], format='%Y/%m/%d')

df2 = df[['handle', 'text', 'is_retweet', 'time',
          'actual_date', 'lang', 'retweet_count', 'favorite_count']]

pretty_print("Selected Columns ", df2.to_string())
pretty_print("Checking n unique values for each column", df2.nunique())
pretty_print("index ", df2.index)
pretty_print("dtypes ", df.dtypes)


# Filter dates > 04/01/2019
# pretty_print("Selecting rows by multiple criteria",
#              df2[(df2['actual_date'] >= '2016-04-01') & (df2['actual_date'] >= '2016-09-30')])

df2.sort_values(by=['actual_date'])
df2 = df2[(df2['actual_date'] >= '2016-4-1') & (df2['actual_date'] <= '2016-9-30')]
print(df2.to_string())
# pretty_print("Filter Dataframe for date >=04/01/2016", df2[df2['actual_date'] >= '2016-04-01'].to_string())


# Correlation
pretty_print("Correlation ", df2.corr().to_string())

# Correlation output.  This shows that the retweet count and favorite_count are positively correlated.
#                 is_retweet  retweet_count  favorite_count
# is_retweet        1.000000      -0.077440       -0.141131
# retweet_count    -0.077440       1.000000        0.928429
# favorite_count   -0.141131       0.928429        1.000000


# Split the text column  - this part will handle the splitting of text column to create a new dataframe

# df2 = df[['handle', 'text', 'time', 'lang', 'retweet_count', 'favorite_count']]
#
# new_df = pd.DataFrame(df.text.str.split(' ').tolist(), index=[df.time, df.handle]).stack()
# for i in new_df:
#     print(i)

# Advanced homework part
pretty_print("new dataframe", df2.to_string())
pretty_print("selected columns", df2.columns)

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(df2['retweet_count'], color='red')
plt.title('Retweet by Index')
plt.xlabel('Index')
plt.ylabel('retweet_count')
plt.savefig(f'plots/retweet_by_candidate.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(df2['handle'], df2['favorite_count'], color='b')
plt.title('Candidate Favorites')
plt.xlabel('handle')
plt.ylabel('favorite_count')
plt.savefig(f'plots/candidate_favorite.png', format='png')

plt.close()

# more plots coming -with group by and sorting.
