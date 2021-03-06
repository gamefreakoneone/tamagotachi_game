import sys
from random import randrange
### SOMETHING IS WRONG
class Pet():
    boredom_decrement=4 # rate at which boredom reduces
    hunger_decrement=6 # rate at which hunger reduces
    boredom_threshold=5 # Limit before boredom starts settling in
    hunger_threshold=10 # Limit before hunger starts setting in
    sounds=["Peep"]

    def __init__(self,name="Sparky"):
        self.name=name
        self.hunger=randrange(self.hunger_threshold)
        self.boredom=randrange(self.boredom_threshold)
        self.sounds=self.sounds[:]
    
    def clock_tick(self):
        self.hunger+=1
        self.boredom+=1
    
    def mood(self):
        if self.hunger<self.hunger_threshold and self.boredom<self.boredom_threshold:
            return "Happy"
        elif self.hunger>self.hunger_threshold and self.boredom>self.boredom:
            return "Hungry and Bored"
        elif self.boredom>self.boredom_threshold:
            return "Bored"
        else:
            return "Hungry"
    def __str__(self):
        state="     I'm "+self.name+"."
        state += "I feel " + str(self.mood()) + "."
        #state+="     Hunger {}\n     Boredom {}\n    Words {}\n".format(self.hunger,self.boredom,self.sounds)
        return state

    def hi(self):
        print("      ",self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom()
        print("     I learnt ",word)
    
    def feed(self):
        self.reduce_hunger
        #print("Feed")

    def reduce_hunger(self):
        self.hunger=max(0,self.hunger-self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom=max(0, self.boredom-self.boredom_decrement)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None

class Cat(Pet):
    sounds=["Meow"]

    def mood(self):
        if self.hunger>self.hunger_decrement:
            return "Hungry"
        if self.boredom<2:
            return "Grumpy: Leave me alone."
        elif self.boredom>self.boredom_threshold:
            return "Bored"
        elif randrange(2)==0:
            return "Randomly annoyed"
        else:
            return "Happy"

class Dog(Pet):
    sounds=["Bark","Ruff"]

    def mood(self):
        if (self.hunger>self.hunger_threshold) and (self.boredom>self.boredom_threshold):
            return "bored and hungry"
        else:
            return "Happy"

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

class Bird(Pet):
    sounds=["chirp"]

    def __init__(self,name="Kitty",chirp_number=2):
        Pet.__init__(self,name)
        self.chirp_number=chirp_number
    
    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

class Lab(Dog):
    def fetch(self):
        self.reduce_boredom()
        return "I found the BALL!"
    
    def hi(self):
        print(self.fetch())
        print(self.sounds[randrange(len(self.sounds))])


class Poodle(Dog):
    def dance(self):
        return "Dancing in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)

pet_types={"dog":Dog, "lab":Lab, "poodle":Poodle,"cat":Cat,"bird":Bird}
def whichtype(adopt_type="general type"):
    return pet_types.get(adopt_type.lower(),Pet)


def play():
    animals=[]

    option=""
    base_prompt="""
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>
    
    Choice:"""
    feedback=""
    while True:
        action=input(feedback+"\n"+base_prompt)
        feedback=""
        words=action.split()
        print(type(words))
        if len(words)>0:
            command=words[0]
        else:
            command=None

        if command=="Quit":
            print("Exiting.2310..")
            break
        elif command=="Adopt" and len(words)>1:
            if whichone(animals,words[1]):
                feedback+="You already have a pet with that name. \n"
            else:
                if len(words)>2:
                    c1=whichtype(words[2])
                else:
                    c1=Pet
                animals.append(c1(words[1]))
        elif command=="Greet" and len(words)>1:
            pet=whichone(animals,words[1])
            if not pet:
                feedback+="I didnt recognize the pet name. Please try again."
                print()
            else:
                pet.hi()
        elif command=="Teach" and len(words)>2:
            pet=whichone(animals,words[1])
            if not pet:
                feedback+="I didnt recognize the pet name. Please try again."
                print()
            else:
                pet.teach(words[2])
        elif command=="Feed" and len(words)>1:
            pet=whichone(animals,words[1])
            if not pet:
                feedback+="I didnt recognize the pet name. Please try again."
                print()
            else:
                pet.feed()
        else:
            feedback+="I didnt understand please try again"

        for pet in animals:
            pet.clock_tick()
            feedback+="\n"+pet.__str__()


play()