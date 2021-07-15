
first_ten = [
  1, 2, 4, 8,
  16, 32, 64, 128,
  256, 512
];

from . import b3;
next_first_ten = b3.first_ten;
# Apparently these kind of imports only work if you're not __main__?
# "Based on the name of the module", though I thought modules had no
# intrinsic names.
