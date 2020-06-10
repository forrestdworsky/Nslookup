#!/usr/bin/env python
#nslookup: Take an input file (input_hostnames.csv) containing domain and port.
#perform an nslookup on each row
#output IP addresses as output_ip_address.csv
 
__author__ = "Forrest Dworsky"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "forrest.dworsky@gmail.com"
__status__ = "Production"

## For Python 2.7
import socket
import csv

# csv_read
# Input: input (filename of a csv to read from)
# Output: hostnames (a list of hostnames to supply to nslookup)

def nslookup(host,port):
	#socket.getaddrinfo performs the nslookup.  Accepts multiple parameters.  Only using host and port for this function
	ip_list = set()
	#create the array first to store the information in.
	#make the array a set because it eliminates duplicates.
	#sets do not have duplicates
	ais = socket.getaddrinfo(host,port)
	#print(ais)
	for result in ais:
		ip_list.add(result[-1][0])
		#iterate through the list
		#print(result[-1][0])
	return ip_list

def csv_read():
	with open('input_hostnames.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		hostnames = []
		#make a list 
		for row in csvreader:
			hostnames.append((row[0],row[1]))
			#take the first 2 columns of the list
			#iterate through the list to get every time
	return hostnames

def glob(ips):
	new_ips = []
	for ip_list in ips:
		for ip in ip_list:
			new_ips.append(ip)
	#print(new_ips)
	return new_ips

def csv_write(ip):
	ip = glob(ip) # in-place assignment
	#in place assignment allows us to use the glob function
	#print(ip)
	with open('output_ip_address.csv', mode='w') as csvfile:
		csvwriter = csv.writer(csvfile, lineterminator='', delimiter='\n')
		csvwriter.writerow(ip)
	return

def main():
	hostnames = csv_read()
	#define hostnames variable
	csv_ip = []
	#create the list to store the hostnames resulting from the nslookup function
	for hostname in hostnames:
		csv_ip.append(nslookup(hostname[0], hostname[1]))

	csv_write(csv_ip)
	#call the csvwrite function and pass in csv_ip which is filled with the IP addresses from nslookup
	
if __name__=="__main__":
	main()