README

The purpose of this project is interacting with a live database with DBI and generating reports solving certain database analysis questions.

1. please copy log_analysis.py under the same directory with newsdata.sql.
2. run 'vagrant ssh' to bring up the virtual machine. 
3. (if you dont have a virtual machine currently running on your computer, please use 'vagrant up' before step 2)
4. all the database we will be using for this project will be installed on virtual machine.
   VirtualBox is the tool we will be using to run this VM, it also has the web apps and SQL database server we need.
   Vagrant is the app we can share file between our OS and the VM.
5. cd /vagrant
6. cd to the newsdata.sql directory
7. create the newsdata database by running psql -d news -f newsdata.sql
8. python log_analysis.py
9. results will be printed out in the terminal window

sample_reults.txt contains the sample outputs for all three assigned questions