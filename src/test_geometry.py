import unittest
from euclid import Point2, LineSegment2
from geometry import Polygon, IntersectingPolygonError

class TestPolygon(unittest.TestCase):
    def setUp(self):
        self.points = [Point2(0, 0),
                  Point2(0, 4),
                  Point2(4, 4),
                  Point2(4, 0),]

    def test_basic(self):
        polygon = Polygon(self.points)

    def test_self_intersecting(self):
        with self.assertRaises(IntersectingPolygonError):
            points = [Point2(0, 0),
                      Point2(4, 4),
                      Point2(0, 4),
                      Point2(4, 0)]
            Polygon(points)

    def test_intersect(self):
        line_segment = LineSegment2(Point2(1, 5), Point2(5, 1))
        square = Polygon(self.points)
        intersect_points = square.intersect(line_segment)
        desired = [Point2(2, 4), Point2(4, 2)]
        self.assertListEqual(desired, intersect_points)

if __name__ == '__main__':
    unittest.main()