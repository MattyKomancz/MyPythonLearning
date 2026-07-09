# display single string

print("FR")

# display multiple strings

print("FR", "ES", "USA", "IT", "DE")

# Use Variables
country_france = "FR"
country_spain = "ES"
country_usa = "USA"
country_italy = "IT"
country_germany = "DE"

print(country_france, country_spain, country_usa, country_italy, country_germany)


# do calculations
pi = 3.14
r = 10
circle_area = pi * r**2

print(circle_area)


# separators

print(1, 2, 3)
print(1, 2, 3, sep="-")
print(
    country_france, country_spain, country_usa, country_italy, country_germany, sep="\n"
)
print(
    country_france, country_spain, country_usa, country_italy, country_germany, sep="\t"
)

print("sound", "\a")


# unicode

print("\u03a3")
