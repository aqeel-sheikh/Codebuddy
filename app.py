import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)



conn = sqlite3.connect("codebuddy.db")  # Connects to the database
cursor = conn.cursor()  # Allows executing SQL queries

@app.route("/")
def home():
    return render_template("index.html")

# Notes page route
@app.route("/notes", methods=["GET", "POST"])
def notes():
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()

    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        tags = request.form.get("tags")
        
        if title and content:
            cursor.execute("INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)", (title, content, tags))
            conn.commit()
        
        cursor.close()
        conn.close()
        return redirect("/notes")  #  Redirect prevents duplicate submission issues

    #  Fetch stored notes from database
    notes = cursor.execute("SELECT * FROM notes").fetchall()

    cursor.close()
    conn.close()

    return render_template("notes.html", notes=notes)  #  Send notes to HTML

        
# Syntax Page Route
@app.route("/syntax", methods=["GET", "POST"])
def syntax():
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()

    if request.method == "POST":
        language = request.form.get("language").capitalize()
        code = request.form.get("code")
        description = request.form.get("description")
        tags = request.form.get("tags")

        if language and code:
            cursor.execute("INSERT INTO syntax (language, code, description, tags) VALUES (?, ?, ?, ?)", (language, code, description, tags))
            conn.commit()
        cursor.close()
        conn.close()
        return redirect("/syntax")
    
    syntax = cursor.execute("SELECT * FROM syntax").fetchall()

    cursor.close()
    conn.close()
    return render_template("syntax.html", syntax=syntax) 

# Docs page Route
@app.route("/docs")
def docs():
    return render_template("docs.html")

# Search notes dynamicaly
@app.route("/searchnotes", methods=["POST"])
def dynamic_search():
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()

    query = request.form.get("query")
    results = []
    if not query.split():
        results = cursor.execute("SELECT * FROM notes").fetchall()
    else:
        results = cursor.execute(
            "SELECT * FROM notes WHERE title LIKE ? OR tags LIKE ?", 
            (f"{query}%", f"{query}%")
        ).fetchall()
    
    conn.close()
    
    return render_template("partials/notes_list.html", results=results)  # ✅ Return only filtered notes

# Search syntax Route
@app.route("/searchsyntax", methods=["GET","POST"])
def dynamic_syntax_search():
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()
    
    results = []
    if request.method == "POST":
        langsearch = request.form.get("langsearch").capitalize()                                                                                           
        
        if langsearch:
            results  = cursor.execute("SELECT * FROM syntax WHERE language = ?", (langsearch,)).fetchall()
            
        conn.close()
        return render_template("searchsyntax.html", results=results, Title=langsearch )

# Global Search
@app.route("/search", methods=["GET","POST"])
def search():
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()
    
    if request.method == "POST":
        query = request.form.get("searchQuery")
        
        notes = []
        syntax = []
        if not query.split():
            notes = cursor.execute("SELECT * FROM notes").fetchall()
            syntax = cursor.execute("SELECT * FROM syntax").fetchall()
        else:
            notes = cursor.execute(
            "SELECT * FROM notes WHERE title LIKE ? OR tags LIKE ?", 
            (f"{query}%", f"{query}%")
            ).fetchall()
            
            syntax = cursor.execute(
            "SELECT * FROM syntax WHERE language LIKE ? OR tags LIKE ?", 
            (f"{query}%", f"{query}%")
            ).fetchall()
    
        conn.close()
    
        return render_template("partials/search.html", notes=notes, syntax=syntax)
    else:
        return render_template("search.html")

# Delete Notes
@app.route("/delete_notes/<int:id>")
def delete_notes(id):
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect('/notes')

# Edit Notes Route
@app.route("/edit_notes/<int:id>", methods=["GET", "POST"])
def edit_notes(id):
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()
    
    if request.method == "POST":
        
        title = request.form.get("title")
        content = request.form.get("content")
        tags = request.form.get("tags")

        if title and content:
            cursor.execute("UPDATE notes SET title = ?, content = ?, tags = ?  WHERE id = ?",
                            (title, content, tags, id))
            conn.commit()
            conn.close()
            return redirect("/notes")
        else:
            notes = cursor.execute("SELECT * FROM notes WHERE id = ?", (id,)).fetchall()
            conn.close()
            return render_template("edit_notes.html", notes=notes, id=id )
    else:
        notes = cursor.execute("SELECT * FROM notes WHERE id = ?", (id,)).fetchall()
        conn.close()
        return render_template("edit_notes.html", notes=notes, id=id )

# Delete Syntax
@app.route("/delete_syntax/<int:id>")
def del_syntax(id):
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM syntax WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/syntax")

# Edit syntax Route
@app.route("/edit_syntax/<int:id>", methods=["GET", "POST"])
def edit_syntax(id):
    conn = sqlite3.connect("codebuddy.db")
    cursor = conn.cursor()

    if request.method == "POST":
        lang = request.form.get("language")
        code = request.form.get("code")
        description = request.form.get("description")
        tags = request.form.get("tags")

        cursor.execute("UPDATE syntax SET language = ?, code = ?, description = ?, tags = ? WHERE id = ?",
                       (lang, code, description, tags, id))
        conn.commit()
        conn.close()
        return redirect("/syntax")
    else:
        syntax = cursor.execute("SELECT * FROM syntax WHERE id = ?", (id,)).fetchall()
        conn.close()
        return render_template("edit_syntax.html", syntax=syntax, id=id)

if __name__ == "__main__":
    app.run(debug=True)
