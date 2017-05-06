Trivago
=======

Trivago is a hotel comparison website. 
This application allows customers of Trivago to compare hotels for a given topic. 
The comparison uses sentiment analysis on review sentences that mention that topic.

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

The Trivago app is a command-line application. See usage example below.


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
21588 review sentence fragments analysed in total
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
1937 sentences found containing the words 'room' or 'rooms'

   HotelID     Score  #Fragments
0  2514817  0.315292         582
1    76790  0.375000          24
2    77923  0.414791         311
3    81363  0.173826         298
4    84333  0.318560         722

Most positive fragment:
The room we were allocated was absolutely fantastic and today we cannot believe how fortunate we were ( 5.0 )

Most negative fragment:
The room decor is old and tired and not very clean ( -3.0 )
```

Topics should be single words. If no topic word is entered, then the scores for all sentences are use
to compare the hotels.

Tests
========

To run all tests:

```
$ python -m unittest discover test
```

Design
============


Implemtation
============

The application is implemented in python 3.


Future Work
============

* Evaluate sentiment analyzer by comparing score 
for topic 'rooms' with ratings for rooms (and other rated topics)
* Training sentiment phrase values by using rated topics (as mentioned above)  
* Experiment with other scoring heuristics


* Show top 3 most positive and most negative sentences for each hotel
* More statistics


* Use dictionairy API for synonys and plural/singular forms
* Use translation API for reviews in other languages  

* Inplace update in-memory data structure when new reviews become available


