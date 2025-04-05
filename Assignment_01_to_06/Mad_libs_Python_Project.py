# Advanced Mad Libs Game

print("🎉 Welcome to the Advanced Mad Libs Game!")
print("Please provide the following words:\n")

# Inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")
food = input("Enter a type of food: ")
number = input("Enter a number: ")
color = input("Enter a color: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
sound = input("Enter a sound: ")
vehicle = input("Enter a vehicle: ")

# Story
madlib = f"""
Once upon a time, {name} went to {place} on a {vehicle}.
On the way, they found a {color} {animal} who looked very {emotion}.
{name} offered the {animal} some {food}, and it made a loud "{sound}" sound.

The {animal} had {number} legs and a very shiny {body_part}.
{name} was so {adjective} that they started to {verb}.

And that's how a beautiful friendship began between {name} and the magical {animal}.
"""

# Output
print("\n🎊 Here is your custom Mad Libs story:\n")
print(madlib)
