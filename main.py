from coffeetracker.coffee import (
    users, validate_users, get_fairest_payer, get_total_cost,
    update_balances, add_user, remove_user
)
from coffeetracker.storage import load_history, save_history
import os

HISTORY_FILE = os.path.join("data", "history.json")

def show_balances(history):
    print("\n~ Current Balances ~")
    for person in users:
        data = history.get(person, {"paid": 0.0, "consumed": 0.0})
        net = data["paid"] - data["consumed"]
        print(f"{person}: Paid ${data['paid']:.2f}, Consumed ${data['consumed']:.2f}, Net ${net:.2f}")

def run_round():
    global history
    payer = get_fairest_payer(users, history)
    total_cost = get_total_cost(users)
    print(f"Today, {payer} will pay ${total_cost:.2f} for everyone.")
    history = update_balances(users, history, payer)
    save_history(HISTORY_FILE, history)

if __name__ == "__main__":
    validate_users(users)
    history = load_history(HISTORY_FILE, users)
    save_history(HISTORY_FILE, history)

    while True:
        try:
            cf_command = input("\n Please type 'pay', 'show', 'add', 'remove', or 'exit': ").strip().lower()
            if cf_command == "pay":
                run_round()
            elif cf_command == "show":
                show_balances(history)
            elif cf_command == "add":
                new_name = input("Enter new coworkers's name: ").strip()
                try:
                    new_price = input("Enter their drink price: ").strip().replace("$", "")
                    price = float(new_price)
                    add_user(users, history, new_name, price)
                    save_history(HISTORY_FILE, history)
                except ValueError:
                    print("Invalid price.")
            elif cf_command == "remove":
                name = input("Enter coworker's name to remove: ").strip()
                remove_user(users, history, name)
                save_history(HISTORY_FILE, history)
            elif cf_command == "exit":
                save_history(HISTORY_FILE, history)
                print("Bye-bye! Have a great coffee break!")
                break
            else:
                print("Unknown command. Please only use: pay, show, add, remove, exit.")
        except EOFError:
            print("\nExiting- EOF (Ctrl+D).")
            break
        except KeyboardInterrupt:
            print("\nExiting- keyboard interruption (Ctrl+C).")
            break
        except Exception as e:
            print(f"[Error] {e}")