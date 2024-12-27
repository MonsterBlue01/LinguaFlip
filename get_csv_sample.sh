#!/bin/bash

SAMPLE_SIZE=${1:-100}
INPUT_FILE=${2:-./data/processed/cleaned_en_es.csv}

if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: File $INPUT_FILE does not exist."
    exit 1
fi

BLOCK_SIZE=100000
echo "Sampling $SAMPLE_SIZE rows from the first $BLOCK_SIZE lines of $INPUT_FILE..."

head -n $BLOCK_SIZE "$INPUT_FILE" | shuf -n $SAMPLE_SIZE