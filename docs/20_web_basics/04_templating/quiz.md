# 🎯 Templating - Quiz

Test your knowledge of HTML templating with Python.

---

## Multiple Choice Questions

### Question 1
Why is HTML escaping important when generating dynamic content?

- A) It makes HTML load faster
- B) It prevents XSS (Cross-Site Scripting) attacks
- C) It compresses the HTML size
- D) It's required by HTML5 specification

### Question 2
What Python function should you use to escape HTML special characters?

- A) `html.encode()`
- B) `html.escape()`
- C) `html.sanitize()`
- D) `html.clean()`

### Question 3
What does `string.Template` provide that f-strings don't?

- A) Better performance
- B) Safe substitution that won't error on missing keys
- C) Automatic HTML escaping
- D) Support for loops and conditionals

### Question 4
Which character sequence does `html.escape()` convert `&` to?

- A) `&amp;`
- B) `&lt;`
- C) `&gt;`
- D) `&and;`

### Question 5
What is the purpose of template inheritance?

- A) To make templates load faster
- B) To share common layout structure across pages
- C) To secure templates from attacks
- D) To compress template files

### Question 6
In a template system, what does `{{ variable }}` typically represent?

- A) A comment
- B) A variable substitution placeholder
- C) A CSS selector
- D) A JavaScript function

### Question 7
What is wrong with this code: `html = f"<p>{user_input}</p>"`?

- A) The f-string syntax is incorrect
- B) It's vulnerable to XSS if user_input contains HTML
- C) The paragraph tag is deprecated
- D) user_input is not defined

### Question 8
What does `Template.safe_substitute()` do differently from `substitute()`?

- A) It's faster
- B) It doesn't raise an error for missing keys
- C) It automatically escapes HTML
- D) It supports more data types

### Question 9
When building HTML tables programmatically, what's the most efficient approach?

- A) String concatenation in a loop
- B) Build a list and use `''.join()`
- C) Use `+=` to append rows
- D) Write directly to a file

### Question 10
What is XSS (Cross-Site Scripting)?

- A) A CSS framework
- B) An attack where malicious scripts are injected into web pages
- C) A Python templating engine
- D) A way to style HTML tables

---

## Short Answer Questions

### Question 11
Explain the difference between `string.Template` and f-strings for HTML generation. When would you use each?

### Question 12
Describe how you would implement a simple template inheritance system where child templates can override specific sections of a parent template.

### Question 13
What are the security implications of not escaping user input in HTML templates? Give a concrete example of an attack.

### Question 14
Explain why building HTML strings with `result += html` in a loop is inefficient, and what the better approach is.

### Question 15
How would you design a component system for reusable HTML elements (like buttons, cards, alerts) in Python?

---

## Code Challenge

### Question 16
Create a complete email template system that:
1. Has a base template with header and footer
2. Supports multiple email types (welcome, notification, newsletter)
3. Properly escapes all dynamic content
4. Includes both HTML and plain text versions
5. Has a clean API for sending different email types

---

## Answers

<details>
<summary>Click to expand answers</summary>

### Multiple Choice

1. **B** - It prevents XSS (Cross-Site Scripting) attacks
2. **B** - `html.escape()`
3. **B** - Safe substitution that won't error on missing keys
4. **A** - `&amp;`
5. **B** - To share common layout structure across pages
6. **B** - A variable substitution placeholder
7. **B** - It's vulnerable to XSS if user_input contains HTML
8. **B** - It doesn't raise an error for missing keys
9. **B** - Build a list and use `''.join()`
10. **B** - An attack where malicious scripts are injected into web pages

### Short Answer

11. **F-strings** are best for simple, one-off substitutions where you have all the data. **string.Template** is better for reusable templates, templates loaded from files, or when you need `safe_substitute()` to handle missing keys gracefully.

12. Create a base template with placeholders like `$content`. Child templates define their specific content and call `base_template.substitute(content=child_content)`. For multiple sections, use multiple placeholders or a more sophisticated system with block definitions.

13. Without escaping, a user could submit `<script>alert(document.cookie)</script>` which would execute in other users' browsers. This could steal cookies, session tokens, or perform actions on behalf of users. Escaping converts `<` to `&lt;` so it's displayed as text, not executed.

14. String concatenation with `+=` creates a new string object each time (strings are immutable), leading to O(n²) time complexity. The better approach is to append to a list and use `''.join(list)` once at the end, which is O(n).

15. Create a `Components` class with static methods like `@staticmethod def button(text, **props):`. Each method returns an HTML string. Components handle their own styling (inline or with CSS classes) and escaping. Build pages by composing these component calls.

### Code Challenge

16. ```python
    from string import Template
    from html import escape
    
    class EmailTemplate:
        BASE_HTML = """<!DOCTYPE html>
        <html>
        <body style="font-family: Arial, sans-serif;">
            <div style="max-width: 600px; margin: 0 auto;">
                <header style="background: #333; color: white; padding: 20px;">
                    <h1>$company_name</h1>
                </header>
                <main style="padding: 20px; background: #f9f9f9;">
                    $content
                </main>
                <footer style="padding: 20px; text-align: center; color: #666;">
                    <p>&copy; 2026 $company_name</p>
                </footer>
            </div>
        </body>
        </html>"""
        
        def __init__(self, company_name="My Company"):
            self.company_name = escape(company_name)
        
        def welcome(self, user_name):
            content = f"""
            <h2>Welcome, {escape(user_name)}!</h2>
            <p>Thank you for joining us. We're excited to have you on board.</p>
            <a href="/get-started" style="background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px;">Get Started</a>
            """
            return self._render(content)
        
        def notification(self, message, action_url=None):
            content = f"<p>{escape(message)}</p>"
            if action_url:
                content += f'<a href="{escape(action_url)}" style="color: #007bff;">Take Action</a>'
            return self._render(content)
        
        def _render(self, content):
            template = Template(self.BASE_HTML)
            return template.substitute(
                company_name=self.company_name,
                content=content
            )
    
    # Usage
    email = EmailTemplate("My App")
    html = email.welcome("Alice")
    ```

</details>

---

**Score your quiz:**
- 14-16 correct: 🌟 Templating expert! You can build secure, maintainable systems!
- 11-13 correct: 👍 Great understanding! Practice more complex templates.
- 8-10 correct: 📚 Good foundation! Review escaping and template patterns.
- Below 8: 🎯 Study HTML escaping and basic template techniques first.
