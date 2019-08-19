# microVM

A really simple virtual machine, that loads a basic bytecode into ram and executes it. 

### VM

- Load / Run

Load BIN files into RAM and execute them.

- Compiler

Compile .mvm ASM code into .bin binary files of ByteCode.

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
- Read
- Write
- Load

## BUS

- Send
- Receive
- Push
- Pop
- Load
- Clear

#### Data BUS

Read and write bytes from the CPU to RAM.

- Read
- Write
- Load
- Clear

#### Address BUS

Push and Pop the current Address for Reading and Writing byte data.

- Push
- Pop
- Peek
- Clear

## RAM

Store all bytes data for the CPU to compute and store the computains from the CPU.

# Programming

## ByteCode
DEC  HEX ASM   
 0 - 0 - END | End Operation
 1 - 1 - LOD | Load into Accumulator
 2 - 2 - STR | Store Accumulator in Address
 3 - 3 - ADD | Add to Accumulator
 4 - 4 - SUB | Sub from Accumulator
 5 - 5 - JMP | Jump to Address
 6 - 6 -     | 
 7 - 7 -     | 
 8 - 8 -     | 
 9 - 9 -     | 
10 - A -     |
11 - B -     | 
12 - C -     | 
13 - D -     | 
14 - E - NUM | Number
15 - F - NOP | No Operation

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
- NUM | Number
- NOP | No Operation

## micro Programming Language

## Sample ByteCode Program

#### Loop Counter

```
HEX     | ASM
------------------
01 06   | LOD 6
03 07   | ADD 7
02 06   | STR 6
05 01   | JMP 1
0f 00   | NOP 0
0f 00   | NOP 0
00 01   | NUM 1
00 01   | NUM 1
```
