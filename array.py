import os
os.system("cls" if os.name=="nt" else "clear")
import random
boxes = [
    {'distance': 2, 'weight': 200}, 
    {'distance': 4, 'weight': 300},  
    {'distance': 6, 'weight': 213}   
]
while True:
    dist1 = int(input("Enter distance for box 1 (1-7): "))
    dist2 = int(input("Enter distance for box 2 (1-7): "))
    dist3 = int(input("Enter distance for box 3 (1-7): "))
    total_weight = 0
    found_boxes = 0  
    for dist in [dist1, dist2, dist3]:
        for box in boxes:
            if box['distance'] == dist:
                total_weight += box['weight']
                found_boxes += 1
                break
    if found_boxes == 3 and total_weight == 713:
        print("Cargo found! Total weight: 713 kg")
        break
    else:
        print(f"Total weight: {total_weight} kg. Try again!")
        for box in boxes:
            box['distance'] = random.randint(1, 7)  
            box['weight'] = random.randint(200, 250)
        print("The boxes have moved to new locations. Try again!")

