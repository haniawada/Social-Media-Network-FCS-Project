import networkx as nx
import matplotlib.pyplot as plt

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = set()
