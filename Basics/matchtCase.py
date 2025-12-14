day = input("Enter the day of the week: ")
match day:
    case "saturday":
        print("Today is the first day of the week")
    case "sunday":
         print("Today is the second day of the week")
    case "Monday":
         print("Today is the third day of the week")
    case "Tuesday":
         print("Today is the fourth day of the week")
    
    case "Friday":
        print("Today is off.")
    case _:
        print("other day")

#----------------
score = int(input("Enter score: "))
match score:
    case _ if score >=90:
        print("A")
    case _ if score >=80:
        print("B")

    case _ if score >=70:
        print("C")
    case _:
        print("F")
#----------------

color = input("Enter a color:")
match color:
    case "red" | "yellow" | "blue":
        print("pimary color")
    case _ :
        print("other color")


#----------------

num = int(input("Enter a number:"))
match num:
    case 0:
        print("zero")
    case _ if num >0:
        print("possitive")
    case _ if num <0 :
        print("negative")



char = input("Enter a letter :")
match char:
    case "a" | "e" | "i" | "o" | "u":
        print("vowel")


    case _ if char.isalpha():
         print("consonant")
    case _:
         print("Not a leter")

    
