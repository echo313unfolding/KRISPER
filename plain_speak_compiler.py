#!/usr/bin/env python3
import re, sys, json, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.krisper_ir import Program

VERBS = [
    (r"^download (?P<url>\S+) to (?P<path>\S+)$",
     lambda m,p: p.add("http_get", url=m["url"]).add("write_file", path=m["path"], from_last=True)),
    (r'^run "(?P<cmd>.+)"$',
     lambda m,p: p.add("run", cmd=m["cmd"])),
    (r"^run (?P<cmd>.+)$",
     lambda m,p: p.add("run", cmd=m["cmd"])),
    (r"^every (?P<secs>\d+)(s| sec| seconds): (?P<cmd>.+)$",
     lambda m,p: p.add("loop", interval=int(m["secs"]), body=[{"kind":"run","args":{"cmd":m["cmd"]}}])),
    (r"^sleep (?P<secs>\d+)$",
     lambda m,p: p.add("sleep", seconds=int(m["secs"]))),
    (r"^write '(?P<data>.*)' to (?P<path>\S+)$",
     lambda m,p: p.add("write_file", path=m["path"], data=m["data"])),
]

def compile_lines(lines):
    prog = Program()
    for raw in [l.strip() for l in lines if l.strip()]:
        matched=False
        for pat,fn in VERBS:
            m = re.match(pat, raw, flags=re.I)
            if m: 
                fn(m, prog)
                matched=True
                break
        if not matched:
            prog.add("comment", text=raw)  # don't fail; carry through
    return prog

if __name__ == "__main__":
    text = sys.stdin.read()
    prog = compile_lines(text.splitlines())
    print(json.dumps(prog.to_dict(), indent=2))