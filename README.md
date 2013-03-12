##Easy Installation of Oracle Instant Client on Ubuntu/Debian Linux

If you've ever had to mess with installing and configuring the Oracle Instant Client on your Ubuntu/Debian machine,
you know that it's a pain in the arse.  This repo contains a simple python script and the necessary Oracle packages 
to get everything set up correctly on your machine.

__Important: Currently, this only supports 64-bit machines.__  
Drop me a line if you want to have support for 32-bit systems.

### Instructions
1. Download the repo as a zip file.
2. Unzip the file wherever you want on your system.
3. Run system_setup as root. [sudo python system_setup.py]
4. Obtain your sqlnet.ora, tnsnames.ora, and possibly ldap.ora files from your DBA.
5. Place those files into the /usr/lib/oracle/11.2/client64/network/admin directory.

### Warnings
__This utility is provided as-is with absolutely no support.__  
I will not be able to help you if it hoses up your system somehow.
