## PART 6

The `yoctf6.sv` contains an obfuscated password-checker module. Following is the module header.

```
module YoCTF6 (
    input logic clk,
    input logic reset,

    input logic [7:0] chr,
    input logic chr_valid,
    input logic check,

    output logic wrong,
    output logic correct
);
```

Run `golden.py` with `python3 golden.py` to check if your password is correct.

DO NOT EDIT `golden.py` AS YOU NEED IT TO VERIFY THE CORRECTNESS OF YOUR SUBMISSION.

To get started, you will most likely want to make a copy of `golden.py` and write your code in the copy. 

Note that you can only make one attempt after every "reset" of the module. Also, the output will take multiple cycles to compute, at which point either "wrong" or "correct" will be set to 1 depending on the result.

The password is maximum 40 characters long

HINT: the first few characters of the password are `98154`
