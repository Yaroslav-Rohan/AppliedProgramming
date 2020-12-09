CREATE TABLE users (
    uid SERIAL NOT NULL,
    email VARCHAR,
    password BYTEA,
    name VARCHAR,
    PRIMARY KEY (uid)
);

CREATE TABLE auditorium (
    uid SERIAL NOT NULL,
    number INTEGER,
    PRIMARY KEY (uid)
);

CREATE TABLE booking (
    uid SERIAL NOT NULL,
    user_uid INTEGER,
    auditorium_uid INTEGER,
    auditorium_status VARCHAR ,
    booking_date_start DATE,
    booking_date_final DATE,
    PRIMARY KEY (uid),
    FOREIGN KEY(user_uid) REFERENCES users(uid),
    FOREIGN KEY(auditorium_uid) REFERENCES auditorium (uid)
);