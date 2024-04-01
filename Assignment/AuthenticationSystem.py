#Function Definition
def n_upper_chars(string):
    if sum(map(str.isupper, string))<2:
        return True

def n_lower_chars(string):
    if sum(map(str.islower, string))<2:
        return True

def check_password_len(password):
    if len(password)<10:
        return True

def check_digits(string):
    if sum(map(str.isdigit,string))<2:
        return True
    
def check_special_characters(password):
    special_characters = "!@#$%^&*()-_+=<>?/\\|{}[]"
    count=0
    for char in password:
        if char in special_characters:
                count+=1
    if count<2:
            return True

def check_repetition(Password):
    for i in range(len(Password)-1):
        if Password[i]==Password[i+1] and Password[i]==Password[i+2] and Password[i]==Password[i+3]:
            return True
            break

def check_sequence(Password):
    for i in range(len(Password)-1):
        if Password[i:i+3] in User_Name:
            return True

Alpha=False
User_Name=input("Enter your UserName: ")
previous_passwords=[]
prv_psw1, prv_psw2, prv_psw3 = map(str,input("Enter your previous 3 passwords (password1 password2 password3): ").split())
previous_passwords.append(prv_psw1)
previous_passwords.append(prv_psw2)
previous_passwords.append(prv_psw3)
print(previous_passwords)

# Password Validation

def password_validation(Password):
 if check_password_len(Password):
     print("Your password must contain at least 10 characters")
     return False
 elif n_lower_chars(Password):
    print("Your password must conatain atleast 2 lowercase characters")
    return False
 elif n_upper_chars(Password):
    print("Your password must contain atleast 2 uppercase characters")
    return False
 elif check_digits(Password):
     print("Your password must contain at least 2 digits")
     return False
 elif check_special_characters(Password):
     print("Your password must contain at least 2 special characters")
     return False
 elif check_repetition(Password):
     print("Your password must not contain any repetitive characters")
     return False
 elif Password in previous_passwords:
     print("Your password must not same to the previous passwords")
     return False
 elif check_sequence(Password):
     print("Your password should not contain any sequence of 3 or more consecutive characters from UserName")
 else:
    return True
 
 
while Alpha!=True:
    Password=((input("Enter your password: ")))
    Alpha=password_validation(Password)
    if Alpha==False:
        print("You have entered a invalid password")   
print("congratulation!")
print("You have entered a valid Password")