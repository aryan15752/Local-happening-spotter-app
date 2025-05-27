events = []

# Function to add a new event
def add_event():
    name = input("Enter the name of the event: ")
    date = input("Enter the date of the event (YYYY-MM-DD): ")
    location = input("Enter the location of the event: ")
    event = {
        "name": name,
        "date": date,
        "location": location
    }
    events.append(event)
    print("Event added successfully!\n")

# Function to display all events
def display_events():
    if not events:
        print("No events to display.\n")
    else:
        print("Upcoming Sports Events:")
        for idx, event in enumerate(events, start=1):
            print(f"{idx}. {event['name']} - {event['date']} at {event['location']}")
        print()

# Function to display the menu
def menu():
    print("Local Happening Sporter App")
    print("1. Add a new event")
    print("2. Display all events")
    print("3. Exit")

# Main program loop
while True:
    menu()
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        add_event()
    elif choice == "2":
        display_events()
    elif choice == "3":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
