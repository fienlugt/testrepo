BookRating = {"Dance of Thieves" :"5 stars!\n A thrilling fantasy love story between fearless heroine and dangerous loyal king who are both misunderstood.", "It ends with us" : "5 big fat stars.\n I was absolutely broken after reading this book and have never seen a situation so clearly from a character's perspective.\n Every women should read this book and understand it's significance", "Punk57" : "4 stars!n I loved how imperfect Ryen and Misha were in this book.\n It made the journey to redemption so much greater and I fell even more in love with them."}
starting = str(input("Do you want to find a book rating?\n"))

for yesno in starting:
    if yesno in ['y', 'Y', 'yes', 'Yes', 'YES']:
        book = input("What book do you want to know about?\n")
        print(BookRating[book])
        answer = input("Do you want to see another book's rating?\n")
        for x in answer:
            if x in ['y', 'Y', 'yes', 'Yes', 'YES']:
                continue
            elif x in ['n', 'N', 'no', 'No', 'NO']:
                print("That's okay, thank you for choosing us!")
        else:
            print("Please answer with yes or no")
            continue
    elif yesno in ['n', 'N', 'no', 'No', 'NO']:
        print("What are you doing here then? Byeeee")
else:
    print("Please answer with yes or no.")

print("See you next time!")
