#!/usr/bin/python3
import dis

def print_defined_names():
    with open("hidden_4.pyc", "rb") as f:
        bytecode = f.read()
    instructions = dis.get_instructions(bytecode)
    names = set()
    for instruction in instructions:
        if instruction.opname == "LOAD_NAME" and not instruction.argrepr.startswith("<"):
            names.add(instruction.argrepr)
    for name in sorted(names):
        print(name)
