# RSECon 2024 workshop: An Introduction to Test-Driven Development

This repository contains materials to support the workshop
**An Introduction to Test-Driven Development**, delivered at
[RSECon 2024](https://rsecon24.society-rse.org/).

⚠ **The material in this repository is under construction and subject to change
without notice. The main content is expected to be finalised by 31 August
2024.** ⚠


## Workshop Prerequisites

The programming language used throughout the workshop will be Python, so you
should be comfortable programming in this language and come expecting to write
code, in whatever IDE / text editor works for you. In particular, you should
have Python installed on the machine you bring to the workshop.

We will also be using the Pytest package for Python in this workshop. Experience
of testing with  Pytest is helpful but not essential: we'll only be using the
most basic features of Pytest, and will explain them during the workshop.

Ahead of the workshop, participants will need to download the workshop materials
(this repository!) and create a virtual environment / Conda environment with
required third party Python packages; details are provided below. Although not
essential, users may wish to have Git installed, in case there is the need to
update the material in this repository during delivery.


### Download / Clone this Repository

TODO: links to GitHub docs


### Create a Virtual / Conda Environment with Required Packages

We recommend that you create a separate virtual / Conda environment for
installing the Python packages required for this workshop. You can use the
Python module `venv` for this, or Conda if you have this installed (or another
way of your choosing, if you have a favourite). 


#### Via `venv`

Create a new `venv` virtual environment called `.venv` in the root folder of this
repository on your local machine. You can find instructions to do this in the section [Create a new virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-a-new-virtual-environment)
from the [Python Packaging User Guide on using virtual environments and pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).


Next, install the packages from the Pip requirements file, `envs/requirements.txt`.

TODO: complete


#### Via `conda`

Assuming you have `conda` installed, you can create a new environment from the
file `envs/tdd-workshop.yml`:

```
conda create -f envs/tdd-workshop.yml
```

This should create a new Conda environment, called `tdd-workshop`, with Python
and Pytest installed within.

TODO: complete.

