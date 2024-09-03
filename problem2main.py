from problem2functions import open_ticket, update_ticket, display_tickets, get_ticket_number

next_ticket_id = 1
service_tickets = {}

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
        display_tickets()
    else:
        break
    #end if