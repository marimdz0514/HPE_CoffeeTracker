import random

users = {
    "Bob": 4.50,      
    "Jim": 3.00,       
    "Pam": 4.25,       
    "Dwight": 3.75,    
    "Michael": 5.00,   
    "Stanley": 4.00,   
    "Angela": 4.10
}

def validate_users(users):
    if not users:
        raise ValueError("User list is empty. Please add at least one coworker's name.")
    for name, price in users.items():
        if not isinstance(price, (int, float)):
            raise ValueError(f"Drink price for {name} must be a number.")
        if price < 0:
            raise ValueError(f"Drink price for {name} cannot be negative.")

def get_total_cost(users):
    return sum(users.values())

def get_fairest_payer(users, history):
    if not users:
        raise ValueError("User list is empty. Please add at least one coworker's name..")

    net_balances = {}
    for name in users:
        paid = history.get(name, {}).get("paid", 0.0)
        consumed = history.get(name, {}).get("consumed", 0.0)
        net_balances[name] = paid - consumed

    if all(balance == 0 for balance in net_balances.values()):
        return random.choice(list(users.keys()))

    min_balance = min(net_balances.values())
    candidates = [name for name, balance in net_balances.items() if balance == min_balance]
    return random.choice(candidates)

def update_balances(users, history, payer):
    total_cost = get_total_cost(users)
    history[payer]["paid"] += total_cost
    for person, price in users.items():
        history[person]["consumed"] += price
    return history

def add_user(users, history, new_name, price):
    new_name_clean = new_name.strip().title()
    for existing in users:
        if existing.lower() == new_name_clean.lower():
            print(f"User {existing} already exists.")
            return
    users[new_name_clean] = price
    history[new_name_clean] = {"paid": 0.0, "consumed": 0.0}
    validate_users(users)
    print(f"{new_name_clean} is now caffeinated! Price of entry: ${price:.2f}.")

def remove_user(users, history, name):
    name_clean = name.strip().lower()
    match = None
    for u in list(users):
        if u.lower() == name_clean:
            match = u
            break
    if match:
        del users[match]
        if match in history:
            del history[match]
        print(f"{match}? Never heard of them.")
    else:
        print(f"Coworker {name.strip()} does not exist.")