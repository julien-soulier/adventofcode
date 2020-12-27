tiles = [(-1,2), (-2,4), (5,-3), (0,8)]

def get_tiles_area(tiles):
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for coord in tiles:
        xmin = min(xmin, coord[0])
        xmax = max(xmax, coord[0])
        ymin = min(ymin, coord[1])
        ymax = max(ymax, coord[1])

    return (xmin, ymin), (xmax, ymax)

print(get_tiles_area(tiles))