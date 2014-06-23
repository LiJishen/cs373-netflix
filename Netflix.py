import functools
import math
import sys
import json


j1 = open("rbrooks-movie_average_rating.json", 'r')
movie_cache = json.loads(j1.read())
j2 = open("bryan-customer_cache.json", 'r')
user_cache = json.loads(j2.read())
j3 = open("osl62-AnswerCache.json", 'r')
answer_cache = json.loads(j3.read())
j4 = open("osl62-MovieCache.json", 'r')
medium = json.loads(j4.read())
j5 = open("eros-movie_cache.json", 'r')
ero = json.loads(j5.read())

prediction = []

def sqre_diff (x, y) :
    return (x - y) ** 2


def rmse(a, p, input_set) :
    v = 0
    l = 0
    #print(input_set)
    for x in input_set:
        s = len(input_set[x])
        l += s
        i = 0
        u = x + "-" + input_set[x][i]
        while i < s :
            v += sqre_diff(a[u], p[i])
            i += 1
    return math.sqrt(v / l)


def netflix_read (r) :
    input_set = {}
    count = 0;
    previous_line = ""

    while True:
        user = {}
        s = r.readline()
        if s == "":
            break

        if ":" in s:
            movie_id = s[:-2]

        if previous_line != "":
            movie_id = previous_line
            user[0] = s[:-1]
            previous_line = ""
            count = 1

        while True:
            u = r.readline()
            if u == "":
                break

            if ":" in u:
                previous_line = u[:-2]
                break
            user[count] = u[:-1]
            count += 1
            
        input_set[movie_id] = user
    return input_set


def netflix_print (w, average) :
    w.write(str(round(average, 1)) + "\n")


def netflix_solve (r, w):
    a = netflix_read(r)
    for x in a:
        netflix_eval(w, x, a[x])
    
    print("RMSE: %.2f" % round(rmse(answer_cache, prediction, a), 2))
    

def netflix_eval(w, movie, user):
    #print(str(movie) + ":")
    for i in range(len(user)):
        #average = (movie_cache[movie]*.55  + user_cache[user[i]]*.45 )
        #average = (float(ero[movie][0])*float(ero[movie][1]) + user_cache[user[i]] * (1 - float(ero[movie][1])) + medium[movie][1]*medium[movie][2])/2.11
        p = movie_cache[movie]
        q = user_cache[user[i]]
        average = (p+q)/2
        if p > 4:           
            p = average *.88
        if p < 2:
            p = average *1.12

        prediction.append(round(p, 2))
        #netflix_print(w, average)   

netflix_solve(sys.stdin, sys.stdout)