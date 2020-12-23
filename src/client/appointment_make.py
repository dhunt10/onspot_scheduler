import mysql.connector
from helper import *


class appointment_make:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="**********",
            database="onspot_scheduler",
            auth_plugin='mysql_native_password'
        )

    def create_appointment(self, time, company, date_of_drive, first_name, last_name, reason, phone):
        if is_appointment_full(self.mydb, company, date_of_drive, time):
            return "Not a valid appointment time"
        else:
            derma_drive_id = find_derma_drive(self.mydb, company, date_of_drive)
            patient_id = find_specific_person(self.mydb, first_name, last_name, phone)
            fill_time_slot(self.mydb, derma_drive_id, patient_id, time)
            mycursor = self.mydb.cursor()
            sql = 'INSERT INTO appointment (appointment_time, derma_drive_id, patient_id, reason) values (%s, %s, %s, %s)'
            val = (time, derma_drive_id, patient_id, reason)
            mycursor.execute(sql, val)
            self.mydb.commit()
