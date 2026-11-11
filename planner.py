"""Simple data-science learning plan CLI; stores tasks in plan.json."""
import argparse,json
from pathlib import Path
DB=Path("plan.json")
DEFAULT=[("Python for data","Practice data types, functions and files"),("NumPy and Pandas","Clean and explore tabular data"),("Statistics","Study distributions and hypothesis tests"),("Visualization","Build clear charts"),("Machine learning","Train and evaluate baseline models"),("Projects","Ship an end-to-end portfolio project")]
def load():return json.loads(DB.read_text()) if DB.exists() else [{"topic":a,"goal":b,"done":False} for a,b in DEFAULT]
def save(x):DB.write_text(json.dumps(x,indent=2))
p=argparse.ArgumentParser();s=p.add_subparsers(dest="cmd",required=True);s.add_parser("init");s.add_parser("list");d=s.add_parser("done");d.add_argument("index",type=int);a=p.parse_args();items=load()
if a.cmd=="init":save(items);print("Plan initialized.")
elif a.cmd=="list":
 for i,x in enumerate(items,1):print(f'{i}. [{"x" if x["done"] else " "}] {x["topic"]}: {x["goal"]}')
else:
 if not 1<=a.index<=len(items):raise SystemExit("Task number out of range.")
 items[a.index-1]["done"]=True;save(items);print("Marked complete.")