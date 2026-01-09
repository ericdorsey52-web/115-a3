# Django Blog Platform - Figma Design Guide

## 🎨 How to Create Matching Designs in Figma

This guide shows you how to create Figma designs that perfectly align with the Django implementation.

---

## Part 1: Setting Up the Figma File

### Step 1: Create Figma Pages

Create these pages in your Figma file:
1. **Design System** - Color palette and typography
2. **Components** - Reusable UI components
3. **Wireframes** - Low-fidelity layouts
4. **High-Fidelity** - Polished designs
5. **Prototype** - Interactive flows

---

## Part 2: Design System Page

### Colors

Create color styles for:

| Color | Hex Code | Usage |
|---|---|---|
| Primary Orange | #FF6B35 | Buttons, links, CTAs |
| Primary Orange (Hover) | #E55A2B | Hover state |
| Secondary Gray | #4A4A4A | Body text |
| Secondary Gray Light | #F5F5F5 | Backgrounds, light surfaces |
| Accent Blue | #006BFF | Secondary links, accents |
| White | #FFFFFF | Main backgrounds |
| Border Gray | #E0E0E0 | Borders, dividers |
| Dark Text | #1F1F1F | Headings, primary text |

**In Figma:**
1. Create color swatches in a frame
2. Right-click each → "Create component"
3. Go to Assets → Colors
4. Save color styles for reuse

### Typography

Create text styles for:

| Style | Font | Size | Weight | Usage |
|---|---|---|---|---|
| Heading 1 | Inter | 28px | 700 | Page titles |
| Heading 2 | Inter | 18px | 600 | Section titles |
| Body | Inter | 14px | 400 | Main content |
| Label | Inter | 12px | 500 | Form labels |
| Button | Inter | 16px | 600 | Button text |

**In Figma:**
1. Create text layers with these properties
2. Right-click → "Create text style"
3. Go to Assets → Typography
4. Reuse styles across designs

---

## Part 3: Components Page

### 1. Button Component

**Default State:**
1. Create rectangle: 280px × 48px
2. Set fill: Primary Orange (#FF6B35)
3. Set corner radius: 8px
4. Add text: "Button Text"
   - Font: Inter 16px, Weight 600, Color white
5. Add padding: 16px horizontal, 12px vertical
6. Select all → Group (Ctrl+G)
7. Right-click → "Create component"
8. Name: `Button/Primary`

**Hover State:**
1. Duplicate component
2. Change fill to #E55A2B (darker orange)
3. Add shadow: 0px 4px 12px rgba(255, 107, 53, 0.25)
4. Name: `Button/Primary - Hover`

**Secondary Button:**
1. Duplicate primary button
2. Change fill to Light Gray (#F5F5F5)
3. Change text color to Dark Gray (#4A4A4A)
4. Add border: 1px solid #E0E0E0
5. Name: `Button/Secondary`

### 2. Text Input Field

**Default State:**
1. Create rectangle: 280px × 44px
2. Set fill: White (#FFFFFF)
3. Set stroke: 1px, #E0E0E0 (Border Gray)
4. Set corner radius: 6px
5. Add padding using Auto Layout (Shift+A):
   - Horizontal: 12px
   - Vertical: 8px
6. Add text layer inside:
   - Text: "Placeholder text"
   - Font: Inter 14px, Weight 400, Color #9CA3AF
7. Group text + rectangle
8. Create component: `Input/Text Field`

**Focused State:**
1. Duplicate input field
2. Change stroke color to #FF6B35 (Primary Orange)
3. Change stroke width to 2px
4. Add shadow: 0px 0px 0px 3px rgba(255, 107, 53, 0.1)
5. Name: `Input/Text Field - Focused`

**With Label:**
1. Create label above field:
   - Text: "Field Label"
   - Font: Inter 12px, Weight 500, Color #1F1F1F
2. Position 8px above input
3. Select label + input
4. Group (Ctrl+G)
5. Create component: `Input/Text Field with Label`

### 3. Shape Components

**Circle (Avatar)**
1. Create ellipse: 48px × 48px
2. Set fill: Primary Orange (#FF6B35)
3. Set stroke: 2px, Border Gray (#E0E0E0)
4. No corner radius needed (it's a circle)
5. Right-click → "Create component"
6. Name: `Shape/Circle`

**Square (Card)**
1. Create rectangle: 320px × auto
2. Set fill: White (#FFFFFF)
3. Set stroke: 1px, Border Gray (#E0E0E0)
4. Set corner radius: 8px
5. Add padding: 24px
6. Right-click → "Create component"
7. Name: `Shape/Square`

---

## Part 4: Wireframes Page

### Sign Up Wireframe

**Frame Setup:**
1. Create frame: 375px × 812px (mobile)
2. Name: "Sign Up - Wireframe"
3. Fill: White (#FFFFFF)

**Layout Structure:**
```
[Header] 60px
  "Create Account"

[Title] 
  "Sign Up"

[Subtitle]
  "Join us to get started"

[Form Fields] 16px spacing
  [Input Field] Full Name
  [Input Field] Email Address
  [Input Field] Password
  [Input Field] Confirm Password

[Agreement Text]
  "By signing up, you agree to Terms"

[Button]
  "Create Account"

[Link]
  "Already have an account? Log In"
```

**Using Components:**
1. Drag `Input/Text Field with Label` → Duplicate 4 times
2. Update labels for each field
3. Drag `Button/Primary` component
4. Add text labels and links

### Log In Wireframe

**Frame:** 375px × 812px, named "Log In - Wireframe"

**Layout Structure:**
```
[Header]
  "Welcome Back"

[Title]
  "Log In"

[Form Fields]
  [Input Field] Email / Username
  [Input Field] Password

[Link]
  "Forgot your password?"

[Button]
  "Log In"

[Link]
  "Don't have an account? Sign Up"
```

---

## Part 5: High-Fidelity Design

### Sign Up High-Fidelity

**Header** (Gradient)
1. Rectangle: 375px × 80px
2. Fill: Gradient
   - Start: #FF6B35
   - End: #E55A2B
3. Add text: "Create Account"
   - Color: White
   - Size: 18px, Weight 600
   - Center-aligned

**Form Container**
1. Rectangle: 340px wide (centered)
2. Fill: Light Gray (#F5F5F5)
3. Stroke: 1px, Border Gray
4. Corner radius: 8px
5. Padding: 32px

**Inside Form:**
1. Title: "Sign Up" (28px, Weight 700, Dark)
2. Subtitle: "Join our community" (14px, Medium Gray)
3. Form fields (using Input components)
   - Spacing: 16px between fields
4. Agreement checkbox + text
5. Button using `Button/Primary` component
6. Navigation link: "Already have account? Log In"

### Log In High-Fidelity

Same structure as Sign Up but with:
- Title: "Log In"
- Subtitle: "Welcome back"
- Only 2 fields: Email + Password
- "Forgot Password?" link (right-aligned)
- Button: "Log In"
- Link: "Don't have account? Sign Up"

---

## Part 6: Blog Homepage

**Header**
1. Navigation bar with logo, menu items, user info
2. Sticky positioning (stays at top when scrolling)

**Hero Section**
1. Centered text
   - Title: "Welcome to Our Blog" (28px, bold)
   - Subtitle: Description text
   - CTA Button: "Get Started" (Primary)

**Blog Post Cards**
1. Card component: 
   - Header: Avatar + Title + Author + Date
   - Content: Excerpt text
   - Footer: View count + "Read More" link
2. Spacing: 16px between cards
3. Hover state: Slight shadow increase

---

## Part 7: Interactive Prototype

### Connect Sign Up to Log In
1. Select "Sign Up - High Fidelity" frame
2. Click "Prototype" tab
3. Click "Don't have account" link
4. Add interaction: On click → Navigate to "Log In - High Fidelity"

### Connect Log In to Blog Homepage
1. On "Log In" button
2. Add interaction: On click → Navigate to "Blog Homepage - High Fidelity"

### Create User Flow
1. Start → Sign Up → Log In → Blog Home
2. Show this flow in prototype

---

## 🎯 Figma Best Practices for This Project

### Naming Convention
```
[Page]
├── [Section]
│   ├── [Component/Type]
│   └── [Component] - [State]
```

Example:
```
Sign Up
├── Header
│   ├── Title
│   └── Subtitle
├── Form
│   ├── Form/Group 1
│   │   ├── Input/Email
│   │   └── Input/Email - Focused
│   └── Button/Primary
└── Footer
    └── Link/Secondary
```

### Auto Layout Usage

**Forms:**
1. Select form container
2. Press Shift+A (Auto Layout)
3. Direction: Vertical
4. Spacing: 16px

**Buttons:**
1. Select button group
2. Press Shift+A
3. Direction: Horizontal
4. Spacing: 12px
5. Padding: 16px

**Cards:**
1. Header: Horizontal auto layout
2. Content: Vertical auto layout
3. Footer: Horizontal space-between

### Component Variants

Create variants for button states:
1. Right-click component → "Create variants"
2. Add property: "State"
3. Values: Default, Hover, Active, Disabled

---

## 📊 Design Specifications Reference

### Spacing Scale
```
4px   (XSmall) - tight spacing
8px   (Small)  - label spacing
16px  (Medium) - field spacing
24px  (Large)  - section spacing
32px  (XLarge) - major section spacing
```

### Border Radius
```
6px  - Input fields
8px  - Cards, containers
12px - Badges
50%  - Circles, avatars
```

### Shadows
```
Subtle:    0px 1px 3px rgba(0,0,0,0.1)
Medium:    0px 2px 8px rgba(0,0,0,0.15)
Heavy:     0px 4px 12px rgba(0,0,0,0.25)
Focus:     0px 0px 0px 3px rgba(color, 0.1)
```

### Typography Sizes
```
28px - Main headings (H1)
18px - Section headings (H2)
16px - Subheadings, buttons
14px - Body text
12px - Labels, small text
```

---

## ✅ Figma File Checklist

- [ ] All colors added to color styles
- [ ] All typography styles created
- [ ] Button components (primary, secondary, states)
- [ ] Input field components (default, focused, error)
- [ ] Shape components (circle, square)
- [ ] Card component with structure
- [ ] Sign Up wireframe created
- [ ] Log In wireframe created
- [ ] Sign Up high-fidelity design
- [ ] Log In high-fidelity design
- [ ] Blog homepage design
- [ ] Blog detail page design
- [ ] Navigation bar component
- [ ] Alert/message component
- [ ] Prototype flows connected
- [ ] All pages named clearly
- [ ] All components organized in library
- [ ] Design system documented

---

## 🔗 Connecting Design to Development

When developers implement this design:

1. **Colors** → Become CSS variables
2. **Typography** → CSS font rules
3. **Spacing** → CSS padding/margin values
4. **Components** → CSS classes (.btn, .form-control, etc.)
5. **States** → CSS pseudo-classes (:hover, :focus)
6. **Layout** → CSS Grid/Flexbox

**Example:**
- Figma: Button/Primary with 48px height
- CSS: `.btn { min-height: 48px; }`

---

## 📚 Figma Resources

- [Figma Components Guide](https://www.figma.com/blog/components-in-figma/)
- [Creating Design Systems](https://www.figma.com/design-systems/)
- [Figma Prototyping](https://www.figma.com/prototyping/)
- [Figma Best Practices](https://www.figma.com/blog/)

---

**Your Figma file is now ready to hand off to developers!**
