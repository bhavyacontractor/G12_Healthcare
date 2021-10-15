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
  
