#sending e-mail using python_simple-without subject,single receiver


import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("GMAIL ADDRESS", "PASSWORD")
 
msg = "MESSAGE TO BE SENT TO RECEIVER"
server.sendmail("SENDER GMAIL ADDRESS", "RECEIVER EMAIL ADDRESS", msg)
server.quit() 