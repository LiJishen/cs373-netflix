from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve, sqre_diff, rmse


class TestNetflix (TestCase) :
	# ----
    # read
    # ----

    def test_read (self) :
        r = StringIO("1:\n30878\n")
        a = netflix_read(r)
        print(a)
        self.assertEqual(a,  {'1': {0: '30878'}})

    def test_read_2 (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        a = netflix_read(r)
        print(a)
        self.assertEqual(a,  {'1': {0: '30878', 1: '2647871', 2: '1283744'}})

    def test_read_3 (self) :
        r = StringIO("1:\n30878\n10:\n1952305\n1531863\n")
        a = netflix_read(r)
        print(a)
        self.assertEqual(a,  {'1': {0: '30878'}, '10': {0: '1952305', 1: '1531863'}})

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)






main()