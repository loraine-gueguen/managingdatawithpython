#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Synopsis : countlines.py is a trivial program to count lines in a (text) file.
Author : Mark HOEBEKE (mark.hoebeke@sb-roscoff.fr)

"""

infile = open("../data/fasta/cyanorak_complete.faa")
lines = infile.readlines()
print(len(lines))