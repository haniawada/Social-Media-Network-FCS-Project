import networkx as nx
import matplotlib.pyplot as plt

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = set()
        
    def add_friend(self, friend_id):
        self.friends.add(friend_id)
        
    def remove_friend(self, friend_id):
        self.friends.remove(friend_id)
        
    def update_profile(self, name=None):
        if name:
            self.name = name
            
    def __str__(self):
        return f"User({self.user_id}, {self.name}, Friends: {len(self.friends)})"

class SocialNetworkGraph:
    def __init__(self):
        self.users = {}
        self.graph = nx.Graph()
        
    def add_user(self, user_id, name):
        if user_id not in self.users:
            user = User(user_id, name)
            self.users[user_id] = user
            self.graph.add_node(user_id, name=name)
        else:
            print("User already exists.")
    

        
