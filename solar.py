#******************************************************************************
# solar.py
#******************************************************************************
# Name: Jared Zambarrano
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): NONE
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# The first two lines take the width and the length of the respective property. 
# Variables "width" and "length" are used to represent their respective inputs.
# To start, the input method is used to allow the user to input some value to represent the width 
# and length of their property.

# However, when entering the input for width, it uses the int method to specify that it will only 
# accept integer data values, this is the same for length. 

width = float(input("Enter width (in ft): "))
length = float(input("Enter length (in ft): "))

# After determining the length and width, we'd like to know several factors for installing solar panels
# The first is total square footage of the area, which  is calculated by taking width and multiplying it 
# by length. You'll notice that we want to specify the output to be a float data type, so we use the 
# float method. 

square_ft = float(width)*float(length)

# The next thing we need to determine is the number of solar panels we can fit on the customer's roof.
# The useable area of panels we can install has some constraints. First, only the south facing side of
# the property can be used, so that reduces total square footage by exactly 50%. In addition to this, 
# to allow for emergencies, we are only allowed to allocate 75% of that 50% to actually installing the 
# solar panels. With all of these constraints in mind,  we take the total square footage, multiply it by 50% 
# and then take 75% of that to determine our total panel area.

panel_area = float((square_ft*(0.50)*0.75))

# Now that we have determined our total panel area, we would also like to know how many solar panels we can fit
# on the area of the customer's roof where we are allowed to install solar panels. A single solar panel takes up
# exactly 21.2 ft**2 of the roof, and we cannot cut solar panels in half. It should also be noted that whatever the
# result is, we need to round to a nice whole number, to do this we can use the int method.

number_of_solar_panels = int(panel_area/21.2)

# We would also like to know the total number of wattage the solar panels take up. A single solar panel is rated for
# 400 watts. To determine total wattage, we take the total number of wattage and multiply that number by 400.

watts = int(number_of_solar_panels*400)

# Next, we would like to determine how many kilowatt-hours our customer will be using. To determine this figure, we 
# must note that in New York, you can expect to generate approximately 0.978 kilowatt-hours per year for each watt.

# For this variable, to calculate the number of kilohours we need by taking the number of solar panels and multiplying
# this number by 400, which manually gives us the total wattage of all solar panels. Using this number we know that for
# Every one watt it generates 0.978 kilowatt hours. To calculate the total amount of kilowatt hours we take the total 
# wattage of all solar panels and multiply it by 0.978.

# We use float and round methods to indicate we want the output to be a float and to round to the nearest tenth.

kilohours = round(float((number_of_solar_panels*400)*0.978), 1)

# Finally, we would like to determine the total cost of electricity for the customer. To determine this figure, we 
# must note that electricity costs about $0.24 per kilowatt-hour. With this in mind, we take the total kilowatt-hours
# multiply that figure by 0.24 to give us our total cost.

# For this variable, like the one above, we used the float method to specify that the result of kilohours multiplied by 
# 0.24 should only be able to output a float data type. We then nested the result of this into a round method 
# which, when put together, specifies that whatever the output is for the kilohours*0.24 we first want it to be a 
# float then we want to round it by two decimal places.

cost = round(float(kilohours*0.24), 2)

# The following print methods outputs the previous variables on the terminal:

print(f"You have {square_ft} square feet of roof area and {panel_area} square feet usable for panels.")
print(f"You can fit {number_of_solar_panels} solar panels on your roof.")
print(f"You can install a system rated for {watts} watts.")
print(f"You can generate about {kilohours} kilowatt-hours in a year.")
print(f"That's equivalent to about ${cost:.2f} of electricity.")
