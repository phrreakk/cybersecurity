# Working with files in Python
with open("login_attempts.txt", "r") as file:
    file_text = file.read()
print(file_text)

users = file_text.split()
print(users)

def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter +1
    if counter >= 3:
        return "You have tried to login three or more times.  Your account has been locked."
    else:
        return "You can log in!"
    
login_response = login_check(users, "hpotter")
print(login_response)