import subprocess

a="netsh wlan show profile name=Nirajan001 key=clear" # it's cmd command to show saved password
output = subprocess.check_output(a, shell=True) # os.system won't help us to save it in a variable
myfile="wifi_pwd.txt"

if path.isdir(myfile):
 f=open(myfile, "x") #creating a file 

f=open(myfile, "a")  #appending it
output=str(output) # since f.write() wont work for byte 
f.write(output)

