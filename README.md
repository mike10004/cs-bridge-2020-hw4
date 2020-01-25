# Homework Project Template

This repository is a template for projects that contain solutions to homework 
assignments for NYU Tandon CS Bridge Winter 2020.

To use this template, fork the repository and perform the following 
modifications:

1. change this readme to reflect that this is an assignment, not the template
2. modify `question.md`, `input.txt`, and `expected-output.txt` as appropriate 
   for the question; delete `input.txt` if no input is necessary
3. for each additional question, copy `q1` to a new subdirectory, add a 
   subdirectory line to `$PARENT/CMakeLists.txt`, change the project name and
   exectuable name in the new directory (e.g. from `q1` to `q2`) and repeat 
   step 2 for the new question  

You can have multiple test cases by naming your input files `input1.txt`, `input2.txt`,
and so on, and including corresponding expected outputs `expected-output1.txt`, etc.

## Commands

The `build.sh` and `clean.sh` scripts do what they sound like they do.

When you execute `check.sh`, for each executable, the executable is launched,
each line from `input.txt` is copied to the process standard input 
stream, and the output is checked against `expected-output.txt`.

This happens inside a `screen` session so that the input text is echoed to
the output, as would happen in a tty.

The `prepare.sh` command is executed when you're done writing all the code and
need the filenames to satisfy the instructors' convention. Each `main.cpp` file
is copied to the `stage` directory with a name of the form `${PREFIX}qN.cpp`,
where `${PREFIX}` is the argument you supply to the script. 

## License

Copyright (c) 2019 Mike Chaberski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.