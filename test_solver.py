__author__ = 'Tirth Patel <complaints@tirthpatel.com>'

import unittest
import solver


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.sudoku = solver.Sudoku()

        # easy (record: 4 iters)
        easy = '830076042' \
               '600300097' \
               '000082100' \
               '090030005' \
               '026000730' \
               '300020010' \
               '003460000' \
               '170003006' \
               '260790054'

        # medium (random record: 8 iters, average ~16 iters)
        medium = '050000006' \
                 '480090003' \
                 '903800000' \
                 '017004000' \
                 '600172005' \
                 '000500810' \
                 '000003508' \
                 '700050041' \
                 '800000090'  # (0, 0) -> 2 to make solvable

        # hard (random record: 24 iters, average ~85 iters)
        hard = '003105060' \
               '000004008' \
               '060000507' \
               '056000000' \
               '094602150' \
               '000000620' \
               '509000040' \
               '600400000' \
               '040203900'

        # evil (random record: 21 iters, average ~262 iters)
        evil = '005090400' \
               '700046000' \
               '000300090' \
               '600000020' \
               '090158030' \
               '080000009' \
               '060005000' \
               '000920001' \
               '008010900'

        # complete
        done = '391286574' \
               '487359126' \
               '652714839' \
               '875431692' \
               '213967485' \
               '964528713' \
               '149673258' \
               '538142967' \
               '726895341'

        # supposedly the world's hardest?
        everest = '800000000' \
                  '003600000' \
                  '070090200' \
                  '050007000' \
                  '000045700' \
                  '000100030' \
                  '001000068' \
                  '008500010' \
                  '090000400'

        self.puzzle = evil  # choose puzzle

    def test_solve(self):
        if self.sudoku.get_input(self.puzzle):
            self.assertTrue(self.sudoku.solve())

    def test_efficiency(self):
        iterations = []
        validity = 50

        for i in range(validity):
            self.sudoku.get_input(self.puzzle)
            self.assertTrue(self.sudoku.solve())

            progress = round(i/(validity/100), 3)
            if progress % 10.0 == 0.0:
                print(str(progress) + "%")
            iterations.append(self.sudoku.current)

            self.sudoku = solver.Sudoku()
            self.sudoku.get_input(self.puzzle)

        print('after', len(iterations))
        print('min', min(iterations))

        total = 0
        for it in iterations:
            total += it

        print('average', total/len(iterations))


if __name__ == '__main__':
    unittest.main(exit=False)