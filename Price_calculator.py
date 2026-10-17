
#business rules

Adult_ticket_price = {
    "normal": 80,
    "prime": 100
}

Child_ticket_price = {
    "normal": 50,
    "prime": 70
}

pass_length_multiplier = {
    "1 Day": 1,
    "3 Months": 1.5,
    "6 Months": 2,
    "12 Months": 2.5
}

def calculate_price(ticket_type, adults, kids, ticket_subtype=None):
    if ticket_type == 0:
        adult_price = Adult_ticket_price["normal"]
        child_price = Child_ticket_price["normal"]
    elif ticket_type == 1:
        adult_price = Adult_ticket_price["prime"]
        child_price = Child_ticket_price["prime"]
    else:
        return None  # Invalid ticket type

    total_adult_price = adults * adult_price
    total_child_price = kids * child_price

    total_price = (total_adult_price + total_child_price) * pass_length_multiplier.get(ticket_subtype, 1)

    return total_price