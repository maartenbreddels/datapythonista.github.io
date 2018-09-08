Title: Allow user to execute root files
Author: Marc
Date: 2007-04-17 15:39:00
Slug: allow-user-to-execute-root-files
Tags: Systems,IT

Sometimes it's useful allowing users to execute programs reserved for root. For example if we have a desktop system, we can allow users to halt or reboot computer.<br/><br/>There are several ways to <span class="blsp-spelling-corrected" id="SPELLING_ERROR_0">achieve</span> it, the proposed here is the simplest one (probably not the securest one).<br/><br/>Just add +s to file permissions; for example:<br/><span style="font-weight: bold"><span class="blsp-spelling-error" id="SPELLING_ERROR_1">chmod</span> +s /<span class="blsp-spelling-error" id="SPELLING_ERROR_2">sbin</span>/halt</span><br/><br/>I don't recommend doing it without reading some documentation, and comparing this method with "<span class="blsp-spelling-error" id="SPELLING_ERROR_3">sudo</span>"...