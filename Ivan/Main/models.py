from django.db import models


# Create your models here.
class Client(models.Model):
    """
CREATE TABLE Client(
    id_client         INT         NOT NULL UNIQUE,
    first_name        VARCHAR(20) NOT NULL,
    last_name         VARCHAR(20),
    registration_date date        NOT NULL,
    contact_number    VARCHAR(15) NOT NULL,
    PRIMARY KEY (id_client)
);
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)

    registration_date = models.DateField()
    contact_number = models.CharField(max_length=15)


class CarBrand(models.Model):
    """
CREATE TABLE  CarBand(
    id_car_brand INT  NOT NULL UNIQUE,
    brand        text NOT NULL UNIQUE,
    PRIMARY KEY (id_car_brand)
);
    """
    brand = models.TextField(unique=True)


class CarBodyType(models.Model):
    """
CREATE TABLE CarBodyType(
    id_car_body_type INT  NOT NULL UNIQUE,
    body_type        text NOT NULL UNIQUE,
    PRIMARY KEY (id_car_body_type)
);
    """
    body_type = models.TextField(unique=True)


class ClientCar(models.Model):
    """
CREATE TABLE ClientCar(
    id_client_car INT NOT NULL UNIQUE,
    client_id     INT NOT NULL,
    brand_id      INT NOT NULL,
    body_type_id  INT NOT NULL,
    FOREIGN KEY (client_id)    REFERENCES Client(id_client),
    FOREIGN KEY (brand_id)     REFERENCES CarBand(id_car_brand),
    FOREIGN KEY (body_type_id) REFERENCES CarBodyType(id_car_body_type)
);
    """
    client = models.ForeignKey("Client", on_delete=models.CASCADE)

    brand = models.ForeignKey("CarBrand", on_delete=models.CASCADE)
    body_type = models.ForeignKey("CarBodyType", on_delete=models.CASCADE)


class Work(models.Model):
    """
CREATE TABLE Work(
    id_work    INT  NOT NULL UNIQUE,
    client     INT  NOT NULL,
    car        INT  NOT NULL,
    start_work date NOT NULL,
    end_work   date,
    FOREIGN KEY (client) REFERENCES Client(id_client),
    FOREIGN KEY (car)    REFERENCES ClientCar(id_client_car)
);
    """
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    car = models.ForeignKey("ClientCar", on_delete=models.CASCADE)
    start_work = models.DateTimeField()
    end_work = models.DateTimeField(blank=True, null=True)
