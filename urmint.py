#!/usr/bin/python

#Interpreter for URM as presented in Nigel Cutland's Computability textbook

import sys

maxregs = 32

def main():
    if len(sys.argv) == 1:
        raise RuntimeError('usage: python urmint.py <URM code> [register1 register2 ...]')

    if len(filter(lambda x: not x.isdigit, sys.argv[2:])) > 0:
        raise RuntimeError('error: registers must contain non-negative integers')

    if len(sys.argv[2:]) > maxregs:
        raise RuntimeError('error: too many registers (max is %d)' % maxregs)

    regs = map(int, sys.argv[2:]) + [0] * (maxregs - len(sys.argv[2:]))

    with open(sys.argv[1]) as f:
        instructions = map(parse, f.readlines())

    pc = 0
    step = 0
    while ( pc >= 0 and pc < len(instructions)):
        pc = execute(instructions, regs, pc)
        print(pc, regs)
        step+=1

    print('Output: %d' % regs[0] if 0 in regs else 0)


#parses instruction
# input: raw_instruction, a string with [IJTZ] followed by 1-3 int arguments
# output: a tuple representation of the former, eg ('T', 2, 1)
def parse( raw_instruction ):
    tokens = raw_instruction.split()
    if tokens[0] not in ['I', 'J', 'T', 'Z']:
        raise RuntimeError('Illegal opcode: ', tokens[0], " - expected [IJTZ]")
    if {'I':1, 'J':3, 'T':2, 'Z':1}[tokens[0]] != len(tokens[1:]):
        raise RuntimeError('Wrong number of args for op ', tokens[0])
    tokens[1:] = map(int, tokens[1:])
    if len(filter(lambda x: x > maxregs, tokens[1:])) > 0:
        raise RuntimeError('error: maximum register is ', maxregs)
    return tuple(tokens)

#executes instruction
# input:
#  instructions : the list of instruction tuples
#  regs         : the register list
#  pc           : program counter
# output: the new value for pc
def execute( instructions, regs, pc ):
    if(instructions[pc][0] == 'I'):
        regs[instructions[pc][1]] += 1
    elif(instructions[pc][0] == 'J'):
        if regs[instructions[pc][1]] == regs[instructions[pc][2]]:
            return instructions[pc][3]
    elif(instructions[pc][0] == 'T'):
        regs[instructions[pc][2]] = regs[instructions[pc][1]]
    elif(instructions[pc][0] == 'Z'):
        regs[instructions[pc][1]] = 0
    return pc + 1

if __name__ == '__main__':
    main()
