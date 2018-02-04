1. What is the grep command?

	grep  searches  the named input FILEs for lines containing a match to the given PATTERN.  If no files are specified, or if the file “-” is given, grep
       	searches standard input.  By default, grep prints the matching lines.

2. What is the meaning of #! /bin/bash at the start of scripts?

	The 'she-bang' (#!) tells the system wich interpreter to use for running the script, in this case it uses the bash shell
        which is located in /bin/bash. (Got the info from [*here*](https://stackoverflow.com/questions/8967902/why-do-you-need-to-put-bin-bash-at-the-beginning-of-a-script-file))

3. How many users exist in the course server?

	Using the ``$cat /etc/passwd`` command, its possible to list all users on the machine ([*info*](https://askubuntu.com/questions/410244/a-command-to-list-all-users-and-how-to-add-delete-modify-users)).
	Counting them with the ``$cat /etc/passwd | wc -l`` command ([*info*](https://stackoverflow.com/questions/371115/count-all-occurrences-of-a-string-in-lots-of-files-with-grep)), gives a total of 38 users.

4. What command will produce a table of Users and Shells sorted by shell (tip: using cut and sort)

	Once listed all the users in the machine with their respecitve shell, the 'table' can be filtered using ``$cut -d: -f 1,7 /etc/passwd | sort -k 2``
	Filtering the output for the relevant fields and sorting them by shell ([*info*](https://stackoverflow.com/questions/21584727/using-linux-cut-sort-and-uniq))
5. Create a script for finding duplicate images based on their content (tip: hash or checksum) You may look in the internet for ideas, Do not forget to include the source of any code you use.

	Check myscript.sh file in the [Answers](https://github.com/santiag0m/IBIO4680/tree/master/01-Linux/Answers) directory.
