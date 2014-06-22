import functools
import math
import sys
import json


j1 = open("cache2.json", 'r')
movie_cache = json.loads(j1.read())
j2 = open("cache1.json", 'r')
user_cache = json.loads(j2.read())
j3 = open("answer.json", 'r')
answer_cache = json.loads(j3.read())

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
    print(rmse(answer_cache, prediction, a))
    

def netflix_eval(w, movie, user):
    print(str(movie) + ":")
    for i in range(len(user)):
        average = (movie_cache[movie] * .8 + user_cache[user[i]] * .2)
        prediction.append(average)
        netflix_print(w, average)   

netflix_solve(sys.stdin, sys.stdout)