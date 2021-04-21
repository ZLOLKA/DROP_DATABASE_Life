CREATE TABLE Client(
    id_client         INT         NOT NULL UNIQUE,
    first_name        VARCHAR(20) NOT NULL,
    last_name         VARCHAR(20),
    registration_date date        NOT NULL,
    contact_number    VARCHAR(15) NOT NULL,
    PRIMARY KEY (id_client)
);
CREATE TABLE  CarBand(
    id_car_brand INT  NOT NULL UNIQUE,
    brand        text NOT NULL UNIQUE,
    PRIMARY KEY (id_car_brand)
);
CREATE TABLE CarBodyType(
    id_car_body_type INT  NOT NULL UNIQUE,
    body_type        text NOT NULL UNIQUE,
    PRIMARY KEY (id_car_body_type)
);
CREATE TABLE ClientCar(
    id_client_car INT NOT NULL UNIQUE,
    client_id     INT NOT NULL,
    brand_id      INT NOT NULL,
    body_type_id  INT NOT NULL,
    FOREIGN KEY (client_id)    REFERENCES Client(id_client),
    FOREIGN KEY (brand_id)     REFERENCES CarBand(id_car_brand),
    FOREIGN KEY (body_type_id) REFERENCES CarBodyType(id_car_body_type)
);
CREATE TABLE Work(
    id_work    INT  NOT NULL UNIQUE,
    client     INT  NOT NULL,
    car        INT  NOT NULL,
    start_work date NOT NULL,
    end_work   date,
    FOREIGN KEY (client) REFERENCES Client(id_client),
    FOREIGN KEY (car)    REFERENCES ClientCar(id_client_car)
);
