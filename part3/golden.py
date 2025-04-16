import os
import logging
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.runner import *

@cocotb.test()
async def check_password(dut):
    print("=========================================")
    print("============= STARTING TEST =============")
    print("=========================================")

    password = input("What is the password? ")

    # Some basic code for parsing
    assert len(password) == 16

    # Feed the password into the DUT
    # ord() is the python function for converting
    # a character to an ASCII code value
    # https://www.asciitable.com/

    dut.chr1.value  = ord(password[0])
    dut.chr2.value  = ord(password[1])
    dut.chr3.value  = ord(password[2])
    dut.chr4.value  = ord(password[3])
    dut.chr5.value  = ord(password[4])
    dut.chr6.value  = ord(password[5])
    dut.chr7.value  = ord(password[6])
    dut.chr8.value  = ord(password[7])
    dut.chr9.value  = ord(password[8])
    dut.chr10.value = ord(password[9])
    dut.chr11.value = ord(password[10])
    dut.chr12.value = ord(password[11])
    dut.chr13.value = ord(password[12])
    dut.chr14.value = ord(password[13])
    dut.chr15.value = ord(password[14])
    dut.chr16.value = ord(password[15])

    # Advance forward in time to let the simulation update
    await ReadOnly()

    # Check the output
    out = bool(dut.correct.value)
    print(f"correct = "+str(out))

    assert out

## Boilerplate code for silencing warnings and running the tests
def run_test():
    sim = os.getenv("SIM", "icarus")

    verilog_sources = ["yoctf3.sv"]
    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="YoCTF3",
                test_module=os.path.splitext(os.path.basename(__file__))[0]+",",
                verbose=False)

if __name__ == "__main__":
    run_test()
