#!/usr/bin/env python3

import os

types = [
    '00: ROM Only',
    '01: MBC1',
    '02: MBC1+RAM',
    '03: MBC1+Battery-Backed RAM',
    '04: UNKNOWN',
    '05: MBC2',
    '06: MBC2+Battery',
    '07: UNKNOWN',
    '08: ROM+RAM',
    '09: ROM+Battery-Backed RAM',
    '0A: UNKNOWN',
    '0B: MMM01',
    '0C: MMM01+SRAM',
    '0D: MMM01+SRAM+Battery',
    '0E: UNKNOWN',
    '0F: MBC3+Timer+Battery',
    '10: MBC3+Timer+RAM+Battery',
    '11: MBC3',
    '12: MBC3+RAM',
    '13: MBC3+Battery-Backed RAM',
    '14','15','16','17','18',
    '19: MBC5',
    '1A: MBC5+RAM',
    '1B: MBC5+Battery-Backed RAM',
    '1C: MBC5+Rumble',
    '1D: MBC5+Rumble+SRAM',
    '1E: MBC5+Rumble+SRAM+Battery',
    '1F: Pocket Camera'
    ]

for f in os.listdir('.'):
    if not os.path.isfile(f): continue
    with open(f, 'rb') as handle:
        handle.seek(0x0147)
        r = int.from_bytes(handle.read(1), 'little')
        if(r < len(types)):
            print('{t}\t{rom}'.format(t = types[r], rom = f))
        else:
            print('{t}\t{rom}'.format(t = hex(r), rom = f))

