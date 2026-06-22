#!/usr/bin/env python3
"""ex_dice.py — Exalted 3e d10 dice pool (honest, shown). Also generic dice.
Commands:
  pool <N> [--diff D] [--double X] [--target T] [--stunt S] [--rerolls]
       roll N d10; success = die>=T (default 7); a die>=X (default 10) counts DOUBLE
       (Ex3 'double 10s' is on by default). Botch = 0 successes AND at least one 1.
  roll <NdM[+/-K]> [adv|dis]   generic dice for tables/generators
"""
import random, re, sys
def d(n): return random.randint(1, n)
def cmd_pool(N, diff=None, double=10, target=7, stunt=0, label=None):
    N = int(N) + int(stunt)
    dice = sorted((d(10) for _ in range(N)), reverse=True)
    succ = sum((1 + (1 if v >= double else 0)) for v in dice if v >= target)
    ones = sum(1 for v in dice if v == 1)
    botch = (succ == 0 and ones > 0)
    print(f"🎲 POOL {N}d10" + (f"  (stunt +{stunt})" if stunt else "") +
          f"  [TN {target}, double {double}{', diff '+str(diff) if diff is not None else ''}]")
    print(f"   dice: {dice}")
    line = f"   SUCCESSES: {succ}"
    if diff is not None:
        thr = succ - int(diff)
        line += f"   vs diff {diff} → " + (f"SUCCESS (threshold {thr})" if thr >= 0 else f"FAIL (short {-thr})")
    if botch: line += "   ⚠ BOTCH"
    print(line)
def cmd_roll(expr, mod=None):
    m = re.match(r"(\d*)d(\d+)([+-]\d+)?$", expr.replace(" ", ""))
    if not m: sys.exit("roll expects NdM[+/-K]")
    n = int(m.group(1) or 1); s = int(m.group(2)); k = int(m.group(3) or 0)
    def once(): return [d(s) for _ in range(n)]
    if mod in ("adv", "dis"):
        r1, r2 = once(), once(); a, b = sum(r1)+k, sum(r2)+k
        pick = max(a, b) if mod == "adv" else min(a, b)
        print(f"🎲 {expr} {mod}: {r1}={a} / {r2}={b} → {pick}")
    else:
        r = once(); print(f"🎲 {expr} = {r}{('%+d'%k) if k else ''} → {sum(r)+k}")
def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    def opt(f, dv=None, cast=str):
        return cast(a[a.index(f)+1]) if f in a else dv
    if a[0] == "pool":
        pos = a[1]
        cmd_pool(pos, diff=opt("--diff",None,int), double=opt("--double",10,int),
                 target=opt("--target",7,int), stunt=opt("--stunt",0,int))
    elif a[0] == "roll":
        cmd_roll(a[1], a[2] if len(a) > 2 else None)
    else: sys.exit("unknown cmd; see --help")
if __name__ == "__main__": main()
