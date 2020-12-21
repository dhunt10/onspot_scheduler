drop database if exists onspot_scheduler;
create database onspot_scheduler;

use onspot_scheduler;

drop table if exists company;
create table company (
	company_id int primary key auto_increment not null,
    company_name VARCHAR(50) NOT NULL,
    address varchar(200) not null
);

drop table if exists provider;
create table provider (
	provider_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    provider_name VARCHAR(50)
);

drop table if exists patient;
create table patient (
	patient_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    patient_first_name VARCHAR(50) NOT NULL,
    patient_last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(15) NOT NULL,
    dob DATE NOT NULL,
    note VARCHAR(200)
);

drop table if exists insurance;
create table insurance (
	patient_id INT,
    member_id VARCHAR(50),
    group_id VARCHAR(50),
    provider_id INT,
	constraint provider_id foreign key (provider_id)
		references provider(provider_id),
	constraint patient_id_insurance foreign key (patient_id)
		references patient(patient_id)
);

drop table if exists doctor;
create table doctor (
	doctor_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    doctor_name VARCHAR(50)
);

drop table if exists patient_has_community;
create table patient_has_community (
	patient_id INT,
    company_id INT,
    constraint patient_id foreign key (patient_id)
		references patient(patient_id),
	constraint company_id foreign key (company_id)
		references company(company_id)
);

drop table if exists head_contact;
create table head_contact (
	contact_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    contact_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    company_id INT,
    notes VARCHAR(200),
    constraint company foreign key (company_id)
		references company(company_id)
);

drop table if exists derma_drive;
create table derma_drive (
	derma_drive_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	company_id INT NOT NULL,
    derma_drive_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    constraint company_2 foreign key (company_id)
		references company(company_id)
);

drop table if exists appointment;
create table appointment (
	appointment_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    appointment_time TIME,
    derma_drive_id INT,
    patient_id INT,
    reason VARCHAR(255),
	constraint patient_id_2 foreign key (patient_id)
		references patient(patient_id),
	constraint derma_drive foreign key (derma_drive_id)
		references derma_drive(derma_drive_id)
);

drop table if exists visit;
create table visit (
	visit_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    appointment_id INT,
    visit_notes varchar(1000) NOT NULL
);

drop table if exists billing;
create table billing (
	visit_id INT,
    billing_code VARCHAR(10),
	label VARCHAR(50),
    constraint visit foreign key (visit_id)
		references visit(visit_id)
);

drop table if exists patient_saw_provider;
create table patient_saw_provider (
	visit_id INT,
    doctor_id INT,
    constraint doctor_id foreign key (doctor_id)
		references doctor(doctor_id),
	constraint visit_id foreign key (visit_id)
		references visit(visit_id)
);

drop table if exists time_slot;
create table time_slot (
	derma_drive_id INT NOT NULL,
    time_slot_time TIME NOT NULL,
    patient_id INT,
    constraint derm_drive_id foreign key (derma_drive_id)
		references derma_drive(derma_drive_id),
	constraint pat_id foreign key (patient_id)
		references patient(patient_id)
);
-- company, patient, patient_has_community, visit, doctor, lifetsyle_director, derma_drive, health_insurance, APPOINTMENTS, providers

insert into provider (provider_name) values
("Humana");

insert into company (company_name, address) values
("Facebook", "105 reservation road andover ma 01810");


insert into patient values
(1, 'Darin Hunt', 'hunt.dar@northeastern.edu', '9788065045', '1998-03-10', "Fat");


SELECT LAST_INSERT_ID();
select * from provider;

select * from company;

insert into company (company_name, address) values
('paseo', '105 reservation road andover ma 01810');

insert into doctor (doctor_name) values 
('Dr. Camisa');

select * from company where company_name like "%PASEO%";

select * from doctor;
select * from derma_drive;
