# 🎯 HTML & CSS Overview - Quiz

Test your knowledge of HTML and CSS fundamentals.

---

## Multiple Choice Questions

### Question 1
What does HTML stand for?

- A) HyperText Markdown Language
- B) HyperText Markup Language
- C) HighText Modern Language
- D) HyperTransfer Markup Language

### Question 2
Which HTML tag creates the largest heading?

- A) `<head>`
- B) `<header>`
- C) `<h6>`
- D) `<h1>`

### Question 3
What is the correct syntax for creating a hyperlink?

- A) `<link href="url">Text</link>`
- B) `<a src="url">Text</a>`
- C) `<a href="url">Text</a>`
- D) `<href url="url">Text</href>`

### Question 4
Which CSS property changes the text color?

- A) `text-color`
- B) `font-color`
- C) `color`
- D) `foreground`

### Question 5
What does the `class` attribute do in HTML?

- A) Identifies a unique element
- B) Groups elements for styling
- C) Creates a CSS class definition
- D) Links to a stylesheet

### Question 6
Which HTML element is used to define a table row?

- A) `<td>`
- B) `<tr>`
- C) `<th>`
- D) `<table>`

### Question 7
What is the default display property of a `<div>` element?

- A) `inline`
- B) `inline-block`
- C) `block`
- D) `flex`

### Question 8
Which CSS selector targets an element with `id="header"`?

- A) `.header`
- B) `#header`
- C) `header`
- D) `*header`

### Question 9
What does the CSS property `margin` control?

- A) Space inside an element
- B) Space outside an element
- C) Border thickness
- D) Content width

### Question 10
Which HTML tag is used to create an unordered list?

- A) `<ol>`
- B) `<list>`
- C) `<ul>`
- D) `<li>`

---

## Short Answer Questions

### Question 11
Explain the difference between `padding` and `margin` in CSS.

### Question 12
What is the difference between the `id` and `class` attributes? When should you use each?

### Question 13
Describe what the box model is and list its components from inside to outside.

### Question 14
How do you include an external CSS file in an HTML document?

### Question 15
What are semantic HTML elements? Name at least three examples.

---

## Code Challenge

### Question 16
Write the HTML and CSS code to create a navigation bar with three links (Home, About, Contact) that:
- Displays horizontally
- Has a dark background
- Changes background color when hovering over links

---

## Answers

<details>
<summary>Click to expand answers</summary>

### Multiple Choice

1. **B** - HyperText Markup Language
2. **D** - `<h1>` (headings go from h1 largest to h6 smallest)
3. **C** - `<a href="url">Text</a>`
4. **C** - `color`
5. **B** - Groups elements for styling (multiple elements can share a class)
6. **B** - `<tr>` (table row)
7. **C** - `block`
8. **B** - `#header`
9. **B** - Space outside an element
10. **C** - `<ul>` (unordered list)

### Short Answer

11. **Padding** is the space between an element's content and its border (inside the element). **Margin** is the space outside an element's border, creating distance from other elements.

12. **`id`** must be unique to one element per page and uses `#` in CSS. **`class`** can be applied to multiple elements and uses `.` in CSS. Use `id` for single unique elements and `class` for reusable styling patterns.

13. The **box model** describes how element space is calculated. From inside to outside: **Content** → **Padding** → **Border** → **Margin**.

14. Use the `<link>` tag in the `<head>` section:
    ```html
    <link rel="stylesheet" href="styles.css">
    ```

15. **Semantic elements** clearly describe their meaning to browsers and developers. Examples: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`, `<aside>`.

### Code Challenge

16. ```html
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            nav {
                background: #333;
                padding: 10px;
            }
            nav ul {
                list-style: none;
                margin: 0;
                padding: 0;
                display: flex;
            }
            nav a {
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                display: block;
            }
            nav a:hover {
                background: #555;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </body>
    </html>
    ```

</details>

---

**Score your quiz:**
- 14-16 correct: 🌟 Excellent! You're ready for web development!
- 11-13 correct: 👍 Good job! Review the topics you missed.
- 8-10 correct: 📚 Getting there! Go back and study the fundamentals.
- Below 8: 🎯 Keep practicing! Review the README and examples again.
