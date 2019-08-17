# microVM

A really simple virtual machine, that loads a basic bytecode into ram and executes it. 

## CPU

Step Cycle CPU that you can set the processing speed of. The CPU consists of a few basic functions.

- Fetch

Get the current byte from the current RAM Address on the BUS.

- Decode

Read the current Byte and Parse it to be Executed.

- Execute

Execute the the current command. 

## BUS

- Data BUS

Read and write bytes from the CPU to RAM.

- Address BUS

Push and Pop the current Address for Reading and Writing byte data.

## RAM

Store all bytes data for the CPU to compute and store the computains from the CPU.

# Programming

## ByteCode

- 00 | End Operation
- FF | No Operation

## micro Assembly Code

- END | End Operation
- NOP | No Operation

## micro Programming Language


