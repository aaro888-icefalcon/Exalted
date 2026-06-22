#!/usr/bin/env python3
"""Extract Core martial-arts styles into charms/martial_arts/<style>.md, and index
ALL style headings across every vault book (so any style can be pulled on request)."""
import re, os, glob, pathlib
def field(blk,key):
    m=re.search(rf"{key}:\s*([^\n]+)",blk); return m.group(1).strip() if m else "—"
def parse_charm(name,blk,cite):
    cm=re.search(r"Cost:\s*(.+?);\s*Mins:\s*([^\n]+)",blk)
    cost,mins=(cm.group(1).strip(),cm.group(2).strip()) if cm else (field(blk,"Cost"),field(blk,"Mins"))
    typ=field(blk,"Type"); kw=field(blk,"Keywords"); dur=field(blk,"Duration"); pre=field(blk,"Prerequisite Charms")
    eff=""
    for p in blk.split("\n"):
        ps=p.strip()
        if ps and not re.match(r"^(Cost|Mins|Type|Keywords|Duration|Prerequisite|Special|EX3)",ps): eff=ps;break
    eff=re.sub(r"\s+"," ",eff)[:220]
    line=f"### {name}\nCost {cost} · Mins {mins} · {typ} · Kw {kw} · Dur {dur}"+(f" · Prereq {pre}" if pre and pre!='None' else "")
    if eff: line+=f"\n{eff}  ‹{cite} › {name}›"
    return line
# 1) Core MA styles
CORE="vault/Exalted 3e - Core Rulebook.md"; lines=open(CORE,encoding="utf-8").read().split("\n")
START,END=19425,21525
styles={}; cur=None
i=START-1
while i<min(END,len(lines)):
    m=re.match(r"^####\s+(.+)$",lines[i].strip())
    if m:
        name=m.group(1).strip()
        base=re.sub(r"\s+(Style|Form)$","",name)
        if re.search(r"\s(Style|Form)$",name):
            cur=base; styles.setdefault(cur,[])
        j=i+1; blk=[]
        while j<min(END,len(lines)) and not re.match(r"^####\s",lines[j]): blk.append(lines[j]); j+=1
        bt="\n".join(blk)
        if cur and re.search(r"Cost:",bt):
            styles[cur].append(parse_charm(name,bt,"Core Rulebook"))
        i=j; continue
    i+=1
pathlib.Path("charms/martial_arts").mkdir(parents=True,exist_ok=True)
for st,cs in styles.items():
    fn="charms/martial_arts/"+re.sub(r"[^a-z0-9]+","_",st.lower()).strip("_")+".md"
    body=[f"# {st} Style", f"*{len(cs)} charms · Core Rulebook › Martial Arts. Full text in vault.*",""]+cs
    pathlib.Path(fn).write_text("\n".join(body),encoding="utf-8")
# 2) index ALL styles across all books
idx={}
for f in glob.glob("vault/*.md"):
    book=os.path.basename(f)[:-3].replace("Exalted 3e - ","")
    for ln in open(f,encoding="utf-8"):
        m=re.match(r"^#{2,4}\s+(.+? Style)\s*$",ln.strip())
        if m: idx.setdefault(m.group(1).strip(),set()).add(book)
out=["# Martial Arts — Style Index","*Core styles fully extracted in this folder. Any other style: pull from the cited vault book on request.*",""]
for st in sorted(idx):
    extracted=" ✓" if (re.sub(r"[^a-z0-9]+","_",re.sub(r" Style$","",st).lower()).strip("_") in {re.sub(r'[^a-z0-9]+','_',s.lower()).strip('_') for s in styles}) else ""
    out.append(f"- **{st}**{extracted} — {', '.join(sorted(idx[st]))}")
pathlib.Path("charms/martial_arts/00_index.md").write_text("\n".join(out),encoding="utf-8")
print(f"Core styles extracted: {len(styles)} ({', '.join(styles)})")
print(f"Total distinct styles indexed across vault: {len(idx)}")
