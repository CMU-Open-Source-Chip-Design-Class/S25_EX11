import os
import logging
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.runner import *

@cocotb.test()
async def check_password(dut):
    print("=============================================================================")
    print("=============================================================================")
    print("============== STARTING TEST ================================================")
    print("=============================================================================")
    print("=============================================================================")

    # Run the clock
    cocotb.start_soon(Clock(dut.clk, 10, units="sec").start())

    # Since our circuit is on the rising edge,
    # we feed inputs on the falling edge
    # This makes things easier to read and visualize
    await FallingEdge(dut.clk)

    password = input("What is the password? ")

    # Some basic code for parsing
    assert len(password) == 3
    assert password[0].isdigit()
    assert password[1].isdigit()
    assert password[2].isdigit()

    # Feed the password into the DUT, one character at a time
    for digit in password:
        dut.dig.value = int(digit)
        dut.dig_valid.value = 1
        await FallingEdge(dut.clk)

    # Check the output
    out = bool(dut.correct.value)
    print(f"correct = "+str(out))

    assert out

## Boilerplate code for silencing warnings and running the tests
def run_test():
    sim = os.getenv("SIM", "icarus")

    verilog_sources = ["yoctf2.sv"]
    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="YoCTF2",
                test_module=os.path.splitext(os.path.basename(__file__))[0]+",",
                verbose=False)

if __name__ == "__main__":
    run_test()
