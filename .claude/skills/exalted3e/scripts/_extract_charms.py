#!/usr/bin/env python3
"""Extract the Lunar Charm catalog from the vault into charms/lunar_<attr>.md + an index.
Distill each charm to its stat line + a 1-line effect summary, with a vault citation."""
import re, os, pathlib
VAULT="vault/Exalted 3e - Lunars - Fangs at the Gate.md"
OUT="charms"; CITE="Fangs at the Gate"
ATTRS=["Appearance","Charisma","Dexterity","Intelligence","Manipulation","Perception","Stamina","Strength","Wits"]
START,END=3725,14905
lines=open(VAULT,encoding="utf-8").read().split("\n")
def field(blk,key):
    m=re.search(rf"{key}:\s*(.+)",blk)
    return m.group(1).strip() if m else "—"
cur=None; i=START-1; charms={a:[] for a in ATTRS}; index=[]
while i<min(END,len(lines)):
    ln=lines[i].strip()
    m3=re.match(r"^###\s+(.+)$",ln)
    if m3 and m3.group(1).strip() in ATTRS: cur=m3.group(1).strip(); i+=1; continue
    m4=re.match(r"^####\s+(.+)$",ln)
    if m4 and cur:
        name=m4.group(1).strip()
        # gather block until next #### or ###
        j=i+1; blk=[]
        while j<min(END,len(lines)) and not re.match(r"^#{3,4}\s",lines[j]):
            blk.append(lines[j]); j+=1
        btext="\n".join(blk)
        if re.search(r"Cost:",btext):   # it's a real charm
            cm=re.search(r"Cost:\s*(.+?);\s*Mins:\s*([^\n]+)",btext)
            if cm: cost=cm.group(1).strip(); mins=cm.group(2).strip()
            else: cost=field(btext,"Cost"); mins=field(btext,"Mins")
            typ=field(btext,"Type")
            kw=field(btext,"Keywords"); dur=field(btext,"Duration"); pre=field(btext,"Prerequisite Charms")
            # effect = first non-empty, non-field paragraph
            eff=""
            for p in blk:
                ps=p.strip()
                if ps and not re.match(r"^(Cost|Mins|Type|Keywords|Duration|Prerequisite|Archetype|Special)",ps) and ps!="EX3":
                    eff=ps; break
            eff=re.sub(r"\s+"," ",eff)[:240]
            charms[cur].append((name,cost,mins,typ,kw,dur,pre,eff))
            index.append((cur,name,mins))
        i=j; continue
    i+=1
# write per-attribute files
total=0
for a in ATTRS:
    cs=charms[a]; total+=len(cs)
    out=[f"# Lunar Charms — {a}", f"*{len(cs)} charms · source: {CITE} › Charms › {a}. Full text in vault.*",""]
    for (name,cost,mins,typ,kw,dur,pre,eff) in cs:
        out.append(f"### {name}")
        out.append(f"Cost {cost} · Mins {mins} · {typ} · Kw {kw} · Dur {dur}" + (f" · Prereq {pre}" if pre and pre!='None' else ""))
        if eff: out.append(f"{eff}  ‹{CITE} › {a} › {name}›")
        out.append("")
    pathlib.Path(f"{OUT}/lunar_{a.lower()}.md").write_text("\n".join(out),encoding="utf-8")
# index
idx=["# Lunar Charm Index", f"*{total} Lunar charms across 9 Attributes. Load charms/lunar_<attribute>.md for full entries.*",""]
for a in ATTRS:
    idx.append(f"## {a} ({len(charms[a])})")
    idx.append(", ".join(n for (n,_,_,_,_,_,_,_) in charms[a]) or "—"); idx.append("")
pathlib.Path(f"{OUT}/00_charm_index.md").write_text("\n".join(idx),encoding="utf-8")
print(f"Extracted {total} Lunar charms across {len(ATTRS)} attributes")
for a in ATTRS: print(f"  {a}: {len(charms[a])}")
