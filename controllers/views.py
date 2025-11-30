from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.modelo import db, Task

bp = Blueprint("tasks", __name__)

@bp.route("/")
def index():
    q = request.args.get("q", "")
    priority = request.args.get("priority", "")

    tasks = Task.query

    if q:
        tasks = tasks.filter(Task.title.ilike(f"%{q}%"))
    if priority:
        tasks = tasks.filter_by(priority=priority)

    tasks = tasks.order_by(Task.created_at.desc()).all()

    return render_template("index.html", tasks=tasks, q=q, priority=priority)


@bp.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        title = request.form["title"]

        if not title:
            flash("O título é obrigatório!")
            return redirect(url_for("tasks.new"))

        task = Task(
            title=title,
            description=request.form.get("description"),
            priority=request.form.get("priority"),
            due_date=request.form.get("due_date"),
        )

        db.session.add(task)
        db.session.commit()

        return redirect(url_for("tasks.index"))

    return render_template("form.html", task=None)


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    task = Task.query.get_or_404(id)

    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form.get("description")
        task.priority = request.form.get("priority")
        task.due_date = request.form.get("due_date")

        db.session.commit()
        return redirect(url_for("tasks.index"))

    return render_template("form.html", task=task)


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks.index"))


@bp.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    task = Task.query.get_or_404(id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("tasks.index"))
