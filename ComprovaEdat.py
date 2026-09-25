import time

edad = int(input("Quina edat tens?: "))

if edad >= 101:
    r = input("Estas segur?: ")
    if r.lower() == "si":
        print("Ets molt gran")
        time.sleep(3)
    else: 
        print("Ja pensava jo...")
        edad = int(input("Quina edat tens?: "))
        time.sleep(3)

if edad < 18:
    print("Ets jove")
    time.sleep(3)
elif edad < 65:
    print("Ets major de edat")
    time.sleep(3)
else:
    print("Ets gran")
    time.sleep(3)
