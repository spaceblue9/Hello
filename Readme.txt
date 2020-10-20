ขั้นตอนการ Upload Heroku
1.ต้องสร้าง Visual Env ใน Python เพื่อสร้าง environtment ของเครื่องที่ใช้
2.สร้าง Procfile ดังนี้ web: gunicorn app:app --log-file=-p
3.python app ต้องตั้งชื่อว่า app.py เท่านั้น
4.ใช้คำสั่ง pip freeze ดูว่ามี Packet อะไรบ้าง
5.เอา packet ที่ install ใน Project มาสร้างเป็นไฟล์ requirements.txt ด้วยคำสั่ง pip freeze > requirements.txt
6.upload ไปที่ github
7.upload ไปที่ Heroku

*** ขั้นตอนสร้าง Visual Env บน MAC
Python3 Virtualenv Setup
Requirements
	• Python 3
	• Pip 3
$ brew install python3
Pip3 is installed with Python3
Installation
To install virtualenv via pip run:
$ pip3 install virtualenv
Usage
Creation of virtualenv:
$ virtualenv -p python3 <desired-path>
Activate the virtualenv:
$ source <desired-path>/bin/activate
Deactivate the virtualenv:
$ deactivate
About Virtualenv
------------------------------------------------------------
