Title: Two simple steps to reduce bandwidth on static files
Author: Marc
Date: 2010-12-05 03:41:00
Slug: two-simple-steps-to-reduce-bandwidth-on
Tags: Google App Engine

First step is to let Google host your JavaScript library of choice for you. Google Libraries API hosts JQuery, Mootools, Prototype... and you can directly link to them from your website.

More info at:
[http://code.google.com/apis/libraries/devguide.html](http://code.google.com/apis/libraries/devguide.html)

<div>Second step is to compress you CSS file (or files, but if you are gonna compress it to save bandwidth, probably you want to merge them in one for better performance). There are several websites which compress CSS files online, and for free. The one I found which works best is:
[http://www.lotterypost.com/css-compress.aspx](http://www.lotterypost.com/css-compress.aspx)</div>