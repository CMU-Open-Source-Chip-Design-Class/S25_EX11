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
    assert len(password) == 3
    assert password[0].isdigit()
    assert password[1].isdigit()
    assert password[2].isdigit()

    # Feed the password into the DUT
    dut.dig1.value = int(password[0])
    dut.dig2.value = int(password[1])
    dut.dig3.value = int(password[2])

    # Advance forward in time to let the simulation update
    await ReadOnly()

    # Check the output
    out = bool(dut.correct.value)
    print(f"correct = "+str(out))

    assert out

## Boilerplate code for silencing warnings and running the tests
def run_test():
    sim = os.getenv("SIM", "icarus")

    verilog_sources = ["yoctf1.sv"]
    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="YoCTF1",
                test_module=os.path.splitext(os.path.basename(__file__))[0]+",",
                verbose=False)

if __name__ == "__main__":
    run_test()
