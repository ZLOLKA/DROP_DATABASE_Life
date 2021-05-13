CREATE TABLE Course(
    id              int               PRIMARY KEY,
    start_course    date    NOT NULL,
    end_course      date    NOT NULL,
    count_lesson    int     NOT NULL,
    cost            float   NOT NULL
);
CREATE TABLE Teacher(
    id          int                   PRIMARY KEY,
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30) NOT NULL,
    patronymic  varchar(30),
    birth_year  int         NOT NULL,
    birth_month int         NOT NULL,
    birth_day   int         NOT NULL,
    education   varchar(50),
    mob_number  int         NOT NULL,
    email       varchar(30),
    passport    varchar(20) NOT NULL,
    start_work  date        NOT NULL,
    end_work    date
);
CREATE TABLE Class(
    id          int PRIMARY KEY,
    id_Course   int REFERENCES Course(id)
);
CREATE TABLE Student(
    id          int PRIMARY KEY,
    id_Class    int REFERENCES Class(id),
    first_name  varchar(30) NOT NULL,
    last_name   varchar(30) NOT NULL,
    patronymic  varchar(30),
    birth_year  int         NOT NULL,
    birth_month int         NOT NULL,
    birth_day   int         NOT NULL,
    passport    varchar(20) NOT NULL,
    mob_number  int         NOT NULL
);
CREATE TABLE Level(
    id          int PRIMARY KEY,
    id_Course   int REFERENCES Course(id)
);
CREATE TABLE Course_To_Teacher(
    id_Course   int REFERENCES Course(id),
    id_Teacher  int REFERENCES Teacher(id),
    PRIMARY KEY (id_Course, id_Teacher)
);
