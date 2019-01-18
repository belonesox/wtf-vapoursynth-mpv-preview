#!/bin/sh
vspipe --y4m release.py - | ffmpeg -i pipe: encoded.mkv