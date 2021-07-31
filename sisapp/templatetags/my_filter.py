from django import template
from django.utils.safestring import SafeString
import re 
import datetime
from datetime import date
 
register = template.Library()

@register.filter
def replace_punc(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    my_str = string

    # To take input from the user
    # my_str = input("Enter a string: ")

    # remove punctuation from the string
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct
    # return string.replace(':', '')

@register.filter
def to_string(sring):
    return str(sring)

@register.filter
def replace_level(string):
    return string[6:]

@register.filter
def replace_term(string):
    return string[5:]

@register.filter
def to_integer(string):
    # x = replace_term(string)
    return int(string)

@register.filter
def levelname(string):
    if string[:7] == 'Basic 7':
        name = 'JHS 1'
    elif string[:7] == 'Basic 8':
        name = 'JHS 2'
    elif string[:7] == 'Basic 9':
        name  = 'JHS 3'
    elif string[:5] == 'Basic':
        punctuations = '''!Basic*_~'''
        primary = "Primary"
        my_str = string
        for char in my_str:
            if char not in punctuations:
                primary = primary + char
                name = primary
            
    return name
    

@register.filter
def calcage(string):
    date_time_str = str(string)
    date_time_obj = datetime.datetime.strptime(date_time_str, "%Y-%m-%d")
    print('Date:', date_time_obj.date())
    print(date.today())
    daysdiff = date.today() - date_time_obj.date()
    intdate = str(daysdiff)[:-14]
    intyears = int(int(intdate)/365)
    print(intyears)
    return intyears
