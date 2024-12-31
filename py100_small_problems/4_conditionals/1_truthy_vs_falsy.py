# Without looking at your notes or the official documentation, try to recall all values that count as falsy in Python.

falsy_values = [ None, 0, 0j, False, '', [], {}, (), set(), range(0) ]

print(any(falsy_values))
