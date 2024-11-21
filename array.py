# Correct distances and weights
distances = [3, 5, 7]  # Distances in km where boxes are buried
weights = [200, 300, 213]  # Corresponding weights of the boxes

# Main loop
while True:
    # Get input from the user for the distances
    dist_1 = int(input("Enter distance for box 1 (km): "))
    dist_2 = int(input("Enter distance for box 2 (km): "))
    dist_3 = int(input("Enter distance for box 3 (km): "))
    
    # Check if the entered distances are correct
    if [dist_1, dist_2, dist_3] == distances:
        # Calculate total weight
        total_weight = sum(weights)
        
        # Check if the total weight is correct
        if total_weight == 713:
            print("Boxes found successfully! Total weight:", total_weight, "kg")
            break  # Exit the loop if everything is correct
        else:
            print("Total weight is incorrect. Try again.")
    else:
        print("Wrong distances entered. Try again.")
