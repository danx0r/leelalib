# Leela Library

This is a library of shared Python code.

## Installation

This is assuming you already have your github authentication set up with the host name github.com-leela in your ~/.ssh/config file something like this:

```
host github.com-leela
    hostname github.com
    user git
    IdentitiesOnly yes
    IdentityFile ~/.ssh/don-leela-ai.pem
    compression yes
```

To use this library without changing it, install from the github repo with pip3:

```
pip3 install git+ssh://git@github.com-leela/leela-ai/leelalib.git
```

To develop on this library, install it with the -e option to pip from github:

```
pip3 install -e git+ssh://git@github.com-leela/leela-ai/leelalib.git#egg=leelalib
```

or from a local repo:

```
cd lelalib
pip3 install -e .
```
