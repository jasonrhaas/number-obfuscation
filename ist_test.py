#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
(c) IST Research 2014

Overview:
The purpose of this exercise is to find the hidden and obfuscated phone numbers
within the file named 'ist_numbers.txt'. This file contains 10 digit phone
numbers of varying degrees of obfuscation in order to thwart code that pulls them out.

Your task is to find as many of these phone numbers as you can, and write the cleaned and prettied 
10 digit phone numbers to the result file 'ist_results.txt'. Please leave 
comments so we may better understands your thoughts and logic behind your code if
it is unclear.

You are free to use any resources except your neighbor.

What to submit:
Your improved 'ist_test.py' file
Your results 'ist_results.txt'

Helpful links:
http://docs.python.org/2/library/stdtypes.html#string-methods
http://docs.python.org/2/library/re.html
https://pythex.org/
"""

import re

class IST_Software_Dev():
    # class specific variables can be created like this
    myCounter = 0
    myString = 'blah'
    # this is where the phone numbers will be stored
    myList = []
    
    # internal method declaration
    # you always need 'self' as the first parameter
    def runTest(self):
        # open the file
        with open('ist_numbers.txt', 'r') as theFile:
            #process each line of the file
            for line in theFile:
                # call another internal class method like this
                self.findNumbers(line)
        
        # write the findings to the file
        self.writeResults()
        
    """
    -------------------------------------------------
    Put your implementation here for extracting and 
    de-obfuscating the phone numbers line by line
    -------------------------------------------------
    """
    def findNumbers(self, aLine):
        # reference class variables declared prior like so
        self.myCounter += 1
        # Please use the 'append' list function to add each
        # cleaned phone number to the results list
        # Ex:
        # self.myList.append(self.myCounter)

    	words = dict(oh='1', one='1', two='2', three='3', four='4', five='5', six='6', seven='7', eight='8', nine='9')
    	newLine = aLine.lower()                # make the string lowercase
    	for key, value in words.items():       # iterate over the key, value pairs and do a substitution
    		newLine = newLine.replace(key, value)
        # Create a regular expression to use for matching
        # The following regex just matches any digit, junk, digit, junk, etc, and captures the digits
        p = re.compile(r'(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)\D*(\d)')
    	m = p.findall(newLine)                 # Find any all occurances of the match in the string
        if m:
            for num in m:                      # Need to iteate over 'm' because 'findall' can return tuples
                # print "line",self.myCounter,":","".join(num)
                self.myList.append("".join(num))    # Apprend the number to the list
    """
    Writes the results of the findings
    This will write a file that looks like:
    9016433769
    6173903733
    5636071868
    etc...
    """
    def writeResults(self):
        with open('ist_results.txt', 'w') as resultsFile:
            for i in range(len(self.myList)):
                resultsFile.write(str(self.myList[i]) + '\n')
                
"""
Ran via 'python ist_test.py' or './ist_test.py'
"""
if __name__ == "__main__":
    mainClass = IST_Software_Dev()
    mainClass.runTest()
            
