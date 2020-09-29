# intoduction to data science

---

#week 1

lamda  
lamda then arguments then one single expression
```py
lambda a, b, c : a + b
```

list comprehension

```py
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list
```
same as
```py
my_list = [number for number in range(0,1000) if number % 2 == 0]
my_list
```

quick on numpy

```py
a.dtype
```

Sometimes we know the shape of an array that we want to create, but not what we want to be in it. numpy
offers several functions to create arrays with initial placeholders, such as zero's or one's.
Lets create two arrays, both the same shape but with different filler values

```py
d = np.zeros((2,3))

e = np.ones((2,3))

np.random.rand(2,3)

```
create a **sequence** of **numbers** in an array with the **arrange**()
The **fist** argument is the **starting** bound and the **second** argument is the **ending** bound, and the **third** argument is the **difference** between
each consecutive numbers
```py
np.arange(10, 50, 2)
```
if we want to generate a **sequence** of **floats**, we can use the **linspace**() function.
In this function the **third** argument isn't the difference between two numbers, but the **total number of items you want to generate**

```py
np.linspace( 0, 2, 15 ) # 15 numbers from 0 (inclusive) to 2 (inclusive)
```

### Array Operations
We can do many things on arrays, such as

1. mathematical manipulation
(addition, subtraction, square,exponents)

2. as well as use boolean arrays, which are binary values.

3. We can also do matrix manipulation such
as product, transpose, inverse, and so forth.
if we want to do elementwise product, we use the "*" sign
```py
A*B
```
if we want to do matrix product, we use the "@" sign or use the dot function
```py
A@B
```

4. Numpy arrays have many interesting aggregation functions on them, such as  sum(), max(), min(), and mean()
```py
array3.sum()
array3.max()
array3.min()
array3.mean()
```
**Now, we often think about two dimensional arrays being made up of rows and columns, but you can also think of these arrays as just a giant ordered list of numbers, and the *shape* of the array, the number of rows and columns, is just an abstraction that we have for a particular purpose. Actually, this is exactly how basic images are stored in computer environments**
---

# Week 2

it referd us to the book [learning the pandas library by matt harrison](https://mcgillmsaa.files.wordpress.com/2018/05/learning-the-pandas-library-python-tools-for-data-munging-analysis-and-visual.pdf)

he refered us to the web site  [excellen blog ](https://planetpython.org/)

missing data in pandas

```py
np.nan != None
np.nan also not  np.nan
type(np.nan) = float64
type(None) = object
```

you need to use special functions to test for the presence of not a number,
```py

np.isnan(np.nan)

```



###qeury

if you wanted to see the fourth entry we would we would use the iloc


If you wanted to see what class Molly has, we would use the loc attribute with a parameter

---

## DataFrameDataStructure

The DataFrame is conceptually a two-dimensional series object, where there's an index and multiple columns of content, with each column having a label. In fact, the distinction between a column and a row is really only a conceptual distinction. And you can think of the DataFrame itself as simply a two-axes labeled array.

 One of the powers of the Panda's DataFrame is that you can quickly select data based on multiple axes.

the first is the row index the second is the column it self
```py
df.loc['school1', 'Name']

# we also can take 2 columns
df.loc[:,['Name', 'Score']]

```


**That's selecting and projecting data from a DataFrame based on row and column labels. The key concepts to remember are that the rows and columns are really just for our benefit. Underneath this is just a two axes labeled array, and transposing the columns is easy. Also, consider the issue of chaining carefully, and try to avoid it, as it can cause unpredictable results, where your intent was to obtain a view of the data, but instead Pandas returns to you a copy.**


### drop

```py
copy_df.drop("Name", inplace=True, axis=1)
```

### columns name tips

create some function that does the cleaning and then tell renamed to apply that function across all of the data.
Python comes with a handy string function to strip white space called "strip()".
When we pass this in to rename we pass the function as the mapper parameter, and then indicate whether the axis should be columns or index (row labels)
```py
new_df=new_df.rename(mapper=str.strip, axis='columns')
```
here we are passig the refrence to that function mapper

We can also use the df.columns attribute by assigning to it a list of column names which will directly rename the columns.
This will directly modify the original dataframe and is very efficient especially when you have a lot of columns and you only want to change a few.
This technique is also not affected by subtle errors in the column names, a problem that we just encountered.
With a list, you can use the list index to change a certain value or use list comprehension to change all of the values

As an example, lets change all of the column names to lower case. First we need to get our list
```py
cols = list(df.columns)
#Then a little list comprehenshion
cols = [x.lower().strip() for x in cols] #remove all spaces and also lower all 
#Then we just overwrite what is already in the .columns attribute
df.columns=cols
```


---

#week 3

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


# week 4

week project to test the ability that i have learnt


test the binomial distribution

```py
n = 'number of times to run '
p = ' probability that it lands for the 0 condition'
np.random.binomial(N, p)
```
the modern computional power allows us to simulate the effects of different parameters in the distribution

we dont have to work with the math we can just simulate e the problem instead and see the results
### bimodel distribution
have 2 or more peaks
![image](Screenshot_1.png)

in the end her refered to Allen B. Downey book [thinkstats](https://greenteapress.com/thinkstats2/thinkstats2.pdf)


### Hypothesis Testing
is a core data analysis activity behind experimentation.

A hypothesis is a statement that we can test.

####case
![image](Screenshot_2.png)

We then examine the groups to determine
whether this null hypothesis is
true or not.

If we find that there is
a difference between groups,
then we can reject the null hypothesis and
we accept our alternative(our IDEA).

If we look at the mean values for
the late data frame as well, we get surprisingly similar numbers.

There are slight differences, though.

It looks like the end
of the six assignments,
the early users are doing better
by about a percentage point.


**So, is this enough to go ahead and make some interventions to actually try and change something in the way we teach?**

#### threshold

When doing hypothesis testing, we have to
choose a significance level as a threshold for how much of a chance
we're willing to accept.
This significance level is
typically called **alpha.**
![image](Screenshot_3.png)

which indicates a tolerance for
a probability of between 5% and
1% of chance.

In a physics experiment where the
conditions are much more controlled and
thus, the burden of proof is much higher,
you might expect to see alpha
levels of 10 to the negative 5 or
100,000th of a percentage.

For this example, let's use a threshold
of 0.05 for our alpha or 5%.

### test the hypothesis
The SciPy library contains a number
of different statistical tests and
forms a basis for
hypothesis testing in Python.

A **T test** is one way to compare
the means of two different populations.
In the SciPy library,
the T test end function will
compare two independent samples to
see if they have different means.

#### code
```py
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
```
The result is a two with a test
statistic and a p-value.

The p-value here is much
larger than our 0.05.
So we cannot reject the null hypothesis(our idea was wrong if the null is true)

we need a p value of .05 or less to reject the null and say that our idea is good

#### p hacking
![image](Screenshot_4.png)
