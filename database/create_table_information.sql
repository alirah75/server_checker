CREATE TABLE information (
	id INTEGER NOT NULL, 
	start_date VARCHAR NOT NULL, 
	end_date VARCHAR NOT NULL, 
	start_time VARCHAR NOT NULL, 
	end_time VARCHAR NOT NULL, 
	interval_minutes VARCHAR NOT NULL, 
	second_interval_minutes VARCHAR NOT NULL, 
	target_addresses VARCHAR NOT NULL, 
	selected_functions VARCHAR NOT NULL, 
	status INTEGER NOT NULL, 
	PRIMARY KEY (id)
)