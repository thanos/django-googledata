import os
os.system('python setup.py sdist --formats=gztar,zip')
os.system('python setup.py bdist_egg')
