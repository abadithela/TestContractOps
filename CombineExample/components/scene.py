# Scene class
# J. Graebener
# December 2022
# Reasoning over Test Specifications in Assume Guarantee Contract form

class Scene:
    def __init__(self, timestamp, agent, tester):
        self.timestamp = timestamp
        self.agent = agent
        self.tester = tester
