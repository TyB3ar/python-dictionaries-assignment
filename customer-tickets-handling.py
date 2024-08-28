'''
Task 1: Customer Service Ticket Tracker - Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
    - Open a new service ticket.
    - Update the status of an existing ticket.
    - Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.

Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''
        
def open_ticket(ticket_dict, new_ticket, customer_name, issue, status):    # function to open ticket, filling in info for values 
    try: 
        if new_ticket not in ticket_dict:   # if ticket given is not in dictionary
            ticket_dict[new_ticket] = {"Customer": customer_name, "Issue": issue, "Status": status}  # add sub dictinoary in, leaving values empty to fill 
            print(f"New ticket '{new_ticket}' added.") 
        else:    # if ticket given is already in dictionary, print out that it is already there 
            print(f"Ticket already in system for service.") 
    except Exception as e: 
        print("Unexpected error occured.")

def update_status(ticket_dict, ticket, status): # function to update value of status 
    #try: 
        if ticket not in ticket_dict: # if ticket called is not in current dictionary
            print("Ticket not found in current tickets for service.") 
        else: 
            for tickets, categories in ticket_dict.items(): 
                if ticket == tickets: 
                    for category in categories.keys():    # within ticket chosen, update "Status" key to status value provided 
                        if category == "Status":
                            categories["Status"] = status
                            print(f"{ticket} status has been updated to {status}.") 
                        else: 
                            continue
                else: 
                    continue 
    #except Exception as e:
        #print("Unexpected error occured.")

def display_tickets(ticket_dict): # function to display all current tickets and sub categories of tickets (name, issue, status) 
    print("Current Tickets: ")
    for tickets, categories in ticket_dict.items():
        print(f"   Ticket: {tickets}")
        for category in categories.keys(): 
            print(f"      {category}: {categories[category]}") 

service_tickets = {
    "Ticket001": {"Customer": "Arielle", "Issue": "Login problem", "Status" : "open"},
    "Ticket002": {"Customer": "Tyler", "Issue": "Payment issue", "Status" : "closed"}
}

display_tickets(service_tickets)  # display initial tickets with categories name, issue, and status

open_ticket(service_tickets, "Ticket003", "Erika", "Login Issue", "open")   # add new ticket

display_tickets(service_tickets)  # display current list of tickets, after adding 2 new

update_status(service_tickets, "Ticket002", "open")

update_status(service_tickets, "Ticket003", "closed")  # update status of one ticket 

display_tickets(service_tickets)  # display list of tickets post update status 