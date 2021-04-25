INSERT INTO Client (
     first_name,
     last_name,
     registration_date,
     contact_number
    ) VALUES (
     get_from_form_first_name,
     get_from_form_last_name,
     get_from_form_registration_date,
     get_from_form_contact_number
    );

INSERT INTO CarBrand (
     brand
    ) VALUES (
     get_from_form_brand
    );

INSERT INTO CarBodyType (
     body_type
    ) VALUES (
     get_from_form_body_type
    );

INSERT INTO ClientCar (
     client,
     brand,
     body_type
    ) VALUES (
     get_from_form_id_client,
     get_from_form_id_car_brand,
     get_from_form_id_car_body_type
    );

INSERT INTO Work (
     client,
     car,
     start_work,
     end_work
    ) VALUES (
     get_from_form_id_client,
     get_from_form_id_client_car,
     get_from_form_start_work,
     get_from_form_end_work
    );
