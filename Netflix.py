import functools
import math
import sys
import json


j1 = open("cache2.json", 'r')
movie_cache = json.loads(j1.read())
j2 = open("cache1.json", 'r')
user_cache = json.loads(j2.read())

def sqre_diff (x, y) :
    return (x - y) ** 2


def rmse_map_sum (actual, prediction) :
    s = len(actual)
    v = sum(map(sqre_diff, actual, prediction))
    return math.sqrt(v / s)


def netflix_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """

    input_set = {}
    user = [0, 0, 0]
    count = 0;
    previous_line = ""

    while True:
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
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(round(average, 1)) + "\n")


def netflix_solve (r, w):
    a = netflix_read(r)
    
    for x in a:
        netflix_eval(w, x, a[x])
    

def netflix_eval(w, movie, user):
    print(str(movie) + ":")
    for i in range(len(user)):
        average = (movie_cache[movie] + user_cache[user[i]])/2
        netflix_print(w, average)

netflix_solve(sys.stdin, sys.stdout)