Title: Linux and Debian simple boot
Author: Marc
Date: 2010-01-01 20:46:00
Slug: linux-and-debian-simple-boot
Tags: Systems,IT

<div>Today I've been researching on Linux and Debian booting.</div><div>
</div><div>There is an excellent article from IBM, which explains the procedure, and the involved parts:</div><div>
</div>[http://www.ibm.com/developerworks/linux/library/l-linuxboot/](http://www.ibm.com/developerworks/linux/library/l-linuxboot/)<div>
</div><div>Basically:</div><div>- <li>BIOS checks CMOS and choose the booting device</li><li>Control is given to device's MBR (physically first 512 bytes)</li><li>MBR checks for partitions on the device (in a self contained table), and gives control to bootable partition.</li><li>Then, Grub, LILO or whatever takes control, to load the kernel, and the file system.</li><li>Usually a [initrd](http://en.wikipedia.org/wiki/Initrd) filesystem is loaded before the "real" one. This way, the kernel can access this filesystem, while the modules for loading the one in the root partition are not yet loaded.</li><li>Finally, init program is called, to load all [user-space](http://en.wikipedia.org/wiki/User_space) applications.</li>
<div>To set this up in a USB drive (my idea), in a simple way, we need:</div><div>
</div><div>Make the drive bootable, using the [syslinux](http://en.wikipedia.org/wiki/Syslinux) tool, which is used for FAT filesystems:</div><div>syslinux /dev/sdb (or whatever device you want)</div><div>
</div><div>Then, mount the filesystem, and copy:</div><div>linux: the linux kernel binary</div><div>initrd.gz: compressed cpio file containing the initrd file tree</div><div>
</div><div>and</div><div>
</div><div>syslinux.cfg: syslinux settings, to let syslinux know where to find the kernel and the initrd. Basically:</div><div>
</div><div>default linux</div><div>append initrd=initrd.gz</div><div>
</div><div>Then, just restart, and your device will boot your kernel, and your filesystem.</div><div>
</div><div>Here, you can find a Linux kernel, and a initrd file, which will load a basic linux system, running the Debian installer:</div><div>
</div><div>[http://ftp.debian.org/debian/dists/stable/main/installer-i386/current/images/netboot/debian-installer/i386/](http://ftp.debian.org/debian/dists/stable/main/installer-i386/current/images/netboot/debian-installer/i386/)</div><div>
</div><div>Some more info on it at:</div><div>
</div><div>[http://www.debian.org/releases/stable/i386/ch04s03.html.en](http://www.debian.org/releases/stable/i386/ch04s03.html.en)</div><div>
</div></div>