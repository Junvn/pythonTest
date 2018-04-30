from fabric.api import run,sudo
from fabric.api import env

env.hosts=['localhost']
env.port=22
env.user='janvn'

def hostname():
	run('hostname')

def ls(path='.'):
	run('ls {}'.format(path))

def tail(path='/etc/password',line=5):
	sudo('tail -n {0} {1}'.format(line,path))
	
