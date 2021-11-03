-- Date format is YYYY-MM-DD

INSERT INTO `doctor` (doc_ID,docName,doc_s,docPassword)
VALUES
('doctor1@hospital.com','Doctor One','Physician','docpass1'),
('doctor2@hospital.com','Doctor Two','Obstetrician','docpass2'),
('doctor3@hospital.com','Doctor Three','Psychiatrist','docpass3'),
('doctor4@hospital.com','Doctor Four','Physician','docpass4'),
('doctor5@hospital.com','Doctor Five','Physician','docpass5');


INSERT INTO `TimeSlots` (Doc_ID,Start_Time,End_Time,Appt_Date,Availability)
VALUES
('doctor1@hospital.com','08:00:00','10:00:00','2021-11-05',1),
('doctor1@hospital.com','08:30:00','10:00:00','2021-11-03',1),
('doctor2@hospital.com','07:40:00','09:00:00','2021-11-05',1),
('doctor2@hospital.com','09:20:00','11:00:00','2021-11-03',0),
('doctor3@hospital.com','08:50:00','11:00:00','2021-11-04',1),
('doctor2@hospital.com','10:20:00','11:30:00','2021-11-05',1),
('doctor2@hospital.com','11:00:00','11:40:00','2021-11-03',0),
('doctor1@hospital.com','16:30:00','17:50:00','2021-11-05',1),
('doctor3@hospital.com','9:30:00','10:50:00','2021-11-03',1),
('doctor1@hospital.com','14:00:00','15:40:00','2021-11-04',0);

INSERT INTO `TimeSlots` (Doc_ID,Start_Time,End_Time,Appt_Date,Availability)
VALUES
('doctor1@hospital.com','08:00:00','10:00:00','2021-11-05',1),
('doctor1@hospital.com','08:30:00','10:00:00','2021-11-03',1),
('doctor2@hospital.com','07:40:00','09:00:00','2021-11-03',1),
('doctor2@hospital.com','09:20:00','11:00:00','2021-11-04',0),
('doctor3@hospital.com','08:50:00','11:00:00','2021-11-05',1),
('doctor2@hospital.com','10:20:00','11:30:00','2021-11-04',1),
('doctor1@hospital.com','05:00:00','17:00:00','2021-11-05',1),
('doctor1@hospital.com','11:30:00','12:00:00','2021-11-04',1),
('doctor2@hospital.com','16:40:00','20:00:00','2021-11-05',1),
('doctor2@hospital.com','15:20:00','17:00:00','2021-11-03',0),
('doctor3@hospital.com','13:50:00','14:40:00','2021-11-03',1),
('doctor2@hospital.com','17:20:00','18:30:00','2021-11-04',1);

INSERT INTO `TimeSlots` (Doc_ID,Start_Time,End_Time,Appt_Date,Availability)
VALUES
('doctor1@hospital.com','08:00:00','10:00:00','2021-10-30',1),
('doctor1@hospital.com','08:30:00','10:00:00','2021-10-30',1),
('doctor2@hospital.com','07:40:00','09:00:00','2021-10-31',1),
('doctor2@hospital.com','09:20:00','11:00:00','2021-11-01',0),
('doctor3@hospital.com','08:50:00','11:00:00','2021-11-01',1),
('doctor2@hospital.com','10:20:00','11:30:00','2021-10-30',1),
('doctor1@hospital.com','05:00:00','17:00:00','2021-10-31',1),
('doctor1@hospital.com','11:30:00','12:00:00','2021-11-01',1),
('doctor2@hospital.com','16:40:00','20:00:00','2021-10-30',1),
('doctor2@hospital.com','15:20:00','17:00:00','2021-11-01',0),
('doctor3@hospital.com','13:50:00','14:40:00','2021-10-31',1),
('doctor2@hospital.com','17:20:00','18:30:00','2021-11-01',1);

INSERT INTO `User` (UserID,UserName,UserPassword)
VALUES
(1,'user 1',1231),
(2,'user 2',1232),
(3,'user 3',1233);




