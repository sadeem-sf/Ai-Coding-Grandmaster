passenger_name = input("Enter passenger name: ")
destination = input("Enter your destination: ")
ticket_price = float(input("Enter ticket price: Rs "))
number_of_tickets = int(input("Enter number of tickets: "))
is_available = True

print("\n--- PASSENGER DETAILS ---")
print("Passenger Name: ",passenger_name)
print("Destination: ",destination)
print("Ticket Price: Rs",ticket_price)
print("Number of Tickets: ",number_of_tickets)
print("Tickets Available?", is_available)

print("\n--- DATA TYPES ---")
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount

print("\n--- TICKET COST ---")
print("Total Cost: Rs", total_cost)
print("Discount: Rs", discount)
print("Final Cost: Rs", final_cost)

print("Double Ticket Price: ",ticket_price * 2)
print("Ticket Price After Rs50 Increase: Rs", ticket_price + 50)
print("Half Ticket Price: Rs", ticket_price / 2)

print("\n--- BOOKING CHECKS ---")
print("Is ticket price under Rs 1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination Islamabad?", destination == "Islamabad")
print("Is final cost more than Rs 2000?", final_cost > 2000)


travel_message = passenger_name + " is travelling to " + destination + "." "Travel Safely!"
print("\nTravel Message:", travel_message)
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))

morning_ticket_price = float(input("\nEnter morning ticket price: Rs "))
evening_ticket_price = float(input("Enter evening ticket price: Rs "))
print("\nBefore Swapping:")
print("Morning Ticket Price: Rs", morning_ticket_price)
print("Evening Ticket Price: Rs", evening_ticket_price)
morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
print("\nAfter Swapping:")
print("Morning Ticket Price: Rs", morning_ticket_price)
print("Evening Ticket Price: Rs", evening_ticket_price)

print("\n================================")
print("      TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: Rs", final_cost)
print("Booking Confirmed?", is_available)
print("================================")