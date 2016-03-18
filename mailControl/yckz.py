import os, time
import poplib, smtplib, email
from email.header import decode_header
from email.mime.text import MIMEText

mailAccount = ['nightwiyr@gmail.com', 'heart804571@sina.com', '547277314@qq.com','myheart8045@163.com']
host='pop.gmail.com'
user= mailAccount[0]
psw='********'

def emailRead():
	read=poplib.POP3_SSL(host)
	try:
		read.user(user)
		read.pass_(psw)
	except:
		print 'login fialed'
		return
	info=read.stat()
	str=read.top(info[0], 0)
	str2=[]
	for x in str[1]:
		try:
			str2.append(x.decode())
		except:
			try:
				str2.append(x.decode('gbk'))
			except:
				str2.append(x.decode('big5'))
	msg=email.message_from_string('\n'.join(str2))
	title=decode_header(msg['subject'])

	if title[0][1]:
		title2=title[0][0].decode(title[0][1])
	else:
		title2=title[0][0]
	print title2
	return title2

def emailSend(msg):
	sent=smtplib.SMTP('smtp.gmail.com')
	sent.login(user, psw)

	to=['heart804571@sina.com']
	content=MIMEText('')
	content['Subject']=msg
	content['From']=user
	content['To']=','.join(to)
	sent.sendmail(user,to,content.as_string())
	sent.close()

def test():
	while True:
	#	time.sleep(20)
		if emailRead() == 'Down':
			os.system('shutdown -s -t 50')
			emailSend("over")
			break
		if emailRead() == 'Restart':
			os.system('shutdown -r')
			emailSend("over")
			break

if __name__ == '__main__':
	test()
	os.system('shutdown -a')
