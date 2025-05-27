# Coffee Payment Tracker

A command-line Python tool to help you and your coworkers decide who should pay for coffee, taking everyone’s drink price into account. Makes sure everyone pays their fair share over time.

## Features

- Tracks each person’s total payments and consumption.
- Always picks the fairest person to pay next (the one with the lowest net balance or at random if tied).
- Data isstored in `data/history.json` for persistence between runs.
- Add/remove users dynamically.
- Simple, intuitive CLI—no external dependencies.

## Getting Started

1. **Clone the Repository:**

    ```sh
    git clone <your-github-repo-url>
    cd HPE_COFFEETRACKER
    ```

2. **Set Up Python:**

    You’ll need Python 3.x installed on your computer.

3. **(Recommended) Create a Virtual Environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  
    # On Windows: .\venv\Scripts\activate
    ```

4. **Install Dependencies:**
    No external dependencies required.

    If you want to be strict:

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Program:**

    ```sh
    python main.py
    ```

## How It Works

1. Each coworker’s drink price is set in the code (`coffeetracker/coffee.py`).
2. At each round, the program selects the fairest payer based on payment/consumption history.
3. Data is stored in `data/history.json`, so balances persist between runs.
4. CLI options:
    - `pay`: Run a coffee round (choose and update payer).
    - `show`: Display current balances.
    - `add`: Add a new user.
    - `remove`: Remove a user.
    - `exit`: Save and quit.

## Customizing Users & Prices

- To add/remove coworkers or change prices, use the CLI or edit the users dictionary in `coffeetracker/coffee.py` (advanced).
- Users can be added by typing `add` in the CLI and following prompts for name and drink price (enter the price as a number, e.g., `4.50`).
- To remove a user, type `remove` and enter the user’s name.

## Assumptions

- Each coworker always orders the same item(s), and the cost per person is evenly split based on the total order.
- The user list and drink prices are hard-coded in `coffeetracker/coffee.py` but can be managed via the CLI.
- Drink prices are assumed to remain constant for each user unless changed in the code or by re-adding a user.
- All users participate in every round unless they are removed.
- Payment history is persisted in `data/history.json`, which is automatically created/updated as needed.
- If `history.json` is missing or corrupted, the program will warn the user and reset all balances to zero.
- Only standard Python libraries are required; no external packages needed.
- Project structure:
    ```
    HPE_COFFEETRACKER/
      coffeetracker/
        coffee.py
        storage.py
        __init__.py
      data/
        history.json
      main.py
      requirements.txt
      README.md
      ...
    ```

## FAQ

**Q: How do I reset all balances?**  
A: Delete the `data/history.json` file. It will be recreated empty next time the program runs.

**Q: What version of Python is required?**  
A: Python 3.9.6+

## Edge Case Testing

All edge cases have been tested, including:

- All zero balances (random payer)
- Tie for lowest balance (random payer among ties)
- Adding/removing users dynamically
- Empty user list (error)
- Non-numeric/negative prices (error)
- Unknown commands (friendly message)
- Corrupted/deleted history file (auto-reset)
- Price changes only affecting future rounds
- Graceful exit with Ctrl+C

## Automated Unit Testing

This project includes a suite of automated unit tests for core functions and algorithms including one functional (end-to-end) test.

- All tests are located in the `tests/` directory.
- To run the tests, use the following command from the project root:

    ```sh
    python -m unittest tests.test_coffee
    ```

### Unit Test Sample output:


```
.......
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

## Deliverables

1. **Instructions on How to Build and Run**
    - See “Getting Started” above and in this README.

2. **Assumptions**
    - See the “Assumptions” section above.

3. **How to Enter Data**
    - Default users and prices are in `coffeetracker/coffee.py`.
    - Users can be added/removed at any time using the CLI with add and remove commands.
    - Drink prices are entered as numbers (e.g., 4.50).

4. **Finished Product**
    - Provided as a ready-to-run Python project for local use with Python 3.x.
    - All features can be accessed and tested using the CLI.

## About

Created as a coding challenge to demonstrate practical Python, fairness algorithms (greedy net-balance selection), and CLI practices.