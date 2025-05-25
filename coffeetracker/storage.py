import json
import os

def load_history(filename, users):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[Warning] {filename} is not valid JSON. Re-initializing history.")
        except Exception as e:
            print(f"[Warning] Could not read {filename}: {e}. Re-initializing history.")
    return {name: {"paid": 0.0, "consumed": 0.0} for name in users}

def save_history(filename, history):
    try:
        with open(filename, 'w') as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"[Error] Could not save to {filename}: {e}")