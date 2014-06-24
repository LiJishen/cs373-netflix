from io       import StringIO
from unittest import main, TestCase
from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve, sqre_diff, rmse

class TestNetflix (TestCase) :
	# ----
    # read
    # ----

    def test_read_1 (self) :
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
        w = StringIO()
        v = netflix_eval(w, "1", {0: '30878'})
        self.assertEqual(v, True)

    def test_eval_2 (self) :
        w = StringIO()
        v = netflix_eval(w, "1", {0: '30878', 1: '2647871', 2: '1283744'})
        self.assertEqual(v, True)

    def test_eval_3 (self) :
        w = StringIO()
        v = netflix_eval(w, "10", {0: '1952305', 1: '1531863'})
        self.assertEqual(v, True)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 3.7389247589)
        self.assertEqual(w.getvalue(), "3.7\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 3)
        self.assertEqual(w.getvalue(), "3.0\n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, 3.7)
        self.assertEqual(w.getvalue(), "3.7\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1:\n30878\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "3.7\n")

    def test_solve_2 (self) :
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "3.7\n3.5\n3.6\n")

    def test_solve_3 (self) :
        r = StringIO("1:\n30878\n10:\n1952305\n1531863\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "3.7\n3.3\n3.2\n")


    # ---------
    # sqre_diff
    # ---------

    def test_sqre_diff_1(self):
        a = sqre_diff(1, 2)
        self.assertEqual(a, 1)

    def test_sqre_diff_2(self):
        a = sqre_diff(0, 0)
        self.assertEqual(a, 0)

    def test_sqre_diff_3(self):
        a = sqre_diff(5, 1)
        self.assertEqual(a, 16)

    # ----
    # rmse
    # ----

    def test_rmse_1(self):
        x = rmse({"1-30878": 4}, {'1': {'30878': 3.700992340036563}}, {'1': {0: '30878'}})
        self.assertEqual(x, 0.2990076599634368)

    def test_rmse_2(self):
        x = rmse({"1-30878": 4, "1-2647871": 4, "1-1283744": 3}, {'1': {'2647871': 3.492592340036563, '1283744': 3.654102340036563, '30878': 3.700992340036563}}, {'1': {0: '30878', 1: '2647871', 2: '1283744'}})
        self.assertEqual(x, 0.5081725380707123)

    def test_rmse_3(self):
        x = rmse({"1-30878": 4, "10-1952305": 3, "10-1531863": 3}, {'1': {'2647871': 3.492592340036563, '1283744': 3.654102340036563, '30878': 3.700992340036563}, '10': {'1952305': 3.290585903614458, '1531863': 3.155125903614458}}, {'1': {0: '30878'}, '10': {0: '1952305', 1: '1531863'}})
        self.assertEqual(x, 0.2568461238877235)

main()