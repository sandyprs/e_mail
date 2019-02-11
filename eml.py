import smtplib
import webbrowser


def getacc():
    global id
    id = input("enter your valid email id: ")
    at_pos = id.find("@")
    dot_pos = id.find(".com")
    domain = id[at_pos+1:dot_pos]
    return id,domain

def connect(id,domain):
    global connection
    dict ={"gmail":"smtp.gmail.com","yahoo":"mail.yahoo.com","outlook":"smtp.live.com","hotmail":"smtp.live.com"}
    try:

        for i in dict.keys():
            if i == domain:
                connection = smtplib.SMTP(dict[i],587)
                connection.ehlo()
                passwd = input("password: ")
                connection.starttls()
                connection.login(id,passwd)
            else:
                continue
    except:
        if domain == "gmail":
            print("there is problem with less secure apps..to proceed type (y)")
            yn = input("would you like to proceed?? ")
            if yn == "y" or yn == "Y":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            Main()

        else:
            print("enter valid email and password")
            Main()

def take_msg():
    sub = input("Suject: ")
    msg = input("Message: ")
    return sub,msg

def send(sub,msg):

    rcvr = input("enter reciever's email id: ")
    connection.sendmail(id,rcvr,"Subject: "+sub +"\n\n" + msg)

def Main():

    id, domain = getacc()
    connect(id,domain)
    sub, msg =take_msg()
    send(sub,msg)


if __name__ == "__main__":
    Main()