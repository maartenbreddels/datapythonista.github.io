Title: Brother printer on GNU/Linux
Author: Marc
Date: 2012-07-10 16:58:00
Slug: brother-stupid-printer-on-gnulinux
Tags: 

For some reason, brother printers (at least mine) do not take into account the settings specified for the printer in the regular way (Gnome settings in my case).

But&nbsp;mysteriously, there is a command which can be used to change them properly (<span style="background-color: white;">brprintconf_mfc235c)</span><span style="background-color: white;">. In my case, I was having problems with top margin, and top of pages was not printed. Apparently it was because of page type, so I could fix it by:</span>

<code>sudo brprintconf_mfc235c -pt A4 </code>