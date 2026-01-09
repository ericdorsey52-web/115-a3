# 🚀 Quick Start Guide

## 5-Minute Setup

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Database
```bash
python manage.py migrate
```

### Step 3: Create Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts to create a username, email, and password.

### Step 4: Run Development Server
```bash
python manage.py runserver
```

### Step 5: Open in Browser
```
http://127.0.0.1:8000
```

---

## 🧪 Test the Application

### Create a New User
1. Click **"Sign Up"** in navigation
2. Fill in form fields:
   - First Name: `John`
   - Last Name: `Doe`
   - Email: `john@example.com`
   - Username: `johndoe`
   - Password: `SecurePass123!`
   - Confirm: `SecurePass123!`
3. Click **"Create Account"**
4. You'll be automatically logged in and redirected to home

### Create a Blog Post
1. Click **"Create Post"** (requires login)
2. Fill in:
   - Title: `My First Blog Post`
   - Summary: `A brief intro`
   - Content: `Full blog post content here...`
3. Click **"Publish Post"**
4. Post appears on homepage

### View Admin Panel
1. Go to `http://127.0.0.1:8000/admin/`
2. Log in with superuser credentials
3. View and manage users, posts, profiles

---

## 📂 Project Structure at a Glance

```
blog_project/
├── blog/                       # Main app
│   ├── models.py               # Database models
│   ├── views.py                # Page logic
│   ├── forms.py                # Form validation
│   ├── templates/              # HTML files
│   │   ├── auth/               # Sign Up & Log In
│   │   ├── blog/               # Blog pages
│   │   └── pages/              # Static pages
│   └── static/css/
│       └── design_system.css    # All styles
└── README.md                   # Full documentation
```

---

## 🎨 Key Files

### `design_system.css` ⭐ MOST IMPORTANT
Contains all styling for:
- Colors (#FF6B35 orange, #006BFF blue, etc)
- Buttons (.btn-primary, .btn-secondary)
- Forms (.form-control, .form-label)
- Cards (.card)
- Alerts (.alert)

**To change styling, edit this file.**

### `views.py` - Page Logic
Functions that handle:
- `signup_view()` - User registration
- `login_view()` - User login
- `home_view()` - Blog homepage
- `create_blog_view()` - Create posts

**To add new pages, add functions here.**

### Templates
- `auth/signup.html` - Sign Up page
- `auth/login.html` - Log In page
- `blog/home.html` - Homepage
- `blog/detail.html` - Blog post page

**To change appearance, edit these files.**

---

## 🔗 Important URLs

| URL | Purpose |
|---|---|
| `/` | Blog homepage |
| `/signup/` | Sign up form |
| `/login/` | Login form |
| `/logout/` | Log out |
| `/create/` | Create blog post |
| `/post/1/` | View blog post #1 |
| `/about/` | About page |
| `/admin/` | Admin panel |

---

## 🎯 Common Tasks

### Add a New Page
1. Create view function in `views.py`
2. Create template in `templates/`
3. Add URL to `urls.py`
4. Add navigation link in `base.html`

### Change Colors
1. Open `blog/static/css/design_system.css`
2. Update CSS variables in `:root {}`
3. All pages automatically update

### Modify Form Fields
1. Edit `forms.py` - Define fields and labels
2. Edit template - Update form HTML
3. Test form submission

### Add Database Field
1. Add field to model in `models.py`
2. Create migration: `python manage.py makemigrations`
3. Apply migration: `python manage.py migrate`
4. Update forms and templates

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

### Database Error
```bash
# Reset database
python manage.py migrate
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic
```

### Import Error
```bash
# Make sure all requirements are installed
pip install -r requirements.txt
```

---

## 📚 Documentation Map

- **README.md** - Full project overview
- **DOCUMENTATION_INDEX.md** - Documentation guide
- **FIGMA_DESIGN_GUIDE.md** - Design system explanation
- **FIGMA_CREATION_GUIDE.md** - How to create Figma designs
- **COMPONENT_REFERENCE.md** - All components, colors, styles
- **QUICK_START.md** - This file (quick reference)

---

## 💡 Pro Tips

1. **Use Chrome DevTools** (F12) to inspect and test styles
2. **Comments in code** explain Figma mappings and user stories
3. **View source** to see how components are combined
4. **Test forms** with validation errors to see error states
5. **Check admin panel** to manage data directly

---

## 🎓 Learning Path

1. **Start:** View homepage at `/`
2. **Try:** Sign up with new user
3. **Explore:** Log in and create post
4. **Study:** Read `design_system.css` comments
5. **Understand:** Review views.py functions
6. **Create:** Add your own features

---

## 📞 Quick Help

**Can't remember a CSS class?**
→ Check `COMPONENT_REFERENCE.md`

**Don't know which file to edit?**
→ Check `DOCUMENTATION_INDEX.md`

**Need to change styling?**
→ Edit `design_system.css`

**Want to add new page?**
→ Follow steps in README.md

**Stuck on something?**
→ Search code comments for explanations

---

## ✅ Checklist - Running Project

- [ ] Python installed
- [ ] requirements.txt installed (`pip install -r requirements.txt`)
- [ ] Database migrated (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)
- [ ] Server running (`python manage.py runserver`)
- [ ] Can access http://127.0.0.1:8000
- [ ] Can sign up new user
- [ ] Can create blog post
- [ ] Can view admin panel

---

## 🚀 Next Steps

**Easy Additions:**
- [ ] Add more form fields
- [ ] Change colors in design_system.css
- [ ] Create new pages
- [ ] Add comments system
- [ ] Add user profiles

**Medium Difficulty:**
- [ ] Add email verification
- [ ] Add search functionality
- [ ] Add tags/categories
- [ ] Add post editing
- [ ] Add pagination

**Advanced:**
- [ ] Create REST API
- [ ] Add JavaScript interactivity
- [ ] Implement caching
- [ ] Add deployment
- [ ] Set up CI/CD

---

## 🎨 Figma & Design

This project includes Figma design guides:
- **FIGMA_CREATION_GUIDE.md** - How to create matching designs
- **FIGMA_DESIGN_GUIDE.md** - How code maps to design

Figma colors used:
- **Orange:** #FF6B35 (main buttons)
- **Blue:** #006BFF (links)
- **Gray:** #4A4A4A (text)

---

**You're all set! 🎉**

The project is ready to run. Start with the homepage, try signing up, create a post, and explore the code!

Questions? Check the other documentation files - they have detailed explanations of every part.
