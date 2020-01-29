#!/usr/bin/env python3

# make_test_cases.py
import json
import math
import os.path
import sys
import traceback
from argparse import ArgumentParser
from typing import NamedTuple, List, Dict, Any, Optional
import logging


_log = logging.getLogger(__name__)
_DEFAULT_CASE_ID_PRECISION = 2
_DEFAULT_DEFINITIONS_FILENAME = "test-cases.json"
_DEFAULT_TEST_CASES_DIRNAME = "test-cases"


def to_pathname(filename, disable_mkdir=False):
    pathname = os.path.join(os.path.dirname(__file__), 'test-cases', filename)
    if not disable_mkdir:
        os.makedirs(os.path.dirname(pathname), exist_ok=True)
    return pathname


def write_case(case_id: int, case):
    case_id = f"{case_id:02d}"
    day, time, duration, cents = case
    intext = f"{day}\n{time}\n{duration}\n"
    in_filename = f"input{case_id}.txt"
    with open(to_pathname(in_filename), 'w') as ofile:
        ofile.write(intext)
    extext = f"""\
Enter day of week call was started: {day}
Enter time of day call was started (24-hour format): {time}
Enter length of call in minutes: {duration}
Cost of call: {cents // 100} dollars and {cents % 100} cents
"""
    ex_filename = f"expected-output{case_id}.txt"
    with open(to_pathname(ex_filename), 'w') as ofile:
        ofile.write(extext)
    print(f"{in_filename} and {ex_filename} written")


class ParameterSource(NamedTuple):
    
    input_text_template: str
    expected_text_template: str
    test_cases: List[Dict[str, Any]]
    case_id_precision: Optional[int]
    
    def __str__(self):
        return f"ParameterSource<num_test_cases={len(self.test_cases)}>"
    
    def precision(self):
        if self.case_id_precision is not None:
            return self.case_id_precision
        return 1 + int(math.log10(len(self.test_cases)))
    
    def render_input_text(self, test_case):
        return self.input_text_template.format(**test_case)
    
    def render_expected_text(self, test_case):
        return self.expected_text_template.format(**test_case)
    
    @staticmethod
    def load(model: Dict) -> 'ParameterSource':
        test_cases = []
        try:
            input_text_template = model['input']
        except KeyError:
            raise ValueError("model does not define 'input'")
        try:
            expected_text_template = model['expected']
        except KeyError:
            raise ValueError("model does not define 'expected'")
        try:
            param_names = None
            for test_case in model['test_cases']:
                if isinstance(test_case, dict):
                    test_cases.append(test_case)
                else:
                    case_dict = {}
                    param_names = param_names or model.get('param_names', None)
                    if param_names is None:
                        raise ValueError("'param_names' must be defined if array test cases are defined")
                    for i in range(len(param_names)):
                        case_dict[param_names[i]] = test_case[i]
                    test_cases.append(case_dict)
        except KeyError:
            _log.warning("test cases not defined")
            pass
        precision = model.get('case_id_precision', None)
        return ParameterSource(input_text_template, expected_text_template, test_cases, precision)


def write_cases(param_source: ParameterSource, dest_dir: str, suffix=".txt"):
    nsuccesses = 0
    for i, test_case in enumerate(param_source.test_cases):
        try:
            rendered_input = param_source.render_input_text(test_case)
            case_id = ("{0:0" + str(param_source.precision()) + "d}").format(i + 1)
            input_filename = f"input{case_id}{suffix}"
            input_pathname = os.path.join(dest_dir, input_filename)
            os.makedirs(os.path.dirname(input_pathname), exist_ok=True)
            with open(input_pathname, 'w') as ofile:
                ofile.write(rendered_input)
            expected_filename = f"expected-output{case_id}{suffix}"
            expected_pathname = os.path.join(dest_dir, expected_filename)
            os.makedirs(os.path.dirname(expected_pathname), exist_ok=True)
            with open(expected_pathname, 'w') as ofile:
                ofile.write(param_source.render_expected_text(test_case))
            nsuccesses += 1
        except Exception:
            exc_info = sys.exc_info()
            info = traceback.format_exception(*exc_info)
            _log.debug("writing cases: exception traceback:\n%s", "".join(info).strip())
            e = exc_info[1]
            _log.warning("failed to write cases to %s: %s, %s", dest_dir, type(e), e)
            continue
    _log.debug("%s of %s test cases generated in %s", nsuccesses, len(param_source.test_cases), dest_dir) 

def find_all_definitions_files(top_dir: str, filename: str) -> List[str]:
    defs_files = []
    for root, dirs, files in os.walk(top_dir):
        for f in files:
            if f == filename:
                defs_files.append(os.path.join(root, f))
    return defs_files


def main():
    parser = ArgumentParser()
    parser.add_argument("subdirs", nargs='*', metavar="DIR", help="subdirectory containing test case definitions file")
    parser.add_argument("--definitions-filename", metavar="BASENAME", default=_DEFAULT_DEFINITIONS_FILENAME, help="filename of the file (within a subdirectory) that contains test case definitions")
    parser.add_argument("--dest-dirname", default="test-cases", metavar="BASENAME", help="destination directory name (relative to definitions file location)")
    parser.add_argument("-l", "--log-level", default="INFO", metavar="LEVEL", choices=('DEBUG', 'WARN', 'ERROR', 'INFO'))
    args = parser.parse_args()
    logging.basicConfig(level=logging.__dict__[args.log_level.upper()])
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    if not args.subdirs:
        defs_files = find_all_definitions_files(proj_dir, args.definitions_filename)
        args.subdirs = list(map(os.path.dirname, defs_files))
    else:
        defs_files = map(lambda d: os.path.join(d, args.definitions_filename), args.subdirs)
        defs_files = list(filter(os.path.exists, defs_files))
    nsuccesses = 0
    for defs_file in defs_files:
        try:
            with open(defs_file, 'r') as ifile:
                model = json.load(ifile)
            param_source = ParameterSource.load(model)
            dest_dir = os.path.join(os.path.dirname(defs_file), args.dest_dirname)
            write_cases(param_source, dest_dir)
            nsuccesses += 1
        except Exception:
            exc_info = sys.exc_info()
            info = traceback.format_exception(*exc_info)
            _log.debug("exception info:\n%s", "".join(info).strip())
            e = exc_info[1]
            _log.warning("failure to load model and write cases from %s: %s, %s", defs_file, type(e), e)
            continue
    _log.debug("test cases generated from %s of %s definitions files", nsuccesses, len(defs_files))
    if nsuccesses == 0:
        _log.error("test case generation did not succeed for any of %s definitions file", len(defs_files))
    return 0 if nsuccesses > 0 else 2


if __name__ == '__main__':
    exit(main())
