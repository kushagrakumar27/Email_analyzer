import whois, re
#from ipwhois import IPWhois

f4=open("hostname.txt", 'r')
f5=open("info.txt", 'w')
for line in f4:
  wh = whois.whois(line.rstrip())
  f5.write(str(wh) +'\n'+'-----------------------------------------------------------------------------------------' +'\n')