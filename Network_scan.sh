#!/usr/bin/bash


echo "Enter subnet: ( e.g 127.1.2.0/24 )"
read subnet



scan_network()
{
local subnet_ip=$1

if [[ -z "$subnet_ip" ]]
then echo "Specify subnet ip"

return 1
else

sudo nmap -sn 192.168.183.0/24 | grep 'Nmap scan report' | awk '{print $5}' > hosts.txt

fi
}



screenshot()
{
  awk '{print "http://" $0}' hosts.txt > url.txt
  eyewitness --web -f url.txt -d Finding --no-prompt
  mv hosts.txt url.txt geckodriver.log Finding/
  echo " Nmap scan is complete! check output in Findings hosts.txt"
 
}

httpRecon()
{
   
  cd Finding
  grep "Successful" Requests.csv | awk -F',' '{print $3}' > http200.txt

  echo "Recon is done!"
}

# call
scan_network "$subnet"
screenshot
httpRecon

