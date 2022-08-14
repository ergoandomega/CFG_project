"""

Incorporate digital pet onto the website and with few buttons on the site we could feed, clean, play and teach the feed.

Thinking to start with a class Pet and each instance of the class will be one digital pet for user to look after.

Each instance will have a current state;

- hunger, an integer

- boredom, an integer

- sounds, a list of strings with a word the pet has been taught.




Using the __init__ method to randomise the boredom and hunger values between 0 and the threshold.

Use the clock_tick method to adjust increments for boredom and hunger variables and to simulate time passing.

Use the __str__ method to produce strings reflecting pet's current state.

"""




from random import randint




import time




#from microbit import *

#display.show()







class Pet():

    boredom_treshold = 5

    hunger_treshold = 6

    boredom_decrement = 2

    hunger_decrement = 2

    sounds = ["Mrrp"]




    def __init__(self, name, animal_type, age):

        self.hunger = range(self.hunger_treshold)

        self.boredom = reange(self.boredom_treshold)

        self.sounds = self.sounds[:]  # copy the class attributes

        self.__name = name

        self.__animal_type = animal_type

        self.__age = age




    def clock_tick(self):

        self.boredom += 1

        self.hunger += 1




    def mood(self):

        if self.hunger <= self.hunger_treshold and self.boredom <= self.boredom_treshold:

            return "happy"

        elif self.hunger > self_hunger_treshold:

            return "hungry"

        else:

            return "bored"




    def __str__(self):

        state = "   I'm " + self.name + "."

        state += " I feel " + self.mood() + "."

        return state




    def pet_words(self):

        print(self.sounds[randrange(len(self.sounds))])

        self.reduce_boredome()




    def teach(self, word):

        self.sounds.append(word)

        self.reduce_boredom()




    def reduce_hunger(self):

        self.hunger = max(0, self.hunger - self.hunger_decrement)




    def reduce_boredome(self):

        self.boredom = max(0, self.boredom - self.boredom_decrement)




    def set_name(self, name):

        self.__name = name




    def set_animal_type(self, animal_type):

        self.__animal_type = animal_type




    def set_age(self, age):

        self.__age = age




    def get_name(self):

        return self.__name




    def get_age(self):

        return self.__age




    def get_animal_tpe(self):

        return self.__animal_type







def main():

    pet_name = input('Please enter your pet\'\s name: ')

    pet_type = input('What animal is your pet?')

    pet_age = int(input('What is the age of your pet?'))




    pet_specs = Pet(pet_name, pet_type, pet_age)




    print('pet name is ', pet_specs.get_name())

    print('pet type is ', pet_specs.get_animal_tpe())

    print('pet age is ', pet_specs.get_age())










#

# p1 = Pet("CFG")

# print(p1)




# for i in range(1):

#     p1.clock_tick()

#     print(p1)




# p1.feed()

#

# p1.pet_words()

#

# p1.teach("Good Morning")




# for i in range(1):

#     p1.pet_words()

#

# print(p1)







def get_yes_or_no(message):

    valid_input = False

    while not valid_input:

        answer = input(message)

        answer = answer.upper()  # convert to upper case

        if answer == 'Y' or answer == 'N':

            valid_input = True

        else:

            print('Please enter Y for yes or N for no.')

    return answer







response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')

if response == 'Y':

    print('Great! They are very healthy.')

else:

    print('Too bad. If cooked right, they are quite tasty.')




# user to enter fitness activity for the day

activity_task = ""

while activity_task != "done":

    activity_task = input(

        "Please write down activities you want to complete today. When you are done writing the tasks simply type: done")

    print(activity_task)




# user to enter meals for the day

meal_item = ""

while meal_item != "done":

    meal_item = input(

        "Please select meals you want to add to your day. When you are done adding your meals simply type: done")

    print(meal_item)




# main()
