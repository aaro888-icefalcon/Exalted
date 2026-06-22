# Oracle — built-in (mythic-optional)

When **mythic-gm is NOT loaded**, use `scripts/oracle.py` for yes/no, scenes, and events, drawing meaning/event flavor from the tables here. When **mythic-gm IS loaded**, route yes/no, scene tests, and random events to it, and treat these tables as the Creation-native content it plays through. `Turmoil` (this skill) and `Chaos` (mythic) are the same 1–9 value in state.

- `python3 scripts/oracle.py augury <odds> <turmoil>` — yes/no (odds: certain…impossible).
- `python3 scripts/oracle.py scene <turmoil>` — expected / altered / interrupt.
- `python3 scripts/oracle.py event` — random-event focus + a meaning pull.

Files: `01_meaning_tables.md` (interpretation words), `02_event_tables.md` (Creation events/encounters).
