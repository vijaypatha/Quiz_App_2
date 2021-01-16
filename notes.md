# Notes on Basic OOP 
## Class
* Class is a blueprint (factory) that produce widgets (objects). Each Widget has (data/attributes) and does (methods)
something.

* Creating classes is pretty straight forward.

```
class Rav4:
    attributes
    def __init__(self, seats):
    #initialize attributes. 
    #Everytime a new object is created from this class, 
    # __init__ function is going to be called.
        self.seats = seats 
        #self.seats is an attribute associated with Rav4 car
    def method_name(self):
    # self in the method is the object. So, when a method gets called
    # it knows the object that called it. 
        self.seats = 2
```

## Objects
mimics real world application. I'm an object, the car on the road. Objects are
living things that has some data and can do stuff. Objects get constructed 
from a class. Since objects "have" attributes, these attributes get passed in
when an objects get created from class. 

```limited = Rav4(5)``` 
this is same as limited.seats = 5. We constructed a limited object from Rav4 class. () = initialize or construct. A limited car has 5 seats.

```xle = Rav4(6)``` 
we constructed an object called xle from Rav4 blueprint with 6 seats
```xle.method_name()```

## Self
It a way for us to refer to the object that is going be 
created from a class blueprint. 

## Example 
Mimicking a user on twitter. 

```
class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.followers = 0
        self.following = 0
        self.tweets = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def post(self):
        self.tweets += 1


user_1 = User("Vijay", "001")
# user_1 object is constructed with the User class that has two parameters.

user_2 = User("Heidi", "002")

print(user_2.user_name)

user_1.follow(user_2)

print(f"user_2 followers: {user_2.followers}")

user_1.tweets = 100

user_1.post()

print(f"user 1 tweets {user_1.tweets}")




```
