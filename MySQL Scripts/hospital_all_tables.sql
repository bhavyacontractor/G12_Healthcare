CREATE TABLE IF NOT EXISTS `Hospital` (
  `hosp_ID` INT,
  `hospName` varchar(255),
  `hospEmail` varchar(255),
  `hospPhone` INT,
  `hospAddress` varchar(255),
  `hospPassword` varchar(255),
  PRIMARY KEY (`hosp_id`));
  
  CREATE TABLE IF NOT EXISTS `VaccineDetails` (
  `hosp_ID` INT,
  `v1_quant` INT,
  `v2_quant` INT,
  `v3_quant` INT,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
   CREATE TABLE IF NOT EXISTS `OxygenDetails` (
  `hosp_ID` INT,
  `litres_available` INT,
  `supply_per_hour` INT,
  `price_per_litre` INT,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  CREATE TABLE IF NOT EXISTS `SurgeryDetails` (
  `hosp_ID` int,
  `heart` BOOLEAN,
  `joint` BOOLEAN,
  `abdominal` BOOLEAN,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
    CREATE TABLE IF NOT EXISTS `BedsDetails` (
  `hosp_ID` int,
  `BedsQuantity` int,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
   CREATE TABLE IF NOT EXISTS `BloodDetails` (
  `hosp_ID` int,
  `AP_Quantity` int,
  `AN_Quantity` int,
  `BP_Quantity` int,
  `BN_Quantity` int,
  `OP_Quantity` int,
  `ON_Quantity` int,
  `ABP_Quantity` int,
   `ABN_Quantity` int,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  CREATE TABLE IF NOT EXISTS `AmbulanceDetails` (
  `hosp_ID` int,
  `AmbulanceQuantity` int,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  
  CREATE TABLE IF NOT EXISTS `doctor` (
  `doc_ID` varchar(100),
  `docName` varchar(255),
  `doc_s` varchar(255),
  `docPhone` INT,
  `docAddress` varchar(255),
  `docPassword` varchar(255),
  `hosp_ID` INT,
  PRIMARY KEY (`doc_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  -- Date format is YYYY-MM-DD
    
    CREATE TABLE IF NOT EXISTS `TimeSlots` (
  `Time_ID` int auto_increment,
  `Doc_ID` varchar(100),
  `Start_Time` time,
  `End_Time` time,
  `Appt_Date` date,
  `Availability` int,
  PRIMARY KEY (`Time_ID`),
  FOREIGN KEY (`Doc_id`) REFERENCES Doctor(`doc_ID`)
  );
  
  
  
    CREATE TABLE IF NOT EXISTS `Appointment` (
    `User_ID` int,
  `Time_ID` int,
  `MeetLink` varchar(100),
  `PreDescription` varchar(100),
  `PostDescription` varchar(100),
  PRIMARY KEY (`User_ID`,`Time_ID`),
  FOREIGN KEY (`User_ID`) REFERENCES Users(`User_ID`),
   FOREIGN KEY (`Time_ID`) REFERENCES TimeSlots(`Time_ID`)
  );
  
