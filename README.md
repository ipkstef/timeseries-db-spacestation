#Project Layout

##Goals 

1. key value store of user name and number in db (sqlite) * Need to format the email to send sms
2. ability to set params for frequency of sms or granular options to trigger. Don't want to spam
3. seperate the different modules and packages (db/compute/scrapping) 



* /data
	* create_db_table.py contains the functions 
		- create_connection(db_file)
		- create_table(conn, create_table_sql)
		- main() stiches those together 

	* create_user.py 
		- create_user(conn, users) - generates the sql statement
		-  write_user(fullname,phonenumber) generates a unique 3 digit id as well

		
