# ============================================================
# Advanced Lesson 2: Generators & Iterators
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

# --- What is an Iterator? ---
# An iterator is an object you can loop through one item at a time.
# It remembers its position between calls.

# --- Custom Iterator ---
class CountUp:
    """Counts from start to end one step at a time."""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 5)
for num in counter:
    print("Count:", num)

# --- What is a Generator? ---
# A generator is a simpler way to create an iterator using 'yield'.
# It pauses at each yield and resumes from there next time.

def count_up(start, end):
    current = start
    while current <= end:
        yield current       # pause here and return value
        current += 1

print("\n--- Generator ---")
for num in count_up(1, 5):
    print("Gen:", num)

# --- Generator is Memory Efficient ---
# Instead of creating a full list in memory, it generates one item at a time.

def large_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = large_range(1000000)
print("\nFirst 5 from large generator:")
for _ in range(5):
    print(next(gen))

# --- Generator Expression ---
squares = (x ** 2 for x in range(10))   # Like list comprehension but with ()
print("\nSquares:")
for sq in squares:
    print(sq, end=" ")
print()

# --- Practical Example: Read large file line by line ---
def read_large_file(filepath):
    """Yields one line at a time — memory efficient for big files."""
    try:
        with open(filepath, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("File not found.")

# --- Chaining Generators ---
def integers(start=1):
    n = start
    while True:
        yield n
        n += 1

def take(n, iterable):
    for i, val in enumerate(iterable):
        if i >= n:
            break
        yield val

def only_even(iterable):
    for val in iterable:
        if val % 2 == 0:
            yield val

print("\nFirst 5 even integers:")
pipeline = take(5, only_even(integers()))
for val in pipeline:
    print(val, end=" ")
print()

# ============================================================
# Practice Exercise:
# 1. Write a generator that yields Fibonacci numbers infinitely
# 2. Write a generator that reads a CSV file row by row
# 3. Write a custom iterator class for a deck of cards
# ============================================================
