Setting up Fedora
#################

Today I've got my new Dell XPS (with Ubuntu preinstalled), and this is the procedure
to set it up, and get my perfect working environment. This is expected to be useful
mainly for my **future self**, but sharing it here in case someone else can find
ideas or tips that are useful. Also happy to receive comments on how you do things
differently (and potentially better).

My operating system of choice is `Fedora MATE Compiz <https://spins.fedoraproject.org/mate-compiz/>`_,
I think GNOME 3 was a big mistake, so staying in what was GNOME 2.

After downloading the ISO, I create the live USB with `UNetbootin <https://unetbootin.github.io/>`_.
This works well, but it has a problem. The label of the volume is not updated, and it becomes inconsistent
with the one that GRUB loads. This will create a lot of warnings like this::

   dracut-initqueue[602]: Warning dracut-initqueue timeout - starting timeout scripts

With couple of final warnings::

   Warning: /dev/disk/by-label/Fedora-Live-WS-x86_64-29-1 does not exist
   Warning: /dev/mapper/live-rw does not exist

To fix it, we just need to know the label of our live USB (can be obtained in the rescue terminal by
calling ``blkid``). And then, in the GRUB menu, press `e` with the `Start Fedora Live` option
selected, and replace the value of `LABEL` by the correct one. A `Ctrl-x` will make the system
boot with the updated configuration, and should start normally. This
`video <https://www.youtube.com/watch?v=C3iSqmfPRxY>`_ shows the process step by step.

The default configurations during the installation work well for me (using 50Gb for `/`, the rest
for `/home/`, and `ext4` filesystem). But I encrypt `/home/`, which is not enabled by default.

Once the new system is installed, and running, those are the tasks I perform.

Configuration
-------------

- Merge both panels into one, and leave it to the bottom (removing the workspaces and Thunderbird,
  which I not use)
- Mouse setup: enable touchpad click, natural scrolling and increase acceleration
- Disable screensaver, and make windows be selected when mouse moves over them
- Change the terminal shorcuts to change and move tabs (I got used to the KDE shortcuts and never
  bothered in learning the GNOME ones)
- Change the default search engine in Firefox to `DuckDuckGo <https://duckduckgo.com/>`_.
- Set up couple of aliases in `~/.bashrc`: ``alias rgrep="grep -R"`` and ``alias vi="vim"`` (which
  doesn't seem to be required anymore)
- Set up `vim` for Python (and remove some unwanted features like folding)::

   syntax on
   set number
   set autoindent
   set expandtab
   set shiftwidth=4
   set tabstop=4
   set nofoldenable

   execute pathogen#infect()
   set statusline+=%#warningmsg#
   set statusline+=%{SyntasticStatuslineFlag()}
   set statusline+=%*
   let g:syntastic_always_populate_loc_list = 1
   let g:syntastic_auto_loc_list = 0
   let g:syntastic_check_on_open = 1
   let g:syntastic_check_on_wq = 0

Installing software
-------------------

Quite happy with the software that comes preinstalled with Fedora, but few things left to install.
First adding `RPM Fusion <https://rpmfusion.org>`_ repositories::

   sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

Then updating the system::

   sudo dnf update

Then installing the development group::

   sudo dnf groupinstall "Development Tools"

Also installing all the missing packages (or not missing, but had this list for some years now)::

   sudo dnf install vim-enhanced git vlc gimp inkscape unzip

And finally installing `Miniconda <https://conda.io/miniconda.html>`_. I prefer Miniconda over
Anaconda, because I don't like to have any package in the base environment. So, in every
environment I'm sure there are the packages I'm using (and it's not falling back to the base
environment version, which can be different of the expected).
