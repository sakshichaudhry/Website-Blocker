import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts"   # r is for raw string
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_list = ["www.netflix.com", "netflix.com"]     # list of the websites to be blocked

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,20):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)  # reset the pointer to the top of the text file
            for line in content:
                # Overwriting the whole file
                if not any(website in line for website in web_sites_list):
                    file.write(line)
                # do nothing otherwise
            file.truncate() # this line is used to delete the trailing lines (that contain DNS)
    time.sleep(5)
