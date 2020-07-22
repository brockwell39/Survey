import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    name = request.form.get("firstname")
    surname = request.form.get("surname")
    email = request.form.get("email")
    registered = request.form.get("registered")
    a7f = request.form.get("sel1")
    a14f = request.form.get("sel2")
    a21f = request.form.get("sel3")

    if name == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if surname == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if email == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if registered == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if a7f == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if a14f == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if a21f == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")

    with open('survey.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, email, registered, a7f, a14f, a21f])

    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():

    f_html = open('templates/sheet.html', 'w')
    with open('survey.csv', 'r',) as file:
        reader = csv.reader(file)
        f_html.write('{% extends "layout.html" %}\n\n{% block main %}')
        f_html.write('<table class="table">\n<tbody>\n')
        for row in reader:
            f_html.write('<tr>\n') # Create a new row in the table
            for column in row: # For each column..
                f_html.write('<td>' + column + '</td>')
            f_html.write('</tr>\n')
        f_html.write("</tbody></table>\n")
        f_html.write("{% endblock %}")
        f_html.close
        f_html = open('templates/sheet.html','r')
    return render_template("sheet.html")
