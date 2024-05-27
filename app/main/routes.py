from flask import render_template, redirect, url_for, flash
from . import main_bp
from .forms import ContactForm


@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Handle the form submission,
        flash("Your message has been sent!", "success")
        return redirect(url_for("main.contact"))
    return render_template("contact.html", form=form)
