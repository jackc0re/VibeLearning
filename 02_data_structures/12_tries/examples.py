"""
Tries (Prefix Trees) - Examples
===============================
Build a trie one word at a time (with printed structure), then ask it
prefix questions: search vs starts_with, autocomplete, and counting
words under a prefix.
"""

print("=" * 50)
print("TRIES (PREFIX TREES) - Examples")
print("=" * 50)

# =============================================================================
# TRIE NODE AND TRIE
# =============================================================================
print("\n--- The TrieNode: one letter per level ---\n")

class TrieNode:
    def __init__(self):
        self.children = {}    # char -> TrieNode
        self.is_end = False   # True if a word ends at this node

class Trie:
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
        # Walk s from the root; None if the path breaks (letter not stored).
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

    def autocomplete(self, prefix):
        node = self._find_node(prefix)
        if node is None:
            return []
        words = []
        self._collect(node, prefix, words)
        return words

    def _collect(self, node, path, words):
        if node.is_end:
            words.append(path)
        for ch in sorted(node.children):   # sorted -> words come out A-Z
            self._collect(node.children[ch], path + ch, words)

    def count_words_with_prefix(self, prefix):
        node = self._find_node(prefix)
        if node is None:
            return 0
        count = 0
        stack = [node]
        while stack:
            current = stack.pop()
            if current.is_end:
                count += 1
            stack.extend(current.children.values())
        return count

    def print_structure(self):
        print("(root)")
        self._print_node(self.root, "")

    def _print_node(self, node, indent):
        for ch in sorted(node.children):
            child = node.children[ch]
            marker = " *" if child.is_end else ""
            print(f"{indent}+-- {ch}{marker}")
            self._print_node(child, indent + "|   ")

# =============================================================================
# BUILD A TRIE, ONE WORD AT A TIME
# =============================================================================
print("\n--- Building a trie, one word at a time ---\n")

trie = Trie()
for word in ["cat", "car", "do"]:
    print(f"insert('{word}'):")
    trie.insert(word)
    trie.print_structure()
    print()

# Now add the rest - notice how 'card' reuses the c -> a -> r branch.
for word in ["card", "care", "dog", "door"]:
    trie.insert(word)

print("Final trie after inserting:")
print("['cat', 'car', 'do', 'card', 'care', 'dog', 'door']")
trie.print_structure()

# =============================================================================
# SEARCH VS STARTS_WITH
# =============================================================================
print("\n--- search vs starts_with: one is_end check apart ---\n")

checks = [
    ("search('cat')", trie.search("cat"), True),
    ("search('ca')", trie.search("ca"), False),
    ("search('card')", trie.search("card"), True),
    ("search('cow')", trie.search("cow"), False),
    ("starts_with('ca')", trie.starts_with("ca"), True),
    ("starts_with('cat')", trie.starts_with("cat"), True),
    ("starts_with('cow')", trie.starts_with("cow"), False),
]
for label, actual, expected in checks:
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status} {label} -> {actual} (expected {expected})")

# =============================================================================
# AUTOCOMPLETE
# =============================================================================
print("\n--- Autocomplete: suggestions shrink as you type ---\n")

for prefix in ["c", "ca", "car", "do", "z"]:
    matches = trie.autocomplete(prefix)
    print(f"autocomplete('{prefix}') -> {matches}")

# =============================================================================
# COUNT WORDS WITH A PREFIX
# =============================================================================
print("\n--- Counting words under a prefix ---\n")

for prefix in ["c", "ca", "car", "d", "z"]:
    count = trie.count_words_with_prefix(prefix)
    print(f"count_words_with_prefix('{prefix}') -> {count}")

# =============================================================================
# TRIE VS SET
# =============================================================================
print("\n--- Trie vs set: same answer, very different walks ---\n")

word_set = {"cat", "car", "card", "care", "dog", "do", "door"}
prefix = "ca"

set_hits = sorted(w for w in word_set if w.startswith(prefix))  # visits all 7
trie_hits = trie.autocomplete(prefix)                            # walks 2 letters

print(f"set scan:  starts_with('{prefix}') -> {set_hits}")
print(f"trie walk: autocomplete('{prefix}') -> {trie_hits}")
print("The set had to look at every one of its 7 words;")
print("the trie followed just 2 letters and read one subtree.")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
