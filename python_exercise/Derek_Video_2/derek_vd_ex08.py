# Enter string to hide in uppercase : HIDE
# Secret Message : 35647890
# Original Message : HIDE

# ______Solution______
# Input "Enter a string to hide in the uppercase"
norm_string = input("Enter a string to hide in uppercase : ")

secret_string =""
# cycle through each character in the string
for char in norm_string:
    # store each character code in a new string
    secret_string += str(ord(char))
# print "Secret Message : 56349078"
print("Secret Message : ", secret_string)
# Cycle through the character code 2 at a time by incrementing by 2 each time
norm_string = ""
for i in range(0, len(secret_string)-1, 2):
    # Get the 1st and 2nd for this two digit number
    char_code = secret_string[i] + secret_string[i+1]
    # convert the code into characters and add them to a new string
    norm_string += chr(int(char_code))
# print original message : HIDE
print("Original Message :", norm_string)
