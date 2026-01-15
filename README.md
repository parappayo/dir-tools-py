# dir-tools-py

This is a dumping ground for one-off tools that walk file directories. No warranties are made here. Use at your own risk.

## fold-up.py

This program looks in the given root dir and finds subdirectories (non-recursively) with the structure "A/A/" where "A/" contains no other content than the dir "A/A/". It then outputs a series of "mv" and "rmdir" commands to flatten those subdirs out. For example, a directory that contains a lot of zip extracts might have cruft like this.
