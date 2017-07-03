from app import app
from flask import render_template
from flask import redirect, request, flash, url_for
from app.models import Todo
from app.forms import AddTodoForm

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    todo = Todo.objects(id=todo_id)[0]
    todo.status = 0
    todo.save()
    todos = Todo.objects()
    return render_template('index.html', todos=todos)


@app.route('/done/<string:todo_id>')
def done(todo_id):
    todo = Todo.objects(id=todo_id)[0]
    todo.status = 1
    todo.save()
    todos = Todo.objects()
    return render_template('index.html', todos=todos)


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.objects(id=todo_id)[0]
    Todo.delete(todo)
    todos = Todo.objects()
    return render_template('index.html', todos=todos)


@app.route('/')
def index():
    todos = Todo.objects()
    return render_template("index.html", todos=todos)


@app.route('/addTodo')
def addTodo():
    return add()


@app.route('/add', methods=['GET','POST'])
def add():
    form = AddTodoForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = Todo(content=form.content.data, time=form.time.data, status=form.status.data)
        todo.save()
        flash('success')
        return redirect('/')
    return render_template('add.html', form=form)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'