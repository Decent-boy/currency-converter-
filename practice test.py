def currncy(usd):
    rs=usd*280
    print(f"PKR : {rs}")

while True:
    try:
        user=input("are you wnated to see currncey of pkr\ntype y: ")
        if user.lower().strip()=="y":
            usd=int(input("Enter usd dollors: "))
            currncy(usd)
        else:
            quit()

            # print("sorry")
    except ValueError:
        print("invalid")