# Figma Design to Django Implementation Guide

## 🎯 Purpose

This document explains how the Figma designs map to the Django implementation, helping you understand the relationship between UI/UX design and code.

---

## 📐 Design System Mapping

### Color Palette

**Figma Color System:**
```
Primary Orange:     #FF6B35
Secondary Gray:     #4A4A4A
Accent Blue:        #006BFF
Light Gray:         #F5F5F5
White:              #FFFFFF
Border Gray:        #E0E0E0
Dark Text:          #1F1F1F
```

**CSS Implementation:**
```css
/* See blog/static/css/design_system.css :root */
--primary-orange: #FF6B35;
--secondary-gray: #4A4A4A;
--accent-blue: #006BFF;
/* ... and more */
```

---

## 🎨 UI Component Mapping

### 1. Button Component

**Figma Design:**
- Button/Primary (Orange, 48px height, 16px font)
- Button/Secondary (Gray, white background)
- Hover state: Color darkening + shadow increase
- Focus state: Outline/highlight

**CSS Classes:**
```css
.btn           /* Base button styling */
.btn-primary   /* Orange primary button */
.btn-secondary /* Gray secondary button */
.btn-tertiary  /* Blue link-style button */
```

**HTML Implementation:**
```html
<!-- Sign Up page example -->
<button type="submit" class="btn btn-primary btn-full">
    Create Account
</button>
```

**Figma Features Implemented:**
- ✅ Hover state with shadow
- ✅ Color transitions
- ✅ Disabled state styling
- ✅ Full-width variant

---

### 2. Text Field Component

**Figma Design:**
- Input/Text Field with 44px height
- Label above field (12px, medium weight)
- Focus state: Blue border + shadow
- Error state: Red border + error message
- Placeholder text for guidance

**CSS Classes:**
```css
.form-group      /* Container for label + input */
.form-label      /* Label styling */
.form-control    /* Input field styling */
.form-error      /* Error message styling */
```

**HTML Implementation:**
```html
<div class="form-group">
    <label for="id_email" class="form-label form-label-required">
        Email Address
    </label>
    <input type="email" class="form-control" placeholder="...">
</div>
```

**Figma Features Implemented:**
- ✅ Clear label with required indicator
- ✅ Placeholder text
- ✅ Focus state (blue border)
- ✅ Error state with message display
- ✅ Hover state

---

### 3. Shape Components

#### Circular Shape (Avatar)
**Figma Design:** Circle 48px × 48px, border, optional image

**CSS:**
```css
.shape-circle {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    /* ... styling */
}
```

**Usage:** User avatars, author profiles
```html
<div class="shape-circle primary">
    {{ user.first_name|first }}
</div>
```

#### Square Shape (Card)
**Figma Design:** Rounded square with border, hover shadow

**CSS:**
```css
.shape-square {
    border-radius: 8px;
    border: 1px solid var(--border-gray);
    /* ... styling */
}
```

---

### 4. Card Component

**Figma Design:** Blog post card with header, content, footer

**Structure:**
```
┌─────────────────────────┐
│  TITLE                  │
│  Author • Date          │
├─────────────────────────┤
│  Excerpt content...     │
├─────────────────────────┤
│  Views    [Read More →] │
└─────────────────────────┘
```

**CSS Classes:**
```css
.card         /* Container */
.card-header  /* Title + author info */
.card-title   /* Post title */
.card-content /* Excerpt text */
.card-footer  /* Meta + actions */
```

**HTML Implementation:**
```html
<div class="card">
    <div class="card-header">
        <h3 class="card-title">{{ post.title }}</h3>
        <div class="card-subtitle">By Author • Date</div>
    </div>
    <div class="card-content">{{ post.get_excerpt }}</div>
    <div class="card-footer">
        <span>{{ post.views_count }} views</span>
        <a href="..." class="btn btn-tertiary">Read More →</a>
    </div>
</div>
```

---

## 📄 Page Mapping

### Sign Up Page

**Figma Wireframe:** Sign Up - Wireframe
**Figma High-Fidelity:** Sign Up - High Fidelity

**Structure:**
```
┌──────────────────────┐
│   HEADER             │
│ "Create Account"     │
├──────────────────────┤
│  [Form Container]    │
│  Title: "Sign Up"    │
│  Subtitle            │
│                      │
│  [First Name Input]  │
│  [Last Name Input]   │
│  [Email Input]       │
│  [Username Input]    │
│  [Password Input]    │
│  [Confirm Pwd]       │
│                      │
│  [Create Button]     │
│                      │
│  Link: Log In        │
└──────────────────────┘
```

**Files:**
- Django View: `blog/views.py` → `signup_view()`
- Django Form: `blog/forms.py` → `UserSignUpForm`
- Template: `blog/templates/auth/signup.html`
- CSS: `blog/static/css/design_system.css`

**Component Usage:**
- Form group containers (`.form-group`)
- Text input fields (`.form-control`)
- Primary button (`.btn-primary`)
- Navigation link (`.btn-tertiary`)
- Form container styling (`.form-container`)

---

### Log In Page

**Figma Wireframe:** Log In - Wireframe
**Figma High-Fidelity:** Log In - High Fidelity

**Structure:**
```
┌──────────────────────┐
│   HEADER             │
│ "Welcome Back"       │
├──────────────────────┤
│  [Form Container]    │
│  Title: "Log In"     │
│                      │
│  [Username/Email]    │
│  [Password Input]    │
│                      │
│  [Forgot Password]   │
│                      │
│  [Log In Button]     │
│                      │
│  Link: Sign Up       │
└──────────────────────┘
```

**Files:**
- Django View: `blog/views.py` → `login_view()`
- Django Form: `blog/forms.py` → `UserLoginForm`
- Template: `blog/templates/auth/login.html`

---

### Blog Homepage

**Figma Wireframe:** Blog Homepage - Wireframe
**Figma High-Fidelity:** Blog Homepage - High Fidelity

**Structure:**
```
┌──────────────────────────────┐
│  HEADER / NAVIGATION         │
├──────────────────────────────┤
│  [Hero Section]              │
│  Title + CTA                 │
├──────────────────────────────┤
│  [Blog Post Card 1]          │
│  ┌────────────────────────┐  │
│  │ ●  Title               │  │
│  │    Author • Date       │  │
│  │                        │  │
│  │ Excerpt...             │  │
│  │ Views    [Read More →] │  │
│  └────────────────────────┘  │
│                              │
│  [Blog Post Card 2]          │
│  [Blog Post Card 3]          │
│                              │
└──────────────────────────────┘
```

**Files:**
- Django View: `blog/views.py` → `home_view()`
- Template: `blog/templates/blog/home.html`

**Component Usage:**
- Cards (`.card`)
- Circular avatars (`.shape-circle`)
- Secondary buttons
- Link styling (`.btn-tertiary`)

---

## 🔄 Design-to-Code Workflow

### Example: Creating a New Form Field

**Step 1: Design in Figma**
- Create input field component
- Set styles: height 44px, radius 6px, gray border
- Add focus state: blue border, blue shadow
- Add label: 12px, medium weight

**Step 2: Map to CSS**
```css
.form-label {
    font-size: var(--font-size-label);      /* 12px */
    font-weight: 500;                       /* medium */
    color: var(--black);
}

.form-control {
    padding: var(--spacing-md);             /* 16px */
    border: 1px solid var(--border-gray);
    border-radius: 6px;
    height: 44px;
}

.form-control:focus {
    border-color: var(--primary-orange);
    box-shadow: 0px 0px 0px 3px rgba(255, 107, 53, 0.1);
}
```

**Step 3: Implement in HTML**
```html
<div class="form-group">
    <label class="form-label">Field Label</label>
    <input type="text" class="form-control" placeholder="...">
</div>
```

---

## 📊 Design System Implementation Checklist

### Colors
- ✅ Primary orange for CTAs
- ✅ Gray for secondary text
- ✅ Blue for links
- ✅ Proper hover states (color shift + shadow)
- ✅ Error/success colors (red/green)

### Typography
- ✅ Headlines: 28px, bold
- ✅ Subheadings: 18px, semi-bold
- ✅ Body text: 14px, regular
- ✅ Labels: 12px, medium
- ✅ Buttons: 16px, semi-bold
- ✅ Consistent font family (Inter)

### Spacing
- ✅ 8px grid system
- ✅ Consistent padding in cards
- ✅ Proper margins between sections
- ✅ Field spacing in forms (16px)

### Components
- ✅ Buttons (primary, secondary, tertiary)
- ✅ Input fields with focus states
- ✅ Cards with hover effects
- ✅ Avatars (circular)
- ✅ Navigation
- ✅ Alerts/messages

### Interactivity
- ✅ Hover states
- ✅ Focus states (keyboard navigation)
- ✅ Error states
- ✅ Success/loading messages
- ✅ Disabled states

---

## 🎯 User Story Implementation

### Story 1: Easy Account Creation
**Figma Solution:** Clear Sign Up form with step-by-step fields
**Code Implementation:**
- `signup_view()` in views.py
- `UserSignUpForm` with validation
- Clear form layout with labels
- Success message after creation

### Story 2: Quick Login
**Figma Solution:** Minimal Log In form (2 fields)
**Code Implementation:**
- `login_view()` in views.py
- `UserLoginForm` (username + password only)
- Auto-redirect to home after login
- Error messages for failed attempts

### Story 3: Clear Input Fields
**Figma Solution:** Labeled fields with placeholders
**Code Implementation:**
- `.form-label` with required indicators
- `.form-control` with placeholder text
- `.form-error` for validation feedback
- Focus states for clarity

---

## 🔧 CSS Variables Reference

```css
:root {
    /* Colors */
    --primary-orange: #FF6B35;
    --primary-orange-hover: #E55A2B;
    --accent-blue: #006BFF;
    --white: #FFFFFF;
    --black: #1F1F1F;
    --border-gray: #E0E0E0;
    
    /* Spacing (8px grid) */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    
    /* Typography */
    --font-family: 'Inter', sans-serif;
    --font-size-body: 14px;
    --font-size-label: 12px;
    --font-size-button: 16px;
    --font-size-heading-1: 28px;
    --font-size-heading-2: 18px;
}
```

---

## 📚 Quick Reference

| Figma Component | CSS Class | Usage |
|---|---|---|
| Button Primary | `.btn-primary` | Submit buttons, CTAs |
| Button Secondary | `.btn-secondary` | Cancel, alternative actions |
| Input Field | `.form-control` | All text inputs |
| Label | `.form-label` | Input labels |
| Card | `.card` | Blog post containers |
| Avatar | `.shape-circle` | User avatars |
| Alert | `.alert` | Success/error messages |
| Container | `.container` | Main content wrapper |

---

## 🚀 How to Extend

### Adding a New Component
1. **Design in Figma:** Create component with states
2. **Define in CSS:** Add classes to `design_system.css`
3. **Implement in HTML:** Use in templates
4. **Document:** Add to this guide

### Example: Creating a Badge Component
```css
.badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: var(--font-size-label);
    background-color: var(--primary-orange);
    color: var(--white);
}
```

---

**This guide serves as a bridge between Figma design and Django implementation.**
