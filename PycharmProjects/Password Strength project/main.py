counter = 0


password = input("Enter a password ")
if len(password) >= 8:
    counter = counter +1
else:
    if len(password) <8:
        print("Warning: Password should contain at least 8 characters.")


special_characters=0
for character in password:
    if character in '!@$*&':
        special_characters=special_characters+1
if special_characters > 0:
    counter = counter +1
else:
    if special_characters == 0:
        print("Warning: password shold contain at least one special character.")



UC=0
for character in password:
    if character in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        UC= UC+1
        if UC > 0:
            counter = counter + 1


if UC < 1:
    print("Warning: Password should contain at least one uppercase letter")




if counter < 1:
    print("Password is too weak please try again")
else:
    if counter == 1:
        print("Password is still weak, please try again")
    else:
        if counter == 2:
            print("Password is okay.")
        else:
            if counter == 3:
                print("Password is strong")






