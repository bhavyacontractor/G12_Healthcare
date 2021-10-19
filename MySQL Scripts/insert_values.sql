-- Date format is YYYY-MM-DD

INSERT INTO `doctor` (doc_ID,docName,docPassword)
VALUES
('doctor1@hospital.com','Doctor One','docpass1'),
('doctor2@hospital.com','Doctor Two','docpass2'),
('doctor3@hospital.com','Doctor Three','docpass3');


INSERT INTO `TimeSlots` (Doc_ID,Start_Time,End_Time,Appt_Date,Availability)
VALUES
('doctor1@hospital.com','08:00:00','10:00:00','2015-09-13',1),
('doctor1@hospital.com','08:30:00','10:00:00','2015-09-23',1),
('doctor2@hospital.com','07:40:00','09:00:00','2016-05-14',1),
('doctor2@hospital.com','09:20:00','11:00:00','2016-07-03',0),
('doctor3@hospital.com','08:50:00','11:00:00','2014-11-30',1),
('doctor2@hospital.com','10:20:00','11:30:00','2018-03-10',1),
('doctor2@hospital.com','11:00:00','11:40:00','2015-02-09',0),
('doctor1@hospital.com','16:30:00','17:50:00','2016-12-13',1),
('doctor3@hospital.com','9:30:00','10:50:00','2019-05-24',1),
('doctor1@hospital.com','14:00:00','15:40:00','2020-10-25',0);
