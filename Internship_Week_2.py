# Constants
NUM_TRAIN_JOURNEYS = 4
NUM_COACHES_NORMAL = 6
NUM_SEATS_PER_COACH = 80
TICKET_PRICE = 25

# Initialize data structures
passengers_count = {'up': [0] * NUM_TRAIN_JOURNEYS, 'down': [0] * NUM_TRAIN_JOURNEYS}
revenue = {'up': [0] * NUM_TRAIN_JOURNEYS, 'down': [0] * NUM_TRAIN_JOURNEYS}

# Function to display the current status
def display_status():
    print("Train Schedule:")
    for i in range(NUM_TRAIN_JOURNEYS):
        print(f"{9 + i * 2:02}:00 - Up Train: {80 - passengers_count['up'][i]} tickets available")
        print(f"{10 + i * 2:02}:00 - Down Train: {80 - passengers_count['down'][i]} tickets available")
        print("")

# Function to calculate the total price including group discount
def calculate_total_price(num_passengers):
    normal_price = TICKET_PRICE * num_passengers
    num_groups = num_passengers // 10
    discount = TICKET_PRICE * num_groups
    total_price = normal_price - discount
    return total_price

# Task 1 - Start of the day
# Display the initial status
print("Start of the day:")
display_status()

# Task 2 - Purchasing tickets
# Simulate ticket purchases
while True:
    try:
        journey_type = input("Enter journey type (up/down/exit): ").lower()
        if journey_type == 'exit':
            break
        if journey_type not in ['up', 'down']:
            print("Invalid journey type. Please enter 'up', 'down', or 'exit'.")
            continue

        journey_index = int(input("Enter journey index (1-4): ")) - 1
        if not (0 <= journey_index < NUM_TRAIN_JOURNEYS):
            print("Invalid journey index. Please enter a number between 1 and 4.")
            continue

        num_passengers = int(input("Enter the number of passengers: "))
        if not (1 <= num_passengers <= NUM_SEATS_PER_COACH * NUM_COACHES_NORMAL):
            print(f"Invalid number of passengers. Please enter a number between 1 and {NUM_SEATS_PER_COACH * NUM_COACHES_NORMAL}.")
            continue

        # Check if enough tickets are available
        if passengers_count[journey_type][journey_index] + num_passengers > NUM_SEATS_PER_COACH * NUM_COACHES_NORMAL:
            print("Not enough tickets available. Please choose a different journey.")
            continue

        # Update data structures
        passengers_count[journey_type][journey_index] += num_passengers
        total_price = calculate_total_price(num_passengers)
        revenue[journey_type][journey_index] += total_price

        print(f"Tickets purchased successfully. Total price: ${total_price}")

        # Display updated status
        display_status()

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break

# Task 3 - End of the day
# Display the end-of-day summary
print("\nEnd of the day summary:")
for journey_type in ['up', 'down']:
    for i in range(NUM_TRAIN_JOURNEYS):
        print(f"{9 + i * 2:02}:00 - {journey_type.capitalize()} Train: {passengers_count[journey_type][i]} passengers, Revenue: ${revenue[journey_type][i]}")
    print("")

total_passengers = sum(passengers_count['up']) + sum(passengers_count['down'])
total_revenue = sum(revenue['up']) + sum(revenue['down'])
print(f"Total passengers for the day: {total_passengers}")
print(f"Total revenue for the day: ${total_revenue}")

most_passengers_index = passengers_count['up'].index(max(passengers_count['up']))
print(f"The train journey with the most passengers today is the {9 + most_passengers_index * 2:02}:00 Up Train.")
