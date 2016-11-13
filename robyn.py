import aiml
import sqlite3

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()
db = sqlite3.connect('diseases.db')

cursor = db.cursor()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("std-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml b")


# Loop forever, reading user input from the command
# line and printing responses.
while True: 
	response = k.respond(str(input("> ")))
	if response[0] == '!':
		response = response[1:]
		cursor.execute(response)
		temp = cursor.fetchone()
		response = temp[0]
	print(response)