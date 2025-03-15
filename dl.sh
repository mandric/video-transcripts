#!/bin/sh

# DibH4GRRWQU Lex and Guido
vidId="${1:-ApQ9NovgnA4}"
lang="${2:-en-US}"
youtube_transcript_api "$vidId" --languages "$lang" --format srt

