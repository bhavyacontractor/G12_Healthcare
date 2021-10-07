CREATE TABLE IF NOT EXISTS `VaccineDetails` (
  `hosp_ID` INT,
  `v1_quant` INT,
  `v2_quant` INT,
  `v3_quant` INT,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  -- DROP TABLE `VaccineDetails`; 
  
  CREATE TABLE IF NOT EXISTS `OxygenDetails` (
  `hosp_id` INT,
  `litres_available` INT,
  `supply_per_hour` INT,
  `price_per_litre` INT,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  -- DROP TABLE `OxygenDetails`;
  
  CREATE TABLE IF NOT EXISTS `SurgeryDetails` (
  `hosp_ID` int,
  `heart` BOOLEAN,
  `joint` BOOLEAN,
  `abdominal` BOOLEAN,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
 --  DROP TABLE `SurgeryDetails`;
  
  CREATE TABLE IF NOT EXISTS `BedsDetails` (
  `hosp_ID` int,
  `BedsQuantity` int,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES Hospital(`hosp_id`)
  );
  
  -- DROP TABLE `BedsDetails`;
  
CREATE TABLE IF NOT EXISTS `BloodDetails` (
  `hosp_ID` INT NOT NULL,
  `AP_Quantity` INT NULL DEFAULT NULL,
  `AN_Quantity` INT NULL DEFAULT NULL,
  `BP_Quantity` INT NULL DEFAULT NULL,
  `BN_Quantity` INT NULL DEFAULT NULL,
  `OP_Quantity` INT NULL DEFAULT NULL,
  `ON_Quantity` INT NULL DEFAULT NULL,
  `ABP_Quantity` INT NULL DEFAULT NULL,
  `ABN_Quantity` INT NULL DEFAULT NULL,
  PRIMARY KEY (`hosp_id`),
  FOREIGN KEY (`hosp_id`) REFERENCES `hospital` (`hosp_id`));

  -- DROP TABLE `BloodDetails`;
 
 CREATE TABLE IF NOT EXISTS `AmbulanceDetails` (
  `hosp_ID` INT NOT NULL,
  `AmbulanceQuantity` INT NULL DEFAULT NULL,
  PRIMARY KEY (`hosp_ID`),
  FOREIGN KEY (`hosp_id`) REFERENCES `hospital` (`hosp_id`));

-- DROP TABLE `AmbulanceDetails`;

