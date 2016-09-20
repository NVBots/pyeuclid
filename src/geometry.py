import numpy as np
from euclid import LineSegment2, Point2


class IntersectingPolygonError(BaseException):
    pass

class Polygon(object):
    def __init__(self, points):
        self.points = np.array(points)
        self.line_segments = np.array([LineSegment2(points[i], points[(i+1)%len(points)]) for i in range(len(points))])
        for seg_a in self.line_segments:
            for seg_b in self.line_segments:
                if seg_a is not seg_b:
                    intersect_point = seg_a.intersect(seg_b)
                    if intersect_point and intersect_point not in (seg_a.p1, seg_a.p2):
                        raise IntersectingPolygonError("{0} intersects {1}".format(seg_a, seg_b))

    def intersect(self, other):
        intersections = []
        for seg in self.line_segments:
            intersect_point = seg.intersect(other)
            if intersect_point:
                intersections.append(intersect_point)
        return intersections