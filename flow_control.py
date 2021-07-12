#!/usr/bin/python3

#str = input("Please give me an integer: ")
#num = int(str)
num = 20
# I'm guessing we can optionally exception catch.
# Perhaps this alone makes people recommend Python over Java.
# Optional error handling was a feature of BASIC.

if num < 0:
	#print(num = 0, "");
	# Among other reasons, Python can't allow this due to positional arguments.
	print("Negative..");
elif num == 0: print("Zero.")
elif num > 0: print("Positive..")

if False: pass
#else: if True: print("Hmm");  # There was an attempt.
elif True: print("Hmm");

words = ['my IME is not working', 'goodbye']
for w in words: print(w, len(w))

room = {}
room["bear"] = "inactive"
room["koala"] = "active"
room["kangaroo"] = "not sure how to explain"
print(room)

for user, status in room.copy().items():
	if status == 'inactive':
		del room[user];
# Rather than preserve your iterator by assembling/modifying a copy,
# this iterates over a copy and modifies the original in-place. Interesting.

room["bear"] = "inactive"  # Bring back kicked user.
copy = {}
for user, status in room.items():
	if status != 'inactive':
		copy[user] = status
# Depending on your scenario there's a bunch of things you can do with a copy.
# This one's a standard filter.

print(range(6))  # There was an attempt. This is a generator function.
for off in range(5): print(off)  # Range defaults at start 0.
for ind in range(1, 6): print(ind)  # Also, range never visits end.
for x in range(0, 85, 10): print(x)

lines = [ 'append', 'edit', 'replace', 'insert', 'write' ]
for off in range(len(lines)): print(off, lines[off])

print(sum(range(6)))  # One reason having range be an iterable is useful.

for o1 in range(10):
	for o2 in range(10):
		for o3 in range(10):
			print("o3", end=' ');
			break;
		print("o2", end=' ');
		break;
	print("o1", end=' ');
	break;
print();

for line in lines:
	if line == 'concatenate':
		print(line);
		break;
else:  # what!
	print("Couldn't find.");

# Fairly convenient over throwing an exception or keeping a variable around.

class StubClass:
	pass

def printer(seq):
	"A docstring can be any string literal."
	for item in seq: print(str(item))

printer(["string", 4, "number", 6, "even", 7])
#help(printer)

# They say that variable lookup traverses all the symbol tables, but
# variable assignment works only on the local symbol table by default.
# Global variables are marked assignable through 'global',
# normally local symbols of enclosing functions 'nonlocal'.

if None: pass
if True: None
# Python doesn't have "nil", it's "None".
# The pass statement seems a bit unnecessary if expressions can be standalone..

class StubClass2:
	None;  # Oui. This works.

print(StubClass2);

def aDecentlyLong(strings):
	for string in strings:
		if (len(string) > 4): return string;
	# We don't have to explicitly return some null.
	# Fallthrough, or return without argument, returns None.

print(aDecentlyLong(['no', 'a long string']));
print(aDecentlyLong(['no']))
print(aDecentlyLong([]))

def dangerous(item, prev=[]):
	prev.append(item);
	return prev;
print(dangerous("One"));
print(dangerous("Two"));
# Default argument being mutated between calls!
# Not a fresh variable declaration as expected.

def safe(item, prev=None):
	if not prev: prev = [];  # Manually default the unspecified.
	prev.append(item);
	return prev;

print(safe("One"));
print(safe("Two", prev=safe("One")));

def curious(number, *addi_pos, **addi_kw):
	for o in range(len(addi_pos)):
		print("..", o, addi_pos[o], "..");
	for k, v in addi_kw.items():
		print("..", k, v, "..");
	return number + 1;

print(curious(4, 6, 5, seven=7, eight=8));
# And we know that (I recall noting somewhere..) we can
# force arguments to be positional or keyword.

print(list(range(4, 5)))
print(list(range(*[4, 5])))
curious(1, **{"start": 4, "end": 5})  # Can't test on range since it takes no kwargs.

perhaps = lambda x: print(x)
perhaps("?")
# Though, Python does have a fairly rich argument system.
# I'm guessing lambdas don't have that luxury?

filesizes = [ ("test.txt", 16), ("music.zip", 64234), ("demo.doc", 1024) ]
filesizes.sort(key = lambda listing: listing[1])
print(filesizes)

def andEggs(ham: str, eggs: str = 'tempeh') -> str:
	print(andEggs.__annotations__);
	return ham + " and " + eggs;

print(andEggs('onion'));

# Note that what follows the colon or arrow is an expression.
# Which will actually be evaluated! __annotations__ show that
# they were identified as the Python class 'str'. Kind of scary.
