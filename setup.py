from setuptools import setup, find_packages
setup(
    name="leelalib",
    version="0.0.0b1",
#    py_modules=['config'],
    packages=find_packages(),
    python_requires='>=3',
#    scripts=[],
    install_requires=[
        "PyYAML             >=5.3.1,    <6",
    ],
    include_package_data=True
)
