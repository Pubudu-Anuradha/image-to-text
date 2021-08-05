# Image-to-text

Some Scripts I'm making for fun to turn a given image to text forms.
Made using [Pillow](https://pillow.readthedocs.io/en/stable/) on [python3.8.10](https://www.python.org/downloads/release/python-3810/).

## Setup

Download and install [Python](https://www.python.org/downloads/)

Install pillow using `pip install pillow` or any other method you prefer.

Use the .py script you want to use(only block converter currently available).

Have fun!

### Using Converters

Run blocks.py or braille.py(braille_generator.py needs to be in same directory) on a terminal with the following options

| Option          | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| -i \<filename\> | specify the file to use                                       |
| -w \<number\>   | choose a width.(default is 250)                               |
| -o \<filename\> | specify a file to putput the result.(Default is result.txt)   |
| -p              | turn off printing to console(recommended if using high width) |

#### Example results

1 [original image from wikimedia commons](https://commons.wikimedia.org/wiki/File:30b_Sammlung_Eybl_USA_James_Montgomery_Flagg_(1877-1960)_I_want_you_for_U.S._Army._1917._101_x_76_cm._(Coll..Nr._3116).jpg) Using block converter

![dskeZFjNub](https://user-images.githubusercontent.com/52956977/128206778-1a08d6ef-e5fa-4c24-8248-3261b5b0ab2e.png)

2 [original image from wikimedia commons](https://commons.wikimedia.org/wiki/File:Horse_December_2014-1.jpg) Using braille converter

![KSbquIeJeZ](https://user-images.githubusercontent.com/52956977/128309120-01400f60-0c50-4af2-9d5c-e2ea42f05972.png)

