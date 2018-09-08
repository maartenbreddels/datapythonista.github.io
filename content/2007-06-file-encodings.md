Title: File encodings
Author: Marc
Date: 2007-06-07 15:52:00
Slug: file-encodings
Tags: Development,Systems,IT

Many times, specially when writing web pages, you have to deal with texts with different encodes (if web site isn't in us-ascii, of course).  Here are some useful tips for not spending too much time with this:<br/><br/><em>bash# </em><em>file -i <filename></em> (for knowing the encoding for a specific file)<br/><br/><em>vim# </em><em>:set fileencoding=utf-8</em> (for changing encoding of current file, converting characters from one charset to the new one in a human understandable way)<br/><br/><em>vim# :set encoding=utf-8</em> (for setting encode of new files; default is system locale)<br/><br/>Remember that those thinks just apply to plain files, that are saved without any header or any information about encoding (editors try to figure out encodes).<br/><br/>A little bit offtopic, but an interesting vim command is also:<br/><br/><em>vim# :set ff=unix</em> (for changing eol from dos/mac to unix)<br/><br/><strong>UPDATE:</strong> If you have many files to convert, or don't know how to use vim... :) you can use GNU <em>iconv</em> program.