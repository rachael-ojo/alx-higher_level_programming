#!/bin/bash

# Check if database name is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <hbtn_0c_0>"
    exit 1
fi

# Database name passed as argument
hbtn_0c_0=$1

# MySQL command to insert a new row into first_table
mysql -u ojo_rachael -p -e "USE $hbtn_0c_0; INSERT INTO first_table (id, name) VALUES (89, 'Best School');"