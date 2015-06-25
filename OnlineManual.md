# Contents #

  1. [System Requirements](OnlineManual#System_Requirements.md)
  1. [Getting google-docs-fs](OnlineManual#Getting_the_latest_stable_version.md)
  1. [Installing](OnlineManual#Installing.md)
  1. [How to use google-docs-fs](OnlineManual#Running.md)
  1. [Supported Filetypes](OnlineManual#Supported_Filetypes.md)
  1. [How to debug google-docs-fs](OnlineManual#Debugging.md)
  1. [FAQ](OnlineManual#FAQ.md)

# System Requirements #

## All Systems ##

  * [Python](http://www.python.org) >= 2.5
  * [fuse-python](http://apps.sourceforge.net/mediawiki/fuse/index.php?title=FusePython) >= 0.2
  * [gdata-python](http://code.google.com/p/gdata-python-client/) >= 2.0.0

## Linux/FreeBSD ##

  * [Fuse](http://apps.sourceforge.net/mediawiki/fuse/index.php?title=Main_Page) - Comes with most Linux distributions. Can be installed on FreeBSD through Ports.

## Mac OSX ##

  * [MacFUSE](http://code.google.com/p/macfuse/) >= 2.0.3
  * [pkg-config](http://pkg-config.freedesktop.org/wiki/) >= 0.23

# Getting the latest stable version #

The latest stable version can be found in the [Downloads section](http://code.google.com/p/google-docs-fs/downloads/list). Select the version appropriate for your operating system.

# Download using Mercurial #

As of 24th September 2010, I have switched google-docs-fs over to using Mercurial for source control. To get a copy of the source, simply do:
```
hg clone https://google-docs-fs.googlecode.com/hg/ google-docs-fs
```

# Installing #

## Linux/FreeBSD ##

To install google-docs-fs you can simply run the setup.py script from within the untarred directory:

`./setup.py install`

Install as root/su/sudo if you wish to install for all users.

### Debian/Ubuntu ###

Ubuntu packages are now provided in the Downloads section, along with python-gdata, to make installation easier for Ubuntu users. It is also hosted on [Launchpad](https://edge.launchpad.net/google-docs-fs).

Thanks to Luca Invernizzi for providing the Ubuntu package and python-gdata.

### Arch Linux ###

google-docs-fs is included in [AUR](http://aur.archlinux.org/packages.php?ID=28666).

Thanks to tocer.


### Fedora/Cent OS ###

There are no packages for RPM based distributions. If anyone would like to create an RPM for google-docs-fs and any dependencies I would be happy to host them here.

## Mac OSX ##

There are two ways to install on OSX.

### Original Instructions ###

To install on Mac OSX do the following:
  1. Ensure you have the Mac-specific libraries above installed.
  1. Download fuse-python.
  1. Run the following commands:
```
sudo cp fuse.pc fuse.bak
sudo sed -i 's#-I${includedir}/fuse -D_FILE_OFFSET_BITS=64#-I${includedir}/fuse -D__FreeBSD__=10 -D_FILE_OFFSET_BITS=64#g' \
/usr/local/lib/pkgconfig
sudo mv fuse.pc fuse.fix && sudo mv fuse.bak fuse.pc
```
  1. Install fuse-python and gdata-python-client.
  1. Download and install google-docs-fs

Thanks to Ben Samuel for this information.

### Alternate Instructions ###

[Alternate instructions](http://blog.vucica.net/2010/11/some-tips-on-building-fuse-python-on-mac-os-x.html) provided by vucica.

# Running #

Use the gmount script to mount the file system:

`gmount directory email@address.net`

To umount the file system just use the gumount script as follows:

`gumount directory`

Do **NOT** invoke fusermount -u directly as doing this will not invoke the cleaning up of any leftover temporary files. You can ignore the following error:

``rm: cannot remove `/home/x/.google-docs-fs': No such file or directory``

as this means that there were no leftover temporary files to clean up.

# Supported Filetypes #

google-docs-fs supports the Microsoft Office filetypes: `.doc` `.xls` and `.ppt`

If you want to change this, you can directly edit `gFile.py` stored in either the `site-packages` or `dist-packages` of your Python directory. Change all occurrences of the filetypes you want to remove to the filetype of your choice.

google-docs-fs does not support the new feature of Google Docs which allows any file type to be stored. I am looking to add this in future releases.

# Debugging #

If you experience any problems with google-docs-fs and wish to help me debug it, get the latest SVN revision and see if that works. If it still doesn't, use the -d flag to enable debugging information:

`gmount directory email@address.net -d`

This will enable debug output in the terminal you are using. Note that you will have to use a different terminal to perform operations on the mounted file system. After you have mounted the file system using this method, perform the task that is giving you errors, then create a new Issue and attach all the output from the debug window. Your help with this is MASSIVELY appreciated =).

# FAQ #

Please see [the FAQ](http://code.google.com/p/google-docs-fs/wiki/FAQ) if you have any questions. If your query is not covered there, then feel free to [email me](mailto:d38dm8nw81k1ng@gmail.com).