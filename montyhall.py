import random as rand

door_image = [0, 1, 2]
doors = [0, 0, 0]

print(door_image)
a = int(input("pick a door"))


# picks a random door to put the car
# 1 means car, 0 means goat
car = rand.randint(0, 2)
doors[car] = 1

# opens the non chosen door containing a goat
door_open = False
while not door_open:
    possible_door = rand.randint(0, 2)
    if doors[possible_door] == 0 and possible_door != a:
        open_door = possible_door
        door_open = True

# Changing the door image
for d in range(3):
    if d == a:
        door_image[d] = "chosen"
    elif d == open_door:
        door_image[d] = "goat"
    else:
        door_image[d] = "closed"
        closed = d
print(door_image)

# Final door choice
switch = input("switch? y/n")
if switch == "y":
    if doors[closed] == 1:
        print("You win a car!")
    else:
        print("You got a goat :(")

else:
    if doors[a] == 1:
        print("You win a car!")
    else:
        print("You got a goat :(")

print(doors)
