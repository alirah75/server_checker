CREATE TABLE log (
	id INTEGER NOT NULL, 
	project_id INTEGER, 
	server_address VARCHAR, 
	message VARCHAR, 
	date DATE, 
	time TIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_id) REFERENCES information (id)
)