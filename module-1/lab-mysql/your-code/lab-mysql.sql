#[lab-mysql]octavio

#Challenge 1 - Design the Database (lab-mysql.mwb, lab-mysql.pdf)


#Challenge 2 - Create the Database and Tables
sudo service mysql start
/usr/bin/mysql -u root -p
CREATE DATABASE lab-mysql;
USE lab-mysql;

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lab-mysql
-- -----------------------------------------------------
-- Schema para realizar los laboratorios lab-mysql y lab-mysql-select (Octavio Garcia Moreno)

-- -----------------------------------------------------
-- Schema lab-mysql
--
-- Schema para realizar los laboratorios lab-mysql y lab-mysql-select (Octavio Garcia Moreno)
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab-mysql` ;
USE `lab-mysql` ;

-- -----------------------------------------------------
-- Table `lab-mysql`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`customer` (
  `id_customer` INT NOT NULL AUTO_INCREMENT,
  `dni` VARCHAR(10) NULL,
  `name` VARCHAR(60) NULL,
  `phone` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(60) NULL,
  `city` VARCHAR(45) NULL,
  `province` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `zip_cp` VARCHAR(45) NULL,
  PRIMARY KEY (`id_customer`))
ENGINE = InnoDB
COMMENT = 'Entity customer: no se usa DNI/NIF como identificador sino un numero correlativo propio, evitando duplicidades.\nPosibles problemas: si la persona cambia de DNI/NIF.';


-- -----------------------------------------------------
-- Table `lab-mysql`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`invoice` (
  `id_invoice` INT NOT NULL AUTO_INCREMENT,
  `customer_id_customer` INT NOT NULL,
  `number` VARCHAR(15) NULL,
  `date` VARCHAR(15) NULL,
  PRIMARY KEY (`id_invoice`, `customer_id_customer`),
  INDEX `fk_car_has_customer_customer1_idx` (`customer_id_customer` ASC) VISIBLE,
  CONSTRAINT `fk_car_has_customer_customer1`
    FOREIGN KEY (`customer_id_customer`)
    REFERENCES `lab-mysql`.`customer` (`id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`car` (
  `id_car` INT NOT NULL AUTO_INCREMENT,
  `invoice_id_invoice` INT NULL DEFAULT NULL,
  `invoice_customer_id_customer` INT NULL DEFAULT NULL,
  `vin` VARCHAR(17) NULL,
  `brand` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  PRIMARY KEY (`id_car`),
  INDEX `fk_car_invoice1_idx` (`invoice_id_invoice` ASC, `invoice_customer_id_customer` ASC) VISIBLE,
  CONSTRAINT `fk_car_invoice1`
    FOREIGN KEY (`invoice_id_invoice` , `invoice_customer_id_customer`)
    REFERENCES `lab-mysql`.`invoice` (`id_invoice` , `customer_id_customer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Entity car: cada coche solo puede estar asociado a una factura y a un cliente.\nSe usa el VIN como identificador por lo tanto el PK no es consecutivo pero si único.';


-- -----------------------------------------------------
-- Table `lab-mysql`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`salesperson` (
  `id_salesperson` INT NOT NULL AUTO_INCREMENT,
  `invoice_id_invoice` INT NULL DEFAULT NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  `nif` VARCHAR(10) NULL,
  PRIMARY KEY (`id_salesperson`),
  INDEX `fk_salesperson_invoice1_idx` (`invoice_id_invoice` ASC) VISIBLE,
  CONSTRAINT `fk_salesperson_invoice1`
    FOREIGN KEY (`invoice_id_invoice`)
    REFERENCES `lab-mysql`.`invoice` (`id_invoice`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Entity salesperson: solo se puede asociar un vendedor a cada factura.';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



#Challenge 3 - Seeding the Database
INSERT INTO `lab-mysql`.`customer` (`dni`, `name`, `phone`, `email`, `address`, `city`, `province`, `country`, `zip_cp`) 
VALUES ('10001', 'Pablo Picasso', '+34 636 17 63 82', '', 'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'Spain', '28045');
INSERT INTO `lab-mysql`.`customer` (`dni`, `name`, `phone`, `email`, `address`, `city`, `province`, `country`, `zip_cp`) 
VALUES ('20001', 'Abraham Lincoln', '+1 305 907 7086', '', '120 SW 8th St', 'Mimia', 'Florida', 'United States', '33130');
INSERT INTO `lab-mysql`.`customer` (`dni`, `name`, `phone`, `email`, `address`, `city`, `province`, `country`, `zip_cp`) 
VALUES ('30001', 'Napoléon Bonaparte', '+33 1 79 75 40 00', '', '40 Rue du Colisée', 'Paris', 'Île-de-France', 'France', '75008');

INSERT INTO `lab-mysql`.`invoice` (`customer_id_customer`, `number`, `date`) 
VALUES (2, '852399038', '22-08-2018');
INSERT INTO `lab-mysql`.`invoice` (`customer_id_customer`, `number`, `date`) 
VALUES (1, '731166526', '31-12-2018');
INSERT INTO `lab-mysql`.`invoice` (`customer_id_customer`, `number`, `date`) 
VALUES (3, '271135104', '22-01-2019');

INSERT INTO `lab-mysql`.`salesperson` (`name`, `store`, `nif`) 
VALUES ('Petey Cruiser', 'Madrid', '00001');
INSERT INTO `lab-mysql`.`salesperson` (`name`, `store`, `nif`) 
VALUES ('Anna Sthesia', 'Barcelona', '00002');
INSERT INTO `lab-mysql`.`salesperson` (`name`, `store`, `nif`) 
VALUES ('Paul Molive', 'Berlin', '00003');
INSERT INTO `lab-mysql`.`salesperson` (`invoice_id_invoice`, `name`, `store`, `nif`) 
VALUES (1, 'Gail Forcewind', 'Paris', '00004');
INSERT INTO `lab-mysql`.`salesperson` (`invoice_id_invoice`, `name`, `store`, `nif`) 
VALUES (2, 'Paige Turner', 'Miami', '00005');
INSERT INTO `lab-mysql`.`salesperson` (`invoice_id_invoice`, `name`, `store`, `nif`) 
VALUES (3, 'Bob Frapples', 'Mexico City', '00006');
INSERT INTO `lab-mysql`.`salesperson` (`name`, `store`, `nif`) 
VALUES ('Walter Melon', 'Amsterdam', '00007');
INSERT INTO `lab-mysql`.`salesperson` (`name`, `store`, `nif`) 
VALUES ('Shonda Leer', 'São Paulo', '00008');

INSERT INTO `lab-mysql`.`car` (`invoice_id_invoice`, `invoice_customer_id_customer`, `vin`, `brand`, `model`, `year`, `color`) 
VALUES (1, 2, '3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', '2019', 'Blue');
INSERT INTO `lab-mysql`.`car` (`invoice_id_invoice`, `invoice_customer_id_customer`, `vin`, `brand`, `model`, `year`, `color`) 
VALUES (3, 3, 'ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', '2019', 'Red');
INSERT INTO `lab-mysql`.`car` (`invoice_id_invoice`, `invoice_customer_id_customer`, `vin`, `brand`, `model`, `year`, `color`) 
VALUES (1, 2, 'RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', '2018', 'White');
INSERT INTO `lab-mysql`.`car` (`invoice_id_invoice`, `invoice_customer_id_customer`, `vin`, `brand`, `model`, `year`, `color`) 
VALUES (2, 1, 'HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', '2018', 'Silver');
INSERT INTO `lab-mysql`.`car` (`invoice_id_invoice`, `invoice_customer_id_customer`, `vin`, `brand`, `model`, `year`, `color`) 
VALUES (2, 1, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60', '2019', 'Gray');
INSERT INTO `lab-mysql`.`car` (`invoice_id_invoice`, `invoice_customer_id_customer`, `vin`, `brand`, `model`, `year`, `color`) 
VALUES (3, 3, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', '2019', 'Gray');


