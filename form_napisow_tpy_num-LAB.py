name = "Mateusz"
age = 39
daysInYear = 365
daysLived = age * daysInYear

message = "{0} is {1} years old, so he is about {2} days old"

print(message.format(name, age, daysLived))

name = "Jan"
age = 26
daysLived = age * daysInYear
print(message.format(name, age, daysLived))


name = "Mateusz"
age = 39
daysInYear = 365
daysLived = age * daysInYear

message = "%s is %d years old, so he is about %d days old"

print(message % (name, age, daysLived))

name = "Jan"
age = 26
daysLived = age * daysInYear
print(message % (name, age, daysLived))


message = "{0} is {1} years old, so he is about {2} days old"
name = "Chris"
age = 17
daysLived = age * daysInYear
print(message.format(name, age, daysLived))

no1 = 1234567890
no2 = 12345

dziel_calk = no1 // no2
dziel_resz = no1 % no2

message_dziel = "{0:d} divided by {1:d} is {2:d} and the rest is {3:d}"
print(message_dziel.format(no1, no2, dziel_calk, dziel_resz))
