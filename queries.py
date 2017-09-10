import database_common


# if __name__ == __main__:


show_mentors = """SELECT mentors.first_name AS mentor_first_name, mentors.last_name AS mentor_last_name,
                                schools.name AS school_name, schools.country AS country FROM mentors
                                JOIN schools ON mentors.city = schools.city
                                ORDER BY mentors.id ASC"""

show_all_schools = """SELECT mentors.first_name AS mentor_first_name, mentors.last_name AS mentor_last_name,
                                schools.name AS school_name, schools.country AS country FROM mentors
                                FULL JOIN schools ON mentors.city = schools.city
                                ORDER BY mentors.id ASC"""

show_mentors_by_country = """SELECT schools.country AS country, COUNT(mentors.id) AS count FROM mentors
                            JOIN schools ON mentors.city = schools.city
                            GROUP BY schools.country
                            ORDER BY schools.country ASC"""

show_contacts = """SELECT DISTINCT schools.name AS school, mentors.first_name AS first_name,
                    mentors.last_name AS last_name FROM schools
                    LEFT JOIN mentors ON schools.contact_person = mentors.id
                    ORDER BY schools.name"""

show_applicants = """SELECT applicants.first_name AS a_first_name, applicants.application_code AS application_code,
                                applicants_mentors.creation_date AS creation_date FROM applicants
                                JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                                WHERE applicants_mentors.creation_date >= '2016-01-01'
                                ORDER BY applicants_mentors.creation_date DESC"""

show_applicants_and_mentors = """SELECT applicants.first_name AS applicant_first_name,
                            applicants.application_code AS application_code,
                            mentors.first_name AS mentor_first_name,
                            mentors.last_name AS mentor_last_name
                            FROM applicants_mentors
                            FULL JOIN applicants ON applicants_mentors.applicant_id = applicants.id
                            FULL JOIN mentors ON applicants_mentors.mentor_id = mentors.id"""

# Az uccsóhoz: "In this case use the string "No data" instead of the
# mentor name."


@database_common.connection_handler
def mass_executor(cursor, sql_query):
    cursor.execute(sql_query)
    answer = cursor.fetchall()
    return answer
