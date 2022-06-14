# a constructor initializes values in the class
# this is done by the init method!
class User:
    def __init__(self, user_id, username):
        print("new user created")
        self.id = user_id
        self.username = username
        self.coolness = 10

    def trip_on_nothing(self):
        self.coolness -= 2
        print(f"coolness: {self.coolness}")


user_1 = User("007", "homer")
for i in range(10):
    print(user_1.username)
    print(user_1.coolness)
    print(user_1.id)
    user_1.trip_on_nothing()

# user_2 = User(2)
# print(user_1.username)