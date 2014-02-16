#!/usr/bin/env python
import os
#Add pydevd to the PYTHONPATH (may be skipped if that path is already added in the PyDev configurations)
import sys;sys.path.append(r'D:\Dev\eclipse\pydev\plugins\org.python.pydev_2.7.5.2013052819\pysrc')

import pydevd #@UnresolvedImport
pydevd.patch_django_autoreload()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
