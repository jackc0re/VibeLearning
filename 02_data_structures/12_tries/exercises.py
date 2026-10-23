"""
Tries (Prefix Trees) - Exercises
================================
Implement a trie, then use it for autocomplete, prefix counting,
longest-common-prefix, and word filtering.
Run tests with:
    python exercises.py

The stubs print FAIL until you implement them - that is expected and the
file still exits cleanly. Reference solutions are at the bottom, and the
same tests run again with the solutions in place - this time they PASS.
"""

print("=" * 50)
print("TRIES (PREFIX TREES) - Exercises")
print("=" * 50)

# The building block - given. Every exercise builds on this node.
class TrieNode:
    def __init__(self):
        self.children = {}    # char -> TrieNode
        self.is_end = False   # True if a word ends at this node


# =============================================================================
# EXERCISE 1: The Trie Itself - insert, search, starts_with
# =============================================================================

class Trie:
    """A prefix tree. Implement the three methods below."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Add word to the trie: walk one character at a time, create any
        missing child, then set is_end = True on the final node."""
        # YOUR CODE HERE
        # TODO: implement (a reference solution is at the bottom of this file)
        pass

    def search(self, word):
        """True ONLY if word is stored: the path must exist AND the final
        node must have is_end = True. "ca" is not the word "cat"!"""
        # YOUR CODE HERE
        # TODO: implement (a reference solution is at the bottom of this file)
        pass

    def starts_with(self, prefix):
        """True if the prefix path exists (no is_end check)."""
        # YOUR CODE HERE
        # TODO: implement (a reference solution is at the bottom of this file)
        pass


# =============================================================================
# EXERCISE 2: autocomplete(trie, prefix)
# =============================================================================

def exercise_2_autocomplete(trie, prefix):
    """Return every stored word that starts with prefix, sorted A-Z.
    Walk to the prefix node, then gather every is_end node below it.
    Example: words cat/car/card -> autocomplete(trie, "ca") == ["car", "card", "cat"]
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 3: count_words_with_prefix(trie, prefix)
# =============================================================================

def exercise_3_count_words_with_prefix(trie, prefix):
    """Return how many stored words start with prefix (an int, no list).
    Walk to the prefix node, then count is_end flags in its subtree.
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 4: longest_common_prefix(words) - via a trie
# =============================================================================

def exercise_4_longest_common_prefix(words):
    """Return the longest prefix shared by ALL words, using a trie.
    Build the trie, then walk down from the root while the node has exactly
    one child and is not itself the end of a word.
    Example: ["flower", "flow", "flight"] -> "fl"
    Edge cases: [] -> "", ["solo"] -> "solo".
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 5: filter_real_words(trie, candidates) - a small word filter
# =============================================================================

def exercise_5_filter_real_words(trie, candidates):
    """Given a trie used as a dictionary, return the candidates that are
    real stored words, keeping their original order.
    Example: dictionary has cat/dog; candidates ["ca", "cat", "dogs", "dog"]
    -> ["cat", "dog"]
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# HELPERS
# =============================================================================

def safe(fn, *args):
    """Call fn; an unimplemented or broken stub comes back as None, not a crash."""
    try:
        return fn(*args)
    except Exception:
        return None


def build_trie(words):
    """Build a Trie from a list of words using your insert from Exercise 1."""
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie


def check(results, label, actual, expected):
    """Print one PASS/FAIL line and remember the outcome."""
    ok = actual == expected
    results.append(ok)
    status = "PASS" if ok else "FAIL"
    print(f"  {status} {label} = {actual!r} (expected {expected!r})")


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("\nRunning Tries Exercises Tests")
    print("=" * 50)
    results = []

    words = ["cat", "car", "card", "care", "dog", "do"]

    # Exercise 1
    print("\nExercise 1: insert / search / starts_with")
    trie = safe(build_trie, words)
    check(results, "search('cat')", safe(trie.search, "cat"), True)
    check(results, "search('ca')", safe(trie.search, "ca"), False)
    check(results, "search('card')", safe(trie.search, "card"), True)
    check(results, "search('cow')", safe(trie.search, "cow"), False)
    check(results, "search('')", safe(trie.search, ""), False)
    check(results, "starts_with('ca')", safe(trie.starts_with, "ca"), True)
    check(results, "starts_with('cat')", safe(trie.starts_with, "cat"), True)
    check(results, "starts_with('cow')", safe(trie.starts_with, "cow"), False)
    check(results, "starts_with('')", safe(trie.starts_with, ""), True)

    # Exercise 2
    print("\nExercise 2: autocomplete")
    check(results, "autocomplete('ca')", safe(exercise_2_autocomplete, trie, "ca"),
          ["car", "card", "care", "cat"])
    check(results, "autocomplete('car')", safe(exercise_2_autocomplete, trie, "car"),
          ["car", "card", "care"])
    check(results, "autocomplete('do')", safe(exercise_2_autocomplete, trie, "do"),
          ["do", "dog"])
    check(results, "autocomplete('z')", safe(exercise_2_autocomplete, trie, "z"), [])

    # Exercise 3
    print("\nExercise 3: count_words_with_prefix")
    check(results, "count('c')", safe(exercise_3_count_words_with_prefix, trie, "c"), 4)
    check(results, "count('car')", safe(exercise_3_count_words_with_prefix, trie, "car"), 3)
    check(results, "count('d')", safe(exercise_3_count_words_with_prefix, trie, "d"), 2)
    check(results, "count('z')", safe(exercise_3_count_words_with_prefix, trie, "z"), 0)

    # Exercise 4
    print("\nExercise 4: longest_common_prefix")
    check(results, "lcp(flower/flow/flight)",
          safe(exercise_4_longest_common_prefix, ["flower", "flow", "flight"]), "fl")
    check(results, "lcp(dog/racecar/car)",
          safe(exercise_4_longest_common_prefix, ["dog", "racecar", "car"]), "")
    check(results, "lcp(interspecies/interstellar/interstate)",
          safe(exercise_4_longest_common_prefix,
               ["interspecies", "interstellar", "interstate"]), "inters")
    check(results, "lcp([])", safe(exercise_4_longest_common_prefix, []), "")
    check(results, "lcp([solo])", safe(exercise_4_longest_common_prefix, ["solo"]), "solo")

    # Exercise 5
    print("\nExercise 5: filter_real_words")
    dictionary = safe(build_trie, ["cat", "car", "card", "dog"])
    check(results, "filter([ca, cat, dogs, dog])",
          safe(exercise_5_filter_real_words, dictionary, ["ca", "cat", "dogs", "dog"]),
          ["cat", "dog"])
    check(results, "filter([card, cart])",
          safe(exercise_5_filter_real_words, dictionary, ["card", "cart"]),
          ["card"])
    check(results, "filter([zebra])",
          safe(exercise_5_filter_real_words, dictionary, ["zebra"]),
          [])

    print("\n" + "=" * 50)
    if all(results):
        print("PASS All tests passed! Great job!")
    else:
        print("FAIL Some tests failed - expected while the stubs are empty.")
        print("     Implement the exercises, then run this file again!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

# The FAIL lines above are expected: the stubs are not implemented yet.
# The reference solutions below re-define the exercise names, and the same
# tests run again at the bottom of this file - this time they PASS.


# Solution 1: insert, search, starts_with
class Trie:
    """A prefix tree: walk letters, create children, flag word endings."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _find_node(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None


# Solution 2: autocomplete
def exercise_2_autocomplete(trie, prefix):
    """Walk to the prefix node, then collect every word in its subtree."""
    node = trie.root
    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]
    words = []
    stack = [(node, prefix)]
    while stack:
        current, path = stack.pop()
        if current.is_end:
            words.append(path)
        for ch, child in current.children.items():
            stack.append((child, path + ch))
    return sorted(words)


# Solution 3: count_words_with_prefix
def exercise_3_count_words_with_prefix(trie, prefix):
    """Walk to the prefix node, then count is_end flags in its subtree."""
    node = trie.root
    for ch in prefix:
        if ch not in node.children:
            return 0
        node = node.children[ch]
    count = 0
    stack = [node]
    while stack:
        current = stack.pop()
        if current.is_end:
            count += 1
        stack.extend(current.children.values())
    return count


# Solution 4: longest_common_prefix via a trie
def exercise_4_longest_common_prefix(words):
    """The walk continues only while every word agrees on the next letter."""
    if not words:
        return ""
    trie = build_trie(words)
    node = trie.root
    prefix_chars = []
    while len(node.children) == 1 and not node.is_end:
        ch = next(iter(node.children))
        prefix_chars.append(ch)
        node = node.children[ch]
    return "".join(prefix_chars)


# Solution 5: a small word filter
def exercise_5_filter_real_words(trie, candidates):
    """Keep the candidates that are whole words in the trie (search, is_end!)."""
    return [word for word in candidates if trie.search(word)]


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests()
