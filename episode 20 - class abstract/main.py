# class abstract

from abc import ABC,abstractmethod # ABC = abstract base class

class Button(ABC):

    @abstractmethod # ini decorator
    def click(self):
        pass

class PushButton(Button):
    
    def click(self):
        print("push button click")

class RadioButton(Button):

    def click(self):
        print("radio button click")

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
# help(tombol1) # Method resolution order: PushButton, Button, abc.ABC, builtins.object
