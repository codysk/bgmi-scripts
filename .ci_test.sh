#!/bin/bash
for f in *.py; do
  coverage run -a "$f"
done
