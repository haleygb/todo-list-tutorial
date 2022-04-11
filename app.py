from flask import Flask, render_template, request
from helpers import todo

app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0

#We will use the todo_list global variable to keep a list of all created todos. 
# We will use the todo_count to keep track of how
# many todos we have so far and what the next id number should be.

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count
        
        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']

        if title == '':
            return render_template("create-todo.html")

        new_todo: todo = todo(todo_count, title, description, color)
        todo_list.append(new_todo)

        todo_count += 1

        return render_template("success.html", title=title, description=description)
    return render_template("create-todo.html")

@app.route('/view-todo-list', methods=["GET", "POST"])
def view_todo_list():
    if request.method == "POST" and len(todo_list) > 0:
        idx: int = int(request.form['check-button'])
        todo_list[idx].checked = not todo_list[idx].checked
    return render_template('view-list.html', todo_list=todo_list)

@app.route('/edit-todo<todo_number>', methods=["GET", "POST"])
def edit_todo(todo_number: str):
    if request.method == "POST":
        global todo_list

        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']

        if title == '':
            return render_template("edit-todo.html")

        todo_list[int(todo_number)].title = title
        todo_list[int(todo_number)].description = description
        todo_list[int(todo_number)].color = color

        return render_template("edit-success.html")
    return render_template('edit-todo.html', todo=todo_list[int(todo_number)])

if __name__ == '__main__':
    app.run(debug=True)

# storing and fetching of data is what is usually 
# alled backend development. In our program we will do a 
# simple version of this by storing our data in global variables 
# that our app file can access.

