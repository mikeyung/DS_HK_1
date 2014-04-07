"""
### GA Data Science Class Final Project
###
### Michael Yung
###
### program_1.py
###
### First Linkedin program to output my connections' URL and my skills
###
### Input - n/a
### Output -
### Connections' URL - output_connections_url.csv
###       Public URL - output_public_url.csv
###        My Skills - output_my_skills.csv
"""

from linkedin import linkedin # pip install python-linkedin
from prettytable import PrettyTable # pip install prettytable
import json

"""
### Define CONSUMER_KEY, CONSUMER_SECRET,  
### USER_TOKEN, and USER_SECRET from the credentials provided in LinkedIn application
"""

CONSUMER_KEY = '75bi1c02skzcm9'
CONSUMER_SECRET = 'ewW1H5Nd4baFXSjl'
USER_TOKEN = 'a0c284f4-a76e-4a4d-8d3b-846a7af89252'
USER_SECRET = '49b9d146-1677-4288-82fe-ece1007e672c'

RETURN_URL = '' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

"""
### Print program information header
"""

print "=========="
print "First Linkedin program to output my connections' URL and my skills"
print " "
print "Input - n/a"
print " "
print "Output -"
print "Connections' URL - output_connections_urls.csv"
print "      Public URL - output_public_urls.csv"
print "       My Skills - output_my_skills.csv"
print " "
print "=========="

"""
### The meat starts here ...
"""

print "Connect to Linkedin ..."
app = linkedin.LinkedInApplication(auth)

print "Get own profile ..."
profile = app.get_profile()

print "Get my connections ..."
connections = app.get_connections()


"""
### Get the connections' URL
"""

print "Get the Linkedin URL of all the connections and output to csv file ..."
connections_url = '/Users/michaelyung/DS_HK_1/finals/mikeyung/output_connections_urls.csv'
f = open(connections_url, 'w')

for c in connections['values']:
	if c.has_key('siteStandardProfileRequest'):
		lhs, rhs = c['siteStandardProfileRequest']['url'].split("&auth", 1)
		s =   lhs + '\n'
		f.write(s)

f.close()

print "Get the Public URL of all the connections and output to csv file ..."
public_url = '/Users/michaelyung/DS_HK_1/finals/mikeyung/output_public_urls.csv'
f = open(public_url, 'w')

public = app.get_connections(selectors=['publicProfileUrl'])
for u in public["values"]:
	if u.has_key('publicProfileUrl'):
		f.write(u['publicProfileUrl'] + '\n')

f.close()

"""
### My own data - skills using selectors
"""

print "Get my own skills and output to csv file ..."
my_skills = app.get_profile(selectors=['skills:(skill:(name))'])
result = my_skills["skills"]["values"]

my_skills_data = '/Users/michaelyung/DS_HK_1/finals/mikeyung/output_my_skills.csv'
f = open(my_skills_data, 'w')

for rs in result:
	f.write(rs["skill"]["name"] + '\n')

f.close()
