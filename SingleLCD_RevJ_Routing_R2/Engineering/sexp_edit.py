import re,json
from dataclasses import dataclass
@dataclass
class Node:
 start:int
 end:int
 value:object
 children:list
 def key(self): return self.children[0].value if self.children else None
 def all(self,k): return [x for x in self.children if x.children and x.key()==k]
 def one(self,k): return next(iter(self.all(k)),None)
 def arg(self,n=1): return self.children[n].value

def parse(s):
 ts=list(re.finditer(r'"(?:\\.|[^"\\])*"|[^\s()]+|[()]',s));i=0
 def rec():
  nonlocal i
  t=ts[i];i+=1
  if t[0]=='(':
   cs=[]
   while ts[i][0]!=')': cs.append(rec())
   e=ts[i].end();i+=1
   return Node(t.start(),e,None,cs)
  return Node(t.start(),t.end(),json.loads(t[0]) if t[0].startswith('"') else t[0],[])
 n=rec();assert i==len(ts);return n

def edits(s,changes):
 for a,b,v in sorted(changes,reverse=True): s=s[:a]+v+s[b:]
 return s

def quoted(x): return json.dumps(x,ensure_ascii=False)
