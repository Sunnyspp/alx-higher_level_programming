# ------- Solution -------
# Ask the user to input miles and assign it to miles variable
miles = input('Enter Miles: ')
# convert from strings to integer
miles = int(miles)
# Perform calculation by multiplying 1.60934 times miles
Kilometres = miles * 1.60934
# print results using format
print("{} miles equals {} Kilometers".format(miles, Kilometres))
