# Fermat Near Miss Finder

## Overview
This program searches for integer **near misses** to Fermat's equation:
`x^n + y^n ≈ z^n`, for `3 ≤ n ≤ 11`, and `10 ≤ x,y ≤ k` where `k > 10`.
It reports the absolute miss and the relative miss (both as fraction and percent),
printing each time a new best (smallest relative miss) is found. 
- **Absolute miss** = the smaller of `|x^n + y^n - z^n|` or `|(z+1)^n - (x^n + y^n)|`  
- **Relative miss** = `absolute_miss / (x^n + y^n)`

Every time a new smallest relative miss is found, it is printed.  
After all combinations are tested, the program prints the **final (smallest) relative miss** and pauses for the user to review the output.

## Files in this repository
- `fermat_near_miss.py` — main source code (Python 3.x)
- `README.md` — this file

## Requirements
- Python 3.8+ (tested with 3.10/3.11)
- No external libraries required.

## How to run
1. Clone the repo:
   `
   git clone https://github.com/<your-username>/fermat-near-miss.git
   `
2.changing directory:
   `
   cd fermat-near-miss
   `
3.Run the program:
Unix/macOS:
`
   python3 fermat_near_miss.py
`
Windows
`
   python fermat_near_miss.py
`

->Notes
  -Input validation ensures that:
     3 ≤ n ≤ 11
     k > 10
  -Only integers are accepted
  -The program handles large values gracefully (Python supports big integers)
  -For very large k, execution may take a while

    

