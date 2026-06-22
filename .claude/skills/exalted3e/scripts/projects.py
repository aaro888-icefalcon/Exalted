#!/usr/bin/env python3
"""projects.py — 'Changing Creation' cost (Scope x Magnitude + Opposition). No RNG.
  cost --scope <hamlet|town|region|nation|realm> --mag <plausible|improbable|impossible> [--opp N ...]
"""
import sys
SCOPE={"hamlet":1,"town":2,"city":2,"region":4,"province":4,"nation":8,"house":8,"realm":16,"direction":16}
MAG={"plausible":1,"improbable":2,"impossible":4}
def main():
    a=sys.argv[1:]
    if not a or a[0]!="cost": print(__doc__); return
    def opt(f,dv,c=str): return c(a[a.index(f)+1]) if f in a else dv
    sc=opt("--scope","town").lower(); mg=opt("--mag","plausible").lower()
    opp=sum(int(x) for i,x in enumerate(a) if a[i-1]=="--opp")
    if sc not in SCOPE or mg not in MAG: sys.exit(f"scope:{list(SCOPE)} mag:{list(MAG)}")
    cost=SCOPE[sc]*MAG[mg]+opp
    print(f"⚙  PROJECT cost = scope({sc}={SCOPE[sc]}) × magnitude({mg}=×{MAG[mg]}) + opposition({opp}) = {cost}")
    print(f"   pay from Resources/Backgrounds/downtime intervals/faction Reach.")
    if mg=="impossible": print(f"   IMPOSSIBLE → requires Mighty Deeds (adventures) to buy down cost; permanent only with lasting investment.")
if __name__=="__main__": main()
