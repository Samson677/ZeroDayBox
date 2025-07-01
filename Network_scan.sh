#!/usr/bin/bash


echo "Enter subnet & output file: (e.g 127.0.0/24 ips.txt) "
read subnet output_file



scan_network()
{
local subnet_ip=$1
local output_file=$2

if [[ -z "$subnet_ip" ]]
then echo "Specify subnet ip"

return 1
fi

if [[ -z "$output_file" ]]
then 
sudo nmap -sn 192.168.183.0/24 | grep 'Nmap scan report' | awk '{print $5}' > ips.txt
echo " Nmap scan is complete! check output in $output_file"
return 1
else

sudo nmap -sn 192.168.183.0/24 | grep 'Nmap scan report' | awk '{print $5}' > "$output_file"

fi

}



screenshot()
{
  awk '{print "http://" $0}' "$output_file" > url.txt
  eyewitness --web -f url.txt -d Finding --no-prompt
  mv ips.txt url.txt geckodriver.log Finding/
  echo " Nmap scan is complete! check output in Findings $output_file file"

}



# call
scan_network "$subnet" "$output_file"
screenshot