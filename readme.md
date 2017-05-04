Trivago
=======

Trivago is a hotel comparison website. 
This application allows customers of Trivago to compare hotels for a given topic. 
The comparison uses sentiment analysis on review sentences that mention that topic.

Setup
=====

This setup requires the [conda](https://conda.io/docs/install/quick.html) package manager to be installed.

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
364 reviews processed for: data/reviews2.json
188 reviews processed for: data/reviews1.json
6748 review sentences analysed in total
5996 words stored in lookup table
```
The semantic file argument is optional, 
by default the semantic file in 'semantics/semantics.json' is loaded.
When no reviews directory is provided, 
the review files in 'data/' are loaded.


**Scoring a topic:**

```
Enter your topic word: room
2 additional topic words found: ['room', 'rooms']
954 sentences found for topic words
  HotelID     Score
0   77923  0.683219
1   84333  0.662387
```

Tests
========

To run all tests:

```
$ python -m unittest discover test
```

Implemtation
============

The application is implemented in python.


