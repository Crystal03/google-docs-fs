# Introduction #
I'll fill this FAQ section with questions and answers as they're asked or as they come to mind and strike me as important.

# FAQ #

## Q: How can I contact the developer(s)? ##
A: I can be contacted through my GMail address on the project home page. Questions asked here will be answered as time allows.

## Q: What operating systems are supported? ##
A: At any given point in time, I'll be running on the most current versions of Ubuntu, so these systems are the ones that get priority treatment. I will also run some tests for Fedora, openSUSE and Debian as and when I can.

I'm unable to support Mac OSX directly as I don't have a Mac to test it on so I am relying on other people to provide installation and usage information.

## Q: I get problems when I try to save a file using OpenOffice.org 3.x. ##
A: See [issue 6](https://code.google.com/p/google-docs-fs/issues/detail?id=6) for more information. Version 1.0rc1 fixed this issue.

## Q: I can mount the file system using the gmount script, however when I attempt to ls the directory I get an error. What is happening? ##
A: This problem is possibly related to the version of python-gdata you have installed. If you have installed this package from a repository then it is most likely out of date and does not work with google-docs-fs. You will need to remove that version and then you need to go to the [python client](http://code.google.com/p/gdata-python-client/) page, download the .tar.gz file there and run the setup.py script it contains (instructions are contained in the INSTALL.txt file). Debian/Ubuntu users can download the .deb package from the Downloads tab. After that, you should be able to mount the file system and use it normally.

## Q: Whenever I mount the file system, folders don't appear or I get an Invalid Argument error ##
A: Download the latest version of Google Docs FS from the Downloads page to fix this problem.

## Q: When I mount the file system I get an Authentication Error or a Fuse Error saying "No such directory: <email address>" ##
A: If you have a space in your directory name, then the gmount script will think that the second word of your directory is your email address. There is currently no fix available so, as a workaround, remove any spaces in the directory name.

## Q: When do you plan to finish this file system? ##
A: All basic functionality is implemented. It isn't fully stable, and one or two issues crop up here and there. When I feel it's ready, I'll push out a 1.0 release.

## Q: Is this project related to GDocsFS? ##
A: No. GDocsFS is a separate project that was started not long before google-docs-fs. GDocsFS is written in Java whilst google-docs-fs is written in Python. There are similarities in that both use FUSE and the Google Data APIs.