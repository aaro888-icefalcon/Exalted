#!/usr/bin/env python3
"""state.py — shared JSON state for exalted-3e (campaign + live combat board).
Other scripts import load()/save(); CLI: init | show | get <path> | set <path> <val>."""
import json, os, sys
STATE = os.environ.get("EX_STATE", os.path.join(os.getcwd(), "campaign_state.json"))
DEFAULT = {"turmoil": 5, "scene": 0, "pc": {}, "intimacies": [],
           "combat": {"round": 0, "combatants": {}},
           "factions": {}, "threads": [], "log": []}
def load():
    if os.path.exists(STATE):
        try: return json.load(open(STATE, encoding="utf-8"))
        except Exception: pass
    return json.loads(json.dumps(DEFAULT))
def save(s): json.dump(s, open(STATE, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
def _walk(s, path):
    cur = s
    for k in path.split("."):
        cur = cur[int(k)] if isinstance(cur, list) else cur[k]
    return cur
def main():
    a = sys.argv[1:]
    if not a: print(f"state file: {STATE}"); print(json.dumps(load(), indent=2)); return
    cmd = a[0]
    if cmd == "init": save(json.loads(json.dumps(DEFAULT))); print(f"initialized {STATE}")
    elif cmd == "show": print(json.dumps(load(), indent=2, ensure_ascii=False))
    elif cmd == "get": print(json.dumps(_walk(load(), a[1])))
    else: print("usage: state.py [init|show|get <dotpath>]")
if __name__ == "__main__": main()
