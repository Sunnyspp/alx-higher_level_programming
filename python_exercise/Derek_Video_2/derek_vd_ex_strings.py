# -----Strings-----
samp_strings = "This is a very important strings"
print("Length :", len(samp_strings))
# ______string slicing_______
print(samp_strings[0:14])
print(samp_strings[1:4])  # this will include 1 but exclude 4
# ______concatenate strings_______
print("Green" + "Eggs")
print("Alexis " + "Isibor")
# ______multiply/repeat strings_______
print("Green " * 5)
print("Alexis " * 6)
# ______convert integer to strings_______
num_strings = str(4)
print(num_strings)
# ______print character in a strings_______
for char in samp_strings:
    print(char)
print(num_strings)

for i in range(0, len(samp_strings)-1, 2):
    print(samp_strings[i] + samp_strings[i+1])
# ______uni code_______
# A - Z 65 - 90
# a - z 97 - 122
print("A =", ord("A"))
print("65 =", chr(65))
