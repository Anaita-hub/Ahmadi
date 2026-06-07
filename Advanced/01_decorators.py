# ============================================================
# Advanced Lesson 3: Context Managers
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

from contextlib import contextmanager
import time

# --- What is a Context Manager? ---
# A context manager controls setup and cleanup of resources.
# The 'with' statement uses context managers automatically.

# --- Built-in Example: File Handling ---
# Bad way (manual close — risky if error happens):
# f = open("test.txt", "w")
# f.write("Hello")
# f.close()

# Good way (with handles close automatically):
with open("test.txt", "w") as f:
    f.write("Hello from context manager!\n")
    f.write("File closes automatically.\n")

with open("test.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# --- Custom Context Manager using a Class ---
class Timer:
    """Measures how long a block of code takes."""
    def __enter__(self):
        self.start = time.time()
        print("Timer started...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Timer stopped. Elapsed: {self.end - self.start:.4f} seconds")
        return False  # Don't suppress exceptions

with Timer() as t:
    total = sum(range(500000))
    print("Sum calculated:", total)

# --- Custom Context Manager using @contextmanager ---
@contextmanager
def managed_resource(name):
    print(f"[OPEN] Resource '{name}' acquired")
    try:
        yield name    # everything between 'with' runs here
    finally:
        print(f"[CLOSE] Resource '{name}' released")

with managed_resource("Database Connection") as res:
    print(f"Using resource: {res}")

# --- Database Simulation with Context Manager ---
class FakeDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from {self.db_name}...")
        self.connected = False
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False

    def query(self, sql):
        if self.connected:
            print(f"Running query: {sql}")
        else:
            raise RuntimeError("Not connected!")

with FakeDatabase("students_db") as db:
    db.query("SELECT * FROM students")
    db.query("SELECT * FROM courses")

# ============================================================
# Practice Exercise:
# 1. Write a context manager that creates a temp file,
#    lets you write to it, then deletes it on exit
# 2. Write a context manager that catches and logs exceptions
# 3. Use @contextmanager to simulate opening/closing a network socket
# ============================================================
