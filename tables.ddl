CREATE DATABASE test;

CREATE TABLE test.creatives(
    id                    INT            NOT NULL AUTO_INCREMENT,
	unique_id             VARCHAR(50)    NOT NULL UNIQUE,
	submission_id         VARCHAR(50)    NOT NULL UNIQUE,
	form_response_id      VARCHAR(50)    UNIQUE,
    first_name            VARCHAR(50),
    last_name             VARCHAR(50),
    csv_last_used         VARCHAR(100),
    date_verified         DATETIME,
    verified              BOOLEAN,
	PRIMARY KEY (id)
);



