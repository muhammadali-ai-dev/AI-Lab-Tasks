class Simple_reflex:
    def __init__(a,desired):
        a.da = desired
        a.previous_mode = None
    def sensor(a,temp,occupied=True):
        a.ca = temp
        a.occupied = occupied
    def act(a):
        if not a.occupied:
            target = "off"
        elif a.ca>a.da:
            target = "AC on"
        elif a.ca == a.da:
            target = "AC off"
        else:
            target = ("AC off")

        if target != a.previous_mode:
            command = True
            a.previous_mode = target
        else:
            command = False
        return target,command

desired = int(input("Enter the desired temperature:"))
obj = Simple_reflex(desired)
rooms = [
    ("Store_room", 30,True),
    ("Store_room", 30,True),
    ("Bed_room", 12,True),
    ("Bed_room", 12,True),
    ("empty_room",30,False)
]
print("\nprevious_mode | rooms | target | command")
for room,temp,occupied in rooms:
    previous = obj.previous_mode
    obj.sensor(temp,occupied)
    target, command = obj.act()
    print(f"{previous} | {room}: {temp} | "
          f"{target} | {'send command' if command else 'no command'}")


