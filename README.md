# 🧠 CodeBuddy

**Final Project for Harvard’s CS50x**

🎥 [Watch Project Demo](https://youtu.be/m5QskIofLx4)

## 🧠 Description

**CodeBuddy** is a personal productivity tool built to help developers manage and organize their notes, code snippets, and documentation access—all in one place. The goal was to reduce context-switching and help coders stay focused while working on projects by bringing frequently used information and references into a single streamlined interface.

This web application allows users to:
- Store, edit, and delete personal notes
- Save reusable code snippets with language tags
- Search dynamically through notes and code
- Access official documentation for popular programming languages
- Search all saved content using a global search feature

CodeBuddy is built for developers, by a developer—focused on simplicity, speed, and real productivity.

---

## 📁 Project Structure and File Overview

The project is composed of the following key components:

### `app.py`
This is the main entry point of the Flask application. It initializes the app, sets up routes, handles request/response logic, and links templates to URLs. All CRUD operations (Create, Read, Update, Delete) for notes and code are defined here.

### `templates/`
This folder contains the Jinja2-based HTML templates for each page of the app:
- `index.html`: Homepage of CodeBuddy with navigation and general layout
- `notes.html`: UI for saving, editing, deleting, and searching personal notes
- `syntax.html`: Dedicated page for managing code snippets (syntax memory)
- `docs.html`: Displays official documentation links for quick reference
- `search.html`: Global search page to look up any saved notes or code snippets

- The `layout.html` file serves as the base template for all other pages in CodeBuddy, defining the overall structure of the
  site including the navigation bar, shared styles, and main content block that gets dynamically filled by child templates
  using Jinja’s templating engine. This approach ensures consistency across pages and promotes DRY (Don't Repeat Yourself)
  coding practices.

- There are many more templates used like for dynamic search, edit pages etc...

### `static/`
Contains CSS and JavaScript files:
- `style.css`: Responsible for the visual design, layout, and responsive styling

## 🛠️ Features and Functionality

### 📒 Notes Page
- Save plain text notes
- Edit or delete saved notes
- Real-time search: Filter through notes dynamically by typing into the search bar. The filter works with titles or tags for faster access.

### 🧾 Syntax Page (Code Snippets)
- Save code snippets for future use
- Associate each snippet with a language name (e.g., Python, JavaScript)
- Edit/delete existing snippets
- Live search filters snippets based on programming language

This feature is particularly useful when you need to reuse commonly written logic like regex, API boilerplates, or utility functions.

### 📚 Docs Page
- Quick access to official documentation for:
  - Python
  - JavaScript
  - HTML
  - CSS
- Easy to add more docs if needed
- Clicking a link opens the official site in a new tab

This page helps avoid Googling every time by keeping official docs just one click away.

### 🔎 Global Search Page
- Search through **all** saved notes and code snippets
- Filters display results in two separate sections:
  - Matched Notes
  - Matched Code Snippets
- Search by title, tag, or language keyword

---

## 🧠 Design Decisions

### Why Flask?
Flask was chosen for its simplicity and flexibility. It made it easy to quickly spin up routes, work with templates, and structure the app without overcomplicating things. It's also beginner-friendly and lightweight, perfect for a solo developer project.

### Dynamic Search
CodeBuddy includes a powerful, lightweight dynamic search feature that filters your saved notes and code snippets in real-time. Instead of relying on external libraries, this feature is fully implemented using vanilla JavaScript and Flask routes, giving you full control over the behavior.

### No Database (for now)
For simplicity and demo purposes, the project may rely on in-memory storage or JSON files instead of a full database. This allows the app to run quickly without any setup. However, the code can be easily adapted to use SQLite or PostgreSQL for persistence.

### Minimalist UI
The user interface is designed to be distraction-free. The focus was to give just what’s needed—no more, no less. CSS handles layout with a modern but basic design, using flex/grid for responsive elements.

---

## 🧪 Challenges Faced

- **Routing and Templates:** Connecting multiple templates and ensuring data consistency across them was a bit tricky in the beginning.
- **Live Filtering:** Implementing dynamic search in vanilla JavaScript and linking it with DOM elements required careful attention.
- **Data Structure Management:** Ensuring CRUD operations were seamless and not buggy—especially when editing items dynamically—required debugging and logical planning.

---

## ✅ Future Improvements

- Add user authentication so that multiple users can have private dashboards
- Integrate a backend database (like SQLite or PostgreSQL) for persistent storage
- Allow syntax highlighting for saved code snippets
- Add tags/categories for better filtering
- Enable export/import options for notes and code

---

## 💡 Summary

CodeBuddy is a compact yet powerful tool that helps developers organize their thoughts and code more efficiently. It supports CRUD operations for both notes and code, includes real-time search, and links to documentation—all within a clean, unified interface. It’s an ideal side project to practice backend skills, improve frontend interactivity, and build something genuinely useful.

---
## 📄 License
This project is licensed under the [MIT License](LICENSE)

---

Author **Aqeel Sheikh** as the final project for CS50x 🧑‍💻
