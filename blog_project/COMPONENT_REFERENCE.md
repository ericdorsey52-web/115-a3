# Django Blog Platform - Component Reference Sheet

## 🎨 All Components at a Glance

This is a quick reference for all UI components, their CSS classes, and Figma equivalents.

---

## 📦 Component Library

### BUTTONS

#### 1. Primary Button (Orange, CTA)
```html
<button class="btn btn-primary">Create Account</button>
```
- **Figma:** Button/Primary
- **Color:** #FF6B35 (Orange)
- **Size:** 48px height, 280px width (default)
- **Hover:** #E55A2B (darker), shadow +
- **Usage:** Main call-to-action (Sign Up, Log In, Create Post)

#### 2. Secondary Button (Gray, Alternative)
```html
<button class="btn btn-secondary">Cancel</button>
```
- **Figma:** Button/Secondary
- **Color:** #F5F5F5 (Light Gray)
- **Border:** 1px solid #E0E0E0
- **Hover:** White background, orange border
- **Usage:** Cancel, back, alternative actions

#### 3. Tertiary Button (Link Style, Blue)
```html
<a class="btn btn-tertiary">Log In</a>
```
- **Figma:** Link/Tertiary
- **Color:** #006BFF (Blue)
- **No Background:** Transparent
- **Hover:** Underline, darker blue
- **Usage:** Links, secondary navigation

#### 4. Full-Width Button
```html
<button class="btn btn-primary btn-full">Submit</button>
```
- **Usage:** Forms (takes full container width)

---

### INPUT FIELDS

#### 1. Text Input (Standard)
```html
<div class="form-group">
    <label class="form-label form-label-required">Email Address</label>
    <input type="email" class="form-control" placeholder="your@email.com">
</div>
```
- **Figma:** Input/Text Field with Label
- **Height:** 44px
- **Padding:** 16px (horizontal), 8px (vertical)
- **Border:** 1px solid #E0E0E0
- **Focus State:** Border #FF6B35 + shadow
- **Error State:** Border #EF4444 + red text

#### 2. Password Input
```html
<div class="form-group">
    <label class="form-label form-label-required">Password</label>
    <input type="password" class="form-control" placeholder="Enter password">
</div>
```
- **Same as text input**
- **Type:** password (hides characters)

#### 3. Textarea (Multi-line)
```html
<textarea class="form-control" rows="5" placeholder="Your content..."></textarea>
```
- **Usage:** Blog post content, long text
- **Expandable height**

#### 4. Input Label
```html
<label class="form-label">Field Label</label>
<!-- OR -->
<label class="form-label form-label-required">Required Field *</label>
```
- **Font:** 12px, Weight 500
- **Color:** #1F1F1F (Dark)
- **Red asterisk for required fields**

#### 5. Form Error Message
```html
<span class="form-error">This field is required.</span>
```
- **Color:** #EF4444 (Red)
- **Font:** 12px
- **Usage:** Show validation errors

#### 6. Form Success Message
```html
<span class="form-success">Account created successfully!</span>
```
- **Color:** #10B981 (Green)
- **Font:** 12px

---

### CARD COMPONENT

#### Blog Post Card
```html
<div class="card">
    <div class="card-header">
        <div class="shape-circle">A</div>
        <div>
            <h3 class="card-title">Blog Post Title</h3>
            <div class="card-subtitle">By Author • Jan 8, 2026</div>
        </div>
    </div>
    
    <div class="card-content">
        This is the excerpt of the blog post...
    </div>
    
    <div class="card-footer">
        <span>150 views</span>
        <a href="#" class="btn btn-tertiary">Read More →</a>
    </div>
</div>
```
- **Figma:** Shape/Square with content
- **Border:** 1px solid #E0E0E0
- **Radius:** 8px
- **Padding:** 24px
- **Hover:** Shadow increases, border orange
- **Background:** White

---

### SHAPE COMPONENTS

#### 1. Circular Shape (Avatar)
```html
<div class="shape-circle">A</div>
<!-- OR -->
<div class="shape-circle primary">
    <img src="avatar.png" alt="User">
</div>
```
- **Figma:** Shape/Circle
- **Size:** 48px × 48px
- **Border:** 2px solid #E0E0E0
- **Border-radius:** 50% (makes it circular)
- **Variant:** `.primary` has orange background
- **Usage:** User avatars, author profiles

#### 2. Square Shape (Container)
```html
<div class="shape-square">
    <!-- Content -->
</div>
```
- **Figma:** Shape/Square
- **Border-radius:** 8px
- **Border:** 1px solid #E0E0E0
- **Usage:** Card containers, image containers

---

### ALERT COMPONENTS

#### Success Alert
```html
<div class="alert alert-success">
    Account created successfully! Welcome!
</div>
```
- **Background:** Light green rgba(16, 185, 129, 0.1)
- **Border:** 1px solid #10B981
- **Text:** #047857 (Dark green)

#### Error Alert
```html
<div class="alert alert-error">
    Invalid username or password.
</div>
```
- **Background:** Light red rgba(239, 68, 68, 0.1)
- **Border:** 1px solid #EF4444
- **Text:** #DC2626 (Dark red)

#### Info Alert
```html
<div class="alert alert-info">
    Please check your email to confirm account.
</div>
```
- **Background:** Light blue rgba(59, 130, 246, 0.1)
- **Border:** 1px solid #3B82F6
- **Text:** #1D4ED8 (Dark blue)

#### Warning Alert
```html
<div class="alert alert-warning">
    Your password will expire soon.
</div>
```
- **Background:** Light orange rgba(245, 158, 11, 0.1)
- **Border:** 1px solid #F59E0B
- **Text:** #D97706 (Dark orange)

---

## 🎨 COLOR PALETTE

### Primary Colors
```
Orange:         #FF6B35  (Buttons, CTAs, Primary accents)
Orange Hover:   #E55A2B  (Darker for hover states)
Orange Dark:    #CC5229  (Darkest for active states)
```

### Secondary Colors
```
Gray Dark:      #4A4A4A  (Body text, secondary content)
Gray Light:     #F5F5F5  (Light backgrounds, cards)
Gray Medium:    #9CA3AF  (Muted text, disabled states)
```

### Accent Colors
```
Blue:           #006BFF  (Links, secondary actions)
Blue Hover:     #0052CC  (Darker for hover)
```

### Neutral Colors
```
White:          #FFFFFF  (Main backgrounds)
Black:          #1F1F1F  (Primary text)
Border:         #E0E0E0  (Borders, dividers)
```

### Status Colors
```
Success:        #10B981  (Confirmations, success messages)
Error:          #EF4444  (Errors, required indicators)
Warning:        #F59E0B  (Warnings)
Info:           #3B82F6  (Information)
```

---

## 📏 SPACING SCALE

All spacing uses 8px increments:
```
4px   (var(--spacing-xs))   - Tight spacing (margins between inline elements)
8px   (var(--spacing-sm))   - Small spacing (label margins)
16px  (var(--spacing-md))   - Medium spacing (form field spacing)
24px  (var(--spacing-lg))   - Large spacing (section margins)
32px  (var(--spacing-xl))   - Extra large spacing (major sections)
```

---

## 🔤 TYPOGRAPHY

### Font Family
**Inter** (or system fallback)

### Heading Hierarchy
```
H1: 28px, Weight 700 (Bold)    - Page titles
H2: 18px, Weight 600 (SemiBold) - Section titles
H3: 16px, Weight 600 (SemiBold) - Subsection titles
```

### Body Text Styles
```
Body:   14px, Weight 400 (Regular)   - Main content
Label:  12px, Weight 500 (Medium)    - Form labels
Small:  12px, Weight 400 (Regular)   - Fine print
Button: 16px, Weight 600 (SemiBold)  - Button text
```

---

## 🌐 LAYOUT CLASSES

### Container
```html
<div class="container">
    <!-- Max-width: 1200px, centered, with padding -->
</div>
```

### Page Structure
```html
<div class="page-container">
    <header>Navigation</header>
    <main class="page-content">Content</main>
    <footer>Footer</footer>
</div>
```

### Form Container
```html
<div class="form-container">
    <!-- Max-width: 400px, centered, with background -->
</div>
```

### Sections
```html
<section class="section">
    <h2 class="section-title">Section Title</h2>
</section>
```

---

## 🎯 FORM PATTERNS

### Sign Up Form Pattern
```html
<form method="POST" class="form-container">
    {% csrf_token %}
    
    <div class="form-header">
        <h1>Create Account</h1>
        <p>Join our community</p>
    </div>
    
    <!-- Form fields here -->
    
    <button type="submit" class="btn btn-primary btn-full">
        Create Account
    </button>
    
    <div class="form-footer">
        Already have account? <a href="#">Log In</a>
    </div>
</form>
```

### Log In Form Pattern
```html
<form method="POST" class="form-container">
    {% csrf_token %}
    
    <div class="form-header">
        <h1>Log In</h1>
        <p>Welcome back</p>
    </div>
    
    <!-- Form fields: username/email, password -->
    
    <button type="submit" class="btn btn-primary btn-full">Log In</button>
    
    <div class="form-footer">
        Don't have account? <a href="#">Sign Up</a>
    </div>
</form>
```

---

## 🏗️ HEADER/NAVIGATION

```html
<header>
    <div class="header-container">
        <a href="/" class="logo">📝 Blog</a>
        <nav>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/about/">About</a></li>
                {% if user.is_authenticated %}
                    <li><a href="/logout/">Log Out</a></li>
                {% else %}
                    <li><a href="/login/">Log In</a></li>
                    <li><a href="/signup/" class="btn btn-primary">Sign Up</a></li>
                {% endif %}
            </ul>
        </nav>
    </div>
</header>
```

---

## 📱 RESPONSIVE BREAKPOINTS

```css
/* Desktop (default) */
/* All components at full size */

/* Tablet (max-width: 768px) */
@media (max-width: 768px) {
    /* Adjusted spacing, possibly single column */
}

/* Mobile (max-width: 480px) */
@media (max-width: 480px) {
    /* Single column, larger touch targets */
    /* Simplified layouts */
}
```

---

## 🎭 INTERACTION STATES

### Button States
```
Default:  Orange (#FF6B35), shadow
Hover:    Darker orange (#E55A2B), larger shadow
Active:   Darkest (#CC5229), no lift
Disabled: Gray (#9CA3AF), no shadow
```

### Input States
```
Default:  White, gray border
Hover:    White, darker border
Focus:    White, orange border, blue shadow
Filled:   White, orange border
Error:    White, red border, red text
Disabled: Light gray, muted text
```

### Link States
```
Default:  Blue (#006BFF), no underline
Hover:    Darker blue (#0052CC), underline
Visited:  Purple (optional)
```

---

## 🔧 UTILITY CLASSES

### Text Alignment
```html
<p class="text-center">Centered text</p>
<p class="text-right">Right-aligned text</p>
```

### Margin Utilities
```html
<div class="mt-sm">Margin-top small (8px)</div>
<div class="mt-md">Margin-top medium (16px)</div>
<div class="mt-lg">Margin-top large (24px)</div>

<div class="mb-sm">Margin-bottom small (8px)</div>
<div class="mb-md">Margin-bottom medium (16px)</div>
<div class="mb-lg">Margin-bottom large (24px)</div>
```

### Visibility
```html
<div class="hidden">Hidden element</div>
<div class="visible">Visible element</div>
```

---

## 🌗 DARK MODE (Future Enhancement)

```css
@media (prefers-color-scheme: dark) {
    :root {
        --white: #1F1F1F;           /* Invert */
        --black: #FFFFFF;           /* Invert */
        --secondary-gray-light: #2D2D2D;
    }
}
```

---

## 🔄 Component Hierarchy

```
Page Container
├── Header/Navigation
├── Messages (Alerts)
├── Main Content
│   ├── Sections
│   │   ├── Form Container
│   │   │   ├── Form Fields
│   │   │   │   ├── Label
│   │   │   │   ├── Input
│   │   │   │   └── Error Message
│   │   │   └── Buttons
│   │   └── Cards
│   │       ├── Card Header
│   │       ├── Card Content
│   │       └── Card Footer
│   └── Text
└── Footer
```

---

## 📋 Component Checklist

When adding a new feature, ensure:
- [ ] Uses existing color palette
- [ ] Uses existing typography scale
- [ ] Uses 8px spacing grid
- [ ] Has hover state (if interactive)
- [ ] Has focus state (if interactive)
- [ ] Has error state (if applicable)
- [ ] Accessible (labels, contrast, etc)
- [ ] Mobile responsive
- [ ] Uses existing CSS classes

---

## 🎯 Common Patterns

### Form Group Pattern
```html
<div class="form-group">
    <label class="form-label form-label-required">Label</label>
    <input class="form-control">
    <span class="form-error">Error message</span>
</div>
```

### Card List Pattern
```html
<div class="section">
    <h2 class="section-title">Posts</h2>
    {% for post in posts %}
        <div class="card">...</div>
    {% endfor %}
</div>
```

### Alert Pattern
```html
<div class="alert alert-success">Success message</div>
<div class="alert alert-error">Error message</div>
```

### Button Group Pattern
```html
<div style="display: flex; gap: var(--spacing-md);">
    <button class="btn btn-primary">Primary</button>
    <button class="btn btn-secondary">Secondary</button>
</div>
```

---

## ✅ Implementation Checklist

- ✅ All colors from palette used
- ✅ Typography hierarchy established
- ✅ 8px grid system followed
- ✅ All interactive states defined
- ✅ Responsive design implemented
- ✅ Accessibility considered
- ✅ Components documented
- ✅ Reusable classes created

---

**This reference sheet covers all components, colors, typography, and patterns in the design system.**

Use this when:
1. Adding new features
2. Creating new pages
3. Building new components
4. Checking design consistency
5. Troubleshooting styles

---

Last Updated: January 2026
