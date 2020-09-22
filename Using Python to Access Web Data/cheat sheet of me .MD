
#Chapter 11 using regexp

### regexp
```regexp
^     start with
$     end                     \$
.     any Char
\s    space
\S    non space
*     repeat 0 or more
*?    not gready
+     one or more
+?    not gready
[asdlasd]   math what is in the set
[^asdladl]  not in the set
[a-z]       in range
[0-9]       in range
() extract start and end
```

### extract data using python

```py
import re
w = what we need to find in regexp
t = the text to look at
re.findall(w , t)
re.findall('[0-9]+' , t)
must have ' '
```
**this returns the thing we are looking for**
### it's gready fucition
```py
import re
w = what we need to find in regexp
t = the text to look at
re.findall(w , t)
re.findall('^F.+:' , t)
```
### stop it with
```py
re.findall('^F.+?:' , t)
```

### find H1 in the some thing
```regexp
<h1>(.+?)<
```

### non blank charater
```regexp
'@([^ ]*)'
```
every thing but blank


get all nums in page
```py
for l in hand:
    l = l.rstrip()
    nums = re.findall('[0-9]+', l)
    for n in nums:
        x = int(n)
        numList.append(x)

y = 0
for j in numList:
            y = y + j
print ( 'There are ' + str(len(numList)) + ' numbers in this file that have a total sum of ' + str(y))
```


# Chapter 12 netwrok and sockets

#url urllib
import
```py
import re
import urllib
```

download link
```py
url = "http://py4e-data.dr-chuck.net/regex_sum_721157.txt"
name = "regex_sum_721157.txt"
urllib.request.urlretrieve(url, name)
```

the charaters have numbers

along
```py
ord('h')
```
```py
chr(71)
```
count every thing
```py
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for l in fhand:
    words = l.decode().split()
    for w in words:
        counts[w] = counts.get(w, 0) + 1
```


open link and grap
```py
url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())
```
open grap find
```py
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page2.htm')
n =  []
for l in fhand:
    w='href="(.+)">'
    l = l.decode().strip()
    find = re.findall(w , l)
    if len(find) > 0:
        n.append(find[0])

print(n) #decode byte >> str # strip remove white spaces in start and the end
```
### takning the head 1 from any page
```py
fhand = urllib.request.urlopen('https://www.coursera.org/learn/python-data-analysis/home/welcome.htm')
n =  []
for l in fhand:
    w='<h1>(.+?)<'
    l = l.decode().strip()
    find = re.findall(w , l)
    if len(find) > 0:
        n.append(find[0])
if len(n) > 0:
        print(n[0]) #decode byte >> str # strip remove white spaces in start and the end
```

## more good web scrap
```py
url = input('Enter - ')
#url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = bs(html, 'html.parser')
tags = soup('a')##dictionary  #anchore tags  
for tag in tags:
    print('print line' , tag.get('href' , None))   #search for the href tag and what that comes after it
    print(tag.contents[0])
print ('the url we entred' ,url)
```

the tags ar
[here](https://www.javatpoint.com/html-tags#:~:text=HTML%20tags%20are%20like%20keywords,HTML%20tags%20are%20unclosed%20tags.)

get h1

```py
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('h1')
for tag in tags:
    print(tag.contents[0])
```
things to get out of the tag
```py
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
```

quiz
```py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# the url start
url = 'http://py4e-data.dr-chuck.net/known_by_Rahman.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# get user input for how many times to search
count = int(input('Enter count:'))

# get user input for which url to click on
position = int(input('Enter position:'))-1

while count >= 1:
    # re-reads the current url
    html = urllib.request.urlopen(url, context=ctx).read()
    # creates a new soup object
    soup = BeautifulSoup(html, 'html.parser')
    # searches the page for all <a> tags
    tags = soup('a')
    # upates the current url
    url = tags[position].get("href", None)
    count = count - 1

print("Retrieving: ", url)
```

out put `Retrieving:  http://py4e-data.dr-chuck.net/known_by_Zaki.html`


# chapter 13 data on the web

we can say that xml and json are data oreinted document that it's goal to communicate 2 language together

### xml
extensible markup language

elemet or node

<people>
  <people>
  </people>
</people>

start tag and end tag
then threr is arrtibutes

<people Attrs="int">

</people Attrs="int">

### xml schema
multi line string in python
```py
data = '''
apaskdpaksdp
aodaskdak
kaodkaskd
'''

tree = et.fromstring(data)
print
```
xml 1
```py
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
```
xml2
```py
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
```
