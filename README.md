colours
=======

Easy CLI colours for Python applications.

Installation
------------

Install from PyPI:

```python
pip install colours
```

Usage
-----

```python
from colours import colour

print colour.red('I am red!')
print colour.blue('I am blue!')
```

Available colours:

* black
* blue
* green
* cyan
* red
* purple
* yellow
* light_grey
* dark_grey
* bold_blue
* bold_green
* bold_cyan
* bold_red
* bold_purple
* bold_yellow
* bright_grey
* bright_blue
* bright_green
* bright_cyan
* bright_red
* bright_purple
* bright_yellow
* white

Stream Output
-------------

The colour methods take an optional argument of the stream you're passing the output to, in order to determine whether to actually colour the output or not. If the stream is a TTY, the output is coloured. If it isn't (such as a file, or the `sys.stdout` is being piped to another program), the output won't be coloured. You can also set this globally.

```python
from colours import colour

import sys

print colour.red('I am red unless this output is piped to another program', stream=sys.stdout)
print colour.blue('I am not blue because my output is a file', stream=open('output.txt', 'w'))

# Set the stream globally
colour.set_stream(sys.stdout)
print colour.green('Now I do not need to worry about passing the stream parameter.')
```
