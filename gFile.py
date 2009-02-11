#!/usr/bin/env python
#
#   gFile.py
#   
#   Copyright 2008-2009 Scott Walton <d38dm8nw81k1ng@gmail.com>
#       
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License (version 2), as
#   published by the Free Software Foundation
#     
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#       
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#   MA 02110-1301, USA.

import fuse
import stat
import os
import sys
import errno
import gNet

from time import time
from subprocess import *

fuse.fuse_python_api = (0,2)

class GStat(object):
    """
    The stat class to use for getattr
    """
    def __init__(self):
        """
        Purpose: Ripped straight from the Fuse SimpleFileSystemHowto wiki
        Returns: Nothing
        """
        self.st_mode = stat.S_IFDIR | 0744
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 2
        self.st_uid = os.getuid()
        self.st_gid = os.getgid()
        self.st_size = 4096
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0
        
		
class GFile(fuse.Fuse):
    """ 
    The main Google Docs filesystem class. Most work will be done
    in here.
    """
    
    def __init__(self, em, pw, *args, **kw):
        """ 
        Purpose: Connect to the Google Docs Server and verify credentials
        em: User's email address
        pw: User's password
        *args: Args to pass to Fuse
        **kw: Keywords to pass to Fuse
        Returns: Nothing
        """
        
        fuse.Fuse.__init__(self, *args, **kw)
        self.gn = gNet.GNet(em, pw)
        self.directories = {}
                          
    def getattr(self, path):
        """
        Purpose: Get information about a file
        path: String containing relative path to file using mountpoint as /
        Returns: a GStat object with some updated values
        """
        
        st = GStat()
        pe = path.split('/')
        
        # Set proper attributes for files and directories
        if path == '/': # Root
            pass
        elif pe[-1] in self.directories: # Is a directory
           pass
        elif pe[-1] in self.directories[pe[-2]]: # Is a file
            st.st_mode = stat.S_IFREG | 0744
            st.st_nlink = 1
            st.st_size = len(pe[-1]) 
        else: # Evidently, it must not exist
            return -errno.ENOENT    
        
        # Set access times to now - try and get actual access times off
        # gdata if possible
        # NOTE - It SHOULD be possible because gdata orders by access time
        st.st_atime = int(time())
        st.st_mtime = st.st_atime
        st.st_ctime = st.st_atime
        # Also need to get the sizes if possible
        
        return st
        
    def readdir(self, path, offset):
        """
        Purpose: Give a listing for ls
        path: String containing relative path to file using mountpoint as /
        offset: Included for compatibility. Does nothing
        Returns: Directory listing for ls
        """

        dirents = ['.', '..']
        pe = path.split('/')[1:]
        
        if path == '/': # Root
            excludes = []
            self.directories[''] = []
            for dir in self.gn.get_docs(filetypes = ['folder']).entry:
                excludes.append('-' + dir.title.text.encode('UTF-8'))
                self.directories[dir.title.text.encode('UTF-8')] = []
            if len(excludes) > 0:
                for doc in self.gn.get_docs(filetypes = excludes).entry:
                    self.directories[''].append(doc.title.text.encode('UTF-8'))
        else: #Directory
            self.directories[pe[-1]] = []
            for file in self.gn.get_docs(folder = pe[-1]).entry:
                if file.category[0].label is 'folder':
                    self.directories[file.title.text.encode('UTF-8')]
                self.directories[pe[-1]].append(file.title.text.encode('UTF-8'))
                       
        for entry in self.directories[pe[-1]]:
            dirents.append(entry)
        
        for r in dirents:
            yield fuse.Direntry(r)
            
    def mknod(self, path, mode, dev):
        pass

    def unlink(self, path):
        """
        Purpose: Remove a file
        path: String containing relative path to file using mountpoint as /
        Returns: 0 to indicate success
        """
        pe = path.split('/')[1:]
        gd_client.erase(pe[-1])
        # TODO: Finish Me!

def main():
    """
    Purpose: Mount the filesystem
    Returns: 0 To indicate successful operation
    """
    
    usage = """Google Docs FS: Mounts Google Docs files on a local
    filesystem gFile.py email password mountpoint""" + fuse.Fuse.fusage
    
    gfs = GFile(sys.argv[1], sys.argv[2], version = "%prog " + fuse.__version__,
        usage = usage, dash_s_do='setsingle')
    gfs.parse(errex=1)
    gfs.main()
    
    return 0

if __name__ == '__main__':
    main()
