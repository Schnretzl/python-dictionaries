# 2. Python Programming Challenges for Customer Service Data Handling

# Task 1: Customer Service Ticket Tracker

def open_ticket(service_tickets, ticket_id):
    ticket_id = f"Ticket{int(ticket_id):03}"
    customer = input("Customer name: ")
    issue = input("Issue: ")
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "Open"}
#end function

def update_ticket(service_tickets, ticket_id):
    ticket_data = service_tickets.get(ticket_id)
    if not ticket_data:
        print("Ticket not found.")
        return
    #end if
    if ticket_data["Status"] == "Closed":
        reopen = input("Reopen ticket? (y/n): ")
        if reopen == "y":
            service_tickets[ticket_id]["Status"] = "Open"
            print("Ticket reopened.")
        else:
            print("Ticket remains closed.")
        #end if
    elif ticket_data["Status"] == "Open":
        close = input("Close ticket? (y/n): ")
        if close == "y":
            service_tickets[ticket_id]["Status"] = "Closed"
            print("Ticket closed.")
        else:
            print("Ticket remains open.")
        #end if
    #end if

    return
#end function

def display_tickets(status):
    pass
#end function

def get_ticket_number():
    while True:
        try:
            ticket_number = int(input("Enter the ticket number to update: "))
        except TypeError:
            print("Please enter a valid ticket number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        else:
            return f"Ticket{int(ticket_number):03}"
        #end try
    #end while
#end function
    