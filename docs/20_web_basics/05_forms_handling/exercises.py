"""
Forms Handling - Exercises
==========================
Practice processing HTML form data.
"""

print("=" * 60)
print("FORMS HANDLING - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Registration Form Validator
# =============================================================================
print("\n--- Exercise 1: Registration Form Validator ---\n")
"""
Create a function `validate_registration(data)` that validates user registration data.

Required fields:
- username: 3-20 characters, alphanumeric only
- email: valid email format
- password: at least 8 characters, must contain uppercase, lowercase, and digit
- confirm_password: must match password
- age: must be 13 or older
- terms: must be True/"on"

Return a list of error messages (empty list if valid).
"""

# Your code here:


# =============================================================================
# EXERCISE 2: Search Form Parser
# =============================================================================
print("\n--- Exercise 2: Search Form Parser ---\n")
"""
Create a function `parse_search_query(query_string)` that parses search parameters.

Expected parameters:
- q: search query (required)
- category: filter category (optional)
- sort: 'relevance', 'date', or 'price' (default: 'relevance')
- page: page number (default: 1, min: 1)
- limit: results per page (default: 20, max: 100)

Return a dictionary with parsed and validated values.
Convert types appropriately (page and limit as integers).
"""

# Your code here:


# =============================================================================
# EXERCISE 3: Survey Form Processor
# =============================================================================
print("\n--- Exercise 3: Survey Form Processor ---\n")
"""
Create a SurveyProcessor class that handles multi-question surveys.

The class should:
- Define survey structure (questions, types, options)
- Parse form submissions
- Validate all answers
- Calculate scores/averages
- Generate summary report

Support question types: text, number, rating (1-5), choice (single/multiple)
"""

# Your code here:


# =============================================================================
# EXERCISE 4: Contact Form Handler
# =============================================================================
print("\n--- Exercise 4: Contact Form Handler ---\n")
"""
Create a complete contact form handler with these features:

- Render a contact form (HTML generation)
- Parse POST submissions
- Validate all fields (name, email, subject, message)
- Send email notification (simulate - just print to console)
- Store submission in a list/file
- Show success or error page with appropriate messages

Include rate limiting (max 3 submissions per email per hour).
"""

# Your code here:


# =============================================================================
# EXERCISE 5: Multi-Step Form
# =============================================================================
print("\n--- Exercise 5: Multi-Step Form Wizard ---\n")
"""
Create a multi-step form wizard for booking an appointment:

Step 1: Select service type (haircut, massage, consultation)
Step 2: Select date and time
Step 3: Enter personal info (name, email, phone)
Step 4: Review and confirm

The wizard should:
- Track current step
- Store intermediate data
- Allow going back to previous steps
- Validate each step before proceeding
- Show progress indicator
"""

# Your code here:


# =============================================================================
# EXERCISE 6: Form Builder with Validation
# =============================================================================
print("\n--- Exercise 6: Form Builder with Validation ---\n")
"""
Create a FormBuilder class that:

- Defines form fields with types and validation rules
- Generates HTML for the form
- Parses and validates submitted data
- Returns cleaned data or validation errors

Support validation rules:
- required: bool
- min_length/max_length: int (for strings)
- min/max: number (for numbers)
- pattern: regex string
- choices: list of valid values

Example:
    builder = FormBuilder()
    builder.add_field('username', 'text', required=True, min_length=3)
    builder.add_field('age', 'number', min=0, max=150)
    html = builder.render()
    result = builder.validate(post_data)
"""

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# -------------------------------------------------------------------------
# Solution 1
# -------------------------------------------------------------------------
print("\n--- Solution 1: Registration Form Validator ---\n")

import re

def validate_registration(data):
    """Validate user registration data."""
    errors = []
    
    # Username validation
    username = data.get('username', '').strip()
    if not username:
        errors.append("Username is required")
    elif len(username) < 3 or len(username) > 20:
        errors.append("Username must be 3-20 characters")
    elif not re.match(r'^[a-zA-Z0-9_]+$', username):
        errors.append("Username must be alphanumeric")
    
    # Email validation
    email = data.get('email', '').strip()
    if not email:
        errors.append("Email is required")
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        errors.append("Invalid email format")
    
    # Password validation
    password = data.get('password', '')
    if not password:
        errors.append("Password is required")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters")
    elif not re.search(r'[A-Z]', password):
        errors.append("Password must contain an uppercase letter")
    elif not re.search(r'[a-z]', password):
        errors.append("Password must contain a lowercase letter")
    elif not re.search(r'\d', password):
        errors.append("Password must contain a digit")
    
    # Confirm password
    confirm = data.get('confirm_password', '')
    if confirm != password:
        errors.append("Passwords do not match")
    
    # Age validation
    try:
        age = int(data.get('age', 0))
        if age < 13:
            errors.append("You must be at least 13 years old")
    except ValueError:
        errors.append("Age must be a number")
    
    # Terms acceptance
    terms = data.get('terms', False)
    if isinstance(terms, str):
        terms = terms.lower() in ('on', 'true', '1', 'yes')
    if not terms:
        errors.append("You must accept the terms and conditions")
    
    return errors

# Test
test_registrations = [
    {'username': 'alice', 'email': 'alice@example.com', 'password': 'Hello123', 'confirm_password': 'Hello123', 'age': '25', 'terms': 'on'},
    {'username': 'a', 'email': 'invalid', 'password': 'short', 'confirm_password': 'different', 'age': '10', 'terms': ''},
]

print("Registration validation:")
for i, test in enumerate(test_registrations, 1):
    errors = validate_registration(test)
    status = "✅ Valid" if not errors else f"❌ {errors}"
    print(f"  Test {i}: {status}")

# -------------------------------------------------------------------------
# Solution 2
# -------------------------------------------------------------------------
print("\n--- Solution 2: Search Form Parser ---\n")

from urllib.parse import parse_qs

def parse_search_query(query_string):
    """Parse and validate search query parameters."""
    # Parse query string
    params = parse_qs(query_string)
    data = {k: v[0] if len(v) == 1 else v for k, v in params.items()}
    
    result = {}
    
    # Required: q (search query)
    result['q'] = data.get('q', '').strip()
    
    # Optional: category
    result['category'] = data.get('category', '').strip() or None
    
    # Sort (default: relevance, options: relevance, date, price)
    sort = data.get('sort', 'relevance')
    valid_sorts = ['relevance', 'date', 'price']
    result['sort'] = sort if sort in valid_sorts else 'relevance'
    
    # Page (default: 1, min: 1)
    try:
        page = int(data.get('page', 1))
        result['page'] = max(1, page)
    except ValueError:
        result['page'] = 1
    
    # Limit (default: 20, max: 100)
    try:
        limit = int(data.get('limit', 20))
        result['limit'] = min(max(1, limit), 100)
    except ValueError:
        result['limit'] = 20
    
    return result

# Test
print("Search query parsing:")
test_queries = [
    "q=python&category=books&sort=price&page=2&limit=10",
    "q=",
    "q=web+development&sort=invalid&page=-1&limit=999",
]

for query in test_queries:
    result = parse_search_query(query)
    print(f"  Input:  {query}")
    print(f"  Parsed: {result}")
    print()

# -------------------------------------------------------------------------
# Solution 3
# -------------------------------------------------------------------------
print("\n--- Solution 3: Survey Form Processor ---\n")

class SurveyProcessor:
    """Process multi-question surveys."""
    
    def __init__(self):
        self.questions = []
        self.responses = []
    
    def add_question(self, id, text, type_, required=True, options=None, validations=None):
        """Add a survey question."""
        self.questions.append({
            'id': id,
            'text': text,
            'type': type_,
            'required': required,
            'options': options or [],
            'validations': validations or {}
        })
    
    def validate(self, answers):
        """Validate survey answers."""
        errors = {}
        
        for q in self.questions:
            qid = q['id']
            value = answers.get(qid)
            
            # Required check
            if q['required'] and (value is None or value == ''):
                errors[qid] = "This question is required"
                continue
            
            if not value:
                continue
            
            # Type-specific validation
            if q['type'] == 'rating':
                try:
                    rating = int(value)
                    if rating < 1 or rating > 5:
                        errors[qid] = "Rating must be between 1 and 5"
                except ValueError:
                    errors[qid] = "Rating must be a number"
            
            elif q['type'] == 'number':
                try:
                    num = float(value)
                    min_val = q['validations'].get('min')
                    max_val = q['validations'].get('max')
                    if min_val is not None and num < min_val:
                        errors[qid] = f"Value must be at least {min_val}"
                    if max_val is not None and num > max_val:
                        errors[qid] = f"Value must be at most {max_val}"
                except ValueError:
                    errors[qid] = "Must be a number"
            
            elif q['type'] == 'choice' and q['options']:
                if value not in q['options']:
                    errors[qid] = "Invalid option selected"
        
        return errors
    
    def process(self, answers):
        """Process validated answers."""
        errors = self.validate(answers)
        if errors:
            return {'success': False, 'errors': errors}
        
        # Clean and store
        cleaned = self._clean_answers(answers)
        self.responses.append(cleaned)
        
        return {'success': True, 'data': cleaned}
    
    def _clean_answers(self, answers):
        """Clean answer values."""
        cleaned = {}
        for q in self.questions:
            qid = q['id']
            value = answers.get(qid)
            
            if q['type'] == 'number' and value:
                value = float(value)
            elif q['type'] == 'rating' and value:
                value = int(value)
            elif q['type'] == 'text' and value:
                value = value.strip()
            
            cleaned[qid] = value
        
        return cleaned
    
    def get_summary(self):
        """Generate summary statistics."""
        if not self.responses:
            return {}
        
        summary = {}
        for q in self.questions:
            qid = q['id']
            values = [r.get(qid) for r in self.responses if r.get(qid) is not None]
            
            if q['type'] == 'rating' or q['type'] == 'number':
                if values:
                    summary[qid] = {
                        'count': len(values),
                        'average': sum(values) / len(values),
                        'min': min(values),
                        'max': max(values)
                    }
            else:
                summary[qid] = {'count': len(values), 'responses': values}
        
        return summary

# Test
survey = SurveyProcessor()
survey.add_question('satisfaction', 'How satisfied are you?', 'rating', required=True)
survey.add_question('age', 'What is your age?', 'number', validations={'min': 18, 'max': 100})
survey.add_question('feedback', 'Any feedback?', 'text', required=False)

# Process responses
responses = [
    {'satisfaction': '5', 'age': '25', 'feedback': 'Great service!'},
    {'satisfaction': '4', 'age': '30', 'feedback': 'Good'},
    {'satisfaction': '5', 'age': '35'},
]

print("Survey processing:")
for resp in responses:
    result = survey.process(resp)
    print(f"  Response: {result['success']}")

print(f"\nSummary: {survey.get_summary()}")

# -------------------------------------------------------------------------
# Solution 4
# -------------------------------------------------------------------------
print("\n--- Solution 4: Contact Form Handler ---\n")

from html import escape
from datetime import datetime, timedelta
from collections import defaultdict
import time

class ContactFormHandler:
    """Handle contact form submissions with rate limiting."""
    
    def __init__(self):
        self.submissions = []
        self.rate_limits = defaultdict(list)  # email -> list of timestamps
        self.max_submissions = 3
        self.window_hours = 1
    
    def render_form(self, errors=None, values=None):
        """Generate contact form HTML."""
        errors = errors or {}
        values = values or {}
        
        error_html = ''
        if errors:
            error_list = ''.join(f'<li>{escape(e)}</li>' for e in errors.values())
            error_html = f'<ul style="color: red;">{error_list}</ul>'
        
        def field(name, type_, label, required=True):
            value = escape(values.get(name, ''))
            req = ' required' if required else ''
            error = f'<span style="color: red;">{escape(errors.get(name, ""))}</span>' if name in errors else ''
            return f"""
            <div style="margin-bottom: 15px;">
                <label>{escape(label)}:</label>
                <input type="{type_}" name="{name}" value="{value}"{req} style="width: 100%; padding: 8px;">
                {error}
            </div>"""
        
        return f"""<!DOCTYPE html>
<html>
<head><title>Contact Us</title></head>
<body style="max-width: 500px; margin: 50px auto; font-family: Arial;">
    <h1>Contact Us</h1>
    {error_html}
    <form method="POST" action="/contact">
        {field('name', 'text', 'Your Name')}
        {field('email', 'email', 'Email Address')}
        {field('subject', 'text', 'Subject')}
        <div style="margin-bottom: 15px;">
            <label>Message:</label>
            <textarea name="message" required style="width: 100%; padding: 8px; height: 100px;">{escape(values.get('message', ''))}</textarea>
            {f'<span style="color: red;">{escape(errors.get("message", ""))}</span>' if 'message' in errors else ''}
        </div>
        <button type="submit" style="background: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer;">Send Message</button>
    </form>
</body>
</html>"""
    
    def check_rate_limit(self, email):
        """Check if email has exceeded rate limit."""
        now = time.time()
        window_start = now - (self.window_hours * 3600)
        
        # Filter to recent submissions only
        self.rate_limits[email] = [t for t in self.rate_limits[email] if t > window_start]
        
        return len(self.rate_limits[email]) < self.max_submissions
    
    def validate(self, data):
        """Validate form data."""
        errors = {}
        
        if not data.get('name', '').strip():
            errors['name'] = "Name is required"
        
        email = data.get('email', '').strip()
        if not email:
            errors['email'] = "Email is required"
        elif '@' not in email:
            errors['email'] = "Invalid email"
        elif not self.check_rate_limit(email):
            errors['email'] = f"Too many submissions. Please try again in {self.window_hours} hour(s)."
        
        if not data.get('subject', '').strip():
            errors['subject'] = "Subject is required"
        
        message = data.get('message', '').strip()
        if not message:
            errors['message'] = "Message is required"
        elif len(message) < 10:
            errors['message'] = "Message must be at least 10 characters"
        
        return errors
    
    def process(self, data):
        """Process form submission."""
        errors = self.validate(data)
        
        if errors:
            return {'success': False, 'errors': errors, 'html': self.render_form(errors, data)}
        
        # Record submission
        email = data.get('email')
        self.rate_limits[email].append(time.time())
        
        submission = {
            'timestamp': datetime.now(),
            'name': data['name'].strip(),
            'email': email,
            'subject': data['subject'].strip(),
            'message': data['message'].strip()
        }
        self.submissions.append(submission)
        
        # Simulate sending email
        print(f"[EMAIL] To: admin@example.com")
        print(f"        Subject: Contact Form: {submission['subject']}")
        print(f"        From: {submission['name']} <{submission['email']}>")
        print(f"        Body: {submission['message'][:100]}...")
        
        return {'success': True, 'submission': submission}
    
    def render_success(self, submission):
        """Render success page."""
        return f"""<!DOCTYPE html>
<html>
<head><title>Message Sent</title></head>
<body style="max-width: 500px; margin: 50px auto; font-family: Arial; text-align: center;">
    <h1>✅ Message Sent!</h1>
    <p>Thank you, <strong>{escape(submission['name'])}</strong>!</p>
    <p>We'll get back to you at {escape(submission['email'])} soon.</p>
    <a href="/contact">Send another message</a>
</body>
</html>"""

# Test
handler = ContactFormHandler()

print("Contact form test:")
# Valid submission
result = handler.process({
    'name': 'Alice',
    'email': 'alice@example.com',
    'subject': 'Hello',
    'message': 'This is a test message that is long enough.'
})
print(f"Submission 1: {'✅ Success' if result['success'] else '❌ Failed'}")

# Rate limit test
for i in range(4):
    result = handler.process({
        'name': 'Bob',
        'email': 'bob@example.com',
        'subject': 'Test',
        'message': 'This is a test message that is long enough.'
    })
    print(f"Submission {i+2} (bob): {'✅ Success' if result['success'] else '❌ Rate limited'}")

# -------------------------------------------------------------------------
# Solution 5
# -------------------------------------------------------------------------
print("\n--- Solution 5: Multi-Step Form Wizard ---\n")

class FormWizard:
    """Multi-step form wizard."""
    
    def __init__(self):
        self.steps = [
            {'id': 'service', 'title': 'Select Service'},
            {'id': 'datetime', 'title': 'Choose Date & Time'},
            {'id': 'personal', 'title': 'Your Information'},
            {'id': 'review', 'title': 'Review & Confirm'}
        ]
        self.sessions = {}  # session_id -> data
    
    def get_progress(self, current_step):
        """Get progress indicator."""
        current_idx = next(i for i, s in enumerate(self.steps) if s['id'] == current_step)
        progress = []
        for i, step in enumerate(self.steps):
            if i < current_idx:
                status = '✓'
            elif i == current_idx:
                status = '→'
            else:
                status = '○'
            progress.append(f"{status} {i+1}. {step['title']}")
        return ' | '.join(progress)
    
    def render_step(self, step_id, data=None, errors=None):
        """Render a specific step."""
        data = data or {}
        errors = errors or {}
        progress = self.get_progress(step_id)
        
        forms = {
            'service': """
                <h3>Select Service</h3>
                <label><input type="radio" name="service" value="haircut" required> Haircut ($30)</label><br>
                <label><input type="radio" name="service" value="massage"> Massage ($80)</label><br>
                <label><input type="radio" name="service" value="consultation"> Consultation (Free)</label>
            """,
            'datetime': """
                <h3>Choose Date & Time</h3>
                <label>Date: <input type="date" name="date" required></label><br><br>
                <label>Time: 
                    <select name="time" required>
                        <option value="">Select...</option>
                        <option value="09:00">9:00 AM</option>
                        <option value="10:00">10:00 AM</option>
                        <option value="14:00">2:00 PM</option>
                        <option value="15:00">3:00 PM</option>
                    </select>
                </label>
            """,
            'personal': """
                <h3>Your Information</h3>
                <label>Name: <input type="text" name="name" required></label><br><br>
                <label>Email: <input type="email" name="email" required></label><br><br>
                <label>Phone: <input type="tel" name="phone" required></label>
            """,
            'review': lambda d: f"""
                <h3>Review Your Appointment</h3>
                <p><strong>Service:</strong> {d.get('service', 'N/A')}</p>
                <p><strong>Date:</strong> {d.get('date', 'N/A')} at {d.get('time', 'N/A')}</p>
                <p><strong>Name:</strong> {d.get('name', 'N/A')}</p>
                <p><strong>Email:</strong> {d.get('email', 'N/A')}</p>
                <p><strong>Phone:</strong> {d.get('phone', 'N/A')}</p>
                <input type="hidden" name="confirmed" value="true">
            """
        }
        
        form_content = forms[step_id]
        if callable(form_content):
            form_content = form_content(data)
        
        # Navigation buttons
        current_idx = next(i for i, s in enumerate(self.steps) if s['id'] == step_id)
        buttons = []
        
        if current_idx > 0:
            buttons.append('<button type="submit" name="action" value="back">← Back</button>')
        
        if current_idx < len(self.steps) - 1:
            buttons.append('<button type="submit" name="action" value="next">Next →</button>')
        else:
            buttons.append('<button type="submit" name="action" value="confirm">Confirm Booking</button>')
        
        return f"""<!DOCTYPE html>
<html>
<head><title>Book Appointment - Step {current_idx+1}</title></head>
<body style="max-width: 600px; margin: 50px auto; font-family: Arial;">
    <h1>Book Appointment</h1>
    <p style="color: #666;">{progress}</p>
    <form method="POST">
        <input type="hidden" name="step" value="{step_id}">
        {form_content}
        <div style="margin-top: 20px;">
            {' '.join(buttons)}
        </div>
    </form>
</body>
</html>"""
    
    def validate_step(self, step_id, data):
        """Validate a specific step."""
        errors = {}
        
        if step_id == 'service':
            if not data.get('service'):
                errors['service'] = "Please select a service"
        
        elif step_id == 'datetime':
            if not data.get('date'):
                errors['date'] = "Please select a date"
            if not data.get('time'):
                errors['time'] = "Please select a time"
        
        elif step_id == 'personal':
            if not data.get('name', '').strip():
                errors['name'] = "Name is required"
            if not data.get('email', '').strip():
                errors['email'] = "Email is required"
        
        return errors
    
    def process(self, session_id, form_data):
        """Process wizard step."""
        # Initialize session if needed
        if session_id not in self.sessions:
            self.sessions[session_id] = {'step': 0, 'data': {}}
        
        session = self.sessions[session_id]
        current_step = form_data.get('step', self.steps[0]['id'])
        action = form_data.get('action', 'next')
        
        # Handle back button
        if action == 'back':
            session['step'] = max(0, session['step'] - 1)
            prev_step = self.steps[session['step']]['id']
            return self.render_step(prev_step, session['data'])
        
        # Validate current step
        errors = self.validate_step(current_step, form_data)
        if errors:
            return self.render_step(current_step, form_data, errors)
        
        # Save step data
        session['data'].update({k: v for k, v in form_data.items() if k not in ('step', 'action')})
        
        # Handle confirmation
        if action == 'confirm':
            return f"""<!DOCTYPE html>
<html>
<head><title>Booking Confirmed</title></head>
<body style="max-width: 600px; margin: 50px auto; font-family: Arial; text-align: center;">
    <h1>✅ Booking Confirmed!</h1>
    <p>Your appointment has been scheduled.</p>
    <p>Confirmation details sent to {escape(session['data'].get('email', 'your email'))}</p>
</body>
</html>"""
        
        # Move to next step
        session['step'] = min(len(self.steps) - 1, session['step'] + 1)
        next_step = self.steps[session['step']]['id']
        return self.render_step(next_step, session['data'])

# Test
wizard = FormWizard()

print("Form wizard steps:")
for step in wizard.steps:
    print(f"  - {step['title']}")

print(f"\nProgress indicator: {wizard.get_progress('datetime')}")

# -------------------------------------------------------------------------
# Solution 6
# -------------------------------------------------------------------------
print("\n--- Solution 6: Form Builder with Validation ---\n")

import re
from html import escape

class FormBuilder:
    """Build forms with validation."""
    
    def __init__(self):
        self.fields = []
    
    def add_field(self, name, field_type, label=None, **options):
        """Add a field with validation options."""
        self.fields.append({
            'name': name,
            'type': field_type,
            'label': label or name.replace('_', ' ').title(),
            'required': options.get('required', False),
            'min_length': options.get('min_length'),
            'max_length': options.get('max_length'),
            'min': options.get('min'),
            'max': options.get('max'),
            'pattern': options.get('pattern'),
            'choices': options.get('choices'),
            'placeholder': options.get('placeholder', ''),
            'default': options.get('default', '')
        })
    
    def render(self):
        """Generate form HTML."""
        fields_html = []
        
        for field in self.fields:
            html = self._render_field(field)
            fields_html.append(html)
        
        return f"""<form method="POST" style="max-width: 400px; padding: 20px;">
{'\n'.join(fields_html)}
    <button type="submit">Submit</button>
</form>"""
    
    def _render_field(self, field):
        """Render a single field."""
        name = field['name']
        label = escape(field['label'])
        required = ' required' if field['required'] else ''
        placeholder = escape(field['placeholder'])
        
        attrs = f'name="{name}" id="{name}"{required}'
        if placeholder:
            attrs += f' placeholder="{placeholder}"'
        
        if field['type'] == 'text':
            input_html = f'<input type="text" {attrs} style="width: 100%; padding: 8px;">'
        
        elif field['type'] == 'email':
            input_html = f'<input type="email" {attrs} style="width: 100%; padding: 8px;">'
        
        elif field['type'] == 'password':
            input_html = f'<input type="password" {attrs} style="width: 100%; padding: 8px;">'
        
        elif field['type'] == 'number':
            attrs += f' min="{field["min"]}"' if field['min'] is not None else ''
            attrs += f' max="{field["max"]}"' if field['max'] is not None else ''
            input_html = f'<input type="number" {attrs} style="width: 100%; padding: 8px;">'
        
        elif field['type'] == 'textarea':
            input_html = f'<textarea {attrs} style="width: 100%; padding: 8px; height: 100px;"></textarea>'
        
        elif field['type'] == 'select' and field['choices']:
            options = '\n'.join(f'        <option value="{escape(c)}">{escape(c)}</option>' for c in field['choices'])
            input_html = f"""<select {attrs} style="width: 100%; padding: 8px;">
        <option value="">-- Select --</option>
{options}
    </select>"""
        
        else:
            input_html = f'<input type="{field["type"]}" {attrs} style="width: 100%; padding: 8px;">'
        
        return f"""<div style="margin-bottom: 15px;">
    <label for="{name}">{label}:</label><br>
    {input_html}
</div>"""
    
    def validate(self, data):
        """Validate submitted data."""
        errors = {}
        cleaned = {}
        
        for field in self.fields:
            name = field['name']
            value = data.get(name, '').strip()
            
            # Required check
            if field['required'] and not value:
                errors[name] = f"{field['label']} is required"
                continue
            
            if not value:
                cleaned[name] = None
                continue
            
            # Length validation
            if field['min_length'] and len(value) < field['min_length']:
                errors[name] = f"{field['label']} must be at least {field['min_length']} characters"
                continue
            
            if field['max_length'] and len(value) > field['max_length']:
                errors[name] = f"{field['label']} must be at most {field['max_length']} characters"
                continue
            
            # Pattern validation
            if field['pattern'] and not re.match(field['pattern'], value):
                errors[name] = f"{field['label']} format is invalid"
                continue
            
            # Number validation
            if field['type'] == 'number':
                try:
                    num = float(value)
                    if field['min'] is not None and num < field['min']:
                        errors[name] = f"{field['label']} must be at least {field['min']}"
                        continue
                    if field['max'] is not None and num > field['max']:
                        errors[name] = f"{field['label']} must be at most {field['max']}"
                        continue
                    cleaned[name] = num
                    continue
                except ValueError:
                    errors[name] = f"{field['label']} must be a number"
                    continue
            
            # Choices validation
            if field['choices'] and value not in field['choices']:
                errors[name] = f"{field['label']} must be one of: {', '.join(field['choices'])}"
                continue
            
            cleaned[name] = value
        
        return {'valid': len(errors) == 0, 'errors': errors, 'cleaned': cleaned}

# Test
builder = FormBuilder()
builder.add_field('username', 'text', required=True, min_length=3, max_length=20)
builder.add_field('email', 'email', required=True)
builder.add_field('age', 'number', min=13, max=120)
builder.add_field('country', 'select', choices=['USA', 'UK', 'Canada'], required=True)

print("Generated form (first 800 chars):")
print(builder.render()[:800] + "...")

# Validation test
print("\nValidation tests:")
test_cases = [
    {'username': 'a', 'email': 'invalid', 'age': '10', 'country': 'USA'},
    {'username': 'alice', 'email': 'alice@example.com', 'age': '25', 'country': 'USA'},
]

for test in test_cases:
    result = builder.validate(test)
    status = "✅ Valid" if result['valid'] else f"❌ {result['errors']}"
    print(f"  {status}")

print("\n" + "=" * 60)
print("All solutions complete! Great job!")
print("=" * 60)
