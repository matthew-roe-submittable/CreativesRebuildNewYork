CREATE DATABASE test;

CREATE TABLE test.creatives(
    id                    INT            NOT NULL AUTO_INCREMENT,
	unique_id             VARCHAR(50)    NOT NULL UNIQUE,
	submission_id         VARCHAR(50)    NOT NULL UNIQUE,
	submitter_id          VARCHAR(50)    NOT NULL UNIQUE,
	form_response_id      VARCHAR(50)    UNIQUE,
    first_name            VARCHAR(50),
    last_name             VARCHAR(50),
    zipcode               VARCHAR(50),
    address               VARCHAR(50),
    dob                   VARCHAR(50),
    last4SNN              VARCHAR(50),
    phone                 VARCHAR(50),
    date_last_checked     DATETIME,
	PRIMARY KEY (id)
);



