
def odds(max):
  return [n for n in range(1, max) if n % 2 == 1];
  # Python doesn't return the last expression automatically.
  # Since that might be a logical line of code.
  
def evens(max):
  return [n for n in range(1, max) if n % 2 == 0];

print(__name__);
# If you `python3 numbers.py` you'll get '__main__'.
# The importer of a module file decides the module's name.

counter = 0;
_private_counter = 0;

def incr_counter():
  global counter, _private_counter;
  # Python wants us to declare we expect these to have been initialised.
  
  counter += 1;
  _private_counter += 1;

if __name__ == "__main__":
  # Since any module finds its __name__ weirdly as '__main__'
  # when run directly, it can use it as a test.
  import sys
  print(evens(int(sys.argv[1])));
  # Parse error handling?

# Some Python programmers run the module's test suite on this.
# They import and call the module from the test package?
# Or they inline tests in the module..
