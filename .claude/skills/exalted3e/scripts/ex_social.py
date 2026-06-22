#!/usr/bin/env python3
"""ex_social.py — Exalted 3e social influence (honest, shown).
  influence <pool> --resolve R [--intimacy N] [--appeal up|down]
     roll (Charisma/Manip + Ability) pool vs target Resolve (instill/persuade) or Guile.
     --intimacy N: an Intimacy supporting the influence adds N dice (+1 Minor/+2 Major/+3 Defining);
                   an opposing Defining Intimacy can make the influence simply fail (note it).
  resolve --integrity I --wits W [--app A]   quick Resolve estimate (2 + traits)
"""
import random, sys
def roll(n,double=10,target=7):
    n=max(0,int(n)); dice=sorted((random.randint(1,10) for _ in range(n)),reverse=True)
    return sum(1+(1 if v>=double else 0) for v in dice if v>=target), dice
def main():
    a=sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    def opt(f,dv,c=int): return c(a[a.index(f)+1]) if f in a else dv
    if a[0]=="influence":
        pool=int(a[1]); res=opt("--resolve",3); inti=opt("--intimacy",0)
        eff=pool+inti; succ,dice=roll(eff)
        print(f"🗣  INFLUENCE: ({pool}+{inti} Intimacy)={eff}d10={dice} → {succ} succ vs Resolve {res}")
        if succ>=res: print(f"   SUCCESS (threshold {succ-res}) — target's stance shifts / acts as urged")
        else: print(f"   FAILED (short {res-succ}) — no change; cannot retry without new leverage")
    elif a[0]=="resolve":
        base=2+opt("--integrity",0)//1; print(f"Resolve ≈ {2+opt('--integrity',0)+0} (2 + relevant; raise via Intimacies)")
    else: sys.exit("see --help")
if __name__=="__main__": main()
