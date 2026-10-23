# 📝 Tries - Quiz

---

## Question 1
What does each TrieNode store?

A) The whole word  
B) A children dict and an is_end flag  
C) A list of all words below it  
D) Only a single character

<details>
<summary>Click for answer</summary>

**B) A children dict and an is_end flag**

Each node maps one character per child and flags whether a word ends there.
No node ever stores a whole word - the word is the path you walked.

</details>

---

## Question 2
A trie stores 100,000 words. How long does `starts_with("fr")` take?

A) O(N) - must check all words  
B) O(log N)  
C) O(L) - one step per prefix letter  
D) O(N · L)

<details>
<summary>Click for answer</summary>

**C) O(L) - one step per prefix letter**

That is the trie's superpower: the walk is 2 steps for "fr" whether the trie
holds 3 words or 3 million. N never appears in the cost.

</details>

---

## Question 3
A trie contains only "cat". What does `search("ca")` return, and why?

A) True - the path c -> a exists  
B) True - "ca" is a prefix of a word  
C) False - no node on that path has is_end = True  
D) False - the path does not exist

<details>
<summary>Click for answer</summary>

**C) False - no node on that path has is_end = True**

The path exists, so `starts_with("ca")` is True - but `search` also requires
`is_end` on the final node, and no word ends at "ca".

</details>

---

## Question 4
What is the ONE difference between `search` and `starts_with`?

A) `search` walks the tree; `starts_with` does not  
B) `search` checks `is_end` on the final node  
C) `starts_with` also checks `is_end`  
D) They are identical

<details>
<summary>Click for answer</summary>

**B) `search` checks `is_end` on the final node**

Both walk the same path. `starts_with` is happy if the path exists;
`search` demands a word ending there too.

</details>

---

## Question 5
How does `autocomplete("ca")` produce its suggestions?

A) Scan every stored word for the prefix  
B) Walk to the "ca" node, then collect every is_end node in its subtree  
C) Sort the trie and read the first row  
D) Re-insert all words into a new trie

<details>
<summary>Click for answer</summary>

**B) Walk to the "ca" node, then collect every is_end node in its subtree**

After the O(L) walk down, everything below the prefix node is a completion.
Walking children in sorted order even yields the words alphabetically.

</details>

---

## Question 6
You only ever need exact lookups ("is THIS word stored?"). Which structure should you pick?

A) A trie - it handles everything  
B) A set - simpler, and just as fast for exact lookups  
C) A trie of single characters  
D) Either - they always use the same memory

<details>
<summary>Click for answer</summary>

**B) A set - simpler, and just as fast for exact lookups**

Both are O(L), but the trie pays roughly one node (a dict plus a flag) per
character. Without prefix questions or shared prefixes, a set wins on
simplicity and memory.

</details>

---

## Question 7
Why can a trie use LESS memory than a set of words?

A) It stores words in compressed binary  
B) It drops the last letter of each word  
C) Words that share prefixes store the shared nodes only once  
D) It never stores the letter "e"

<details>
<summary>Click for answer</summary>

**C) Words that share prefixes store the shared nodes only once**

"card", "care", and "careful" share one c -> a -> r chain. A set keeps a
full copy of every string.

</details>

---

## Question 8
Which real-world system famously uses tries for "longest prefix match"?

A) Spreadsheet sorting  
B) IP routing - picking the most specific route for a packet  
C) Image compression  
D) Random number generation

<details>
<summary>Click for answer</summary>

**B) IP routing - picking the most specific route for a packet**

Routers walk the destination address bit by bit, keeping the deepest
matching routing-table prefix. Autocomplete, spellcheckers, and T9
keyboards are other classic trie users.

</details>

---

## How did you do?

- **7-8 correct:** Excellent!
- **4-6 correct:** Good, review the ones you missed.
- **0-3 correct:** Re-read the README, then try again.
