from problem2functions import open_ticket, update_ticket, display_tickets, get_ticket_number, get_ticket_status_type

next_ticket_id = 4
service_tickets = {"Ticket000": {"Customer": "John Doe", "Issue": "My computer won't start", "Status": "Closed"},
                    "Ticket001": {"Customer": "Jane Doe", "Issue": "My printer won't print", "Status": "Open"},
                    "Ticket002": {"Customer": "Joe Smith", "Issue": "My computer is slow", "Status": "Open"},
                    "Ticket003": {"Customer": "John Smith", "Issue": "My phone won't charge", "Status": "Closed"}}

while True:
    print("Please select a menu option:")
    print("1. Open a new ticket")
    print("2. Update an existing ticket")
    print("3. Display tickets by status")
    print("4. Quit")
    try:
        menu_option = int(input("Enter your selection: "))
    except TypeError:
        print("Please enter a valid menu option.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
    #end try
    
    if menu_option <= 0 or menu_option > 4:
        print("Please enter a valid menu option.")
        continue
    elif menu_option == 1:
        open_ticket(service_tickets, next_ticket_id)
        next_ticket_id += 1
    elif menu_option == 2:
        ticket_number = get_ticket_number()
        update_ticket(service_tickets, ticket_number)
    elif menu_option == 3:
        status_type = get_ticket_status_type()
        display_tickets(service_tickets, status_type)
    else:
        break
    #end if