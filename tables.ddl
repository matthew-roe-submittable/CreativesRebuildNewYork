CREATE DATABASE test;

CREATE TABLE test.creatives(
    id                    INT            NOT NULL AUTO_INCREMENT,
	primary_unique_id     VARCHAR(50)    NOT NULL UNIQUE,
	submission_id         VARCHAR(50)    NOT NULL,
	submitter_id          VARCHAR(50)    NOT NULL,
	form_response_id      VARCHAR(50),
	entry_id              VARCHAR(50),
    primary_last_name     VARCHAR(50),
    primary_zipcode       VARCHAR(50),
    primary_dob           VARCHAR(50),
    date_last_checked     DATETIME,
	PRIMARY KEY (id)
);

CREATE TABLE test.collaborators(
   id                  INT          NOT NULL AUTO_INCREMENT,
   creatives_id        INT          NOT NULL UNIQUE,
   collab_unique_id    VARCHAR(50)  NOT NULL UNIQUE,
   submission_id       VARCHAR(50)  NOT NULL,
   form_response_id    VARCHAR(50)  NOT NULL,
   collab_last_name    VARCHAR(50),
   collab_zipcode      VARCHAR(50),
   collab_dob          VARCHAR(50),
   form_id             VARCHAR(300) NOT NULL,
   PRIMARY KEY (id),
   CONSTRAINT fk_collaborators_creatives FOREIGN KEY (creatives_id) REFERENCES creatives(id)
);