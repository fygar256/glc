#!/usr/bin/python3
import sys
argvs = sys.argv
argc = len( argvs )
greekc = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
if argc != 2:
  exit(1)
v = argvs[1].upper()
s = sum(greekc.find(c) + 1 for c in v)
print(s)
exit(0)
