def otp_login(email_to,user_name):
    import random
    import smtplib
    import ssl
    smtp_port=587
    smtp_server="smtp.gmail.com"
    passwd="thhi cwbg vjrh dlav" # app's account password
    email_from="cricketmanagementsystem@gmail.com"
    # email_to="tjeyeshbspsss10@outlook.com"
    # email_to='tjeyesh@bspsss10.edu.in'
    otp=random.randint(100000,999999)
    message=f"Cricket Management System Welcomes You {user_name}\n\nYour otp to login to your CRICKET MANAGEMENT SYSTEM(CMS) account is {otp}"
    try:
        simple_email_context=ssl.create_default_context()
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=simple_email_context)
        server.login(email_from,passwd)
        server.sendmail(email_from,email_to,message)
        server.quit()
    except Exception as e:
        print(e)
        otp='Invalid Email Id'
    return otp
def otp_reset(email_to,user_name):
    import random
    import smtplib
    import ssl
    smtp_port=587
    smtp_server="smtp.gmail.com"
    passwd="thhi cwbg vjrh dlav" # app's account password
    email_from="cricketmanagementsystem@gmail.com"
    otp=random.randint(100000,999999)
    message=f"Cricket Management System Welcomes You {user_name}\n\nYour otp to reset password is {otp}"
    try:
        simple_email_context=ssl.create_default_context()
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=simple_email_context)
        server.login(email_from,passwd)
        server.sendmail(email_from,email_to,message)
        server.quit()
    except Exception as e:
        print(e)
        otp='Invalid Email Id'
    return otp
