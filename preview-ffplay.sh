#!/bin/sh
vspipe --y4m release.py - | ffplay -i pipe: