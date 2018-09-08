Title: MySQL and encoding
Author: Marc
Date: 2008-03-27 21:14:00
Slug: mysql-and-encoding
Tags: IT

Today I had <strong>another</strong> encoding problem in my life...<br/><br/>I had a file with sql inserts, encoded with utf-8. My unix terminal, also encoded with utf-8. I had a database as well, and both database and tables encoded with utf-8.<br/><br/>My problem: when executing my sql file to my database, the data encoding was corrupted. There were just one missing piece not encoded with utf-8, MySQL terminal.<br/><br/>To fix it: <strong>mysql -u myuser --default_character_set utf8 mydatabase < myfile</strong>