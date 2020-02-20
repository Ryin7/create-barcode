import pyqrcode 

url = pyqrcode.create('http://uca.edu') 
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
url.png('code.png', scale=6, module_color=[0,0,0,128], background= [0xff, 0xff, 0xff])
print(url.terminal(quiet_zone=1)) 
http://instagram.com/ry.iinnn