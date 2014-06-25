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

prediction = {}

def sqre_diff (x, y) :
    return (x - y) ** 2


def rmse(a, p, input_set) :
    v = 0
    l = 0
    for x in input_set:
        s = len(input_set[x])
        l += s
        i = 0
        while i < s :
            u = x + "-" + input_set[x][i]
            v += sqre_diff(a[u], p[x][input_set[x][i]])
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
    w.write("{0:.1f}".format(average) + "\n")


def netflix_solve (r, w):
    a = netflix_read(r)
    #counter = 0
    for x in a:
        netflix_eval(w, x, a[x])
        #counter += 1
    
    print("RMSE: %.4f" % rmse(answer_cache, prediction, a))
    #return counter == len(a)

def netflix_eval(w, movie, user):
    print(str(movie) + ":")
    pre = 0
    users = {}
    counter = 0
    for i in range(len(user)):
        p = movie_cache[movie]
        q = user_cache[user[i]]
        pre = (q*.521 + p*.52) - .14
        users[user[i]] = pre
        prediction[movie]  = users
        counter += 1     
        netflix_print(w, round(pre,1))

    #for test purpose
    return counter == len(user)

