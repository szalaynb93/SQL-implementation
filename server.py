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
    actual_keys = ["mentor_first_name", "mentor_last_name", "school_name", "country"]
    to_the_table = queries.mass_executor(queries.show_mentors)
    return render_template("result.html", to_the_table=to_the_table, titles=titles, actual_keys=actual_keys)


@app.route("/all-schools")
def schools_list():
    titles = ["First Name", "Last Name", "School Name", "Country"]
    actual_keys = ["mentor_first_name", "mentor_last_name", "school_name", "country"]
    to_the_table = queries.mass_executor(queries.show_all_schools)
    return render_template("result.html", to_the_table=to_the_table, titles=titles, actual_keys=actual_keys)


@app.route("/mentors-by-country")
def countries_list():
    titles = ["Country", "Number of Mentors"]
    actual_keys = ["country", "count"]
    to_the_table = queries.mass_executor(queries.show_mentors_by_country)
    return render_template("result.html", to_the_table=to_the_table, titles=titles, actual_keys=actual_keys)


@app.route("/contacts")
def contacts_list():
    titles = ["School", "First Name", "Last Name"]    
    actual_keys = ["school", "first_name", "last_name"]
    to_the_table = queries.mass_executor(queries.show_contacts)
    return render_template("result.html", to_the_table=to_the_table, titles=titles, actual_keys=actual_keys)


@app.route("/applicants")
def applicants_list():
    titles = ["First Name", "Application Code", "Creation Date"]
    actual_keys = ["a_first_name", "application_code", "creation_date"]
    to_the_table = queries.mass_executor(queries.show_applicants)
    return render_template("result.html", to_the_table=to_the_table, titles=titles, actual_keys=actual_keys)


@app.route("/applicants-and-mentors")
def connections_list():
    titles = ["Applicant F. Name", "Apllication Code", "Mentor F. Name", "Mentor L. Name"]
    actual_keys = ["applicant_first_name", "application_code", "mentor_first_name", "mentor_last_name"]
    to_the_table = queries.mass_executor(queries.show_applicants_and_mentors)
    return render_template("result.html", to_the_table=to_the_table, titles=titles, actual_keys=actual_keys)


if __name__ == "__main__":
    app.secret_key = "app_magic"  # Change the content of this string
    app.run(
        debug=True,
        port=5000
    )
