from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector


def homepage(request):
    return render(request, 'home.html', {'key1':'value1'})


def count(request):
    fulltext = request.GET['fulltext']
    print("request_print:")
    print(request)

    wordlst = fulltext.split()
    wordcnt = len(wordlst)

    worddict = dict()
    for word in wordlst:
        worddict[word] = worddict.get(word, 0) + 1
    return render(request, 'count.html', {'fulltext': fulltext, 'wordcnt': wordcnt, 'worddict': worddict,
                                          'items': worddict.items()})


def about(request):
    return render(request, 'about.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def new_game(request):
    return render(request, 'new_game.html')


def signup_complete(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root', passwd='L18_jhk123qwe',database='signup')
    cursor = cnx.cursor()
   # sql_create_table="CREATE TABLE game01(userid SMALLINT NOT NULL auto_increment PRIMARY KEY, " \
   #                  + "name CHAR(20)," \
   #                  + "age SMALLINT," \
   #                  + "gender CHAR(4)" \
   #                  + ");"

#    cursor.execute(sql_create_table)
#    name = request.GET['name']
    signup_dict = dict()
    for i in request.GET:
        key = i
        value = request.GET[i]
        signup_dict[key] = value
    keylist = list(signup_dict.keys())
    valuelist = list(signup_dict.values())
    keystr = str(keylist).strip('[').strip(']')
    valuestr = str(valuelist).strip('[').strip(']')
    print(keystr)
    print(valuestr)
    return render(request, 'signup_complete.html')
