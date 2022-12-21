# Map class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class Map():
    def __init__(self,lane_length, width, cwloc):
        self.xs = lane_length
        self.width = width
        self.crosswalk_cell = cwloc
        self.crosswalk_length = 10
