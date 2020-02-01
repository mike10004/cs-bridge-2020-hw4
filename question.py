#!/usr/bin/env python3

"""
    question.py generates a new question subdirectory
"""

import re
import shutil
import sys
import logging
import threading
import uuid
import tempfile
import os.path
import subprocess
from subprocess import PIPE, DEVNULL
import time
from argparse import ArgumentParser
from typing import List, Tuple, Optional, NamedTuple


_log = logging.getLogger(__name__)


_QUESTIONMD_TEMPLATE = """\
# Question {n}

Write a program...
"""

_CMAKELISTSTXT_TEMPLATE = """
cmake_minimum_required(VERSION 3.7)
project({q_name})

set(CMAKE_CXX_STANDARD 14)

add_executable({q_name} main.cpp)
"""

_MAINCPP_TEMPLATE = """\
// Question {n}

#include <iostream>

using namespace std;

int main()
{
    cout << "{q_name} executed" << endl;
    return 0;
}
"""

def detect_next_qname(proj_dir):
    child_dirs = []
    for root, dirs, _ in os.walk(proj_dir):
        for d in dirs:
            child_dirs.append(os.path.join(root, d))
        break
    q_names = list(filter(lambda d_: re.match(r'^q\d+$', d_), map(os.path.basename, child_dirs)))
    q_numerals = []
    for q_name in q_names:
        try:
            q_numerals.append(int(q_name[1:]))
        except ValueError as e:
            _log.debug("failed to parse numeral from q_dir %s due to %s", q_name, e)
    _log.debug("existing q names: %s; numerals = %s", q_names, q_numerals)
    if not q_numerals:
        return 'q1'
    return "q{}".format(max(q_numerals) + 1)


def _render(template: str, q_name: str, output_file: str):
    model = {
        'q_name': q_name,
        'n': q_name[1:]
    }
    with open(output_file, 'w') as ofile:
        ofile.write(template.format(**model))


def populate(proj_dir, q_dir):
    q_name = os.path.basename(q_dir)
    skel_dir = os.path.join(proj_dir, 'skel')
    shutil.copytree(skel_dir, q_dir)
    _log.debug("copied skel to %s", q_dir)
    q_cmakelists_file = os.path.join(q_dir, 'CMakeLists.txt')
    _render(_CMAKELISTSTXT_TEMPLATE, q_name, q_cmakelists_file)
    _render(_QUESTIONMD_TEMPLATE, q_name, os.path.join(q_dir, 'question.md'))
    _render(_MAINCPP_TEMPLATE, q_name, os.path.join(q_dir, 'main.cpp'))
    _log.debug("generated question.md and CMakeLists.txt")


def config_root_proj(proj_dir, q_name):
    root_cmakelists_file = os.path.join(proj_dir, 'CMakeLists.txt')
    with open(root_cmakelists_file, 'a') as ofile:
        print(f"add_subdirectory(\"${{PROJECT_SOURCE_DIR}}/{q_name}\" \"${{PROJECT_SOURCE_DIR}}/{q_name}/cmake-build\")", file=ofile)
    _log.debug("appended subdirectory line to %s", root_cmakelists_file)

def main():
    this_file = os.path.abspath(__file__)
    proj_dir = os.path.dirname(this_file)  # also might want to handle the case where script piped in on stdin
    parser = ArgumentParser()
    parser.add_argument("name", nargs='?', help="name of subdirectory, e.g. 'q2'")
    parser.add_argument("-l", "--log-level", metavar="LEVEL", choices=('DEBUG', 'INFO', 'WARNING', 'ERROR'), default='INFO', help="set log level")
    args = parser.parse_args()
    logging.basicConfig(level=logging.__dict__[args.log_level])
    q_name = args.name if args.name is not None else detect_next_qname(proj_dir)
    q_dir = os.path.join(proj_dir, q_name)
    populate(proj_dir, q_dir)
    config_root_proj(proj_dir, q_name)
    return 0


if __name__ == '__main__':
    exit(main())
