## PART 1

The `yoctf1.sv` contains an obfuscated password-checker module. Following is the module header.

```
module YoCTF1 (
    input logic [3:0] dig1,
    input logic [3:0] dig2,
    input logic [3:0] dig3,
    output logic correct
);
```

Run `golden.py` with `python3 golden.py` to check if your password is correct.

DO NOT EDIT `golden.py` AS YOU NEED IT TO VERIFY THE CORRECTNESS OF YOUR SUBMISSION.

To get started, you will most likely want to make a copy of `golden.py` and write your brute-force code in the copy. 
