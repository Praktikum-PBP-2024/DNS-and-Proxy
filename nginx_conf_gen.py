import os
import csv
import sys


if len(sys.argv) > 1:
    first_argument = sys.argv[1]
    
    if first_argument == "ssh":
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("\
server {" f"""
        listen {row[1]};
        proxy_pass 10.99.99.{int(row[0][-3:])}:22;
        proxy_timeout 300s;

""" "}")
    
    elif first_argument == "http":
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("\
server {" f"""
        server_name {row[0]}.shariyl.cloud;
        client_max_body_size 4096M;

        location / """ "{" f"""
                proxy_pass http://10.99.99.{int(row[0][-3:])}/;
                proxy_buffering off;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-Host $host;
                proxy_set_header X-Forwarded-Port $server_port;

                proxy_connect_timeout       300;
                proxy_send_timeout          300;
                proxy_read_timeout          300;
                send_timeout                300;
        """ "}\n"
"}")
else:
    print("No arguments passed. Possible args: ssh and http")





