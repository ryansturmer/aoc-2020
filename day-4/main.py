import sys
import re

HEIGHT_RE = re.compile(r'^\s*(\d+)\s*(cm|in)\s*$')
HAIR_RE = re.compile(r'^#[0-9a-f]{6}$')
PN_RE = re.compile(r'^\d{9}$')

def is_valid(p):
    reasons = []
    if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
        try:
            assert 1920 <= int(p['byr']) <= 2002, 'byr'
            assert 2010 <= int(p['iyr']) <= 2020, 'iyr'
            assert 2020 <= int(p['eyr']) <= 2030, 'eyr'
            assert len(p['eyr']) == 4, 'eyr'
            h,u = HEIGHT_RE.match(p['hgt']).groups()
            assert 150 <= int(h) <= 193 if u == 'cm' else 59 <= int(h) <= 76, 'hgt'
            assert HAIR_RE.match(p['hcl']), 'hcl'
            assert p['ecl'].strip() in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 'ecl'
            assert PN_RE.match(p['pid']), 'pid'
        except Exception as e:
            return True, False
        return True, True
    else:
        return False, False

with open(sys.argv[1]) as fp:
    records = ['']
    for line in fp.readlines():
        if not line.strip():
            records.append('')
            continue
        records[-1] = records[-1] + line.replace('\n',' ')
    passports = map(dict, [[kv.split(':') for kv in line.split()] for line in records if line.strip()])

    part1 = part2 = 0
    for p in passports:
        p1,p2 = is_valid(p)
        part2 += 1 if p2 else 0
        part1 += 1 if p1 else 0

    print('Part 1: ', part1)
    print('Part 2: ', part2)


