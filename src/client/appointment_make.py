import mysql.connector
from helper import *


class appointment_make:

    def __inti__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*********",
            database="onspot_scheduler",
            auth_plugin='mysql_native_password'
        )

    def create_appointment(self, time, company, date_of_drive, first_name, last_name, reason, phone):
        derma_drive_id = find_derma_drive(self.mydb, company, date_of_drive)
        patient_id = find_specific_person(self.mydb, first_name, last_name, phone)
        mycursor = self.mydb.cursor()
        # todo check if appointment time is taken or not
        sql = 'INSERT INTO appointment (appointment_time, derma_drive_id, patient_id, reason) values (%s, %s, %s, %s)'
        val = (time, derma_drive_id, patient_id, reason)
        try:
            mycursor.execute(sql, val)
        except:
            return #404
        self.mydb.commit()
