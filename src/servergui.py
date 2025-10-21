import tkinter as tk
import os
import subprocess
from datetime import datetime
from time import time
from pathlib import Path
import customtkinter as ctk
from PIL import Image
#from errorlog import errormessage

def errormessage(error):
    print("")

def clearLog():
    print("")

##headers
#mainwindow | header
root = ctk.CTk()
root.title("Server Gui")
root.geometry("600x500")
root.resizable(False, False) 
root.withdraw()

#background image
bg_image_path = os.path.expanduser("/home/kali2/Schreibtisch/apachecontroller/bilder/bg.jpg")
pil_image = Image.open(bg_image_path)
window_width = 600
window_height = 500
pil_image.thumbnail((window_width, window_height), Image.Resampling.LANCZOS)
bg_image = ctk.CTkImage(light_image=pil_image, size=pil_image.size)
bg_label = ctk.CTkLabel(root, image=bg_image, text="")
bg_label.place(
    x=0,  
    y=0                                    
)
bg_label.lower()

#statuswindow | header
status = ctk.CTkToplevel()
status.title("Status Apache")
status.geometry("500x400")
status.resizable(False, False)
status.withdraw()

#header window | header
header = ctk.CTkToplevel()
header.title("Server Header")
header.geometry("600x500")
header.resizable(False, False)
header.withdraw()

#sudo passwort window | header
sudo = ctk.CTkToplevel()
sudo.geometry("300x150")
sudo.title("Sudo Passwort")
sudo.resizable(False, False)
sudo.withdraw()

##funktionen
#restart apache | funktion
def restart():
    global pwd
    pwd = str(pwd)
    try:    
        cmd = f"echo {pwd} sudo -S systemctl restart apache"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            listbox.insert(0, "> Apache restarted.")
        elif result.returncode ==  1:
            listbox.insert(0, "> Apache couldn't be restarted.")
        else:
            listbox.insert(0, "> ", result.stderr)
            error = str(result.stderr)
            errormessage(error)
    except Exception as e:
        error = str(e)
        errormessage(error)
        listbox.insert(0, "> Error logged in 'errorlog.txt'")

#disable apache | funktion
def disable():
    global pwd
    try:
        cmd = f"echo {pwd} | sudo -S systemctl disable apache2"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            listbox.insert(0, "> Apache disabled.")
        else:
            error = result.stderr.strip()
            listbox.insert(0, f"> Apache couldn't be disabled: {error}")
            errormessage(error)

    except Exception as e:
        error = str(e)
        errormessage(error)
        listbox.insert(0, "> Error logged in 'errorlog.txt'")

def enable():
    global pwd
    try:
        cmd = f"echo {pwd} | sudo -S systemctl enabled apache2"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            listbox.insert(0, "> Apache enabled.")
        else:
            error = result.stderr.strip()
            listbox.insert(0, f"> Apache couldn't be enabled: {error}")
            errormessage(error)

    except Exception as e:
        error = str(e)
        errormessage(error)
        listbox.insert(0, "> Error logged in 'errorlog.txt'")

#stop apache | funktion
def stop():
    global pwd
    pwd = str(pwd)
    try:
        cmd = f"echo {pwd} | sudo -S systemctl stop apache2"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            listbox.insert(0, "> Apache stopped.")
        elif result.returncode == 1:
            listbox.insert(0, "> Apache couldn't be stopped.")
        else:
            listbox.insert(0, "> ", result.stderr)
            error = str(result.stderr)
            errormessage(error)
    except Exception as e:
        error = str(e)
        errormessage(error)
        listbox.insert(0, "> Error logged in 'errorlog.txt'")

#status apache | funktion
def statusApache():
    cmd = "systemctl status apache2"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    with open("/home/kali2/Schreibtisch/apachecontroller/status.txt", "w") as file:
        for line in result.stdout.splitlines():
            file.write(line)
    cmd = "micro /home/kali2/Schreibtisch/apachecontroller/status.txt"
    subprocess.run(cmd, shell=True)

#destroy status | funktion
def destroystatus():
    status.destroy()

#exit header | funktion
def exitHeader():
    header.withdraw()
    root.deiconify()

def showRoot():
    root.deiconify()

#troubleshout apache | funktion        
def troubleShoot():
    cmd = "apachectl configtest"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    listbox.insert(0, "> " + str(result.stderr))
    
#start apache | funktion
def startApache():
    global pwd
    pwd = str(pwd)
    cmd = f"echo {pwd} | sudo -S systemctl start apache"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            listbox.insert(0, "> Starting Apache")
        else:
            listbox.insert(0, "> Apache couldn't be started or is already running.")
            error = str(result.stderr)
            errormessage(error)
    except Exception as e:
        error = str(e)
        errormessage(error)
        listbox.insert(0, "> Error logged in 'errorlog.txt'")

#runtime apache | funktion
def showRuntime():
    cmd = "ps -eo pid,comm,etime | grep apache2"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    listbox.insert(0, result.stdout)
    
#delete messages | funktion
def clearBox():
    listbox.delete(0, ctk.END)
    listbox.insert(0, "> Messages Deleted")

#show online sides | funktion
def showSidesOnline():
    output = []
    cmd = ""
    try:
        result = subprocess.run()
        result.split(" ")
    except Exception as e:
        error = str(e)
        errormessage(error)
        listbox.insert(0, "> Error logged in 'errorlog.txt'")

#ports apache | funktion
def showOpenPorts():
    global pwd
    cmd = f"echo {pwd} | sudo -S ss -tulpen | grep apache2"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True,text=True)
        listbox.insert(0, f"> {result.stdout}")
    except Exception as e:
        listbox.insert(0, f"Ports couldn't be laoded. 'Error: {e}'")

#sudo passwort window  | funktion
def submitSudoPwd():
    value = inputlist.get()
    value = value.strip()
    if value:
        with open("/home/kali2/Schreibtisch/apachecontroller/pwd.txt", "w") as file:
            file.write(value)
        sudo.withdraw()
        checkSudo()

def start():
    if checkSudo():
        cmd = "ls /etc/apache2/sites-enabled/ | wc -l"
        try:
            result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
            if result.returncode == 0:
                listbox.insert(0, f"> Apache sites Online: [{result.stdout.strip()}]")
            else:
                print(f"Error: {result.stderr}")
        except Exception as e:
            error = e
            errormessage(error)
            listbox.insert(0, f"> Error: {error}")

def statusApache():
    status.deiconify()

def sudoPwd():
    sudo.deiconify()

#show config files | funktion
def showConfig():
    header.deiconify

def checkSudo():
    global pwd
    try:
        with open("/home/kali2/Schreibtisch/apachecontroller/pwd.txt", "r") as file:
            fileread = file.read().strip()
            if not fileread:
                sudoPwd()
                return False
            else:
                cmd = f"echo {fileread} | sudo -S -v"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    pwd = fileread
                    root.deiconify()
                    return True
                else:
                    with open("/home/kali2/Schreibtisch/apachecontroller/pwd.txt", "w") as f:
                        f.write("")
                    sudoPwd()
                    return False
    except FileNotFoundError:
        open("/home/kali2/Schreibtisch/apachecontroller/pwd.txt", "w").close()
        sudoPwd()
        return False

def getPwd():
    with open("/home/kali2/Schreibtisch/apachecontroller/pwd.txt", "r") as file:
        global pwd
        filerad = file.read().strip()
        pwd = filerad
        return pwd

## tkinter configs
btn_height = 30
btn_width = 130
fgcolor = "#000000"      
hovercolor = "#706A6A"        
textcolor = "#FFFFFF"       

#root Exit Button | tkinter
btnexit = ctk.CTkButton(root, text="Exit", command=exit, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnexit.place(x=440, y=15)

#root start Button | tkinter
btnstart = ctk.CTkButton(root, text="Start", command=startApache, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnstart.place(x=20, y=75)

#root stop button | tkinter
btnstop = ctk.CTkButton(root, text="Stop", command=stop, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnstop.place(x=160, y=75)

#root restart button | tkinter
btnrestart = ctk.CTkButton(root, text="Restart", command=restart, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnrestart.place(x=300, y=75)

#status root button | tkinterbtnlog.place(x=300, y=165)
btnstatus = ctk.CTkButton(root, text="Status", command=statusApache, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnstatus.place(x=440, y=75)

#root troubleshooting button | tkinter
btntrouble = ctk.CTkButton(root, text="Troubleshoot", command=troubleShoot, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btntrouble.place(x=20, y=120)

#root openports button | tkinter
btnports = ctk.CTkButton(root, text="List Ports", command=showOpenPorts, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnports.place(x=160, y=120)

#button root runtime | tkinter
btnruntime = ctk.CTkButton(root, text="Uptime", command=showRuntime, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnruntime.place(x=300, y=120)

#disable button | tkinter
btndisable = ctk.CTkButton(root, text="Disable", command=disable, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btndisable.place(x=440, y=120)

#confiles button | tkinter
confbutton = ctk.CTkButton(root, text="Conf Files", command=showConfig, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
confbutton.place(x=20, y=165)

#root clear button | tkinter
btnclear = ctk.CTkButton(root, text="Clear Infos", command=clearBox, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnclear.place(x=160, y=165)

#btn clearlog root | tkinter
btnlog = ctk.CTkButton(root, text="Clear Log", command=clearLog, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
btnlog.place(x=300, y=165)

#header button | tkinter
headerbtn = ctk.CTkButton(root, text="Header", command=exitHeader, width=btn_width, height=btn_height, fg_color=fgcolor, hover_color=hovercolor, text_color=textcolor)
headerbtn.place(x=440, y=165)

#message box root | tkinter
listbox = tk.Listbox(root)
listbox.pack(side="bottom", fill="x")

#message box status | tkinter
statusbox = tk.Listbox(status)
listbox.pack(fill="x", side="bottom")

#sudo input pwd | tkinter
inputlist = ctk.CTkEntry(sudo, placeholder_text="Sudo Password")
inputlist.pack(pady=10, padx=10, fill="x")
submit_button = ctk.CTkButton(sudo, text="Submit", command=submitSudoPwd)
submit_button.pack(pady=10)

##main
#script root window
#passwort aus file holen 
getPwd()

start()

if __name__  == "__main__":
    root.mainloop()
