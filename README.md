# microVM

A really simple virtual machine, that loads a basic bytecode into ram and executes it. 

### VM

- Load / Run

	- Load BIN files into RAM and execute them.

- Compiler

	- Compile '.mvm' files containing mVM ASM code into '.bin' binary files of mVM ByteCode.

## CPU

Step Cycle CPU that you can set the processing speed of. The CPU consists of a few basic functions.

- Fetch

	- Get the current byte from the current RAM Address on the BUS.

- Decode

	- Read the current Byte and Parse it to be Executed.

- Execute

	- Execute the the current command. 

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

Store all bytes data for the CPU to compute and store the output from the CPU.

# Programming

## microVM ByteCode
```
HEX 
00 | End Operation
01 | Load into Accumulator
02 | Store Accumulator in Address
03 | Add to Accumulator
04 | Sub from Accumulator
05 | Jump to Address
06 | Print to Console
07 | 
08 | 
09 | 
0A |
0B | 
0C | 
0D | 
0E | Number
0F | No Operation
```

## microVM Assembly Code
```
END | End Operation
LOD | Load into Accumulator
STR | Store Accumulator in Address
ADD | Add to Accumulator
SUB | Sub from Accumulator
JMP | Jump to Address
PNT | Print to Console
-   |
-   |
-   |
-   |
-   |
-   |
-   |
NUM | Number
NOP | No Operation
```

## microVM Programming Language

```
```

## Sample microVM Program

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
