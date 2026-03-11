def shutdown():
    shutdowninput=input("Do you want to shutdown the computer:")
    if shutdowninput=="Yes":
        print("Shutting Down")
    elif shutdowninput=="No":
        print("Not Shutting Down")
    else:
        print("Sorry")

shutdown()