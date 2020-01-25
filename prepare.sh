#!/bin/bash

OUTPUT_DIR=${OUTPUT_DIR:-./stage}

PREFIX=$1

PREFIX_FILE="$OUTPUT_DIR/.prefix"

if [ -z "$PREFIX" ] ; then
  if [ -f "$PREFIX_FILE" ] ; then
    PREFIX=$(cat "$PREFIX_FILE")
  else
    echo "must specify prefix (e.g. 'net123_hw4_') as first argument" >&2
    exit 1
  fi
fi

set -e

for QDIR in ./q*
do
  [[ -e "$QDIR" ]] || break   # in case of no q* directories
  CPP_FILE="$QDIR/main.cpp"
  QBASE="$(basename "$QDIR")"
  DST="${OUTPUT_DIR}/${PREFIX}${QBASE}.cpp"
  mkdir -p "$(dirname "$DST")"
  cp -nv "$CPP_FILE" "$DST"
done

