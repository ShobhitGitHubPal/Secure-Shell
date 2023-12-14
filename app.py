from flask import Flask, request, jsonify

import paramiko
from flask_cors import CORS
import time


app = Flask(__name__)
CORS(app) # Add CORS to your app

#####################################################################################################################

def authenticate_ssh(ipaddress,username, password):    
    hostname = ipaddress
    ssh_username = username
    ssh_password = password
    
    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=ssh_username, password=ssh_password)
    # print("dsjgdsajgdjafdjyf" , ssh_client)
    return ssh_client

##################################################################################################################




#####################################################################################################################

# def execute(ssh_client,tail):
#     try:
#         stdin,std,stderr=ssh_client.exec_command("tail remotefilepath.txt")
#         print(std.readline())
#         # print(std)
#         ftp_client=ssh_client.open_sftp()
#         ftp_client.get("remotefilepath.txt","remotefilepath.txt")
#         ftp_client.close()

#     except paramiko.AuthenticationException as e:
#         print(e)


###########################################################

def execute(ssh_client, cmd):
    try:
        stdin, std, stderr = ssh_client.exec_command(f"{cmd}")
        print(std.readline())
        # print(std)
        ftp_client = ssh_client.open_sftp()
        ftp_client.get("example.txt", "example.txt")
        ftp_client.close()

    except paramiko.AuthenticationException as e:
        print(e)
        time.sleep(10)
        stdin,std,stderr=ssh_client.exec_command("date")
        
        print(std.readline())

 

############################## 

#####################################################################################################################

def abcd(ssh_client):
    try:
        # this code use for current direcory seen
        stdin, stdout, stderr = ssh_client.exec_command("cd shobhit && pwd")
        current_directory = stdout.read().decode().strip()
        print("Current working directory:", current_directory)


        # Connect to the remote server

        # print(hostname,ssh_username,"")
        # connect=ssh_client.connect(hostname, username=ssh_username, password=ssh_password)
        # ssh_client.exec_command("cd shobhit")
        cd_command = "cd shobhit && pwd && ls"
        ssh_client.exec_command(cd_command)

    
        stdin,stdout,stderr=ssh_client.exec_command("cd shobhit && ls")
        directory_contents = stdout.read().decode()
        print(directory_contents)
        
        time.sleep(2)
        stdin,stdout,stderr=ssh_client.exec_command("date")
        
        print(stdout.readline())
        
        # time.sleep(2)
        # ftp_client=ssh_client.open_sftp()
        # ftp_client.put("localfilepath.txt","remotefilepath.txt")
        # ftp_client.close()

        # stdin,stdout,stderr=ssh_client.exec_command("vi remotefilepath.txt")
        
        # print(stdout.read())

    #       
#
#         ftp_client=ssh_client.open_sftp()
#         ftp_client.get("example.txt","example.txt")
#         ftp_client.close()
# #
#         time.sleep(10)

#

#
        ftp_client=ssh_client.open_sftp()
        ftp_client.get("remotefilepath.txt","remotefilepath.txt")
        ftp_client.close()
#
        time.sleep(10)

        # Authentication successful
        return True
    except paramiko.AuthenticationException as e:
        # Authentication failed
        print("Authentication failed")

        print(e)
        return False
    finally:
        ssh_client.close()
try:
    ssh_clienter=authenticate_ssh('34.151.229.50','ashutosh','F!u@b#i$k@tech')
    execute(ssh_clienter,"ls")
    abcd(ssh_clienter)

except  Exception as e:
    print(e)
    
###########################   this is  authentication api##########################################

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username') 
    password = data.get('password')

    if username and password:
        if authenticate_ssh('34.151.229.50',username, password):
            return jsonify({'message': 'Authentication successful'}), 200
        else:
            return jsonify({'message': 'Authentication failed'}), 401
    else:
        return jsonify({'message': 'Invalid request'}), 400
    # print ('hiiiii')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
   
################################ this code use for all command###########################################

# def execute_commands(ssh_client, commands):
#     try:
#         # Execute each command in the list
#         for command in commands:
#             stdin, std, stderr = ssh_client.exec_command(command)
#             # Process the output (you can choose how to handle it)
#             print(f"Output of '{command}': {std.read().decode()}")

#         # After executing all the commands, close the SSH and SFTP connections
#         ssh_client.close()
#     except paramiko.AuthenticationException as e:
#         print(e)

# # # Example usage:
# # if __name__ == "__main__":
# #     # Create and set up your SSH client (ssh_client) here
# #     # ...

# #     # List of commands to execute on the remote server
#     commands_to_execute = [
#         "ls",
#         "pwd",
#         "cat remotefilepath.txt",
#         "echo 'Hello, World!' > newfile.txt",
#         "ls",
#     ]

#     execute_commands(ssh_client, commands_to_execute)

########################################################################################################


# import time  

# try:
        

#     def abc(ls):

#         return "jhcuw",ls


#     def defin():

#         return "defi"

#     def add(fun,a,b):


#         return fun()+str(a+b)

#     a=abc()

#     print(add(defin,2,3))

#     time.sleep(3)

# except Exception as e:
#     print(e)


#     time.sleep(3)

