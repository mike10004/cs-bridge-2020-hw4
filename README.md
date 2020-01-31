# Homework Project Template

This repository is a template for projects that contain solutions to homework 
assignments for NYU Tandon CS Bridge Winter 2020.

To use this template, clone, fork, or otherwise duplicate the repository and 
perform the following modifications:

1. change this readme to reflect that this is an assignment, not the template
2. modify `question.md`, `input.txt`, and `expected-output.txt` as appropriate 
   for the question; delete `input.txt` if no input is necessary
3. for each additional question, copy `q1` to a new subdirectory, add a 
   subdirectory line to `$PARENT/CMakeLists.txt`, change the project name and
   exectuable name in the new directory (e.g. from `q1` to `q2`) and repeat 
   step 2 for the new question  

You can have multiple test cases by naming your input files `input1.txt`, `input2.txt`,
and so on, and including corresponding expected outputs `expected-output1.txt`, etc.

## Clone or duplicate?

Which one to do here depends on how you want to use your working copy. If you only 
plan to keep the local copy, then just clone the repo and create a new branch for 
the new homework assignment. If you want to push your work to a remote repository, 
then it's probably best to [duplicate](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository), 
meaning you create a new repository in your GitHub account, clone the repo, and 
mirror-push to your new repo. Then you clone the new repo.

## Commands

### Build

The `build.sh` and `clean.sh` scripts do what they sound like they do.

To run `build.sh`, your system must have `make` and `cmake` available.
If they are not available on the path, use environment variables `MAKE`
and `CMAKE` to define their absolute pathnames. 

For example, if you have `cmake` from a CLion installation, then execute

    $ export CMAKE=$PATH_TO_CLION/bin/cmake/linux/bin/cmake

`$CLION_INSTALL_DIR/bin/cmake/linux/bin/cmake` to a location on your
path.

On Linux, you can install `make` with `sudo apt install build-essentials`.

### Check

The program `check.py` runs the build script and then runs tests cases
for each executable. (The build script depends on `cmake` and `make`; 
see note above.)

The check program uses `screen` to capture input and output that would be seen 
in an interactive terminal. Test cases are defined by corresponding pairs of 
files named `input*.txt` and `expected-output*.txt` in the question 
subdirectory (or anywhere beneath it). 

Execute 

    $ ./check.py --help

to see options for running the test cases. For example, you can execute

    $ ./check.py q3 

to run only the `q3` test cases. Test cases are run in parallel, but you 
can control that with the `--threads` option.

### Generate Test Cases

Create a test cases definitions file named `test-cases.json` in a question 
subdirectory, following the example in `q2/test-cases.json`. Execute

    $ ./make_test_cases.py [SUBDIR]

to generate input files and expected output files for each subdirectory that
contains a test cases definitions file. Specifying `SUBDIR` is optional, and 
causes the program to generate test cases only for the definitions file in 
the specified subdirectory. 

### Prepare

The `prepare.sh` command is executed when you're done writing all the code and
need the filenames to satisfy the instructors' convention. Each `main.cpp` file
is copied to the `stage` directory with a name of the form `${PREFIX}qN.cpp`,
where `${PREFIX}` is the argument you supply to the script. For example, 

    $ ./prepare.sh abc123_hw3_

would copy your `q1/main.cpp` to `abc123_hw3_q1.cpp` and likewise for the
other `main.cpp` files in subdirectories.
