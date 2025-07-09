#!/bin/bash

while true; do
    DURATION=5  # seconds
    RAW_FILE="record_raw.wav"
    CLEAN_FILE="clean_record.wav"

    echo "Cleaning older records"
    rm -f $CLEAN_FILE $RAW_FILE

    echo "Recording audio for $DURATION seconds..."
    sox -d -c 1 -r 16000 $RAW_FILE trim 0 $DURATION

    echo "Re-encoding to PCM 16-bit WAV..."
    sox $RAW_FILE -c 1 -r 16000 -b 16 $CLEAN_FILE

    echo "Done. Clean audio saved in $CLEAN_FILE"

    echo "Running docker"
    output=$(docker run --rm -v $(pwd)/$CLEAN_FILE:/app/record.wav audio-processor)

    echo "$output"

    echo "Press Ctrl+C to stop or wait to record again..."
done
