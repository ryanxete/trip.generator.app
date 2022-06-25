# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing

import random

destinations = ["Bali", "Tulum", "Marbella", "Berlin"]
transportation = ["Rental Car", "Bus", "Train", "Helicopter"]
food_category = ["Local Foods", "Pizzas", "Burgers", "Steak and Fried Chicken"]
fav_hobby = ["to chill by the pool in the hotel", "to go for outdoor activities in nature", "to visit Historical sites", "Partying"]
chosen_destination = ''
chosen_transportation = ''
chosen_food_category = ''
chosen_fav_hobby = ''
answer = ''
def decision_prompt():
    global answer
    answer = input("please answer with yes or no. ")
def too_many():
    print("please choose one of these options(more will be added soon)")
    # destinations functions
def random_destination(arr):
    global chosen_destination
    chosen_destination = random.choice(arr)
    print(f"ok {name}, we have chosen {chosen_destination} for you to go! is that an option to consider? ")
    decision_prompt()
    return
def good_w_destination():
    print(f"awesome {name} next please confirm your fav method of transportation.")
def again():
    print("no problem")
    random_destination(destinations)
    # print(f"ok {name}, we have chosen {chosen_destination} for you to go! is that an option to consider? ")
    # decision_prompt()
# transportation functions
def random_transportation(arr):
    global chosen_transportation
    chosen_transportation = random.choice(arr)
    if chosen_transportation == "Helicopter":
        print(f"here it is, the chosen method for you is the '{chosen_transportation}'! \nwould you like to confirm? ")
    else:
        print(f"here is the chosen transportation method for you {chosen_transportation}!\nto be honest there are better options(stay with no)\nis that still a choice? ")
    decision_prompt()
    return
def good_w_tranportation():
    print("awesome next please confirm your fav food category for most of the trip.")
def again_trans():
    print("no problem")
    random_transportation(transportation)
# food functions
def random_food(arr):
    global chosen_food_category
    chosen_food_category = random.choice(arr)
    print(f"couple more to go, would you like {chosen_food_category} as of one of the fav meals? ")
    decision_prompt()
    return
def good_w_food():
    print("good taste, lastly let's get to know your favourite hobby while we're on the vacation.")
def again_food():
    print("no problem")
    random_food(food_category)
# hobby functions
def random_hobby(arr):
    global chosen_fav_hobby
    chosen_fav_hobby = random.choice(arr)
    print(f"one of our options is {chosen_fav_hobby}, would you like it? ")
    decision_prompt()
    return
def good_w_hobby():
    print("love it, we are finally done with the choices! would you like to confirm the trip?" )
    decision_prompt()
    if answer == "yes" or answer == "Yes":
        print("perfect, here is the summary of your generated trip,\nsure you'll have a lot of fun!")
        summary()
    else:
        print("please come back later")
def again_hobby():
    print("no problem")
    random_hobby(fav_hobby)
# is done function
def summary():
    print(f"here is the summary of your trip:\ndestination: {chosen_destination}\ntransportation: {chosen_transportation}\nfood category: {chosen_food_category}\nfav hobby: {chosen_fav_hobby}\nthanks for choosing tripy.")
# first we want to welcome the user
print("welcome to tripy,\nbeen wanting to go on a vacation but don't know where?\nwant to free your mind, but can't manage to plan?\nwe got you! we will provide you with our top destinations and you'll get to choose your favourite. ")
name = input("please enter your full name! ")
welcomed = True
# choosing a random destination, prompt it and ask if they'd like it. if not prompt them with another random choice
while welcomed is True:
    random_destination(destinations)
    if answer == "yes":
        good_w_destination()
        break
    else:
        again()
        if answer == "yes" or answer == "Yes":
            good_w_destination()
            break
        else:
            again()
            if answer == "yes" or answer == "Yes":
                good_w_destination()
                break
            else:
                again()
                if answer == "yes" or answer == "Yes":
                    good_w_destination()
                    break
                else:
                    too_many()
# if liked the last one, generate random transportation options, if not liked prompt back
while welcomed is True:
        random_transportation(transportation)
        if answer == "yes" or answer == "Yes":
            good_w_tranportation()
            break
        else:
            again_trans()
            if answer == "yes" or answer == "Yes":
                good_w_tranportation()
                break
            else:
                again_trans()
                if answer == "yes" or answer == "Yes":
                    good_w_tranportation()
                    break
                else:
                    too_many()
# if liked the last one, generate random food-category options, if not liked prompt back
while welcomed is True:
        random_food(food_category)
        if answer == "yes" or answer == "Yes":
            good_w_food()
            break
        else:
            again_food()
            if answer == "yes" or answer == "Yes":
                good_w_food()
                break
            else:
                again_food()
                if answer == "yes" or answer == "Yes":
                    good_w_food()
                    break
                else:
                    too_many()
# if liked the last one, generate random entertainment options, if not liked prompt back
while welcomed is True:
        random_hobby(fav_hobby)
        if answer == "yes" or answer == "Yes":
            good_w_hobby()
            break
        else:
            again_hobby()
# when agreed with the options confirm the trip and print the complete trip 