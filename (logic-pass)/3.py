#function that count how many the given character repeatedin a given string
string=input("enter a string:")
c=input("enter character to check its frequency:")
count=0
for i in string:
    if i==c:
        count+=1
        reminder = count % 2
        if (reminder == 0):
            print(c, "occurs", count, "times")
        else:
            print(c, "occurs", count, "time")