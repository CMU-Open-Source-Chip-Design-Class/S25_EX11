## PART 2

The `yoctf2.sv` contains an obfuscated password-checker module. Following is the module header.

```
module YoCTF2 (
    input logic clk,
    input logic [3:0] dig,
    input logic dig_valid,
    output logic correct
);
```

Run `golden.py` with `python3 golden.py` to check if your password is correct.

DO NOT EDIT `golden.py` AS YOU NEED IT TO VERIFY THE CORRECTNESS OF YOUR SUBMISSION.

To get started, you will most likely want to make a copy of `golden.py` and write your brute-force code in the copy. 
