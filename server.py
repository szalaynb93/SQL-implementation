from flask import Flask, render_template, redirect, request, session
import queries
from operator import itemgetter

app = Flask(__name__)


@app.route("/")
def route_list():
    return render_template("main_page.html")


@app.route("/mentors")
def mentors_list():
    titles = ["First Name", "Last Name", "School Name", "Country"]
    #titles = ["mentors.first_name", "mentors.last_name", "schools.name", "schools.country"]
    to_the_table = queries.mass_executor(queries.show_mentors)
    return render_template("result.html", to_the_table=to_the_table, titles=titles)


@app.route("/all-schools")
def schools_list():
    titles = ["First Name", "Last Name", "School Name", "Country"]
    #titles = [mentors.first_name , mentors.last_name,schools.name, schools.country]
    to_the_table = queries.mass_executor(queries.show_all_schools)
    return render_template("result.html", to_the_table=to_the_table, titles=titles)


@app.route("/mentors-by-country")
def countries_list():
    titles = ["Country", "Number of Mentors"]
    #titles = [schools.country, count]
    to_the_table = queries.mass_executor(queries.show_mentors_by_country)
    return render_template("result.html", to_the_table=to_the_table, titles=titles)


@app.route("/contacts")
def contacts_list():
    titles = ["School", "First Name", "Last Name"]    
    #schools.name, mentors.first_name, mentors.last_name
    to_the_table = queries.mass_executor(queries.show_contacts)
    return render_template("result.html", to_the_table=to_the_table, titles=titles)


@app.route("/applicants")
def applicants_list():
    titles = ["First Name", "Application Code", "Creation Date"]
    #applicants.first_name, applicants.application_code, applicants_mentors.creation_date
    to_the_table = queries.mass_executor(queries.show_applicants)
    return render_template("result.html", to_the_table=to_the_table, titles=titles)


@app.route("/applicants-and-mentors")
def connections_list():
    titles = ["Applicant F. Name", "Apllication Code", "Mentor F. Name", "Mentor L. Name"]
    #applicant_first_name, applicants.application_code, mentor_first_name, mentor_last_name
    to_the_table = queries.mass_executor(queries.show_applicants_and_mentors)
    return render_template("result.html", to_the_table=to_the_table, titles=titles)


if __name__ == "__main__":
    app.secret_key = "app_magic"  # Change the content of this string
    app.run(
        debug=True,
        port=5000
    )
