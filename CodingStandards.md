# Introduction #

To keep consistency, we need to use an agreed set of standards. Obviously, using Python limits what the code will look like somewhat but it's still essential that coding practices be agreed. Besides, writing this gives me something to do on a boring Wednesday afternoon :P


# Layout Standard #

## File Layout ##

  * The first line _must_ be:
```
      #!/usr/bin/env python
```
  * The list of copyright owners. If you're adding to a file, just stick your name + email address after the other copyright owners.
  * The GPLv2 notice.
  * import statements.
  * from... import statements.
  * Any other vital start-up code (in this case, `fuse.fuse_python_api = (0,2)`).
  * Classes.
  * Functions.
  * Main.

## Class Layout ##

  * Use standard class naming.
  * New-style classes:
> > `class example(object):`
  * Doc-string, formatted as such:
```
    """
    Documentation
    """
```
  * `__init__` function.
  * Other functions.

## Function Layout ##

  * Lower case names. White space to be denoted by "`_`":
```
    def example_func():
```
  * Doc-string, as in classes.

## Indentation ##

  * All indentation should be 4 spaces. Comments should, obviously, be indented along with code for clarity

# Example #

```
#!/usr/bin/env python
#
#   Copyright A N Other <a.n@other.com>, E X Ample <e.x@ample.com>
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

from time import time

fuse.fuse_python_api = (0,2)

class Example(object):
    """
    An example Class
    """
    def __init__(self):
        self.pretentious = True

    def a_life(self, get_one):
        """
        Purpose: Something a little like 1-Up.
        get_one: The function to call to give the user a life
        Returns: A life
        """
        self.life = get_one
        return self.life

def main():
    return 0
if __name__ == '__main__':
    main()
```