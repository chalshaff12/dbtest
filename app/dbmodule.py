import mysql.connector

def allUsers():	
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
		database="test_db"
	)
	cursor = mydb.cursor(buffered=True)
	sql = '''SELECT * FROM users;'''
	cursor.execute(sql)
	num_fields = len(cursor.description)
	columns = [i[0] for i in cursor.description]
	resultSet = cursor.fetchall()
	cursor.close()
	mydb.close()
	return columns + resultSet

def findUsers(usernameValue):
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
		database="test_db"
	)
	cursor = mydb.cursor(buffered=True)
	#if len(userID) > 0:
	column = 'username'
	value = usernameValue
	#elif len(username) > 0:

	#else:
	#	column = 'email'
	#	value = email
	sql = f"SELECT * FROM users WHERE {column} = '{value}'"
	cursor.execute(sql)
	#num_fields = len(cursor.description)
	#columns = [i[0] for i in cursor.description]
	resultSet = cursor.fetchall()
	cursor.close()
	mydb.close()
	return resultSet

def insertUser(email, password, username, first, last):
	mydb = mysql.connector.connect(
		host="35.239.141.59",
		user="backendteam",
		passwd="UZSDmp7J2J2ZYHw",
		database="test_db"
	)
	cursor = mydb.cursor(buffered=True)
	sql = f"INSERT INTO users (email, password, username, first, last) VALUES ('{email}','{password}','{username}','{first}','{last}')"
	cursor.execute(sql)
	mydb.commit()
	resultSet=allUsers()
	cursor.close()
	mydb.close()
	return resultSet



