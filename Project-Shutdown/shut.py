print("Welcome to the shut down program!")

def shutdown():
    ans = input("Do you want to shut down your computer?")

    if ans == "Yes" or ans == "YES" or ans == "yes":
        print("Shutting down systems")
    else:
        print("Aborting shut down")

shutdown()