#!/usr/bin/env python3

# make_test_cases.py
import json
import os.path
from argparse import ArgumentParser
from typing import NamedTuple, List, Dict, Any
import logging


_log = logging.getLogger(__name__)
_DEFAULT_CASE_ID_PRECISION = 2


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
    case_id_precision: int
    
    def render_input_text(self, test_case):
        return self.input_text_template.format(*test_case)
    
    def render_expected_text(self, test_case):
        return self.expected_text_template.format(*test_case)
    
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
        except KeyError:
            _log.warning("test cases not defined")
            pass
        precision = model.get('case_id_precision', _DEFAULT_CASE_ID_PRECISION)
        return ParameterSource(input_text_template, expected_text_template, test_cases, precision)


def write_cases(param_source: ParameterSource, dest_dir: str, suffix=".txt"):
    for i, test_case in enumerate(param_source.test_cases):
        rendered_input = param_source.render_input_text(test_case)
        case_id = ("{0:0" + str(param_source.case_id_precision) + "d}").format(i)
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


_DEFAULT_DEFINITIONS_FILENAME = "test-case-definitions.json"
_DEFAULT_TEST_CASES_DIRNAME = "test-cases"


def find_all_definitions_files(top_dir: str, filename: str) -> List[str]:
    defs_files = []
    for root, dirs, files in os.walk(top_dir):
        for f in files:
            if f == filename:
                defs_files.append(os.path.join(root, f))
    return defs_files


def main():
    parser = ArgumentParser()
    parser.add_argument("subdirs", nargs='*', metavar="DIR", help="subdirectories containing test case definitions")
    parser.add_argument("--definitions-filename", default=_DEFAULT_DEFINITIONS_FILENAME)
    parser.add_argument("--dest-dirname", default="test-cases", help="destination directory name (relative to definitions file location)")
    args = parser.parse_args()
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    if not args.subdirs:
        defs_files = find_all_definitions_files(proj_dir, args.definitions_filename)
        args.subdirs = list(map(os.path.dirname, defs_files))
    else:
        defs_files = list(map(lambda d: os.path.join(d, args.definitions_filename), args.subdirs))
    nsuccesses = 0
    for defs_file in defs_files:
        with open(defs_file, 'r') as ifile:
            model = json.load(ifile)
        try:
            param_source = ParameterSource.load(model)
            dest_dir = os.path.join(os.path.dirname(defs_file), args.dest_dirname)
            write_cases(param_source, dest_dir)
        except Exception as e:
            _log.warning("failure to load model and write cases from %s: %s", defs_file, e)
            continue
    return 0


if __name__ == '__main__':
    exit(main())
