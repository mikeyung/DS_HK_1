"""
### GA Data Science Class Final Project
###
### Michael Yung
###
### program_2.py
###
### Python program to output my connections' skills by scraping their Linkedin public profile
### with BeautifulSoup
###
### Input - n/a
### Output -
### Connections' skills - output_connections_skills.csv
###
"""

import cookielib
import os
import urllib
import urllib2
import re
import string
from bs4 import BeautifulSoup

username = " "
password = " "

cookie_filename = "parser.cookies.txt"

class LinkedInParser(object):

    def __init__(self, login, password):
        """ Start up... """
        self.login = login
        self.password = password

        # Simulate browser with cookies enabled
        self.cj = cookielib.MozillaCookieJar(cookie_filename)
        if os.access(cookie_filename, os.F_OK):
            self.cj.load()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

#       Login
#       self.loginPage()

        skill = self.loadSkill()

        self.cj.save()


    def loadPage(self, url, data=None):
        """
        Utility function to load HTML from URLs for us with hack to continue despite 404
        """
        # We'll print the url in case of infinite loop
        # print "Loading URL: %s" % url
        try:
            if data is not None:
                response = self.opener.open(url, data)
            else:
                response = self.opener.open(url)
            return ''.join(response.readlines())
        except:
            # If URL doesn't load for ANY reason, try again...
            # Quick and dirty solution for 404 returns because of network problems
            # However, this could infinite loop if there's an actual problem
            return self.loadPage(url, data)

    def loginPage(self):
        """
        Handle login. This should populate our cookie jar.
        """
        login_data = urllib.urlencode({
            'session_key': self.login,
            'session_password': self.password,
        })

        html = self.loadPage("https://www.linkedin.com/uas/login-submit", login_data)
        return

    def loadSkill(self):
        
        f_url = open('/Users/michaelyung/DS_HK_1/finals/mikeyung/output_public_urls.csv', 'r')
        f_skill = open('/Users/michaelyung/DS_HK_1/finals/mikeyung/output_connections_skills.csv', 'w')
        
        i = 1

        for line in f_url:
            print i, line            
            html = self.loadPage(line)
            soup = BeautifulSoup(html)

            for s in soup.find_all("span", "endorse-item-name-text"):
                f_skill.write(s.string + ' ')

            f_skill.write('\n')

            i = i + 1
        
        f_skill.close()
        f_url.close()

        return 

parser = LinkedInParser(username, password)