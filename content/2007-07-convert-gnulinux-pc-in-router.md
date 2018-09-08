Title: Convert a GNU/Linux PC in a router
Author: Marc
Date: 2007-07-08 13:28:00
Slug: convert-gnulinux-pc-in-router
Tags: Systems,IT

For converting a simple computer with two interfaces (or more) in a router, it's necessary just to type two sentences in a console:<br/><br/><em>echo 1 > /proc/sys/net/ipv4/ip-forward</em><br/><br/><em>iptables -t nat -A POSTROUTING -o <interface> -j MASQUERADE</em>