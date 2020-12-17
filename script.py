a="netsh wlan show profile name=Nirajan001 key=clear" # it's cmd command to show saved password
import subprocess
output = subprocess.check_output(a, shell=True) # os.system won't help us to save it in a variable
f=open("myfile.txt", "x") #creating a file 
f=open("myfile.txt", "a") #appending it
output=str(output) # since f.write() wont work for byte 
f.write(output)

