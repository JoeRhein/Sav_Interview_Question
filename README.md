# Sav_Interview_Question
The purpose of this repository is to show my skills in creating and documenting code projects


WhoIs client for python

## Usage: python WhoIs.py [domain.com]

Code Challenge Requirements:
Without using any prebuilt APIs, Packages, SDKs, Linux "whois" or examples found on Stack Overflow, how can you get a domain name's expiration date using Python 3.6+? The input should be any .com domain name, the output should be just the expiration date as a datetime object. Code is preferred, pseudocode is acceptable. Hint: It should utilize a socket. (Please provide link to Github code)*

Base Requirements:
INPUT : .com domain (ex. Google.com)
Output: datetime object of domain name expiration dates

Limitations for implementation:
- Does not accomodate domains that are not in the .com domain space
- Not fully tested on domains hosted out of the USA
- The substring rules may not work for all .com domains 'whois.markmonitor.com'

Potential Improvements: 
- More complete input sanitation
- Other webservers to accomodate more efficient searches
- More efficient overhead in terms of recieving and parsing the string, as the current implementation takes the whole payload and uses indexing to extract the correct substring

Discussion:
This software uses the WHOAMI protocol to collect information on a given domain name. The game requires first finding a server that allows for these quieries. I used Turmux and the whois call to find a suitable server for conducting WHOIS quieries. This protocol uses port 43 for communication.

The program does the following: 
- Sanitize the user input
- Creates a TCP WHOIS protocol call on port 43 to 
- A buffer captures the output and filters the output
- Closes the TCP socket
- The program outputs a datetime value for the expiration date
