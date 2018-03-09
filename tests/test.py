import unittest
from pybktreespellchecker import levenshtein_distance
from pybktreespellchecker import BKTree


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.bktree = BKTree(words=['zero', 'one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])

    def test_levenshtein_distance_function(self):
        self.assertEqual(levenshtein_distance('kitten', 'sitting'), 3)
        self.assertEqual(levenshtein_distance.ratio, 0.7692307692307693)
        self.assertEqual(levenshtein_distance.distance_matrix, [[0, 1, 2, 3, 4, 5, 6],
                                                                [1, 1, 2, 3, 4, 5, 6],
                                                                [2, 2, 1, 2, 3, 4, 5],
                                                                [3, 3, 2, 1, 2, 3, 4],
                                                                [4, 4, 3, 2, 1, 2, 3],
                                                                [5, 5, 4, 3, 2, 2, 3],
                                                                [6, 6, 5, 4, 3, 3, 2],
                                                                [7, 7, 6, 5, 4, 4, 3]])

        self.assertEqual(levenshtein_distance('Saturday', 'Sunday'), 3)
        self.assertEqual(levenshtein_distance.ratio, 0.7857142857142857)
        self.assertEqual(levenshtein_distance.distance_matrix, [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                                                                [1, 0, 1, 2, 3, 4, 5, 6, 7],
                                                                [2, 1, 1, 2, 2, 3, 4, 5, 6],
                                                                [3, 2, 2, 2, 3, 3, 4, 5, 6],
                                                                [4, 3, 3, 3, 3, 4, 3, 4, 5],
                                                                [5, 4, 3, 4, 4, 4, 4, 3, 4],
                                                                [6, 5, 4, 4, 5, 5, 5, 4, 3]])

        self.assertEqual(levenshtein_distance('good', 'banana'), 6)
        self.assertEqual(levenshtein_distance.ratio, 0.4)
        self.assertEqual(levenshtein_distance.distance_matrix, [[0, 1, 2, 3, 4],
                                                                [1, 1, 2, 3, 4],
                                                                [2, 2, 2, 3, 4],
                                                                [3, 3, 3, 3, 4],
                                                                [4, 4, 4, 4, 4],
                                                                [5, 5, 5, 5, 5],
                                                                [6, 6, 6, 6, 6]])

    def test_bktree_functions(self):
        self.bktree.add_word('car')

        result = self.bktree.search('car', 0)

        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[0][1].word, 'car')

        result = self.bktree.search('eiggt', 4)
        self.assertEqual(len(result), 4)

        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][1].word, 'eight')


if __name__ == '__main__':
    unittest.main()