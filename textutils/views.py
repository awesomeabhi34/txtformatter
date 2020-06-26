from django.http import HttpResponse
from django.shortcuts import render
from termcolor import colored


def index(request):
    # USE OF TEMPLATES
    return render(request, 'index.html')


def analyze(request):
    # GETTING THE TEXT FROM TEXT AREA
    txt = (request.POST.get('text', 'default'))

    # FOR RADIOBUTTON STYLE
    x = (request.POST.get('format', 'default'))

    if x == 'rempun':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char  # this gives punc less words
        purp = 'Removed Punctuations'
    elif x == 'caps':
        analyzed = txt.upper()
        purp = 'Capitalize'
    elif x == 'now':
        t = txt.split(" ")
        analyzed = f'Number of words: {len(t)}'
        purp = 'Number of Words'
    elif x == 'capword':
        t = txt.split(" ")
        analyzed = ""
        for item in t:
            analyzed = analyzed + " " + item.capitalize()
        purp = 'Capitalized Words'
    elif x == 'charcnt':
        nl = '\n'
        temp = ''
        for i in txt:
            if not (i == " "):
                temp = temp + i
        a, n, s = 0, 0, 0
        for i in temp:
            if i.isalpha():
                a = a + 1
            if i.isnumeric():
                n = n + 1
            if not(i.isalnum()):
                s = s + 1
        analyzed = f'''Number of characters including whitespace : {len(txt)}
Number of characters excluding whitespace : {len(temp)} 
Number of aplhabets : {a}
Number of numeric digits : {n}
Number of special characters : {s}'''
        purp = 'Character Count'
    elif x == 'rnl':
        analyzed = ""
        for item in txt:
            if item != '\n' and item != '\r':
                analyzed = analyzed + item
        purp = 'Remove NewLine'
    elif x == 'rsp':
        analyzed = ""
        for index, item in enumerate(txt):
            if not (txt[index] == ' ' and txt[index + 1] == ' '):
                analyzed = analyzed + item
        purp = 'Remove Extra Spaces'
    else:
        analyzed = txt
        purp = 'No Changed Applied'
    params = {'purpose': purp, 'analyzed_text': analyzed}
    return render(request, 'utils.html', params)
