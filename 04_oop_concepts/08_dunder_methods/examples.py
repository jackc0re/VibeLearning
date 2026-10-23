"""
Dunder Methods and the Data Model - Examples
============================================
One Playlist class, built one dunder at a time. Each section re-defines the
class with one more dunder, so you can watch it grow:

    __repr__ / __str__ -> __eq__ / __hash__ -> __len__ -> __getitem__
    -> __contains__ -> __iter__ -> __call__ -> __add__

Songs are (title, artist) tuples, e.g. ("Imagine", "John Lennon").
"""

import random

print("=" * 60)
print("DUNDER METHODS AND THE DATA MODEL - Examples")
print("=" * 60)

# =============================================================================
# 1. WHAT DUNDERS ARE: PYTHON CALLS THEM FOR YOU
# =============================================================================
print("\n--- 1. Python calls dunders for you ---\n")

# You have been triggering dunders all along -- through friendly syntax.
# The dunder is the wiring behind the wall; you just flip the switch:
print(f"len('hi')             -> {len('hi')}")
print(f"'hi'.__len__()        -> {'hi'.__len__()}")
print(f"repr([1, 2])          -> {repr([1, 2])}")
print(f"[1, 2].__repr__()     -> {[1, 2].__repr__()}")
print(f"repr(x) == x.__repr__()? {repr('hi') == 'hi'.__repr__()}")


# Our class starts with data only: a name and a list of (title, artist) songs.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name


playlist = Playlist(
    [("Bohemian Rhapsody", "Queen"), ("Imagine", "John Lennon")],
    name="Favorites",
)

# With no dunders at all, this is everything Python can say about our object:
print("\nprint(playlist) with zero dunders:")
print(playlist)  # <__main__.Playlist object at 0x...>  -- useless!
print("That default repr is the problem the next section fixes.")


# =============================================================================
# 2. __repr__ VS __str__
# =============================================================================
print("\n--- 2. __repr__ vs __str__ ---\n")

# Playlist grows: repr for debugging, str for humans.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        # For DEVELOPERS: unambiguous, looks like the code that built it.
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        # For USERS: readable. print() and str() pick this one.
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)


playlist = Playlist(
    [("Bohemian Rhapsody", "Queen"), ("Imagine", "John Lennon")],
    name="Favorites",
)

print("print(playlist)  -> uses __str__:")
print(playlist)
print(f"\nrepr(playlist)   -> uses __repr__: {repr(playlist)}")

# Inside a container, Python shows each item with __repr__:
print(f"\n[playlist] shows reprs: {[playlist]}")


# =============================================================================
# 3. __eq__ AND THE __hash__ CONTRACT
# =============================================================================
print("\n--- 3. __eq__ and the __hash__ contract ---\n")

# Act 1: define __eq__ (compare by content, not identity) ... and nothing else.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented  # let Python decide (e.g. playlist == 42)
        return self.songs == other.songs


favorites = Playlist([("Bohemian Rhapsody", "Queen")], name="Favorites")
copy_of_favorites = Playlist([("Bohemian Rhapsody", "Queen")], name="Favorites")
other = Playlist([("Imagine", "John Lennon")], name="Other")

print(f"favorites == copy_of_favorites -> {favorites == copy_of_favorites}")
print(f"favorites == other             -> {favorites == other}")
print(f"favorites == 42                -> {favorites == 42}")

# Defining __eq__ set __hash__ to None: our objects are now UNHASHABLE.
print("\nTrying to use a playlist as a dict key:")
try:
    {favorites: "evening run"}
except TypeError as exc:
    print(f"  PASS: caught the expected TypeError: {exc}")

# Act 2: the fix -- define __hash__ too, and keep it consistent with __eq__.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    def __hash__(self):
        # The contract: equal objects must have equal hashes.
        return hash(tuple(self.songs))


favorites = Playlist([("Bohemian Rhapsody", "Queen")], name="Favorites")
copy_of_favorites = Playlist([("Bohemian Rhapsody", "Queen")], name="Favorites")

print(f"\nhash(a) == hash(b) for equal playlists -> "
      f"{hash(favorites) == hash(copy_of_favorites)}")
night_runs = {favorites: "evening", copy_of_favorites: "morning"}
print(f"dict with both equal playlists has {len(night_runs)} key(s)")
print(f"lookup by the copy -> {night_runs[copy_of_favorites]}")


# =============================================================================
# 4. __len__
# =============================================================================
print("\n--- 4. __len__ ---\n")

# Playlist grows: __len__ (the song count). Must return an int --
# return "3" or 3.0 and len() raises TypeError when Python checks it.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    def __hash__(self):
        return hash(tuple(self.songs))

    def __len__(self):
        return len(self.songs)


playlist = Playlist(
    [("Bohemian Rhapsody", "Queen"), ("Imagine", "John Lennon")],
    name="Favorites",
)
empty = Playlist(name="Empty")

print(f"len(playlist)         -> {len(playlist)}")
print(f"bool(empty playlist)  -> {bool(empty)}   (empty containers are falsy)")
print(f"bool(playlist)        -> {bool(playlist)}")


# =============================================================================
# 5. __getitem__ (AND ITERATION FOR FREE)
# =============================================================================
print("\n--- 5. __getitem__ (and iteration for free) ---\n")

# Playlist grows: __getitem__ -> playlist[0], playlist[-1], playlist[1:3].
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    def __hash__(self):
        return hash(tuple(self.songs))

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        if isinstance(index, slice):
            # playlist[1:3] hands back a NEW Playlist
            return Playlist(self.songs[index], name=self.name)
        return self.songs[index]


playlist = Playlist(
    [("Bohemian Rhapsody", "Queen"), ("Imagine", "John Lennon")],
    name="Favorites",
)

print(f"playlist[0]   -> {playlist[0]}")
print(f"playlist[-1]  -> {playlist[-1]}")
print(f"playlist[1:]  -> {repr(playlist[1:])}   (a new Playlist)")

# The aha moment: with indexing in place, iteration ALREADY works --
# Python falls back to playlist[0], playlist[1], ... until IndexError.
print("\nfor song in playlist  (no __iter__ defined yet!):")
for song in playlist:
    print(f"   {song}")


# =============================================================================
# 6. __contains__
# =============================================================================
print("\n--- 6. __contains__ ---\n")

# Playlist grows: __contains__ -> the 'in' operator.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    def __hash__(self):
        return hash(tuple(self.songs))

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Playlist(self.songs[index], name=self.name)
        return self.songs[index]

    def __contains__(self, item):
        # Accept a full ("Title", "Artist") tuple OR just a title string.
        for title, artist in self.songs:
            if item == title or item == (title, artist):
                return True
        return False


playlist = Playlist(
    [("Bohemian Rhapsody", "Queen"), ("Imagine", "John Lennon")],
    name="Favorites",
)

print(f"'Imagine' in playlist                    -> {'Imagine' in playlist}")
print(f"('Imagine', 'John Lennon') in playlist   -> "
      f"{('Imagine', 'John Lennon') in playlist}")
print(f"'Stairway to Heaven' in playlist         -> "
      f"{'Stairway to Heaven' in playlist}")


# =============================================================================
# 7. __iter__: THE MODERN WAY
# =============================================================================
print("\n--- 7. __iter__ (the modern way) ---\n")

# Playlist grows: __iter__ as an explicit generator method (it uses yield).
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    def __hash__(self):
        return hash(tuple(self.songs))

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Playlist(self.songs[index], name=self.name)
        return self.songs[index]

    def __contains__(self, item):
        for title, artist in self.songs:
            if item == title or item == (title, artist):
                return True
        return False

    def __iter__(self):
        for song in self.songs:
            yield song


playlist = Playlist(
    [("Bohemian Rhapsody", "Queen"), ("Imagine", "John Lennon")],
    name="Favorites",
)

print("for title, artist in playlist   (unpacking works too):")
for title, artist in playlist:
    print(f"   {title} by {artist}")

# One __iter__ unlocks every iteration context:
print(f"\nlist(playlist)              -> {list(playlist)}")
print(f"[t.upper() for t, _ in ...] -> "
      f"{[title.upper() for title, _ in playlist]}")
print(f"first song via next(iter(...)) -> {next(iter(playlist))}")


# =============================================================================
# 8. __call__: AN OBJECT YOU CALL LIKE A FUNCTION
# =============================================================================
print("\n--- 8. __call__ ---\n")

# A DJ object: configured ONCE (playlist, intro length), then just called.
class ShuffleIntroDJ:
    def __init__(self, playlist, intro_count=2, seed=42):
        self.playlist = playlist
        self.intro_count = intro_count
        self.rng = random.Random(seed)  # seeded -> the demo is reproducible

    def __call__(self):
        # list(self.playlist) works because Playlist defines __iter__.
        picks = self.rng.sample(list(self.playlist), self.intro_count)
        return Playlist(picks, name="Shuffle intro")


big_playlist = Playlist(
    [
        ("Bohemian Rhapsody", "Queen"),
        ("Imagine", "John Lennon"),
        ("Superstition", "Stevie Wonder"),
        ("Hotel California", "Eagles"),
        ("Dreams", "Fleetwood Mac"),
    ],
    name="Party Mix",
)

dj = ShuffleIntroDJ(big_playlist, intro_count=2)
intro = dj()  # calling the OBJECT triggers __call__
print("dj() returned:")
print(intro)  # __str__ does the pretty printing
print(f"\nrepr(intro) -> {repr(intro)}")
print(f"calling dj() again -> {repr(dj())}   (a fresh shuffle)")


# =============================================================================
# 9. __add__ (AND A WORD ON __radd__)
# =============================================================================
print("\n--- 9. __add__ ---\n")

# Playlist, final form: everything from before, plus __add__.
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []
        self.name = name

    def __repr__(self):
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    def __hash__(self):
        return hash(tuple(self.songs))

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Playlist(self.songs[index], name=self.name)
        return self.songs[index]

    def __contains__(self, item):
        for title, artist in self.songs:
            if item == title or item == (title, artist):
                return True
        return False

    def __iter__(self):
        for song in self.songs:
            yield song

    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented  # let Python try the other operand
        # '+' returns a NEW playlist -- it never mutates either side.
        return Playlist(
            self.songs + other.songs,
            name=f"{self.name} + {other.name}",
        )


favorites = Playlist([("Bohemian Rhapsody", "Queen")], name="Favorites")
workout = Playlist(
    [("Superstition", "Stevie Wonder"), ("Dreams", "Fleetwood Mac")],
    name="Workout",
)

party = favorites + workout  # one dunder, natural syntax
print("party = favorites + workout:")
print(party)
print(f"\nrepr(party) -> {repr(party)}")
print(f"originals untouched: len(favorites)={len(favorites)}, "
      f"len(workout)={len(workout)}")

# About __radd__ (in prose, no code needed): if Python cannot use the LEFT
# operand's __add__ (it is missing, or it returned NotImplemented), Python
# tries the RIGHT operand's __radd__ instead. That is how `3 + my_object`
# can work even though ints know nothing about your class.

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
