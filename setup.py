print("LEELALIB SETUP.PY")

from setuptools import setup, find_packages

import os, sys
print("PATH", sys.path)
print("CWD", os.getcwd())
os.system('ls -la "' + os.getcwd() + '"')

from leelalib.version import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="leelalib",
    version=version,
    py_modules=['config'],
    packages=find_packages(where="leelalib"),
    python_requires='>=3.6',
    scripts=[],
    install_requires=[
        "PyYAML             >=5.3.1,    <6",
    ],
    include_package_data=True
)
