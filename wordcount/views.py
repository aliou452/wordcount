from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'Great': 'Nice to see you again'})

def count(request):
    fulltext=request.GET['fulltext']
    wordCount = fulltext.split()
    countword = len(wordCount)
    worddict = {}
    for word in fulltext:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1
    words = sorted(worddict.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'countword':countword, "worddict":worddict, 'words': words})