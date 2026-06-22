#!/usr/bin/env python3
"""oracle.py — built-in solo oracle (used when mythic-gm is NOT present;
if mythic-gm IS loaded, defer yes/no, scene, and event to it). Honest, shown.
Commands:
  augury <odds> <turmoil>     yes/no on d100 (odds: certain..impossible)
  scene <turmoil>             expected / altered / interrupt (1d10)
  event                       random event: focus + two meaning words
Odds: certain, nearly-certain, very-likely, likely, 50/50, unlikely, very-unlikely,
      nearly-impossible, impossible
"""
import random, sys
def d(n): return random.randint(1, n)
ODDS = {"certain":95,"nearly-certain":90,"very-likely":80,"likely":70,"50/50":50,
        "unlikely":30,"very-unlikely":20,"nearly-impossible":10,"impossible":5}
FOCUS = [(0,7,"Remote event"),(8,28,"NPC action"),(29,35,"New NPC"),(36,45,"Move toward a thread"),
         (46,52,"Move away from a thread"),(53,55,"Close a thread"),(56,67,"PC negative"),
         (68,75,"PC positive"),(76,83,"Ally negative"),(84,92,"Ally positive"),
         (93,100,"Current context shift")]
ACTIONS = ["Betray","Bestow","Demand","Pursue","Conceal","Threaten","Bargain","Reveal",
           "Hunt","Bind","Corrupt","Liberate","Usurp","Mourn","Ascend","Sacrifice","Awaken","Ruin"]
THEMES = ["fate","blood","jade","ghosts","ambition","exile","famine","sorcery","oaths","empire",
          "the wild","memory","divinity","plague","rebellion","hunger","masks","the dead","gold","ruin"]
def augury(odds, turmoil):
    odds = odds.lower().replace(" ","-")
    if odds not in ODDS: sys.exit(f"unknown odds '{odds}'")
    base = ODDS[odds]; t = int(turmoil)
    yes = max(2, min(99, base + (t-5)*5))
    r = d(100)
    exc_yes = max(1, yes//5); exc_no = 100 - max(1, (100-yes)//5)
    if r <= exc_yes: ans = "EXCEPTIONAL YES"
    elif r <= yes: ans = "YES"
    elif r >= exc_no: ans = "EXCEPTIONAL NO"
    else: ans = "NO"
    tens, ones = divmod(r, 10)
    ev = (tens == ones) and (ones if ones else 10) <= t
    print(f"🔮 AUGURY [{odds} @ turmoil {t}]  yes≤{yes}")
    print(f"   d100 = {r}  → {ans}" + ("   ⚡RANDOM EVENT (run: oracle.py event)" if ev else ""))
def scene(turmoil):
    t=int(turmoil); r=d(10)
    out = "EXPECTED" if r>t else ("ALTERED" if r%2 else "INTERRUPT")
    print(f"🎬 SCENE [turmoil {t}]  1d10={r} → {out}")
def event():
    r=d(100); foc=next(f for lo,hi,f in FOCUS if lo<=r<=hi)
    a=ACTIONS[d(len(ACTIONS))-1]; th=THEMES[d(len(THEMES))-1]
    print(f"⚡ EVENT  focus d100={r} → {foc}\n   meaning: {a} / {th}")
def main():
    a=sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    if a[0]=="augury": augury(a[1], a[2])
    elif a[0]=="scene": scene(a[1])
    elif a[0]=="event": event()
    else: sys.exit("unknown cmd; see --help")
if __name__=="__main__": main()
