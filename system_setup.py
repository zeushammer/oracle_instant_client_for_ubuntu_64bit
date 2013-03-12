#!/usr/bin/python
import os
import subprocess

class SystemSetup(object):
	def __init__(self):
		pass

	def install_curl(self):
		subprocess.check_call(["sudo", "apt-get", "install", "curl"])	

	def install_alien(self):
		subprocess.check_call(["sudo", "apt-get", "install", "alien"])

	def oracle_setup(self):
		self.install_curl()
		self.install_alien()

		# subprocess.check_call(
		# 	['sudo',
		# 	'curl',
		# 	'-vL',
		# 	'-o',
		# 	'/opt/oracle_libraries_primary_package.rpm',
		# 	'https://notredame.box.com/shared/static/p1gdmp4b1t0lcg2cm42g.rpm'])

		# subprocess.check_call(
		# 	['sudo',
		# 	'curl',
		# 	'-vL',
		# 	'-o',
		# 	'/opt/oracle_libraries_supplemental_sqlplus.rpm',
		# 	'https://notredame.box.com/shared/static/1qjgd9kx7pcfq4t2lptw.rpm'])

		# subprocess.check_call(
		# 	['sudo',
		# 	'curl',
		# 	'-vL',
		# 	'-o',
		# 	'/opt/oracle_libraries_supplemental_sdk.rpm',
		# 	'https://notredame.box.com/shared/static/kgyw7tcmqi8yk1mlfij9.rpm'])

		subprocess.check_call(
			['sudo',
			'alien',
			'-iv',
			'oracle_rpms/oracle-instantclient11.2-basic-11.2.0.3.0-1.x86_64.rpm'])

		subprocess.check_call(
			['sudo',
			'alien',
			'-iv',
			'oracle_rpms/oracle-instantclient11.2-sqlplus-11.2.0.3.0-1.x86_64.rpm'])

	def python_setup(self):
		pass

	def ruby_setup(self):
		pass

	def install_git(self):
		subprocess.check_call(["sudo", "apt-get", "install", "git"])	

if __name__ == '__main__':
	setup = SystemSetup()
	setup.oracle_setup()
	setup.install_git()
