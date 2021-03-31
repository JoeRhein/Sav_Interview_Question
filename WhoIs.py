"""
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
- More efficient overhead in terms of receiving and parsing the string, as the current implementation takes the whole payload and uses indexing to extract the correct substring

Discussion:
This software uses the WHOAMI protocol to collect information on a given domain name. The game requires first finding a server that allows for these quieries. I used Turmux and the whois call to find a suitable server for conducting WHOIS quieries. This protocol uses port 43 for communication.

The program does the following: 
- Sanitize the user input
- Creates a TCP WHOIS protocol call on port 43 to 
- A buffer captures the output and filters the output
- Closes the TCP socket
- The program outputs a datetime value for the expiration date

References:
-https://tools.ietf.org/html/rfc3912
-https://en.wikipedia.org/wiki/WHOIS

Copyright (c) 2021 Joe Rhein

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

  Last edited by:  $Joe_Rhein$
              on:  $3_30_21$
        Revision:  $Basic$
              Id:  $Id$
          Author:  Joe_Rhein
"""
## Usage: python WhoIs.py [domain.com]

#Import needed native Python 3.6 libraries
import socket    # Needed to craft WHOIS protocol packets
import datetime  # Needed to convert to the standard Datetime Structure
import sys       # Needed to take user input at the command line

Usage = 'Usage: python WhoIs.py [domain.com]'

# Define a def to allow quick reference/copy paste for other projects
def Query_WHOIS(query,src='whois.markmonitor.com'):
    query = query + "\r\n"     # The server's hostname or IP address + port 43 call syntax
    
    # Using 'with' syntax as a normal method for reducing memory for large datasets
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((src, 43))          # Connect to Port 43
        s.send(query.encode('utf-8')) # Send and encoded query string
        while True:
            data = str(s.recv(4096))
            if 'Registration Expiration Date:' in data:
                ind = data.index('Registration Expiration Date:')
                payload = data[ind+30 : ind+49].replace('T',' ')
                obj = datetime.datetime.strptime(payload, '%Y-%m-%d %H:%M:%S')
                break
            elif not d: # Edge case where d does not return valid contents to break the loop
                break
            s.close()
    return obj


if __name__ == "__main__":
    Query = sys.argv[1]
    #Conduct Input Sanitation (The code included is not complete, but is an example of needed input sanitation)
    if not Query.endswith('.com'):
        ## TO DO: Include beter input sanitation to check against other common domains
        Query = Query + '.com' # Correct input 
        print('Domain name must be a .com domain\n{}'.format(Usage))
    try:
        res = Query_WHOIS(Query)
        print('Domain {} expires on {}'.format(Query,res))
    except:
        print('Domain Name was not found. Please verify inputs and try again\n{}'.format(Usage))
