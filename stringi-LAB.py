quote = "A good programmer is someone who always looks both ways before crossing a one-way street"

print(quote.upper())

print(quote.lower())

ends_with_street = quote.endswith("street")

print("quote ends with street -", ends_with_street)

print(quote.upper().isupper())

print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())

print(quote.split(" "))

print(quote.replace("one", "1").replace("both", "2"))

print(quote.find("one"))
