from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    rip=gethostbyname(mailserver)
    clientSocket.connect((rip, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    # if recv[:3] != '220':
        #print('220 reply not received from server.')
        # sys.exit()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    # if recv1[:3] != '250':
    #print('250 reply not received from server.')
    #sys.exit()

    # Send MAIL FROM command and print server response.
    # Fill in start
    c = 'MAIL FROM:<dean.norris@gmail.com>\r\n'
    #print(c)
    clientSocket.send(c.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #print('250 reply not received from server.')
    #sys.exit()
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    c = 'RCPT TO:<dean@norrispty.com>\r\n'
    #print(c)
    clientSocket.send(c.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    # if recv1[:3] != '250':
    #print('250 reply not received from server.')
    #sys.exit()
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    c = 'DATA\r\n'
    #print(c)
    clientSocket.send(c.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '354':
    #print('354 reply not received from server.')
    #sys.exit()

    # Fill in end

    # Send message data.
    # Fill in start
    c = '\r\nFrom: "Dean" <dean.norris@gmail.com>\r\nTo: "Dean" <dean@norrispty.com>\r\nSubject: Test\r\n\r\nTest One\r\n'
    #print(c)
    clientSocket.send(c.encode())
    #clientSocket.send(msg.encode())

    # Fill in end

    # Message ends with a single period.
    # Fill in start
    c = '\r\n.\r\n'
    clientSocket.send(c.encode())
    #clientSocket.send(endmsg.encode())
    #print(endmsg)

    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #    if recv1[:3] != '250':
    #        print('250 reply not received from server.')
    #sys.exit()

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    c = 'QUIT\r\n'
    #print(c)
    clientSocket.send(c.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #    if recv1[:3] != '221':
    #        print('221 reply not received from server.')
    #        sys.exit()

    # Fill in end
    clientSocket.close()
    #sys.exit()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
