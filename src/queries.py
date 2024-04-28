creacion_esquema = "CREATE SCHEMA IF NOT EXISTS `NomeRiu_Hotels`;"

crear_tabla_hotel = """CREATE TABLE IF NOT EXISTS `NomeRiu_Hotels`.`Hotel_details` (
  `hotel_id` INT NOT NULL AUTO_INCREMENT,
  `hotel_name` VARCHAR(45) NULL,
  PRIMARY KEY (`hotel_id`));
  """

insertar_hotel = "INSERT INTO Hotel_details (hotel_name) VALUES (%s)"
  
crear_tabla_meal = """CREATE TABLE IF NOT EXISTS `NomeRiu_Hotels`.`Meal_details` (
  `meal_id` VARCHAR(25) NOT NULL,
  `extra_price` FLOAT NULL,
  PRIMARY KEY (`meal_id`));
"""

insertar_meal = "INSERT INTO Meal_details (meal_id) VALUES (%s)"

crear_tabla_room = """CREATE TABLE IF NOT EXISTS `NomeRiu_Hotels`.`Room_details` (
  `room_id` VARCHAR(25) NOT NULL,
  `price` FLOAT NULL,
  PRIMARY KEY (`room_id`));
"""

insertar_room = "INSERT INTO Room_details (room_id) VALUES (%s)"

crear_tabla_agent = """CREATE TABLE IF NOT EXISTS `NomeRiu_Hotels`.`Agent_details` (
  `agent_id` VARCHAR(25) NOT NULL,
  `agent_name` VARCHAR(45) NULL,
  `company_name` VARCHAR(45) NULL,
  PRIMARY KEY (`agent_id`));
"""

insertar_agent = "INSERT INTO Agent_details (agent_id) VALUES (%s)"

crear_tabla_booking = """CREATE TABLE IF NOT EXISTS `NomeRiu_Hotels`.`Booking_details` (
  `record_id` INT NOT NULL AUTO_INCREMENT,
  `hotel_id` INT NULL,
  `agent_id` VARCHAR(25) NULL,
  `adr` FLOAT NULL,
  `lead_time` INT NULL,
  `arrival_date` DATE NULL,
  `stays_in_weekend_nights` INT NULL,
  `stays_in_week_nights` INT NULL,
  `adults` INT NULL,
  `children` INT NULL,
  `babies` INT NULL,
  `reserved_room_type` VARCHAR(25) NULL,
  `assigned_room_type` VARCHAR(25) NULL,
  `meal_id` VARCHAR(25) NULL,
  `required_car_parking_spaces` INT NULL,
  `total_of_special_requests` INT NULL,
  `booking_changes` INT NULL,
  `days_in_waiting_list` INT NULL,
  `reservation_status_date` DATE NULL,
  `reservation_status` VARCHAR(45) NULL,
  `courtesy` TINYINT NULL,
  `is_canceled` TINYINT NULL,
  PRIMARY KEY (`record_id`),
  FOREIGN KEY (`hotel_id`) REFERENCES `NomeRiu_Hotels`.`Hotel_details`(`hotel_id`),
  FOREIGN KEY (`agent_id`) REFERENCES `NomeRiu_Hotels`.`Agent_details`(`agent_id`),
  FOREIGN KEY (`reserved_room_type`) REFERENCES `NomeRiu_Hotels`.`Room_details`(`room_id`),
  FOREIGN KEY (`assigned_room_type`) REFERENCES `NomeRiu_Hotels`.`Room_details`(`room_id`),
  FOREIGN KEY (`meal_id`) REFERENCES `NomeRiu_Hotels`.`Meal_details`(`meal_id`)
);
"""

insertar_booking = """INSERT INTO Booking_details (
                                                hotel_id, 
                                                agent_id, 
                                                adr, 
                                                lead_time, 
                                                arrival_date, 
                                                stays_in_weekend_nights, 
                                                stays_in_week_nights,
                                                adults,
                                                children,
                                                babies,
                                                reserved_room_type,
                                                assigned_room_type,
                                                meal_id,
                                                required_car_parking_spaces,
                                                total_of_special_requests,
                                                booking_changes,
                                                days_in_waiting_list,
                                                reservation_status_date,
                                                reservation_status,
                                                courtesy,
                                                is_canceled) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

crear_tabla_clients = """CREATE TABLE IF NOT EXISTS `NomeRiu_Hotels`.`Client_details` (
  `record_id` INT NOT NULL AUTO_INCREMENT,
  `country` VARCHAR(45) NULL,
  `market_segment` VARCHAR(45) NULL,
  `distribution_channel` VARCHAR(45) NULL,
  `customer_type` VARCHAR(45) NULL,
  `is_repeated_guest` TINYINT NULL,
  `previous_booking_not_canceled` INT NULL,
  `previous_cancellations` INT NULL,
  PRIMARY KEY (`record_id`),
  FOREIGN KEY (`record_id`) REFERENCES `NomeRiu_Hotels`.`Booking_details`(`record_id`)
);
"""

insertar_client = """INSERT INTO Client_details (
                                                country, 
                                                agent_id, 
                                                market_segment, 
                                                distribution_channel, 
                                                customer_type, 
                                                is_repeated_guest, 
                                                previous_booking_not_canceled,
                                                previous_cancellations,
                                                ) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""