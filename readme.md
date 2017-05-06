Trivago
=======

Trivago is a hotel comparison website. 
This application allows customers of Trivago to compare hotels for a given topic. 
The comparison uses sentiment analysis on review fragments that mention that topic.

Setup
=====
This application is implemented in Python 3. 
The easiest setup is by using the [conda](https://conda.io/docs/install/quick.html) 
package manager.

```
$ conda env create -f environment.yml
$ source activate trivago-env
```

In windows: ``` activate trivago-env ``` (without the ```source```)

Examples
========

The trivago app is a command-line application. See usage example below.


**Loading review files and semantic data:**

```
$ python src/main.py <reviews-dir> <semantics-file>

59 phrases detected
13 intensifiers detected
188 reviews processed for: data/reviews1.json
364 reviews processed for: data/reviews2.json
13 reviews processed for: data/reviews3.json
142 reviews processed for: data/reviews4.json
369 reviews processed for: data/reviews5.json
21588 review fragments scored
9058 words stored in lookup table
```

The semantic file argument is optional, 
by default the semantic file in 'semantics/semantics.json' is loaded.
When no reviews directory is provided, 
the review files in 'data/' are loaded.


**Scoring a topic:**

```
Enter your topic word: room

1 additional topic words found: ['rooms']
1941 sentences found containing the words 'room' or 'rooms'

   HotelID     Score  #Fragments
2    77923  0.411576         311
1    76790  0.375000          24
4    84333  0.318560         722
0  2514817  0.306701         582
3    81363  0.171523         302

Most positive fragment:
The room we were allocated was absolutely fantastic and today we cannot believe how fortunate we were ( 5.0 )

Most negative fragment:
Rooms are very old with dirty carpet and some strange smell ( -3.0 )
```

Topics should be single words. If no topic word is entered, then the scores for all review sentences are used
to compare the hotels.

Tests
========

To run all tests:

```
$ python -m unittest discover test
```

Design
============

The trivago application analyzes review sentences to determine a sentiment score.
The tool takes as input a list of hotel reviews and a topic word. 
The output of the tool is a list of hotels ranked by their 
sentiment score for the given topic. In this section we discuss the 
the scoring algorithm.


### Text Fragments
The first task is to split the reviews into text fragments that cover a single topic. 
This is not a trivial task. A topic may be discussed in multiple sentences,
as in 'The rooms looked very nice. However, we did not like the smell.' 
On the other hand, it can also be the case that a single sentence
covers multiple topics, for example: 
'The rooms were nice but the breakfest was a bit disappointing.'
We manually inspected some reviews and decided to split sentences 
based on the following punctuation marks .,!? and the substring '&nbsp;&nbsp;-'.
We did not further evaluate this heuristic.

### Topic Words
The next task is to select from the text fragments
exactly those fragments that are relevant for a given topic. 
The basic idea is to select the sentences that contain
the topic word entered by the user. 
However, we also have to take into account 
synonyms and singular and plural nouns.
We think that this can best be implemented by using a dictionairy API.
For now, we hard coded a list of synonyms and we implemented some
simple rules to build singular and plural forms.

### Scoring
The final question is how to score the text fragments that were 
selected for the topic.
For this purpose we look for specific phrases that 
express a positive or negative sentiment. These 
phrases and their sentiment values are looked up from a
predefined list. Examples are: 'nice' (+1), 'great' (+2) and 'terrible' (-2).
The values change when a phrase is preceded by an intensifier,
examples are: 'really' (+2) and 'not' (-1). 
To score a text fragment,
we sum the values of positive and negative phrases, 
whereby the value of the phrase is multiplied with the values
of all directly preceding intensifiers.
For example: 'The room was not really nice and the beds were terrible' is scored
as: -1 * 2 * 1 - 2 = -4.


### Performance
We want to respond fast when a user requests a sentiment analysis for a topic.
For this reason we build an in-memory data structure that is optimized for
detecting and scoring topic fragments. The first object in this data structure 
is a table containing all review fragments. 
The fragments are already scored in the processing stage. 
To filter this table efficiently, we also keep in memory a dictionairy
containing all words that occur in the reviews, associated with their list of
indices that point to the table with the scored text fragments.


Future Work
============

* Evaluate sentiment analyzer by comparing score 
for topic 'rooms' with ratings for rooms (and other rated topics)
* Training sentiment phrase values by using rated topics (as mentioned above)  
* Output more statistics
* Use dictionairy API for synonys and plural/singular forms
* Use translation API for reviews in other languages  
* Inplace update in-memory data structure when new reviews become available


