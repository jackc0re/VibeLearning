# 🔬 Module 17: Computer Science Fundamentals

> Understanding the low-level concepts that power programming

---

## Welcome to CS Fundamentals!

This module bridges the gap between high-level programming and the underlying computer science concepts that make it all work. While you can write Python code without knowing this stuff, understanding these fundamentals will make you a better programmer.

---

## What You'll Learn

| Topic | Description | Difficulty |
|-------|-------------|------------|
| **Number Systems** | Binary, octal, decimal, hexadecimal conversions | ⭐⭐ |
| **Bitwise Operations** | AND, OR, XOR, shifts, and masks | ⭐⭐ |
| **Boolean Logic** | Logic gates, truth tables, De Morgan's Laws | ⭐⭐ |
| **Memory Architecture** | Stack vs heap, references, memory management | ⭐⭐⭐ |
| **How Python Works** | Bytecode, GIL, interpreter internals | ⭐⭐⭐ |

---

## Why This Matters

### Number Systems
- Understand how computers "think" in binary
- Read memory addresses, color codes, and file permissions
- Debug low-level issues with confidence

### Bitwise Operations
- Optimize flags and permissions systems
- Work with binary protocols and file formats
- Understand compression and encryption basics

### Boolean Logic
- Write better conditional statements
- Simplify complex logic in your code
- Understand digital circuit design

### Memory Architecture
- Write memory-efficient code
- Understand why Python behaves the way it does
- Debug memory-related issues

### How Python Works
- Optimize your Python code effectively
- Understand performance characteristics
- Make informed architectural decisions

---

## Learning Path

### Recommended Order

1. **[Number Systems](01_number_systems/README.md)** - Start here! The foundation for everything else
2. **[Bitwise Operations](02_bitwise_operations/README.md)** - Build on number systems
3. **[Boolean Logic](03_boolean_logic/README.md)** - Logic that connects to programming
4. **[Memory Architecture](04_memory_architecture/README.md)** - How data is stored
5. **[How Python Works](05_how_python_works/README.md)** - Tie it all together with Python internals

### Time Estimate

- **Total Time:** 6-8 hours
- **Per Topic:** 1-1.5 hours

---

## Each Topic Contains

```
topic_name/
├── README.md      # Theory and explanations
├── examples.py    # Runnable demonstration code
├── exercises.py   # Practice problems with solutions
└── quiz.md        # Knowledge check questions
```

---

## Quick Reference

### Number Systems
```python
bin(10)        # '0b1010'
oct(10)        # '0o12'
hex(10)        # '0xa'
int('1010', 2) # 10
```

### Bitwise Operations
```python
a & b    # AND
a | b    # OR
a ^ b    # XOR
~a       # NOT
a << n   # Left shift (×2ⁿ)
a >> n   # Right shift (÷2ⁿ)
```

### Boolean Logic Laws
```
A AND (B OR C) = (A AND B) OR (A AND C)  # Distributive
NOT (A AND B) = (NOT A) OR (NOT B)       # De Morgan's
A OR (A AND B) = A                        # Absorption
```

---

## Prerequisites

Before starting this module, you should be comfortable with:
- Python basics (variables, functions, control flow)
- Basic math (powers, remainders)
- Module 01: Foundations

---

## Real-World Applications

After completing this module, you'll understand:

- **Why** `chmod 755` works (number systems)
- **How** flags and permissions systems work (bitwise)
- **When** to use `and` vs `&` (boolean vs bitwise)
- **Why** Python threads have limitations (GIL)
- **How** to avoid memory leaks (memory architecture)

---

## Common Questions

### Q: Do I really need to know binary?
**A:** For day-to-day Python, no. But understanding binary helps you:
- Debug encoding issues
- Work with network protocols
- Optimize certain algorithms
- Understand how computers work

### Q: Is the GIL bad?
**A:** It's a trade-off. The GIL:
- ✅ Makes single-threaded code faster
- ✅ Simplifies C extension development
- ❌ Limits CPU parallelism with threads
- ❌ Can be worked around with multiprocessing

### Q: Should I memorize all this?
**A:** No! Understand the concepts, bookmark this module, and come back when you need specifics. The goal is awareness, not memorization.

---

## Next Steps

1. Start with [Number Systems](01_number_systems/README.md)
2. Run the examples: `python examples.py`
3. Try the exercises: `python exercises.py`
4. Test yourself with the quiz: `quiz.md`
5. Move to the next topic

---

## Additional Resources

- [Python's dis module documentation](https://docs.python.org/3/library/dis.html)
- [Inside the Python GIL](https://dabeaz-course.github.io/practical-python/Notes/09_Packages/05_GIL.html)
- [Real Python: CPython Internals](https://realpython.com/cpython-source-code-guide/)

---

**Ready?** Let's dive into [Number Systems →](01_number_systems/README.md)

---

*"To understand recursion, one must first understand recursion."* — Unknown
