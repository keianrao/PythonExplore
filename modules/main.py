#!/usr/bin/env python3

import numbers;

print(numbers.evens(10));
print(numbers.odds(20));

# Since you can grab functions, you can just assign it to a variable.
evens = numbers.evens;
print(evens(20));

import numbers;
# Python keeps track of how many times something has been imported.

# Since modules are namespaced, they can put variables in their
# top-level, not worrying about name collisions when imported.
numbers.counter += 1;
numbers.incr_counter();
print(numbers.counter);

from numbers import odds;
print(odds(4));

from numbers import *;
try: _private_counter += 1;
except: pass;
# Underscored symbols are ignored when mass importing.

numbers._private_counter += 1;
print(numbers._private_counter);
# Not actual security. But definitely reveals invasive use.

import numbers as nbrs
print(nbrs.evens(-5))
# Depending on implementation detail (to not fail, instead [])

from importlib import reload as module_reload;
module_reload(numbers);
# Note that this will re-run the module's top-level code.
print(counter);
print(numbers.counter);
# Hmmm....

import sys
sys.path += [ "bizarre" ];
import bizarre;
# Goodness, that actually worked. Adding a plain name into path refers
# to it in the current directory, I'm guessing.

# When you use modules, __pycache__ will be created, and CPython
# at least would compile the modules and put them there. The directory
# sticks after execution is over, Python recompiles the modules if
# the source files have been modified since.

import no_longer_existent;
# I grabbed the .pyc from __pycache__, but had to rename away the
# version suffix. And, you have to place it among your actual sources.

print(dir());
print(__file__);

def print_builtins():
  import builtins;
  print(dir(builtins)[-4:]);
  
print_builtins();
print("bizarre" in dir());
print("builtins" in dir());
# I wonder how that local import works.

import strange_lists.one;
print(strange_lists.one.cycling);

from normal_lists.bases import *;
try: print(b2.first_ten);
except: pass;
import normal_lists.bases.b2;
from normal_lists.bases import *;
print(b2.first_ten);
print(b2.next_first_ten);
