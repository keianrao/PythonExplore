#!/usr/bin/env python3

letters = [ 'z', 'y', 'c', 'w', 'g' ];
letters.append('t');
print(letters);  # Append mutates

letters[len(letters):] = [ 'k' ];
print(letters);
# Any assignment by slice, even if it introduces elements, mutates
#letters2 = letters[len(letters):] = [ 'k' ];
# More obvious if you try to assume it's not. Chained equals appears.

addees = { 'p': 0, 'q': 1, 'r': 3 };
for iterated in addees: print(iterated);
# When a dictionary is iterated, it returns keys.
letters.extend({ 'p': 0, 'q': 1, 'r': 3 });
print(letters);

letters.insert(0, 'f');
letters.insert(len(letters), 'b');
letters.insert(1, 'v');
print(letters);
letters.insert(len(letters) + 10, 'a');
letters.insert(-2, 'm');
print(letters);
# letters.insert lacks bound errors. For exceeds, it seems it just adds
# to the end. For subceeds, it interprets it as index from end of list.
# For the behaviour of exceeds, the description says 'will insert before
# element whose index is given' - adding to end of list technically
# results in addee being before that index.
# 
# I wonder how many Python methods have forgiving behaviour like this.

letters.remove('v');
try: letters.remove('e');
except: pass;
# And proceed to be unforgiving like this. 

print(letters);
letters.pop();
letters.pop(0);
print(letters);

lettersbak = list(letters);
letters[len(letters)//2:] = [];
print(letters);
del letters[1:];
print(letters);
letters.clear();
print(letters);
# Readability? Fundamental difference in how these work?
letters = lettersbak;
del lettersbak;
# We can delete within the variable, or we can delete just the variable.
print(letters);
print(letters.index('z'), letters.index('b'));
print(letters.index('q', -5));
try: print(letters.index('k', -5));
except: pass;

letters.sort();
print(letters);  # Mutate sort.
letters.reverse();

lettersbak = list(letters);
lettersbak2 = letters[:];
lettersbak3 = lettersbak.copy();
print(lettersbak);
print(lettersbak2);
print(lettersbak3);
# Data structure constructors copy elements.
# Slicing creates copies.
# Do the standard data structures consistently implement copy?
# Or is it more like, each has their own clone method.

# The docs say any method that mutates in-place will return None,
# as a hint.

try: letters.push('j');
except: pass;
letters.append('j');
letters.pop();
print(letters);
letters.insert(0, 'j');
letters.pop(0);
print(letters);
# I expected lists to be singly-linked lists, but they say that
# if you change elements before the end it's inefficient because
# the rest of the list have to be shifted. Which is strange.
# Anyways, they recommend a deque.

roots = [];
for n in range(1, 11): roots.append(pow(n, 0.5)); 
print(roots);
# The builder. Even Lisps do this I thought?

rootgen_inst = map(lambda n: pow(n, 0.5), range(1, 11));
print(rootgen_inst);
print(list(rootgen_inst));
# Python is interesting here in how it doesn't evaluate the map.

roots.clear();
roots = [pow(n, 0.5) for n in range(1, 11)];
print(roots);
# An inline-expression, followed by binds.
# A bit hard to memorise and reason about..

pairs = [(glyph, word) for glyph in [ '0', '1', '2' ] \
  for word in [ 'zero', 'one', 'two' ]];
print(pairs);
# Standard binding does a sort of two-level loop.
# Docs say you should read it like it were blocks of code,
# 'for _ in _' like a for loop, 'if _' like an if block.
# Order matters, per this logic.

numbers = [ 5, 10, 15 ];
print([n / numbers[0] for n in numbers]);
print([n for n in numbers if n % 10 == 0]);
numbers = [ [5], [10], [15] ];
print([n for sublist in numbers for n in sublist]);
# Can make temporary bindings like so.

# So much for "hard to reason about". It's just like control structures.

matrix = [
  [ 1, 5, 4, 3 ],
  [ 0, 2, 2, 2 ],
  [ 0, 0, 0, 2 ]
];
print([row for row in matrix]);
print([o for o in range(4)]);
print([[row[o] for row in matrix] for o in range(4)]);
# The inner comprehension collects row[o] for each row into a list.
# The outer comprehension collects the lists from the inner.

print(*matrix);
print(list(zip(*matrix)));
# The * spreads elements of the seq as separate arguments.
# zip tuples elements from its multiple list arguments.

strange = 10, 20, 30;
# Was this added in Python 3?
# Tuples literally being values separated by commas.
double = strange, (5, 15, 25);
print(double);

n_ai_pas = ();
a_une = 4,;
a_une_deux = (2);
print(n_ai_pas);
print(a_une);
print(a_une_deux);
# Nice try! (2) just resolves to 2.
a_une_deux = (2,);
print(a_une_deux);

stranger = 0x50, 9.9, True;
# Tuple packing.
hex, float, bool = stranger;
# Tuple unpacking.
print(hex, float, bool);
del hex, float, bool;
print(hex(10));

a, b = 4, 5;
a, b = b, a;
print(a, b);
# Python implements multiple assignment by not really.
# The expected syntax for multiple assignment conveniently
# ends up as tuple packing and unpacking.
# In that case, any language that allows arbitrary lists/tuples
# can provide multiple assignment?

dict = {};
set = set();
set = { 'Ocean', 'Land', 'Air' };
print('Ocean' in set);
print('Ocean' in ['Ocean']);
del set;
set = set('a string');
print(set);
# Boolean operations like |, &, ^ all work on sets.
del set;
set = { letter for letter in 'peter piper' };
print(set);
# Tuple comprehensions aren't a thing, but set comprehensions are.
del set;

dict = { 'a': 'A' };
dict['b'] = 'B';
del dict['a'];
# dict addition, removal.
print(dict);
try: print(dict['c']);
except: pass;
print(list(dict));  # Like in iteration, a list of keys.
print('c' in dict);

del dict;
kv_pairs = (('A', 1), ('B', 2), ('C', 3));
print(dict(kv_pairs));
# If you happen to have a list of pairs around, you can pass it
# to dict's constructor.

print({ letter: letter.capitalize() for letter in ('a', 'b', 'c') });
dict = dict(a='A', b='B', c='C');
# dict handles arbitrary keyword arguments.

print(list(dict));
print(list(dict.items()));
del dict;

hmm = [ list(), tuple(), set() ];
print(hmm);
print(list(enumerate(hmm)));

keys = [k for (k, v) in kv_pairs];
values = [v for (_, v) in kv_pairs];
print(keys, values);
for k, v in zip(keys, values): print(k, v);
# You don't have to zip into a sequence.

print(hmm);
print(list(reversed(hmm)));
# You can make a reverseiterator for many things.
# Useful for looping, not needing to reverse the sequence beforehand.
# Similarly, rather than seq.sort(), try sorted(seq).

unsorted = [ 'Vanilla', 'Chocolate', 'Strawberry' ];
sorted = list(sorted(unsorted));
print(sorted, unsorted);
del sorted;

something = None;
another = 'a';
print(something and something.capitalize());
print(another and another.capitalize());
# Python has the quirk that boolean expressions return the last 
# component visited. This provides a sort of basic safe navigation.
# But note that I have a named preevaluated expression here.
# It's not the safe navigation operator - I can't build expressions.
# Really, this is equal to but terser than
# something == None ? None : something.capitalize().
