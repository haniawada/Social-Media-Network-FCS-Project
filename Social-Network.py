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
            
    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            self.graph.remove_node(user_id)
        else:
            print("User not found.")
            
    def add_relationship(self, user_id1, user_id2):
        if user_id1 in self.users and user_id2 in self.users:
            self.users[user_id1].add_friend(user_id2)
            self.users[user_id2].add_friend(user_id1)
            self.graph.add_edge(user_id1, user_id2)
        else:
            print("One or both users not found.")
            
    def remove_relationship(self, user_id1, user_id2):
        if user_id1 in self.users and user_id2 in self.users:
            self.users[user_id1].remove_friend(user_id2)
            self.users[user_id2].remove_friend(user_id1)
            self.graph.remove_edge(user_id1, user_id2)
        else:
            print("One or both users not found.")
            
    def update_profile(self, user_id, name=None):
        if user_id in self.users:
            self.users[user_id].update_profile(name=name)
            if name:
                self.graph.nodes[user_id]['name'] = name
        else:
            print("User not found.")
            
    def bfs(self, start_user_id):
        visited = set()
        queue = [start_user_id]
        result = []

        while queue:
            user_id = queue.pop(0)
            if user_id not in visited:
                visited.add(user_id)
                result.append(user_id)
                queue.extend(self.graph.neighbors(user_id))

        return result
    
    def dfs(self, start_user_id):
        visited = set()
        stack = [start_user_id]
        result = []

        while stack:
            user_id = stack.pop()
            if user_id not in visited:
                visited.add(user_id)
                result.append(user_id)
                stack.extend(self.graph.neighbors(user_id))

        return result
    
    def shortest_path(self, user_id1, user_id2):
        try:
            path = nx.shortest_path(self.graph, source=user_id1, target=user_id2)
            return path
        except nx.NetworkXNoPath:
            return None
        
    def connected_components(self):
        return list(nx.connected_components(self.graph))
    
    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'name')
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=5000, node_color='skyblue', font_size=10)
        plt.show()
        
    

        
