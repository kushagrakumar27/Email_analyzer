import os, re, socket

f1="email_down.txt"
f2="dns.txt"
fi=open(f1, 'r')
fo=open(f2, 'w')
f3=open("ipadd.txt", 'w')
f4=open("hostname.txt", 'w')

for line in fi:
 #print line
    result = re.search('@(.*)>', line)
    #try:
    if result:	
	 fo.write (result.group(1)+ "\t" +socket.gethostbyname(result.group(1)) + "\n")
	 f3.write (socket.gethostbyname(result.group(1)) + "\n")
	 f4.write (result.group(1) + "\n")
    #fo.close()
    #except:
        #pass
