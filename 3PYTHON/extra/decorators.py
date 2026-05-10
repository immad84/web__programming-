def check__password(f):
     def wrapper(*args):
          print("Checking Password.")
          print("Done Checking Password")
          f(*args)
     return wrapper


@check__password
def login(password):
     if password == "secret":
          print("Login Success")
     else:
          print("Your Password is not correct")


login("sec")