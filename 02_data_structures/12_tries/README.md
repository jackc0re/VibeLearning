# 🌲 Tries (Prefix Trees)

A tree-shaped data structure that stores strings **one character per level**, so
every path down from the root spells a prefix. Its superpower: answering
*"does anything start with...?"* costs one step per letter — no matter how many
words are stored.

---

## The Prefix Problem

Autocomplete, spellcheck, "does any word start with FR?" — none of these are
exact lookups. Sets and dicts (see [Sets](../04_sets/README.md) and
[Dictionaries](../03_dictionaries_maps/README.md)) are brilliant at
"is this **exact** word stored?" but hopeless at prefixes, because a prefix
question forces you to visit every word:

```python
words = {"cat", "car", "card", "dog"}

"car" in words                            # True  - exact match, instant
any(w.startswith("ca") for w in words)    # True  - but it checked ALL 4 words
```

With 100,000 words that `any(...)` reads all 100,000 of them to answer a
2-letter question. A trie answers by spelling the prefix — 2 steps.

---

## The Phone Book Analogy

To find "Rivera" in a phone book you never read page one. You open the **R**
section, then the **I** tab inside it, then **V**... Each letter you know lets
you skip everything that doesn't match. A trie is that filing system turned
into a data structure: the root holds the empty prefix, and every edge you
follow adds one letter.

> 💡 **First time seeing `class`?** Start with the [10-line primer in Stacks and Queues](../06_stacks_queues/README.md#stack-class-implementation) - a class is a blueprint, `__init__` sets it up, `self` is the instance. Full treatment in [Module 04](../../04_oop_concepts/01_classes_and_objects/README.md).

---

## What a Trie Looks Like

Here is a trie holding `cat`, `car`, `card`, and `do`. A `*` marks a node where
a word **ends** (`is_end = True`):

```
(root)
├── c
│   └── a
│       ├── t *        <- "cat"
│       └── r *        <- "car"
│           └── d *    <- "card"
└── d
    └── o *            <- "do"
```

Read any path from the root and you spell a prefix. Paths that finish on a `*`
spell stored words. Notice how `cat`, `car`, and `card` **share** their
`c -> a` branch — shared prefixes are stored once, not once per word.

---

## TrieNode: One Letter Per Level

Each node is tiny: a dict of children plus an end-of-word flag. The whole trie
is just a tree of these (trees refresher: [Trees](../08_trees/README.md)).

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char -> TrieNode
        self.is_end = False   # True if a word ends at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
```

---

## insert: Grow the Tree

Walk the word one character at a time, creating a child whenever the next
letter is missing, then flag the last node:

```python
def insert(self, word):
    node = self.root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.is_end = True
```

Inserting `card` after `car` creates just **one** new node — the `d` — because
`c -> a -> r` already exists.

---

## search vs starts_with

These two differ by exactly **one check**: whether the final node is flagged as
a word ending.

```python
def _find_node(self, s):
    """Walk s from the root; return the final node, or None if the path breaks."""
    node = self.root
    for ch in s:
        if ch not in node.children:
            return None
        node = node.children[ch]
    return node

def search(self, word):
    node = self._find_node(word)
    return node is not None and node.is_end    # must be a WHOLE word

def starts_with(self, prefix):
    return self._find_node(prefix) is not None # any stored word may continue it
```

```python
trie.insert("cat")

trie.search("cat")       # True  - "cat" is a stored word
trie.search("ca")        # False - the path exists, but no word ends there!
trie.starts_with("ca")   # True  - "cat" starts with "ca"
```

---

## autocomplete: Collect Everything Below

Walk down to the prefix's node, then gather every `*` in the whole subtree,
attaching the letters you passed on the way:

```python
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
    for ch in sorted(node.children):          # sorted -> words come out A-Z
        self._collect(node.children[ch], path + ch, words)
```

```python
trie.autocomplete("ca")   # ['car', 'card', 'care', 'cat']
trie.autocomplete("car")  # ['car', 'card']
trie.autocomplete("x")    # []
```

---

## count_words_with_prefix

Same walk, then count the `*` flags instead of collecting them:

```python
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
```

(You could also just call `len(self.autocomplete(prefix))` — the stack version
skips building the word list when you only need the number.)

---

## When a Trie Beats a Set (and When It Doesn't)

**Reach for a trie when:**
- You answer **prefix questions** ("everything starting with...") - a set must
  scan every word; the trie walks the prefix once.
- You need **sorted output** - a depth-first walk over sorted children yields
  words in A-Z order for free.
- Many words **share prefixes** (`card`, `care`, `careful`) - the shared part
  is stored once, so memory drops.

**Stick with a set when:**
- You only do **exact lookups** - a set is simpler, uses less code, and hashes
  the whole word in one step.
- Words share almost **no prefixes** - a trie pays roughly one node (one dict,
  one flag) per character, which costs more than storing the strings outright.

| Question | Set | Trie |
|----------|-----|------|
| Is `word` stored? | O(L) - ideal | O(L) |
| Does anything start with `P`? | O(N·L) - scan all | O(L) |
| All words starting with `P` | O(N·L) - scan all | O(L + matches) |
| Words in sorted order | O(N log N) - sort | free during the walk |
| Memory, no shared prefixes | compact | ~one node per character |

---

## Complexity

Every operation — `insert`, `search`, `starts_with` — is **O(L)**, where L is
the length of the word or prefix. Crucially, that bound has **nothing to do
with how many words are stored**: a trie with a million words answers
`starts_with("fr")` in the same 2 steps as a trie with 3 words. Autocomplete is
O(L + M), where M is the total size of the words it reports.

---

## Real Uses

- **Autocomplete** - search bars suggest completions by walking the prefix.
- **Spellcheckers** - `search` says "real word", `starts_with` says "still
  plausible, keep typing".
- **IP routing** - routers pick the *longest prefix match* by walking the
  address bit by bit.
- **T9 keyboards** - old phone texting walked digit prefixes to suggest words.

---

## Common Mistakes

### 1. Treating a prefix match as a word match
```python
def search(self, word):
    return self._find_node(word) is not None   # ❌ too permissive

trie.insert("cat")
trie.search("ca")      # ❌ True - "ca" is only a PREFIX, not a stored word

# ✅ The final node must also be flagged as an ending
return node is not None and node.is_end
```
This is the single most common trie bug: `starts_with` and `search` look
almost identical, but only `search` checks `is_end`.

### 2. Mutating a dict while walking it
```python
# "prune" every child that is not a word ending
for ch in node.children:
    if not node.children[ch].is_end:
        del node.children[ch]      # ❌ RuntimeError: dictionary changed size
```
Python forbids adding/removing entries while a `for` loop iterates that same
dict. Build the list of keys first, or iterate over a copy:

```python
for ch in list(node.children):     # ✅ iterate over a snapshot
    if not node.children[ch].is_end:
        del node.children[ch]
```

### 3. Walking into a child that does not exist
```python
def search(self, word):
    node = self.root
    for ch in word:
        node = node.children[ch]   # ❌ KeyError on the first wrong letter
```
There is no node for a word the trie never heard of — the guard **is** the
base case:

```python
if ch not in node.children:
    return False                   # ✅ path broke, word cannot be stored
node = node.children[ch]
```
Recursive helpers need the same base case: `_collect(None, ...)` must return
immediately, or a missing branch crashes the whole walk.

---

## Quick Reference

| Operation | Code | Cost |
|-----------|------|------|
| Create | `Trie()` | O(1) |
| Add a word | `trie.insert("cat")` | O(L) |
| Exact word? | `trie.search("cat")` | O(L) |
| Any word starts with...? | `trie.starts_with("ca")` | O(L) |
| Suggest completions | `trie.autocomplete("ca")` | O(L + M) |
| Count completions | `trie.count_words_with_prefix("ca")` | O(L + subtree) |

L = word/prefix length, N = number of stored words, M = size of the matches
reported. N never appears in an operation's cost.

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
