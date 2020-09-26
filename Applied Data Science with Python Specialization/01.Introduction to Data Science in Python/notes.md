# intoduction to data science

#week 3
---
## how to merge data
use
```py
df1
df2
how = "inner" , "outer" , "left" , "right"
left_index = True
right_index = True

pd.merge()
```
### Note

**u dont need index to use merge u can use columns it selfs **

```py
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
```

### what happens when we have conflicts between the DataFrames?

The merge function preserves this
information, but appends an _x or_y to help differentiate between which index went with which column of data.

The _x is always the left DataFrame information, and the _ y is always the right DataFrame information.

### Note

we can use 2 indecs to join
```py
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
```

---
## Idiomatic Pandas: Making Code Pandorable

An idiomatic solution is often one which has both high performance and high readability.


chain indexing
```py
df.loc["column1"]['column2']
```
it's bad pandas return a copy of a view depending upon the numpy

it's better to do some thing called methid chaining
```py
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))
```
tradintional way not good but it's working

```py
df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
```
it's noticable to understand the fucntion Map

and applymap

apply

example 1
```py
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df.apply(min_max, axis=1)
```
better
```py
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)
```
### to improve coding
Go look at some of the top ranked
questions on pandas on Stack Overflow, and look at how some of the more experienced
authors, answer those questions.

---
## group by
This function takes some column name or names and splits the dataframe up into
chunks based on those names,
it returns a dataframe group by object.
Which can be iterated upon, and
then returns a tuple where the first
item is the group condition,
and the second item is the data
frame reduced by that grouping.
(condition, hole data frame reduced by the grouping)


### note
99% of the time, you'll use group by on one or more columns.
But you can actually provide a function to group by as well and
use that to **segment your data.**

### note
It's important to note that in order
to do this you need to set the index of
the data frame to be the column
that you want to group by first.


##code
pass in the columns to agg on the fucntion we want to be done
```py
df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
```
### note
Now, I want to flag a potential issue and using the aggregate method
of group by objects.

You see, when you pass in a **dictionary**
it can be used to either to identify
the **columns to apply a function** on or
to **name an output column** if there's
multiple functions to be run.

**The difference depends on the keys that
you pass in from the dictionary and
how they're named.**
this thing has been fixed in new pandas [Stackoverflow](https://stackoverflow.com/questions/60229375/solution-for-specificationerror-nested-renamer-is-not-supported-while-agg-alo)
change
```py
temp['total'] = pd.DataFrame(project_data.groupby(col1)[col2].agg({'total':'count'})).reset_index()['total']

temp['Avg'] = pd.DataFrame(project_data.groupby(col1)[col2].agg({'Avg':'mean'})).reset_index()['Avg']
```

to
```py
temp['total'] = pd.DataFrame(project_data.groupby(col1)[col2].agg(total='count')).reset_index()['total']
temp['Avg'] = pd.DataFrame(project_data.groupby(col1)[col2].agg(Avg='mean')).reset_index()['Avg']
```
`
.agg({'total':'count'})) into
.agg(total='count'))
`


### note

```py
print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))
```


### Note
while much of the documentation
and examples will talk about a single
groupby object,
there's really two different objects.
The data frame groupby and
the series groupby.
And these objects behave a little
bit differently with aggregate.

`
<class 'pandas.core.groupby.generic.DataFrameGroupBy'>

<class 'pandas.core.groupby.generic.SeriesGroupBy'>
`
----
## scales

1. Nominal Scale.
- categorical data
- There are a limited number of teams but changing their order or playing mathematical function to them is meaningless.
- we generally refer to categories where there are only two possible values as binary.

   Nominal variables (also called categorical variables) can be placed into categories. They don’t have a numeric value and so cannot be added, subtracted, divided or multiplied. They also have no order; if they appear to have an order then you probably have ordinal variables instead.

2. Ordinal Scale.
- the order
of values is important
- the differences between the values
are not equally spaced.
- grading method
- **Ordinal data is very common in machine learning and can sometimes be a challenge to work with.**

   The ordinal scale contains things that you can place in order. For example, hottest to coldest, lightest to heaviest, richest to poorest. Basically, if you can rank data by 1st, 2nd, 3rd place (and so on), then you have data that’s on an ordinal scale.

3. Interval Scale.
- units are equally spaced
- no clear absence of value. no True zero
- the temperatures measured in Celsius or Fahrenheit.

   An interval scale has ordered numbers with meaningful divisions. Temperature is on the interval scale: a difference of 10 degrees between 90 and 100 means the same as 10 degrees between 150 and 160. Compare that to high school ranking (which is ordinal), where the difference between 1st and 2nd might be .01 and between 10th and 11th .5. If you have meaningful divisions, you have something on the interval scale.

4. Ratio Scale.
- measurements units are equally spaced and mathematical
- operations, such as subtract, division,
and multiplication are all valid.
- height and weight.

   The ratio scale is exactly the same as the interval scale with one major difference: zero is meaningful. For example, a height of zero is meaningful (it means you don’t exist). Compare that to a temperature of zero, which while it exists, it doesn’t mean anything in particular (although admittedly, in the Celsius scale it’s the freezing point for water).

---
## time in python

### Timestamp
point of time
```py
pd.Timestamp('9/1/2016 10:05AM')
```

### period
span of time specfic date or month
```py
pd.Period('1/2016')
pd.Period('3/5/2016')
```

### DatetimeIndex
it's time stamp index

### PeriodIndex
 it's a period index

### Converting to Datetime
```py
pd.to_datetime('column')
```
 to order

```py
pd.to_datetime('4.7.12', dayfirst=True)
```

### Timedeltas
it's the deffrect in time

```py
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')

pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')
```
---
## Working with Dates in a Dataframe

creat date time index
```py
pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
```

the day it self
```py
df.index.day_name()
````

### find the mean for each month

```py
df.resample('M').mean()
```

### find value for particular year or month as long as the date is the index

```py
df['2017']

df['2016-12']

df['2016-12':]

```
### change the frequnecy of the dates in our DataFrame

```py
df.asfreq('W', method='ffill')
```
