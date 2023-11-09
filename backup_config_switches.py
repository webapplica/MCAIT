import paramiko # before you have install this lib : pip install paramiko
# to use ftp uncomment the following 
#import ftplib # before you have install this lib : pip install ftplib

#list of IP addresses of all switches
switches = ['172.16.2.100', '172.16.2.101', '172.16.2.102','172.16.2.103', '172.16.2.104', '172.16.2.105','172.16.2.106', '172.16.2.107', '172.16.2.108','172.16.2.109', '172.16.2.110', '172.16.2.111']

username = ''  # SSH username
password = ''  # SSH password

for switch in switches:
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(switch, username=username, password=password)

        # Send command to retrieve configuration
        ssh_shell = ssh.invoke_shell()
        ssh_shell.s.send('show running-config\n')
        output = ''
        while not output.endswith('#'):
            output += ssh_shell.recv(65535).decode('utf-8')

        # Save configuration to a file
        filename = f'{switch}_config.txt'
        with open(filename, 'w') as file:
            file.write(output)
            # To store the file on ftp server 
            #ftp = ftplib.FTP("ip_of_ftp_server")
            #ftp.login(ftp_username, ftp_password)
            #ftp.storbinary("STOR " + filename, file)
            #ftp.quit()
        print(f"Configuration saved for {switch} to {filename}")
        
        # Close SSH connection
        ssh.close()
    except paramiko.AuthenticationException:
        print(f"Failed to connect to {switch}: Authentication failed.")
    except paramiko.SSHException as e:
        print(f"Failed to connect to {switch}: {str(e)}")
    except Exception as e:
        print(f"An error occurred while connecting to {switch}: {str(e)}")
