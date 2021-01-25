import time


name = input("Username: ")
if name == "YourName":
    pass
else:
    sys.exit(0)
password = input("Password: ")
if password == "YourPassword":
    pass
else:
    sys.exit(0)
print("")
firstquestion = input("What is your favorite color? ")
if firstquestion == "YourAnswer":
    pass
else:
    sys.exit(0)
secondquestion = input("What was your first pets name? ")
if secondquestion == "YourAnswer":
    pass
else:
    sys.exit(0)
thirdquestion = input("What is your favorite game? ")
if thirdquestion == "YourAnswer":
    pass
else:
    sys.exit(0)
if "pass":
    print("Verified")
time.sleep(1.5)
