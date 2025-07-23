#!/bin/bash
host=$1
start_port=$2
end_port=$3

echo "Scanning ports from $start_port to $end_port on $host"

for ((port=$start_port; port<=$end_port; port++))
do
    timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Port $port is open"
    fi
done