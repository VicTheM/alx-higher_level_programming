#!/usr/bin/python3
bytecode = dis.Bytecode(myfunc)
for instr in bytecode:
	print(instr.opname)
