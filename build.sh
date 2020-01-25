#!/bin/bash

set -e

THIS_DIR=$(dirname "$0")
BUILD_DIR="${THIS_DIR}/cmake-build-debug"

cmake -DCMAKE_BUILD_TYPE=Debug -S "${THIS_DIR}" -B "${BUILD_DIR}"

pushd "${BUILD_DIR}" >/dev/null

make

popd >/dev/null
