#hej = 1
#hej = ord("a")
#hej = chr(10)

#print("värde")
#print("hej")

options = 0

while options != 3:
    try:
        options = int(input("välj ett nummer mellan 1-3\n:"))
    except:
        print("måste vara ett nummer")
    if options == 1:
        print("du har valt 1")
    elif options == 2:
        print("du har valt 2")
    elif options == 3:
        break
    else:
        print("kan du inte nummer eller")