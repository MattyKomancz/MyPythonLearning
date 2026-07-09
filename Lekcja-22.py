# To jest komentarz do tej części kodu (początek)
text = "powered by 'spaghetti code'"
text2 = 'Powered By SPAGHETTI CODE'
print(text == text2)

'''
# here we print the variable
print(text)
print(text)
print(text)
'''

import datetime
import calendar

start_year = datetime.date.today().year
end_year = 2027
end_month = 12

for year in range(start_year, end_year + 1):
    last_month = end_month if year == end_year else 12
    for month in range(1, last_month + 1):
        print(calendar.month(year, month))


'''
Alt + / - uzupełnij nazwę funkcji w oparciu o jej początkowe litery

TAB - wyświetl listę dostępnych funkcji

F5 - uruchom skrypt

Ctrl + 0 - podświetl dopasowane nawiasy otwierające i  zamykające

Alt + 3 - zakomentuj zaznaczony fragment kodu

Alt + 4 - odkomentuj zaznaczony fragment kodu
'''
