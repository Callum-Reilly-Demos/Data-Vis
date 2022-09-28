# This calculator converts a cm height to ft. 

#Asks the user for input
height_cm = input('Enter your height in cm: ')
#input is stored in the variable as a string, this needs to be converter to a numerical value
#in order to be divisible, the type casting below does this. 
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48 )
