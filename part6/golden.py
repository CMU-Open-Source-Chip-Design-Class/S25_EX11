import os
import logging
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import *
from cocotb.runner import *
from cocotb.utils import get_sim_time

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

    dut.reset.value = 0
    dut.chr.value = 0
    dut.chr_valid.value = 0
    dut.check.value = 0

    # Reset the DUT (we must do this before feeding the password
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    password = input("What is the password? ")

    # Some basic code for parsing
    assert len(password) <= 40

    ts1 = get_sim_time("step")
    print("Sim time = ", ts1)

    # Feed the password into the DUT, one character at a time
    for char in password:
        dut.chr.value = ord(char)
        dut.chr_valid.value = 1
        await FallingEdge(dut.clk)

    ts2 = get_sim_time("step")
    print("Sim time = ", ts2)
    print("Feeding password took time = ", ts2-ts1)

    dut.check.value = 1
    await FallingEdge(dut.clk)
    dut.check.value = 0
    await FallingEdge(dut.clk)

    for i in range(200):
        await FallingEdge(dut.clk)
        if bool(dut.correct.value) or bool(dut.wrong.value):
            break


    ts3 = get_sim_time("step")
    print("Done, sim time = ", ts3)
    print("Checking password took time = ", ts3-ts2)

    if bool(dut.correct.value):
        print("PASSWORD CORRECT")

    elif bool(dut.wrong.value):
        print("PASSWORD WRONG")

    else:
        print("Something went wrong")

    assert bool(dut.correct.value)

## Boilerplate code for silencing warnings and running the tests
def run_test():
    sim = os.getenv("SIM", "icarus")

    verilog_sources = ["yoctf6.sv"]
    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="YoCTF6",
                test_module=os.path.splitext(os.path.basename(__file__))[0]+",",
                verbose=False)

if __name__ == "__main__":
    run_test()
