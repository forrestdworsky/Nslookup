# Nslookup

This script automates the nslookup function allowing you to quickly perform an nslookup on hundreds of hostnames.

# Purpose

The idea for this project came from a task in the workplace.  
I was tasked with finding the the Ip addresses for a list of hundreds of hostnames in order to convert a list of hostnames to IP address ranges to reduce the size of a list in a vulnerability scanner.


## Usage

It takes a CSV input file containing a list of hostnames.  
The first column contains the hostname or domanin name.  
The second column contains the port number. 
Both columns are required and the CSV must be named "input_hostnames.csv".
The script will output a new CSV containing the IP addresses in a file called "output_ip_address.csv".

An incorrect hostname may cause a socket error.
