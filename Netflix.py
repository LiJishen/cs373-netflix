import functools
import math
import sys
import json

average_movie_ratings = {}
with open(" /u/mukund/cs373-netflix-tests/rbrooks-movie_average_rating.json", "r") as f:
	average_movie_ratings = json.load(f)

def sqre_diff (x, y) :
    return (x - y) ** 2


def rmse_map_sum (actual, prediction) :

    s = len(actual)
    v = sum(map(sqre_diff, actual, prediction))
    return math.sqrt(v / s)



def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]


def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")



def netflix_solve (r, w):
