def id_getter_from_name(db, name, type):
    mycursor = db.cursor()
    mycursor.execute('select * from {} where {}_name like "%{}%"'.format(type, type, name))
    try:
        return mycursor.fetchall()[0][0]
    except IndexError:
        return 'No Company By That Name'

def day_maker(db, derma_drive_id, start_time, end_time):
    mycursor = db.cursor()
    for i in range(start_time, end_time + 1):
        for x in ("00", "15", "30", "45"):
            var = str(str(i) + ":" + str(x))
            sql = "INSERT INTO time_slot (derma_drive_id, time_slot_time) VALUES (%s, %s)"
            val = (derma_drive_id, var)
            mycursor.execute(sql, val)
    db.commit()

def find_derma_drive(db, company_name, date):
    mycursor = db.cursor()
    company_id = id_getter_from_name(db, company_name, "company")
    mycursor.execute('select * from derma_drive where company_id = {}'.format(company_id))
    return mycursor.fetchall()[0][0]

def find_specific_person(db, first_name, last_name, phone):
    mycursor = db.cursor()
    mycursor.execute('select * from patient where patient_first_name = {} '
                     'AND patient_last_name = {}'
                     'AND phone = {}'.format(first_name, last_name, phone))
    return mycursor.fetchall()[0][0]