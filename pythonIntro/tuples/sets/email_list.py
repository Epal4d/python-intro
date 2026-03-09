#initialize empty sets
subscribers = set()
unsubscribers =set()

#Function to add an email
def add_email(email, set_name):
    if set_name == "subscribers":
        subscribers.add(email) 
        print(f"Email '{email}' added to '{set_name}'")
    else:
        unsubscribers.add(email)
        print(f"Email '{email}' added to '{set_name}' ")

# Function to remove an email
def remove_email(email, set_name):
    if set_name == "subscribers" and email in subscribers:
        subscribers.remove(email)
        print(f"Email '{email}' removed from '{set_name}'")
    else:
        if set_name == "unsubscribers" and email in unsubscribers:
            unsubscribers.remove(email)
            print(f"Email '{email}' removed from '{set_name}'")
        else:
            print(f"'{email}' not found try another email.")

#Function to display emails
def display_emails(set_name):
    print(f"{set_name} Emails")
    if set_name == "subscribers":
        for email in subscribers:
            print(f"{email}")
    else:
        if set_name == "unsubscribers":
            for email in unsubscribers:
                print(f"{email}")
#function for finding active subscribers. returns the set
def find_active_subscribers():
    active_subs = subscribers - unsubscribers
    return active_subs

# Adding e"mails to subscribers "(notice tha"t some people subscribe more than once)
add_email("user3@example.com", "subscribers")
add_email("user1@example.com", "subscribers")
add_email("user4@example.com", "subscribers")
add_email("user11@example.com"," subscribers")
add_email("user5@example.com", "subscribers")
add_email("user6@example.com", "subscribers")
add_email("user2@example.com", "subscribers")
add_email("user5@example.com", "subscribers")
add_email("user2@example.com", "subscribers")
add_email("user7@example.com", "subscribers")
add_email("user8@example.com", "subscribers")
add_email("user9@example.com", "subscribers")
add_email("user2@example.com", "subscribers")
add_email("user11@example.com"," subscribers")
add_email("user7@example.com", "subscribers")
add_email("user10@example.com"," subscribers")
add_email("user12@example.com"," subscribers")

# Adding emails to unsubscribers
add_email("user6@example.com", "unsubscribers")
add_email("user8@example.com", "unsubscribers")
add_email("user1@example.com", "unsubscribers")
add_email("user10@example.com"," unsubscribers")

# Displaying subscribers and unsubscribers
print("All Subscribers:")
display_emails(subscribers)


print("All Unsubscribers:")
display_emails(unsubscribers)


# Finding active subscribers
print("Active Subscribers:")
find_active_subscribers()