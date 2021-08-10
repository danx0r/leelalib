from setuptools import setup, find_packages
from src.version import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="leelalib",
    version=version,
    py_modules=['config'],
    packages=find_packages(),
    python_requires='>=3.6',
    scripts=[],
    install_requires=[
        "PyYAML             >=5.3.1,    <6",
    ],
    include_package_data=True
)
