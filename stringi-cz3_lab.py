article = """
Monty Python, also known as the Pythons,[1][2] were a British comedy troupe formed in 1969 consisting of Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones and Michael Palin. The group initially came to prominence in the UK for the sketch comedy television series Monty Python's Flying Circus, which aired on the BBC from 1969 to 1974. Their work then developed into a larger collection that included live shows, films, albums, books, and musicals; their influence on comedy has been compared to the Beatles' influence on music.[3][4][5] Their sketch show has been called "an important moment in the evolution of television comedy".[6]
"""

print(article.upper())

print(article.lower().replace("monty", "flying"))

print(article.split(" "))

print("word Python appears", article.lower().count("python"), "times")

print("to print the \\ you need to put \\ twice in your text like this: \\\\")

print("The best hits of '80s!!!")
print("The best hits of '80s!!!")

amountPLN = 234
rateUSD = 3.65
rateEUR = 4.23

print("cur", "\texchange", "\tamont")
print("USD", "\t", str(rateUSD), "\t", (amountPLN / rateUSD))
print("EUR", "\t", str(rateEUR), "\t", (amountPLN / rateEUR))

valueAsText = "123.45"
factor = 1.23

print(
    "value is",
    valueAsText,
    "factor is",
    factor,
    "value * factor =",
    float(valueAsText) * factor,
)
