helloMessage = "Hello %s!"

Name = "Kate"
print(helloMessage % (Name))

Name = "Chris"
print(helloMessage % (Name))

helloMessage = "Hello {0:s}!"
Name = "Chris"
print(helloMessage.format(Name))

Name = "Kate"
print(helloMessage.format(Name))

# 5. Zmień zawartość zmiennej helloMessage na

message = "%s has %d %s"
Name = "Kate"
no_of_animals = 1
of_what = "animals"
print(message % (Name, no_of_animals, of_what))

Name = "Chris"
cash = 100000
currency = "$"
print(message % (Name, cash, currency))

massage = "{0:s} has {1:d} {2:s}"
Name = "Kate"
no_of_animals = 1
of_what = "animals"
print(massage.format(Name, no_of_animals, of_what))

massage = "{0:s} has {1:d} {2:s}"
Name = "Chris"
cash = 100000
currency = "$"
print(massage.format(Name, cash, currency))


# zadanie 9 napis formatujący

import unicodedata

EUR = "\u20ac"

line = "{0:20s} costs {1:6d} {2}"

print(line.format("ICE CREAM", 3, EUR))
print(line.format("TRIP TO VENICE", 119, EUR))
print(line.format("PIZZA", 6, EUR))

line = "{0:s} {1:2} {2}"
print(line.format("ICE CREAM", 3, EUR))
print(line.format("TRIP TO VENICE", 119, EUR))
print(line.format("PIZZA", 6, EUR))
