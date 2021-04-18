# Project Layout

## Functions and Modules

* /data
	* create_db_table.py contains the functions 
		- create_table `accepts the connection object from create_connection and an sql statement`
		- initialize_db `uses the create_table() function to actually initialize and create the db`
	* create_user.py 
		- create_user() `generates the sql statement for the row information`
		-  write_user `actual write action to db`


* comconnection 
	* startdb_connection
		- create_connection() `returns a connection object for the sqlite datebase`




		
