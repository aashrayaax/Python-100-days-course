# discussed about modules in python:built in and external modules
# import math 
# import pandas as pd 
import pyjokes


# Get a random joke
joke = pyjokes.get_joke()
print(joke)

# You can also get multiple jokes
# jokes = pyjokes.get_jokes()
# for joke in jokes:
#     print(joke)

# You can specify the category and language
# Categories: neutral, chuck, all
# Languages: en, es, de, gl, eu
# joke = pyjokes.get_joke(language='en', category='neutral')
# print(joke)