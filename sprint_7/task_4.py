# Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes but all the tasks separately. 
# We need a system that can automate the whole task without the disturbance or interference of us. 

# To solve the above-described problem, we would like to hire the Facade Method. 
# It will help us to hide or abstract the complexities of the subsystems as follows.

class WashingSubsystem:
    def wash(self):
        print("Washing...")

class RinsingSubsystem:
    def rinse(self):
        print("Rinsing...")

class SpinningSubsystem:
    def spin(self):
        print("Spinning...")

class WashingMachine:
    def __init__(self):
        self.washing_subsystem = WashingSubsystem()
        self.rinsing_subsystem = RinsingSubsystem()
        self.spinning_subsystem = SpinningSubsystem()

    def startWashing(self):
        self.washing_subsystem.wash()
        self.rinsing_subsystem.rinse()
        self.spinning_subsystem.spin()
