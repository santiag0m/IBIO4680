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

	Check [myscript.sh](https://github.com/santiag0m/IBIO4680/tree/master/01-Linux/Answers/myscript.sh).

6. Download the bsds500 image segmentation database and decompress it (keep it in you hard drive, we will come back over this data in a few weeks).
	
	With the command ``scp BSR_bsds500.tar cristinaraul@157.253.63.53:/datos1/cristinaraul`` it is possible to copy the compressed file of the database from the local machine to the virtual machine. This can be decompressed with the command ``tar -xf BSR_bsds500.tar``

7. What is the disk size of the uncompressed dataset, How many images are in the directory 'BSR/BSDS500/data/images'?

	The disk size of the uncompressed dataset is obtained  with the command ``du -sh BSR``. 
	![Image_01](https://github.com/santiag0m/IBIO4680/blob/master/01-Linux/Answers/images/image_01.png)

	The number of images in the directory is found with the commands:  
	``cd BSR/BSDS500/data/images/`` 
	``find . -name "*.jpg" -exec identify {} \; | grep -c .jpg`` 
	![Image_02](https://github.com/santiag0m/IBIO4680/blob/master/01-Linux/Answers/images/image_02.png)

8. What is their resolution, what is their format?

	We can know their resolution and their format with the following command:  
	``find . -name "*.jpg" -exec identify {} \;``  
	![Image_3](https://github.com/santiag0m/IBIO4680/blob/master/01-Linux/Answers/images/image_03.png) 

9. How many of them are in landscape orientation (opposed to portrait)?

	The number of images in landscape orientation is given by the command 
	``find . -name "*.jpg" -exec identify -format "\n%[fx:(w>h)?1:0]"  {} \; | grep -c 1`` 
	![Image_04](https://github.com/santiag0m/IBIO4680/blob/master/01-Linux/Answers/images/image_04.png) 

10. Crop all images to make them square (256x256). Tip: do not forget about imagemagick.
	
	To crop all images and make then square, a new folder is created where the images are copied and then overwritten with the corresponding cropped images. It is made with the followings commands: 
	``cd ..`` 
	``mkdir crop_images`` 
	``cp -r ./images/ crop_images`` 
	``cd crop_images`` 
	``find . -name "*.jpg" -exec convert -crop 256x256+0+0 {} {} \;`` 
	``find . -name "*.jpg" -exec identify {} \;`` 
	![Image_05](https://github.com/santiag0m/IBIO4680/blob/master/01-Linux/Answers/images/image_05.png)
