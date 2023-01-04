# ======Comparing concatenation and formatted string ====
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
name = 'Sunny'
work = 'doctor'
email_message = name + ' is a ['+ work + ']'
print(email_message)
msg = f'{first} [{last}] is a coder'
email_msg = f'{name} is a [{work}]'
print(msg)
print(email_msg)
#  ====== Manipulation of strings =====
course = 'Python for Beginners'
print(len(course))
print(course)
print(course.upper())
print(course.lower())
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute beginners'))
print('python' in course)
print('Python' in course)
