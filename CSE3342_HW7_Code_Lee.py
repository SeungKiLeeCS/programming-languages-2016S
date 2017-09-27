# -*- coding: utf-8 -*-
#Seung Ki Lee
#HW7 : Python PUBSUB
#
class Observable(object):
    def __init__(self):
        pass
    def addObserver(self, inObserver):
        if hasattr(inObserver, 'update'):
            self.observers.add(inObserver)
        else:
            print("The input does not have 'update' function implemented.")
    def removeObserver(self, inObserver):
        self.observers.discard(inObserver)
    def notifyObservers(self, message):
        pass

class MyObservable(Observable):
    #for all users in self.observer, call update
    def __init__(self, color, design):
        self.color = color
        self.design = design
        self.observers = set()
    def notifyObservers(self, message):
        for var in self.observers:
            var.update(message)
    def changeColor(self, changeColor):
        self.color = changeColor
        self.notifyObservers("The Color of your item has changed to " + str(changeColor))
    def changeDesign(self, changeDesign):
        self.design = changeDesign
        self.notifyObservers("The Design of your item has changed to " +str(changeDesign))
        
class MyObserver():
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{}, a new message has been sent: "{}"'.format(self.name, message))

        
def main():
    #create instances
    item = MyObservable("White", "Cup")
    seungki = MyObserver("Seung Ki")
    #add observer
    item.addObserver(seungki)
    #change the state -> report the state
    item.changeColor("Black")
    #to break the code
    wierdNonObserverGuy = "GDB"
    item.addObserver(wierdNonObserverGuy)
    item.changeDesign("If you see this message, the the code isn't breaking")

if __name__ == "__main__":
    main()

    
    