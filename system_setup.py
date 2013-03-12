#!/usr/bin/python
import os
import sys
import subprocess

class SystemSetup(object):
	def __init__(self):
		print (
			'###############################################################\n'
			'This program will install and configure the Oracle Instant\n'
			'Client on your system.\n\n'
			'You must run this program as root for it to work correctly.\n\n'
			'Press enter to continue.\n'
			'###############################################################\n'
			)

		self.file_insert_header = (
			'###############################################\n',
			'# Added by Oracle Instant Client Easy-Install\n',
			'# On Github @ bit.ly/XoqtcH\n')

		raw_input()

	def install_alien(self):
		subprocess.check_call(["sudo", "apt-get", "install", "alien"])

	def oracle_setup(self):
		# todo: Remove sudo from all calls. Require the user to invoke as root.
		self.install_alien()
		subprocess.check_call(["sudo", "apt-get", "install", "libaio1"])

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

		oracle_configuration_file = open('/etc/ld.so.conf.d/oracle.conf', 'w')
		oracle_configuration_file.writelines(self.file_insert_header)
		oracle_configuration_file.write('/usr/lib/oracle/11.2/client64/lib\n')
		oracle_configuration_file.close()

		subprocess.check_call(["sudo", "ldconfig"])

		system_environment_vars = open('/etc/profile.d/oracle.sh', 'w')
		system_environment_vars.writelines(self.file_insert_header)
		system_environment_vars.write(
			'export ORACLE_HOME=/usr/lib/oracle/11.2/client64\n')
		system_environment_vars.write(
			'export TNS_ADMIN=/usr/lib/oracle/11.2/client64/network/admin\n')
		system_environment_vars.close()

		os.makedirs('/usr/lib/oracle/11.2/client64/network/admin')

		home_directory = os.environ['HOME']
		bash_profile = open(home_directory + '/.bashrc', 'a')
		bash_profile.writelines(self.file_insert_header)
		bash_profile.write(
			'export LD_LIBRARY_PATH=/usr/lib/oracle/11.2/client64/lib\n')
		bash_profile.write(
			'export ORACLE_HOME=/usr/lib/oracle/11.2/client64\n')
		bash_profile.write(
			'export TNS_ADMIN=/usr/lib/oracle/11.2/client64/network/admin\n')
		bash_profile.close()

if __name__ == '__main__':
	setup = SystemSetup()
	setup.oracle_setup()
	setup.install_git()
