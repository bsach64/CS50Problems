months = {
    "January" : 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


while True:
    user_date = input("Date: ").strip()
    if user_date.count('/') == 2:
        user_date = user_date.split('/')
        try:
            if int(user_date[0]) > 0 and int(user_date[0]) <= 12:
                if int(user_date[1]) > 0 and int(user_date[1]) <= 31:
                    print(f"{int(user_date[2]):04}-{int(user_date[0]):02}-{int(user_date[1]):02}", end)
                    break
        except ValueError:
            pass
    elif user_date.count(" ") == 2 and user_date.count(',') == 1:
        user_date = user_date.replace(',','')
        user_date = user_date.split(" ")
        if user_date[0] in months:
            if int(user_date[1]) > 0 and int(user_date[1]) <= 31:
                print(f"{int(user_date[2]):04}-{months[user_date[0]]:02}-{int(user_date[1]):02}")
                break



