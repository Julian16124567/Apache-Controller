from time import localtime, strftime
import os

date = strftime("%Y-%m-%d", localtime())
time = strftime("%H:%M:%S", localtime())
datetimenow = f"[{date} | {time}]"

def errormessage(error):
    message = f"{datetimenow} {error}"
    with open("errorlog.txt", "a") as file:
        file.write(message + "\n")
         
pwd = "juju1612" 
cmd = f"echo {pwd}| systemctl start apache"