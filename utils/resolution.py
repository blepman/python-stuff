#!usr/bin/env python
def get_xy_from_resolution(from_xy, from_res, to_res):
    """ Get new proportional location of coords (x,y) from known coords (x,y) at a specific resolution.
    :arg from_xy:   list[int, int] coords (x,y) to convert from.
    :arg from_res:  list[int, int] Resolution (x,y) to convert from.
    :arg to_res:    list[int, int] Resolution (x,y) to convert to.
    :returns:       dict[float, float] New coords as key/value. """
    return {"x": (from_xy[0] / from_res[0]) * to_res[0], "y": (from_xy[1] / from_res[1]) * to_res[1]}
