import unittest
from graphics import *


class ExtentsTestCase(unittest.TestCase):
    def test_extent_basic(self):
        xmin, ymin, xmax, ymax = extent([(10, 10), (30, 50), (120, 40)])

        self.assertEqual(10, xmin)
        self.assertEqual(120, xmax)
        self.assertEqual(10, ymin)
        self.assertEqual(50, ymax)

    def test_extent_zeros(self):
        xmin, ymin, xmax, ymax = extent([(0, 0), (0, 0), (0, 0)])

        self.assertEqual(0, xmin)
        self.assertEqual(0, xmax)
        self.assertEqual(0, ymin)
        self.assertEqual(0, ymax)

    def test_extent_out_of_bounds(self):
        xmin, ymin, xmax, ymax = extent([(-1000, 0), (2000, 1002)])

        self.assertEqual(-1000, xmin)
        self.assertEqual(2000, xmax)
        self.assertEqual(0, ymin)
        self.assertEqual(1002, ymax)

    def test_single_point_out_of_bounds(self):
        xmin, ymin, xmax, ymax = extent([(1002, 1002)])

        self.assertEqual(1002, xmin)
        self.assertEqual(1002, xmax)
        self.assertEqual(1002, ymin)
        self.assertEqual(1002, ymax)

    def test_checkbounds(self):
        graphics = Graphics(1000, 1000);
        with self.assertRaises(ValueError) as context:
            graphics.checkbounds([(1002, 0)])
            self.assertTrue(
                'The shape extends beyond the canvas: x=1002 is greater than canvas width 1000' in context.exception)
            graphics.checkbounds([(0, 1002)])
            self.assertTrue(
                'The shape extends beyond the canvas: y=1002 is greater than canvas height 1000' in context.exception)
            graphics.checkbounds([(0, -100)])
            self.assertTrue(
                'The minimum boundary y=-100 cannot be less than 0' in context.exception)


if __name__ == '__main__':
    unittest.main()
