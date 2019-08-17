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

- Program Counter
- Instruction Register
- Accumulator

## BUS

- Data BUS

Read and write bytes from the CPU to RAM.

- Address BUS

Push and Pop the current Address for Reading and Writing byte data.

## RAM

Store all bytes data for the CPU to compute and store the computains from the CPU.

# Programming

## ByteCode

- 0 | End Operation
- 1 | Load into Accumulator
- 2 | Store Accumulator in Address
- 3 | Add to Accumulator
- 4 | Sub from Accumulator
- 5 | Jump to Address
- 6 | 
- 7 | 
- 8 | 
- 9 | 
- A | 
- B | 
- C | 
- D | 
- E | 
- F | No Operation

## micro Assembly Code

- END | End Operation
- LOD | Load into Accumulator
- STR | Store Accumulator in Address
- ADD | Add to Accumulator
- SUB | Sub from Accumulator
- JMP | Jump to Address
- 
- 
- 
- 
- 
- 
- 
- 
- 
- NOP | No Operation

## micro Programming Language

## Sample ByteCode Program

#### Loop Counter

```
HEX | ASM
16  | LOD 6
37  | ADD 7
26  | STR 6
51  | JMP 1
f0  | NOP
f0  | NOP
01  | 1
01  | 1
```
