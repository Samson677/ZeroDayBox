#!/usr/bin/bash

host=$1
start_port=$2
end_port=$3
port_count=0

port_scanner()
{
  
  echo " "
for((port=start_port; port<=end_port; port++))
do
  if timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null;
    then

   echo "Port: $port is Open. ip: $host"
   ((port_count++))
   
  fi
done  
 echo "Port Scan Complete: $port_count found Open"
}

port_scanner