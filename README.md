# pybktree-spell-checker

Implementation of BK-tree and Levenshtein distance to perform spell checking.
More details about used algorithms:
* [BK-tree](https://en.wikipedia.org/wiki/BK-tree)
* [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

This library allows you to enter incorrect/misspelled word and perform dictionary search for similar words using some distance function (Levenshtein by default). 

### Performance of algorithms
There two ways how single word search and addition to tree can be performed:
* Using recursion functions
* Not using recursion functions

Too test performance of both functions types I used dictionary of 466544 words. Test single word search unique words where used to see performance without memoization technique.

| Function type                 | Seconds       |
|:------------------------------|:--------------|
| Recursion load dictionary     | ±450          |
| Recursion single search       | ±4.4          |
| Not recursion load dictionary | ±450          |
| Not recursion search          | ±4            |

Results shows that full dictionary loading time is equal using both functions. While single word search os performed better using not recursion function.
All experiments were made on my MacBook Air.

For quicker search memoization optimization technique is used.

### Installation
Two ways to install:

* Clone repo and execute
```
pip install .
```

* Pip install
```
pip install pybktreespellchecker
```

### Usage
By default distance between two words is calculated using Levenshtein distance algorithm. While creating new BKTree instance you can set new distance function. Functionmust accept two parameters and return integer value of those words distance.


```python
from pybktreespellchecker import BKTree
bkt = BKTree() # instance without dictionary and Levenshtein distance function
bkt = BKTree(words=['one', 'two', 'three']) # instance with dictionary and Levenshtein distance function

# custom words distance function
def length_distance(w1, w2):
    return abs(len(w1) - len(w2))
    
bkt = BKTree(words=['one', 'two', 'three'], distance_func=length_distance) # instance with custom distance function and dictionary

bkt = BKTree.from_file('words.txt') # instance with dictionary whitch is loaded from file
```

After you created BKTree instance you can add words to tree using function add_word.
```python
bkt.add_word('hello')
```

Similar word search in BKTree is performed using method search. As a result method returns list of tuples, where first element is distance between words and second element is Node object. Results are sorted by distance value.
```python
result = bkt.search('basketbal', 2)
for i in result:
    print(i[0], i[1].word)
```

If you want to use only Levenshtein distance function.
```python
from pybktreespellchecker import levenshtein_distance
print(levenshtein_distance('kitten', 'sitting'))
print(levenshtein_distance.ratio)
print(levenshtein_distance.distance_matrix)
```