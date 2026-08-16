class Utils:

    # axis aligned bounding box overlap
    #
    # two boxes miss whenever there is a gap on either axis, so they only hit
    # when both axes overlap at the same time
    #
    # touching edges do not count as a hit, because the comparisons are strict
    @staticmethod
    def aabb(a, b):
        overlaps_x = a.x < b.x + b.width and a.x + a.width > b.x
        overlaps_y = a.y < b.y + b.height and a.y + a.height > b.y

        return overlaps_x and overlaps_y
