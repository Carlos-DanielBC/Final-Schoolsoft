CREATE DATABASE school_system;
DROP DATABASE school_system;

USE school_system;
insert into school_students(first_name, last_name, birthdate,mail,phone_number,status) VALUES('adrian','Baez',STR_TO_DATE('26-08-2023', '%d-%m-%Y'),'carlosdaniel@gmail.com',8298683654,1);

insert into school_subject(name,start_date,description,level) VALUES('Ingles',STR_TO_DATE('26-08-2023', '%d-%m-%Y'),'asignatura de ingles','medio');

insert into school_course(level,nombre_aula,subject_id_id) VALUES('medio','2A',1);

insert into school_teachers(first_name,last_name,code,id_number) VALUES('Felipe','Rodriguez',14234,42578962351);

insert into school_relationship( Subject_id_id, Teachers_id_id) VALUES(1,1);

insert into school_inscription( date_inscription, pay_status, ref_pay, inscription_status, course_id_id, student_id_id) VALUES(STR_TO_DATE('26-08-2023', '%d-%m-%Y'),1,'referencia de algo',1,1,1);