#!/bin/bash

OUTPUT_DIR=${OUTPUT_DIR:-./stage}

PREFIX=$1

PREFIX_FILE="$OUTPUT_DIR/.prefix"

if [ -z "$PREFIX" ] ; then
  if [ -f "$PREFIX_FILE" ] ; then
    PREFIX=$(cat "$PREFIX_FILE")
    echo "prefix $PREFIX read from $PREFIX_FILE"
  else
    echo "no stored prefix found in $PREFIX_FILE" >&2
    echo "must specify prefix (e.g. 'net123_hw4_') as first argument" >&2
    exit 1
  fi
else
  mkdir -p "$OUTPUT_DIR"
  echo "$PREFIX" > "$PREFIX_FILE"
  echo "prefix $PREFIX stored in $PREFIX_FILE" >&2
fi

if [ -z "$PREFIX" ] ; then
  echo "prefix not valid; fix $PREFIX_FILE or specify argument if you try again" >&2
  exit 1
fi 

for QDIR in ./q*
do
  [[ -e "$QDIR" ]] || break   # in case of no q* directories
  CPP_FILE="$QDIR/main.cpp"
  QBASE="$(basename "$QDIR")"
  DST="${OUTPUT_DIR}/${PREFIX}${QBASE}.cpp"
  mkdir -p "$(dirname "$DST")"
  cp -v "$CPP_FILE" "$DST"
done

