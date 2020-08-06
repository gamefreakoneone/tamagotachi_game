
from random import randrange

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


p1=Pet("Fido")
print(p1)
for i in range(10):
    p1.clock_tick()
    #print(p1)
p1.feed()
p1.teach("bark")
for i in range(10):
    p1.hi()
print(p1)