#/bin/env python3

from parse import *

def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

class Sensor():
    def __init__(self, position, beacon):
        self.position = position
        self.range = distance(position, beacon)

    def get_empty_segment_on_line(self, y):
        D = self.range - abs(self.position[1] - y)
        return (self.position[0]-D, self.position[0]+D) if D>=0 else None

def get_sensors(infile="input.txt"):
    sensors = []
    with open(infile, "r") as f:
        for sensor_line in f.readlines():
            r = parse("Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}\n", sensor_line)
            if not r:
                raise RuntimeError("Cannot parse line: {sensor_line}")

            sensors.append(Sensor((r['sx'],r['sy']), (r['bx'],r['by'])))

    return sensors

def merge_segments(segments):
    segments.sort(key=lambda x: x[0])
    start = end = segments[0][0]
    merged = []
    for seg in segments:
        if seg[0] > end:
            merged.append((start, end))
            start = seg[0]
        end = max(end, seg[1])
    merged.append((start, end))

    return merged    

def get_empty_segments_on_line(sensors, line=2000000):
    segments = [sensor.get_empty_segment_on_line(line) for sensor in sensors]
    
    # remove None segments for segments not intersecting the line
    segments = [seg for seg in segments if seg]

    return merge_segments(segments)
 
def get_distress_beacon(sensors, size=4000000):
    for y in range(size+1):
        if y%100000 == 0:
            print(y)
        
        segments = get_empty_segments_on_line(sensors, y)

        # remove segments which are off limits
        if (len(segments)>1):
            while segments[0][1]<0:
                segments.pop(0)
            while segments[-1][0]>size:
                segments.pop()

        # if there are more than 1 segment, there is a free hole in line
        if len(segments)>1:
            return (segments[0][1]+1,y)

    raise RuntimeError("Cannot find distress beacon")

sensors = get_sensors("input.txt")
segments = get_empty_segments_on_line(sensors)
print(f"Soution part1  is {sum((s[1]-s[0] for s in segments))}")

beacon = get_distress_beacon(sensors)
print(f"Soution part2  is {beacon[0]*4000000+beacon[1]} for a beacon at {beacon}")
