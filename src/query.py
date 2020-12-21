import mysql.connector
from helper import *

class admin_connection:

  def __init__(self):
    self.mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    database="onspot_scheduler",
    auth_plugin='mysql_native_password'
  )

  def create_company(self, company, address):

    mycursor = self.mydb.cursor()
    sql = "insert into company (company_name, address) values (%s, %s)"
    val = (company, address)
    mycursor.execute(sql, val)
    self.mydb.commit()

  def create_patient(self,
                     company, first_name, last_name, email, dob, member_id,
                     group_id, provider_name, phone, note=None):
    mycursor = self.mydb.cursor()
    sql = "INSERT INTO PATIENT (patient_first_name, patient_last_name, email, phone, dob, note) " \
          "values (%s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, email, phone, dob, note)
    mycursor.execute(sql, val)
    self.mydb.commit()
    patient_id = mycursor.lastrowid
    self.add_insurance(patient_id, member_id, group_id, provider_name)
    self.add_patient_company_join(patient_id, company)


  def add_provider(self, provider_name):
    mycursor = self.mydb.cursor()
    mycursor.execute("INSERT INTO provider (provider_name) VALUES ({})".format("\"" + provider_name + "\""))
    self.mydb.commit()

  def add_insurance(self, patient_id, member_id, group_id, provider_name):
    mycursor = self.mydb.cursor()
    provider_id = id_getter_from_name(self.mydb, provider_name, "provider")
    sql = "INSERT INTO insurance () VALUES (%s, %s, %s, %s)"
    val = (patient_id, member_id, group_id, provider_id)
    mycursor.execute(sql, val)
    self.mydb.commit()

  def create_doctor(self, doctor_name):
    mycursor = self.mydb.cursor()
    sql = "INSERT INTO doctor (doctor_name) values ({})".format("\"" + doctor_name + "\"")
    mycursor.execute(sql)
    self.mydb.commit()

  def add_patient_company_join(self, patient_id, company_name):
    mycursor = self.mydb.cursor()
    company_id = id_getter_from_name(self.mydb, company_name, "company")
    sql = "INSERT INTO patient_has_community (patient_id, company_id) VALUES (%s, %s)"
    val = (patient_id, company_id)
    mycursor.execute(sql, val)
    self.mydb.commit()

  def add_derma_drive(self, company_name, drive_date):
    mycursor = self.mydb.cursor()
    company_id = id_getter_from_name(self.mydb, company_name, "company")
    sql = "INSERT INTO derma_drive (company_id, derma_drive_date) VALUES (%s, %s, %s, %s)"
    val = (company_id, drive_date)
    mycursor.execute(sql, val)
    self.mydb.commit()

  def add_head_contact(self, contact_name, company_name, email=None, note=None, phone=None):
    mycursor = self.mydb.cursor()
    company_id = id_getter_from_name(self.mydb, company_name, "company")
    sql = "INSERT INTO head_contact (contact_name, email, phone, company_id, notes) VALUES (%s, %s, %s, %s, %s)"
    val = (contact_name, email, phone, company_id, note)
    mycursor.execute(sql, val)
    self.mydb.commit()

  def add_derma_drive(self, company_name, derma_drive_date, start_time, end_time):
    mycursor = self.mydb.cursor()
    company_id = id_getter_from_name(self.mydb, company_name, "company")
    sql = "INSERT INTO derma_drive (company_id, derma_drive_date) values (%s, %s)"
    val = (company_id, derma_drive_date)
    mycursor.execute(sql, val)
    day_maker(self.mydb, mycursor.lastrowid, start_time, end_time)
    self.mydb.commit()



