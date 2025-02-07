import maskpass # to hide the password

# masking the password
pwd = maskpass.askpass(mask="") 
print(pwd)
