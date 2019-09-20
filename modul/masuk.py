import os, sys

print ("Masuk yang bener yah beb:*")
username = 'Mr.ExAid'      
password = 'hasantampan'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "Login sukses.."
			sys.exit()

		else:
			print "Salah Goblok"
			print "Balik Login"
			restart()

	else:
		print "Salah Goblok"
		print "Balik Login"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()