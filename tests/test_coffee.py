import unittest
from coffeetracker.coffee import (
    users, validate_users, get_total_cost, get_fairest_payer, update_balances, add_user
)

class TestCoffeePaymentTracker(unittest.TestCase):

    # --- Unit Tests ---
    def setUp(self):
        self.users = users.copy()
        self.history = {name: {"paid": 0.0, "consumed": 0.0} for name in self.users}

    def test_validate_users_valid(self):
        validate_users(self.users)

    def test_validate_users_empty(self):
        with self.assertRaises(ValueError):
            validate_users({})

    def test_validate_users_negative(self):
        bad = self.users.copy()
        bad["Fake"] = -10
        with self.assertRaises(ValueError):
            validate_users(bad)

    def test_validate_users_non_numeric(self):
        bad = self.users.copy()
        bad["Fake"] = "Latte"
        with self.assertRaises(ValueError):
            validate_users(bad)

    def test_get_total_cost(self):
        total = get_total_cost(self.users)
        self.assertAlmostEqual(total, sum(self.users.values()))

    def test_fairest_payer_zero_balances(self):
        payer = get_fairest_payer(self.users, self.history)
        self.assertIn(payer, self.users)

    def test_update_balances(self):
        payer = list(self.users.keys())[0]
        update_balances(self.users, self.history, payer)
        self.assertAlmostEqual(self.history[payer]['paid'], sum(self.users.values()))
        for person, price in self.users.items():
            self.assertAlmostEqual(self.history[person]['consumed'], price)

    def test_add_user(self):
        new_name = "Oscar"
        price = 4.80
        add_user(self.users, self.history, new_name, price)
        self.assertIn(new_name, self.users)
        self.assertEqual(self.users[new_name], price)
        self.assertIn(new_name, self.history)
        self.assertEqual(self.history[new_name], {"paid": 0.0, "consumed": 0.0})

    # --- Functional Test---
    def test_full_round_flow(self):
        payers = []
        for _ in range(3):
            payer = get_fairest_payer(self.users, self.history)
            payers.append(payer)
            update_balances(self.users, self.history, payer)
        self.assertGreaterEqual(len(set(payers)), 1)
        for payer in set(payers):
            self.assertGreater(self.history[payer]['paid'], 0)
        for user, price in self.users.items():
            self.assertAlmostEqual(self.history[user]['consumed'], price * 3)

if __name__ == "__main__":
    unittest.main()