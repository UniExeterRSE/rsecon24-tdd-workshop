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

We will be using the Pytest package for Python in this workshop. Experience
of testing with Pytest is helpful but not essential: we'll only be using the
most basic features of Pytest, and will explain them during the workshop.

Ahead of the workshop, you will need to

1. Download / clone the workshop materials (this repository!).
2. Create a virtual environment / Conda environment with required third party
   Python packages, using the Pip requirements file `envs/requirements.txt` or
   the Conda environment spec file `envs/conda.yml`.
3. Verify that Pytest was successfully installed into the environment created
   in 2.

Details on how to do this are provided below, should you need them.

Although not essential, you may wish to have Git installed to pull in any
changes to the material during the workshop, in the event that this is required.


### Step 1: Download / Clone this Repository

Clone this repository using Git or download the contents of
this repository as a zip archive (and unzip it). If you require details on how
to do this, you can refer to the following GitHub documentation links:

* [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)
* [Downloading a zip archive of the repository from the main branch](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives#downloading-source-code-archives-from-the-repository-view)
  (Refer to the section, **Downloading source code archives from the repository view**.)


### Step 2: Create a Virtual / Conda Environment with Required Packages

We recommend that you create a separate virtual / Conda environment for
installing the Python packages required for this workshop. You can use the
Python module `venv` for this, or Conda if you have this installed (or another
way of your choosing, if you have a favourite). See below if you require
details on how to do this.


#### Option 1: Via `venv`:

1. Create a new `venv` virtual environment called `.venv` in the root folder of
   this repository on your local machine. You can find instructions to do this
   in the section
   [Create a new virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-a-new-virtual-environment)
   from the
   [Python Packaging User Guide on using virtual environments and pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
   
2. Next, make sure to activate the virtual environment. Assuming you are located
   in the parent directory of the repository, run the following from a terminal
   (or a suitable command prompt for Windows):

   **MacOS / Unix**:
   
   ```
   source .venv/bin/activate
   ```

   **Windows**:
   
   ```
   .venv\Scripts\activate
   ```

3. Install the packages from the Pip requirements file
   `envs/requirements.txt`. 

   **MacOS / Unix**:
   
   ```
   python3 -m pip install -r envs/requirements.txt
   ```
   
   **Windows**:
   
   ```
   py -m pip install -r envs\requirements.txt
   ```


#### Option 2: Via `conda`:

1. Assuming you have `conda` installed, and are located in the parent directory
   of the repository, create a new environment from the
   file `envs/conda.yml`, by running the following from a terminal
   (or suitable command prompt for Windows):
   
   **MacOS / Unix**:
   
   ```
   conda env create -f envs/conda.yml
   ```

   **Windows**:

   ```
   conda env create -f envs\conda.yml
   ```

   This should create a new Conda environment, called `tdd-workshop`, with
   Python and Pytest installed within.
   
2. Activate the Conda environment:
   
   ```
   conda activate tdd-workshop
   ```


### Step 3: Verify Pytest installation in virtual / Conda environment

Step 2 should have installed Pytest into the virtual environment / Conda
environment that you created. To verify this, activate the environment and
run the following from a terminal (or suitable command prompt for Windows),
verifying that you don't get an error:

```
pytest --version
```

If this runs without error then you are all set for the workshop! We look
forward to welcoming you.
