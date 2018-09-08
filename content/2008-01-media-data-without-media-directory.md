Title: Media data without media directory
Author: Marc
Date: 2008-01-17 16:13:00
Slug: media-data-without-media-directory
Tags: Applications,Django,IT

It's not a big trouble, but I wanted to remove the /media/ prefix on all my media links, like...<br/><br/><code><br/><img alt="My Image" src="/media/img/myimage.png"/><br/><link rel="stylesheet" href="/media/css/mysheet.css" type="text/css"/><br/></code><br/><br/>and so on.<br/><br/>This can be easily achieved by replacing in apache's configuration file:<br/><br/><code><br/><Location "/media/"><br/>SetHandler None<br/></LocationMatch><br/></code><br/><br/>by<br/><br/><code><br/><LocationMatch "/((css|js|img|swf|pdf)/|favicon.ico)"><br/>SetHandler None<br/></LocationMatch><br/></code><br/><br/>Of course you have to have all you media files in folders like css, js, img... or anything that you specify in last regular expression.<br/><br/><strong>UPDATE:</strong> See this [post](http://vaig.be/2008/05/09/unable-to-define-my-urls-exactly-my-way-resignation-statement/) before using this approach.