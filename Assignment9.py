"""
Homework Assignment #9: Classes


Details:
 
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".

The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.

Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  It should have another method called 
"Stop" that sets the value of isDriving to false.

Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100, then 
the NeedsMaintenance boolean should be set to true.

Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out their values for Make, Model, 
Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to 
Driving and Stopping), but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be 
rejected (return false), and an error message should be printed saying that the plane can't fly until it's repaired.


Submitted by: Jansen Gomez

"""
import random
from termcolor import colored, cprint

class Vehicle:

    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

class Cars(Vehicle):
    def __init__(self,Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isDriving=False):
        Vehicle.__init__(self,Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance)
        self.isDriving = isDriving

    def drive(self):
        self.isDriving = True
        
    def stop(self):
        if self.isDriving:
            self.isDriving = False
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = colored(True,'red',attrs=['bold'])


class Planes(Vehicle):
    def __init__(self,Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isFlying=False):
        Vehicle.__init__(self,Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance)
        self.isFlying = isFlying

    def flying(self):
        self.isFlying = True
        
    def landing(self):
        if self.isFlying:
            self.isFlying = False
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = colored(True,'red',attrs=['bold'])


# Drive cars at different number of times (using random function)
def driveCar(car):
    driveXTimes = random.randint(1,100)
    for i in range(driveXTimes):
        car.drive()
        car.stop()

# Fly planes at different number of times (using random function)
def flyPlane(plane):
    if plane.NeedsMaintenance == colored(True,'red',attrs=['bold']):
        cprint("\n" + plane.Make + ", " + plane.Model + " NEEDS TO BE REPAIRED BEFORE IT CAN FLY!!! (trips remain the same until repaired...)",'red',attrs=['bold'])
    else:
        flyXTimes = random.randint(1,100)
        for i in range(flyXTimes):
            plane.flying()
            plane.landing()

#Car details
Car1 = Cars("Honda","CRV",1999,2700)
Car2 = Cars("Toyota","Avanza",2016,1600)
Car3 = Cars("Isuzu","MuX",2020,3500)

#Plane details
Plane1 = Planes("RotaryWing","Apache",2016,2340)
Plane2 = Planes("FixedWing","F15",2018,1890)


#Ask what the user wants to do, Drive or Fly
while(True):
    UserOption = input(colored("\n\nDo you want to DRIVE or FLY?(Type 'D' for Drive, 'F' for Fly, other keys to exit) ",'yellow',attrs=['bold']) )
    
    # if User selected to Drive
    if UserOption == 'D' or UserOption == "d":
        #start driving all cars at different times
        while(True):
            driveCar(Car1)
            driveCar(Car2)
            driveCar(Car3)


            print(colored("\nCars details:\t\t\tCar1\t\tCar2\t\tCar3",'blue',attrs=['bold']) + "\n\n"
                    +colored("Make:\t\t\t\t",'yellow',attrs=['bold']) + Car1.Make + "\t\t" + Car2.Make + "\t\t" + Car3.Make + "\n"
                    +colored("Model:\t\t\t\t",'yellow',attrs=['bold']) + Car1.Model + "\t\t" + Car2.Model + "\t\t" + Car3.Model + "\n"
                    +colored("Year:\t\t\t\t",'yellow',attrs=['bold']) + str(Car1.Year) + "\t\t" + str(Car2.Year) + "\t\t" + str(Car3.Year) + "\n"
                    +colored("Weight:\t\t\t\t",'yellow',attrs=['bold']) + str(Car1.Weight) + "\t\t" + str(Car2.Weight) + "\t\t" + str(Car3.Weight) + "\n"
                    +colored("Needs Maintenance:\t\t",'yellow',attrs=['bold']) + str(Car1.NeedsMaintenance) + "\t\t" + str(Car2.NeedsMaintenance) + "\t\t" + str(Car3.NeedsMaintenance) + "\n"
                    +colored("Trips since Maintenance:\t",'yellow',attrs=['bold']) + str(Car1.TripsSinceMaintenance) + "\t\t" + str(Car2.TripsSinceMaintenance) + "\t\t" + str(Car3.TripsSinceMaintenance))

            # added additional method to use repair function when vehicle needs maintenance
            for i in range(3):
                if i==0:
                    CarX = Car1
                elif i==1:
                    CarX = Car2
                else:
                    CarX = Car3

                if CarX.NeedsMaintenance == colored(True,'red',attrs=['bold']):
                    repairCar = input(colored("\nCar" + str(i+1) + " needs Overhauling! Do you want to repair it?(Y/N) ",'red',attrs=['bold']))
                    if repairCar == "Y" or repairCar == "y":
                        CarX.repair()
                        print(colored("Car" + str(i+1) + " Repaired/Overhauled! Trips reset to 0...",'yellow',attrs=['bold']))

            driveAgain = input("\nDo you want to continue driving?(Y/N) ")
            if driveAgain == "N" or driveAgain == "n":
                break
    
    elif UserOption == "F" or UserOption == "f":

        #start flying all planes at different times
        while(True):
            flyPlane(Plane1)
            flyPlane(Plane2)

            print(colored("\nPlane details:\t\t\tPlane1\t\tPlane2",'blue',attrs=['bold']) + "\n\n"
                    +colored("Make:\t\t\t\t",'yellow',attrs=['bold']) + Plane1.Make + "\t" + Plane2.Make + "\n"
                    +colored("Model:\t\t\t\t",'yellow',attrs=['bold']) + Plane1.Model + "\t\t" + Plane2.Model + "\n"
                    +colored("Year:\t\t\t\t",'yellow',attrs=['bold']) + str(Plane1.Year) + "\t\t" + str(Plane2.Year) + "\n"
                    +colored("Weight:\t\t\t\t",'yellow',attrs=['bold']) + str(Plane1.Weight) + "\t\t" + str(Plane2.Weight) + "\t\t" + "\n"
                    +colored("Needs Maintenance:\t\t",'yellow',attrs=['bold']) + str(Plane1.NeedsMaintenance) + "\t\t" + str(Plane2.NeedsMaintenance) + "\t\t" + "\n"
                    +colored("Trips since Maintenance:\t",'yellow',attrs=['bold']) + str(Plane1.TripsSinceMaintenance) + "\t\t" + str(Plane2.TripsSinceMaintenance))

               # added additional method to use repair function when plane needs maintenance
            for i in range(2):
                if i==0:
                    PlaneX = Plane1
                elif i==1:
                    PlaneX = Plane2

                if PlaneX.NeedsMaintenance == colored(True,'red',attrs=['bold']):
                    repairPlane = input(colored("\nPlane" + str(i+1) + " needs to be repaired and WILL NOT FLY UNTIL REPAIRED! Do you want to repair it?(Y/N) ",'red',attrs=['bold']))
                    if repairPlane == "Y" or repairPlane == "y":
                        PlaneX.repair()
                        cprint("Plane" + str(i+1) + " Repaired and ready to fly! Trips reset to 0...",'yellow',attrs=['bold'])

            flyAgain = input("\nDo you want to continue flying?(Y/N) ")
            if flyAgain == "N" or flyAgain == "n":
                break                

    else:
        break # exit if other keys besides "D" and "F" are pressed





