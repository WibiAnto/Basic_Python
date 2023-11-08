class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.sound} I'm {self.name}! {self.sound}")


class Cow(Animal):
    sound = "Moo~"

class goat(Animal):
    sound = "Mbee~"
Milky = Cow("Milky White")
Milky.speak()

Goat = goat("Andy")
Goat.speak()
