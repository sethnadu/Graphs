import random
from util import Queue
from graph import Graph

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if num_users <= avg_friendships:
            print("Users must be higher than the average number of friends")
            return
        # Add users
        for i in range(num_users):
            self.add_user(i + 1)

        # Create friendships
        # Total friends is average times num_users
        total_friends = avg_friendships * len(self.users)
        max_friend_user = avg_friendships * 2
        friend_count = 0
        # loop through the highest number of friends
        while friend_count < total_friends:
            # Random number between 1 and len of users, saved as user
            random_user = random.randint(1, len(self.users))
            # Random number between 1 and len of users, saved as friend
            random_friend = random.randint(1, len(self.users))
            # Only works if user is less than friend
            if random_user < random_friend:
                # If check to make sure user-friend relationship doesn't already exist
                if random_friend not in self.friendships[random_user] or random_user not in self.friendships[random_friend]:
                    if len(self.friendships[random_user]) < max_friend_user and len(self.friendships[random_friend]) < max_friend_user:
                        self.add_friendship(random_user, random_friend)
                        # Add 2 to friend count as a mutual two-way relationship between user and friend
                        friend_count += 2




    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue.enqueue([user_id])
        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]
            if v not in visited:
                visited[v] = path
                for next_v in self.friendships[v]:
                    shortest_path = list(path)
                    shortest_path.append(next_v)
                    queue.enqueue(shortest_path)        
        return visited
        


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    for i in range(len(sg.users)):
        print(sg.users[i + 1].name)
    connections = sg.get_all_social_paths(1)
    print(connections)
