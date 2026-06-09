# ये है हमारा पुराना रोबोट (Parent)
class Robot:
    def speak(self):
        print("मैं बात कर सकता हूँ!")

# ये है नया रोबोट (Child), जो Robot से विरासत में सब कुछ ले रहा है
class FlyingRobot(Robot):
    def fly(self):
        print("मैं उड़ भी सकता हूँ!")

# अब देखते हैं क्या FlyingRobot बात कर सकता है?
my_bot = FlyingRobot()
my_bot.speak() # यह बात करेगा (विरासत में मिला)
my_bot.fly()   # और ये उड़ेगा भी!





# मम्मी की क्लास (Parent Class)
class Animal:
    def eat(self):
        print("मैं खाना खा रहा हूँ!")

# तुम्हारी क्लास (Child Class) - हमने ब्रैकेट में 'Animal' लिखा, इसका मतलब हमने विरासत ले ली!
class Dog(Animal):
    def bark(self):
        print("भौं-भौं!")

# अब देखो जादू!
my_dog = Dog()

my_dog.eat()  # ये तो मम्मी वाली रेसिपी है (विरासत में मिली)
my_dog.bark() # ये तुम्हारी अपनी रेसिपी है!
















