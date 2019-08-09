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
			'You must run this program as root for it to work correctly.\n'
			'You will be prompted for permission to install software.\n'
			'Say yes if you want the program to work. :)\n\n'
			'Press enter to continue.\n'
			'###############################################################\n'
			)

		self.file_insert_header = (
			'\n################################################\n',
			'# Added by Oracle Instant Client Easy-Install  #\n',
			'# On Github @ bit.ly/XoqtcH                    #\n',
			'################################################\n')

		self.program_completion_message = (
			'\n###############################################################\n'
			'Congratulations, the program completed successfully.\n'
			'Oracle Instant Client should now be correctly installed.\n\n'
			'There are a couple of things that you still need to do.\n'
			'1. Obtain sqlnet.ora, tnsnames.ora, and possibly ldap.ora \n'
			'   from your DBA.\n'
			'2. Place these files into the following directory: \n'
			'   /usr/lib/oracle/11.2/client64/network/admin\n'
			'3. Restart your terminal to load the new environment variables.\n'
			'4. Attempt to connect to your database with sqlplus64.\n'
			'5. Star this repo on Github so that I know if it is being used.\n'
			'6. Submit any issues on Github(http://bit.ly/XoqtcH).\n'
			'###############################################################\n')

	def install_alien(self):
		subprocess.check_call(["apt-get", "-y", "install", "alien"])

	def oracle_setup(self):
		self.install_alien()
		subprocess.check_call(["apt-get", "-y", "install", "libaio1"])

		subprocess.check_call(
			['alien',
			'-iv',
			'oracle_rpms/oracle-instantclient11.2-basic-11.2.0.3.0-1.x86_64.rpm'])

		subprocess.check_call(
			['alien',
			'-iv',
			'oracle_rpms/oracle-instantclient11.2-sqlplus-11.2.0.3.0-1.x86_64.rpm'])

		subprocess.check_call(
			['alien',
			'-iv',
			'oracle_rpms/oracle-instantclient11.2-devel-11.2.0.3.0-1.x86_64.rpm'])

		oracle_configuration_file = open('/etc/ld.so.conf.d/oracle.conf', 'w')
		oracle_configuration_file.writelines(self.file_insert_header)
		oracle_configuration_file.write('/usr/lib/oracle/11.2/client64/lib\n')
		oracle_configuration_file.close()

		subprocess.check_call(["ldconfig"])

		system_environment_vars = open('/etc/profile.d/oracle.sh', 'w')
		system_environment_vars.writelines(self.file_insert_header)
		system_environment_vars.write(
			'export ORACLE_HOME=/usr/lib/oracle/11.2/client64\n')
		system_environment_vars.write(
			'export TNS_ADMIN=/usr/lib/oracle/11.2/client64/network/admin\n')
		system_environment_vars.write(
			'export LD_LIBRARY_PATH=/usr/lib/oracle/11.2/client64/lib\n')
		system_environment_vars.write(
			'export PATH=$ORACLE_HOME:$PATH\n')		
		system_environment_vars.close()

		os.makedirs('/usr/lib/oracle/11.2/client64/network/admin')

if __name__ == '__main__':
	setup = SystemSetup()
	setup.oracle_setup()
	print setup.program_completion_message
