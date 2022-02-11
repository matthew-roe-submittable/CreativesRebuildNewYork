CREATE DATABASE test;

CREATE TABLE test.creatives(
    id                    INT            NOT NULL AUTO_INCREMENT,
	primary_unique_id     VARCHAR(50)    NOT NULL UNIQUE,
	submission_id         VARCHAR(50)    NOT NULL,
	submitter_id          VARCHAR(50)    NOT NULL,
	form_response_id      VARCHAR(50),
	entry_id              VARCHAR(50),
    collab_unique_id_1    VARCHAR(50)  UNIQUE,
    collab_unique_id_2    VARCHAR(50)  UNIQUE,
    collab_unique_id_3    VARCHAR(50)  UNIQUE,
    collab_unique_id_4    VARCHAR(50)  UNIQUE,
    collab_unique_id_5    VARCHAR(50)  UNIQUE,
    collab_unique_id_6    VARCHAR(50)  UNIQUE,
    collab_unique_id_7    VARCHAR(50)  UNIQUE,
    collab_unique_id_8    VARCHAR(50)  UNIQUE,
    collab_unique_id_9    VARCHAR(50)  UNIQUE,
    date_last_checked     DATETIME,
	PRIMARY KEY (id)
);

