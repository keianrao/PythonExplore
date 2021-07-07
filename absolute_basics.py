#!/usr/bin/python3

True;  # Expressions can be standalone.
	#Spurious tabs are fine for comment-only lines.
text = "# Ceci n'est pas une remarque."
text = ""

print(5 + 10)
print(100 - 5*20)

print(9 / 5)  # 1.8. Division always floats.
print(9 // 5)
print(9 % 5)  # Note that strings have a % operator too.

print(60**2)
print(60**0.5)

count = 2
print(count)
count = 2 * 5
print(count)

try: offset  # NameError.
except: pass  # I think any block with only one line can..

print(4 * 3.5)  # (x + 0.5) * (2y) = xy + y.   3.5 * 4 = 2*6 + 2.
# Anyways, result is a float.

provincialTax = 8 / 100
nationalTax = 5 / 100  # If I recall correctly.
subtotal = 144.99
extra = (subtotal * provincialTax) + (subtotal * nationalTax)
total = subtotal + extra
print(total)
print(round(total, 2))
print(round(total), 2)

print('Single-quoted string.')
print("Double-quoted string.")
print('This isn\'t not an escape.')
print('"Nested quotes."')

print('"This\'s a perfectly fine string, when passed to print."')
print("""
I think they're following Lisp conventions, where if you evaluate
an expression in the interpreter, it gives you it in a format that's
suitable for feeding back into the interpreter. This can seem a bit
inconsistent but really, it won't be in the exam.
""")
print("""\
By the way, escaped newlines in a \
multi-line string are omitted.
""")

print(r"\n, \r, \t, are not in this raw string.")

print(("fee" + "fi" + "fo" + "fum... ") * 4);

print('Adjacent literals' 'are concatenated')
print('Decent for a function that accepts'
	' a string.')
text = 'If not conveniently in parentheses like so, can\n' \
	'wrap in parentheses anyways, or escape newlines.'
print(text)

print("Print"[0])
print("Print"[-1])
print("Print"[0:2])
print("Print"[2:])
print("Print"[:2] + "Print"[2:])

text = "Strings are immutable sequences."
try: text[:] = "Strings are mutable sequences."
except: pass

print(text[-len(text):])

list_literal = [2**2, 2**2**2, 2**2**2**2]
print(list_literal)
print(list_literal[1:], "What sequence is this?")

text = "As an rvalue, are strings references or values?"
text2 = text;
text2 = "You cannot know, since strings cannot be mutated."
text = "A philosophical riddle?"

list_literal_2 = list_literal;
list_literal_2[0] = 8;
print(list_literal, "Anyways, lists as rvalues are references.")
list_literal_2[0] = 2**2;
list_literal_2 = list_literal[:]
list_literal_2[0] = 8;
print(list_literal, "Repaired.")
print(list_literal_2, "Use the side effect of slicing (always returns")
print(" " * len(str(list_literal)), "a new sequence) to shallow copy.")

print([1, 2] + [5, 6])
try: print([1, 2] - [1])
except: print("Technically we can write an function for [1, 2] - [1].")

comedically_large = 2**2**2**2**2
list_literal.append(len(str(comedically_large -- 2**2**2**2)))  # append to extend in-place.

list_literal[0] = []
print(list_literal)
list_literal[:1] = []
print(list_literal)
print(len(list_literal), "Use builtins len() and str() for any sequence.")

text = "fancy"
off1, off2 = 0, len(text) - 1
while off1 != len(text):
	print(text[off1], text[off2])
	off1 += 1
	off2 -= 1
off1, off2 = 0, len(text) - 1
n = 5
while n:
	print(text[off1], text[off2], end=' ')
	off1, off2 = off2, off1  # Multiple assignment.
	n -= 1
print()
# For languages without multiple assignment, I think
# you can simulate it by using a typeless stack..
# Casting back would be terrible though.

# Python, by being less verbose, is quite readable without syntax highlighting.
# Compared to TypeScript.
