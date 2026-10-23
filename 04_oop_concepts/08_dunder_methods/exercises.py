"""
Bookshelf Dunder Methods - Exercises
====================================
Build ONE Bookshelf class by adding dunders step by step -- the same journey
the Playlist took in examples.py. Each book is a (title, author) tuple.

Run this file with:
    python exercises.py

The stubs at the top print FAIL -- that is expected! Reference solutions live
at the bottom of this file, and the same tests run again against them.
"""

print("=" * 60)
print("BOOKSHELF DUNDER METHODS - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: __repr__ and __str__
# =============================================================================
# Give the shelf two faces:
# 1. __repr__ returns EXACTLY this debug form (note the quotes around the
#    name -- use an f-string with !r):
#        Bookshelf(name='Sci-Fi Shelf', books=3)
# 2. __str__ returns a readable listing:
#        Sci-Fi Shelf (3 books)
#          1. Dune - Frank Herbert
#          2. 1984 - George Orwell
#          3. Fahrenheit 451 - Ray Bradbury
#    (two leading spaces before each numbered line)

# =============================================================================
# EXERCISE 2: __eq__ and __hash__
# =============================================================================
# 1. __eq__: two shelves are equal when their book lists are equal.
#    If other is not a Bookshelf, return NotImplemented.
# 2. __hash__: hash the books as a tuple: hash(tuple(self.books)).
#    Define BOTH -- defining __eq__ alone makes instances unhashable!

# =============================================================================
# EXERCISE 3: __len__ and __contains__
# =============================================================================
# 1. __len__: the number of books (must return an int).
# 2. __contains__: support "Dune" in shelf (title) AND
#    ("Dune", "Frank Herbert") in shelf (full tuple).

# =============================================================================
# EXERCISE 4: __getitem__
# =============================================================================
# 1. shelf[0] returns the first book, shelf[-1] the last.
# 2. shelf[1:3] (a slice) returns a NEW Bookshelf with the same name.
# 3. Bonus aha: with __getitem__ alone, `for book in shelf:` already works
#    (Python indexes 0, 1, 2, ... until IndexError). The tests check it!

# =============================================================================
# EXERCISE 5: __iter__ and __add__
# =============================================================================
# 1. __iter__: a generator method -- loop over the books and `yield` each one
#    (the modern way; do not rely on the __getitem__ fallback).
# 2. __add__: shelf_a + shelf_b returns a NEW Bookshelf holding both book
#    lists, named f"{self.name} + {other.name}". Never mutate either operand.
#    If other is not a Bookshelf, return NotImplemented.

# =============================================================================
# THE CLASS TO BUILD
# =============================================================================

class Bookshelf:
    """A shelf of books; each book is a (title, author) tuple."""

    def __init__(self, books=None, name="Reading list"):
        self.books = list(books) if books else []  # provided -- do not change
        self.name = name

    # --- Exercise 1 ---
    def __repr__(self):
        # TODO: return "Bookshelf(name=..., books=N)" using {self.name!r}.
        pass  # YOUR CODE HERE

    def __str__(self):
        # TODO: "Name (N books)" then "  1. Title - Author" per book.
        pass  # YOUR CODE HERE

    # --- Exercise 2 ---
    def __eq__(self, other):
        # TODO: compare self.books == other.books; NotImplemented otherwise.
        pass  # YOUR CODE HERE

    def __hash__(self):
        # TODO: return hash(tuple(self.books)).
        pass  # YOUR CODE HERE

    # --- Exercise 3 ---
    def __len__(self):
        # TODO: return the number of books (an int).
        pass  # YOUR CODE HERE

    def __contains__(self, item):
        # TODO: True if item matches a book title or a full (title, author).
        pass  # YOUR CODE HERE

    # --- Exercise 4 ---
    def __getitem__(self, index):
        # TODO: slices return a NEW Bookshelf; plain indexes return the book.
        pass  # YOUR CODE HERE

    # --- Exercise 5 ---
    def __iter__(self):
        # TODO: yield each book (a generator method).
        pass  # YOUR CODE HERE

    def __add__(self, other):
        # TODO: return a NEW Bookshelf named "A + B"; NotImplemented otherwise.
        pass  # YOUR CODE HERE


# =============================================================================
# TESTS
# =============================================================================
# You can read these to see exactly what each exercise must do.
# Every check is failure-safe, so the stub run prints FAIL (not crashes).

def run_tests(bookshelf_cls, label):
    """Run every exercise check against bookshelf_cls; print PASS/FAIL."""
    print("\n" + "=" * 60)
    print(f"SELF-TESTS: {label}")
    print("=" * 60)

    failures = 0

    def check(description, fn):
        nonlocal failures
        try:
            ok = bool(fn())
            detail = ""
        except Exception as exc:
            ok = False
            detail = f" (raised {type(exc).__name__}: {exc})"
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(f"  [{status}] {description}{detail}")

    sci_fi_books = [
        ("Dune", "Frank Herbert"),
        ("1984", "George Orwell"),
        ("Fahrenheit 451", "Ray Bradbury"),
    ]
    poetry_books = [("Leaves of Grass", "Walt Whitman")]

    sci_fi = bookshelf_cls(sci_fi_books, name="Sci-Fi Shelf")
    same_books = bookshelf_cls(sci_fi_books, name="Sci-Fi Shelf")
    poetry = bookshelf_cls(poetry_books, name="Poetry")

    # Exercise 1: __repr__ and __str__
    print("\nExercise 1: __repr__ and __str__")
    check("repr(sci_fi) matches the spec form",
          lambda: repr(sci_fi) == "Bookshelf(name='Sci-Fi Shelf', books=3)")
    check("str(sci_fi) starts with 'Sci-Fi Shelf (3 books)'",
          lambda: str(sci_fi).startswith("Sci-Fi Shelf (3 books)"))
    check("str(sci_fi) lists '  1. Dune - Frank Herbert'",
          lambda: "  1. Dune - Frank Herbert" in str(sci_fi))

    # Exercise 2: __eq__ and __hash__
    print("\nExercise 2: __eq__ and __hash__")
    check("equal book lists -> sci_fi == same_books",
          lambda: sci_fi == same_books)
    check("different books -> sci_fi != poetry",
          lambda: sci_fi != poetry)
    check("sci_fi == 42 is False (NotImplemented path)",
          lambda: (sci_fi == 42) is False)
    check("hashes of equal shelves match",
          lambda: hash(sci_fi) == hash(same_books))
    check("equal shelves collapse to one dict key",
          lambda: len({sci_fi: 1, same_books: 2}) == 1)

    # Exercise 3: __len__ and __contains__
    print("\nExercise 3: __len__ and __contains__")
    check("len(sci_fi) == 3", lambda: len(sci_fi) == 3)
    check("'Dune' in sci_fi (by title)", lambda: "Dune" in sci_fi)
    check("('Dune', 'Frank Herbert') in sci_fi (full tuple)",
          lambda: ("Dune", "Frank Herbert") in sci_fi)
    check("'Hobbit' not in sci_fi", lambda: "Hobbit" not in sci_fi)

    # Exercise 4: __getitem__
    print("\nExercise 4: __getitem__")
    check("sci_fi[0] == ('Dune', 'Frank Herbert')",
          lambda: sci_fi[0] == ("Dune", "Frank Herbert"))
    check("sci_fi[-1] == ('Fahrenheit 451', 'Ray Bradbury')",
          lambda: sci_fi[-1] == ("Fahrenheit 451", "Ray Bradbury"))
    check("sci_fi[1:] is a Bookshelf with 2 books",
          lambda: isinstance(sci_fi[1:], bookshelf_cls)
          and len(sci_fi[1:]) == 2)
    check("for book in sci_fi works (free iteration)",
          lambda: [t for t, a in sci_fi]
          == ["Dune", "1984", "Fahrenheit 451"])

    # Exercise 5: __iter__ and __add__
    print("\nExercise 5: __iter__ and __add__")
    check("list(sci_fi) yields the book tuples",
          lambda: list(sci_fi) == sci_fi_books)
    check("sci_fi + poetry is a Bookshelf",
          lambda: isinstance(sci_fi + poetry, bookshelf_cls))
    check("the combined shelf has 4 books",
          lambda: len(sci_fi + poetry) == 4)
    check("combined name is 'Sci-Fi Shelf + Poetry'",
          lambda: (sci_fi + poetry).name == "Sci-Fi Shelf + Poetry")
    check("operands unchanged ('+' never mutates)",
          lambda: len(sci_fi) == 3 and len(poetry) == 1)

    print("\n" + "=" * 60)
    if failures == 0:
        print(" All checks passed! Great job!")
    else:
        print(f"FAIL {failures} check(s) did not pass. Keep practicing!")
    print("=" * 60)
    return failures


if __name__ == "__main__":
    run_tests(Bookshelf, "stub Bookshelf (FAILs expected -- solve the TODOs!)")

# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================
# The FAIL lines above are expected: the stubs are not implemented yet.
# The reference class below re-defines Bookshelf, and the same tests run
# again at the bottom of the file -- this time they PASS.

class Bookshelf:
    """Reference solution: a Bookshelf with the useful dunders."""

    def __init__(self, books=None, name="Reading list"):
        self.books = list(books) if books else []
        self.name = name

    # Exercise 1
    def __repr__(self):
        return f"Bookshelf(name={self.name!r}, books={len(self.books)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.books)} books)"]
        for i, (title, author) in enumerate(self.books, 1):
            lines.append(f"  {i}. {title} - {author}")
        return "\n".join(lines)

    # Exercise 2
    def __eq__(self, other):
        if not isinstance(other, Bookshelf):
            return NotImplemented
        return self.books == other.books

    def __hash__(self):
        return hash(tuple(self.books))

    # Exercise 3
    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        for title, author in self.books:
            if item == title or item == (title, author):
                return True
        return False

    # Exercise 4
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Bookshelf(self.books[index], name=self.name)
        return self.books[index]

    # Exercise 5
    def __iter__(self):
        for book in self.books:
            yield book

    def __add__(self, other):
        if not isinstance(other, Bookshelf):
            return NotImplemented
        return Bookshelf(
            self.books + other.books,
            name=f"{self.name} + {other.name}",
        )


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests(Bookshelf, "reference Bookshelf (solutions)")
