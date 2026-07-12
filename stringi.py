filename = "december_production_report.xlsx"

is_excel = filename.endswith(".xlsx")

is_word = filename.endswith(".docx")

print("The file", filename)
print("- is excel", is_excel)
print("- is word", is_word)

1 + 2
"1" + "2"
"1" * 2
"=" * 40

print("10a".isalnum())
print("aaa1".isalpha())
print("AE".isascii())
print("123".isdecimal())
print("2")

continent = "Europe"
continent.upper()
print(continent)

print(continent.upper())

age = 30
birth_year = input("Wha is the birth date?")
type(birth_year)
type(age)
message = (
    "Person born in "
    + str(birth_year)
    + " is "
    + str(age)
    + " years old in "
    + str(int(birth_year) + age)
)
print(message)
