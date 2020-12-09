import sys
import re

RE_INSTRUCTION = re.compile(r'(nop|acc|jmp)\s*((?:\+|\-)?\d+)\n?')

class YouDidItEverybodyYoureDoingGreatExceptionKeepUpTheGoodWork(Exception):
    def __init__(self, pc, acc, reason):
        self.pc = pc
        self.acc = acc
        self.reason = reason

def execute(program):
    pc = acc = 0
    seen = set()

    while True:
        if pc in seen:
            raise YouDidItEverybodyYoureDoingGreatExceptionKeepUpTheGoodWork(pc, acc, 'infinite')
        elif pc == len(program):
            raise YouDidItEverybodyYoureDoingGreatExceptionKeepUpTheGoodWork(pc, acc, 'end')
        elif pc < 0 or pc > len(program):
            raise YouDidItEverybodyYoureDoingGreatExceptionKeepUpTheGoodWork(pc, acc, 'exception')
        else:
            seen.add(pc)

        op,n = program[pc]
        
        if op == 'acc':
            acc += n
            pc += 1
        elif op == 'jmp':
            pc += n
        elif op == 'nop':
            pc += 1
        else:
            raise Exception("ERROR'D!")

def part1(program):
    try:
        execute(program)
    except YouDidItEverybodyYoureDoingGreatExceptionKeepUpTheGoodWork as e:
        print("Part 1:", e.acc)

def part2(program):
    for pc,(op, n) in enumerate(program):
        if op in ('jmp', 'nop'):
            pgp = program[:]
            pgp[pc] = ('nop',pgp[pc][1]) if op == 'jmp' else ('jmp',pgp[pc][1])
            try:
                execute(pgp)
            except YouDidItEverybodyYoureDoingGreatExceptionKeepUpTheGoodWork as e:
                if e.reason == 'end':
                    print('Part 2: %d (Changed %s to %s at %s)' % (e.acc, op, pgp[pc][0], pc))
                else:
                    continue


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        program = map(lambda line : RE_INSTRUCTION.match(line).groups(), fp.readlines())
        program = list(map(lambda x : (x[0], int(x[1])), program))

        part1(program)
        part2(program)