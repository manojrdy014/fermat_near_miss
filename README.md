# Fermat Near Miss Finder

## Overview
This program searches for integer **near misses** to Fermat's equation:
`x^n + y^n ≈ z^n`, for `3 ≤ n ≤ 11`, and `10 ≤ x,y ≤ k` where `k > 10`.
It reports the absolute miss and the relative miss (both as fraction and percent),
printing each time a new best (smallest relative miss) is found. The final best is printed last.

## Files in this repository
- `fermat_near_miss.py` — main source code (Python 3.x)
- `run.bat` — optional Windows run script (calls `python fermat_near_miss.py`)
- `run.sh` — optional Unix run script (`#!/bin/sh` then `python3 fermat_near_miss.py`)
- `README.md` — this file

## Requirements
- Python 3.8+ (tested with 3.10/3.11)
- No external libraries required.

## How to run
1. Clone the repo:
   ```
   git clone https://github.com/<your-username>/fermat-near-miss.git
   ```
2.changing directory:
   ```
   cd fermat-near-miss
   ``` 
3.Run the program:
Unix/macOS:
```
   python3 fermat_near_miss.py
```
Windows
```
   python fermat_near_miss.py


    

