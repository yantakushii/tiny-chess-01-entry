import json,os,sys,random,urllib.request
U=os.environ.get("MAKEFUN_ENV_URL")
N=60000
V=(0,100,320,330,500,900,0)
NO=(-21,-19,-12,-8,8,12,19,21);BO=(-11,-9,9,11);RO=(-10,-1,1,10);KO=BO+RO
CS=tuple(21+f+10*r for r in range(8) for f in range(8))
IX={}
for r in range(8):
 for f in range(8):IX[21+f+10*r]=r*8+f
G=random.Random(7)
ZO={}
for p in tuple(range(1,7))+tuple(range(-6,0)):
 for i in range(64):ZO[p,i]=G.getrandbits(64)
ZS=G.getrandbits(64);ZC=[G.getrandbits(64) for _ in range(16)];ZE=[G.getrandbits(64) for _ in range(120)]
T={1:"00,00,00,00,00,00,00,00,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,10,20,30,30,20,10,5,0,0,10,20,20,10,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0",2:"-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,-10,-10,-10,-10,-20,-40,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-50,-40,-30,-30,-30,-30,-40,-50",3:"-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,-10,-10,-10,-10,-20,-40,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-50,-40,-30,-30,-30,-30,-40,-50",4:"00,00,00,00,00,00,00,00,50,50,50,50,50,50,50,50,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,00,00,00,05,05,00,00,00",5:"00,00,00,00,00,00,00,00,50,50,50,50,50,50,50,50,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,-10,05,05,05,05,05,05,-10,00,00,00,05,05,00,00,00",6:"-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-40,-40,-20,-20,-10,20,20,00,00,00,00,20,20,20,30,10,00,00,10,30,20"}
P={k:[int(x) for x in v.split(",")] for k,v in T.items()}
EW=[[0]*120 for _ in range(7)];EB=[[0]*120 for _ in range(7)]
for p in range(1,7):
 for s in CS:
  i=IX[s];EW[p][s]=V[p]+(P[6][i] if p==6 else P[p][i]);EB[p][s]=V[p]+(P[6][63-i] if p==6 else P[p][63-i])
def parse(fen):
 pt=fen.split();bd=[7]*120
 for i in CS:bd[i]=0
 r=f=0
 for ch in pt[0]:
  if ch=="/":r+=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   p="PNBRQK".index(ch.upper())+1;bd[21+f+10*r]=p if ch.isupper() else -p;f+=1
 w=pt[1]=="w";cs=0
 for i,ch in enumerate("KQkq"):
  if ch in pt[2]:cs|=1<<i
 ep=-1
 if pt[3]!="-":ep=21+(ord(pt[3][0])-97)+10*(8-int(pt[3][1]))
 return bd,w,cs,ep
def nm(i):return chr(97+(i-21)%10)+str(8-(i-21)//10)
def atk(bd,s,by):
 for d in NO:
  if bd[s+d]==(2 if by else -2):return 1
 for d in BO:
  t=s+d
  while bd[t]==0:t+=d
  if bd[t]==(3 if by else -3):return 1
 for d in RO:
  t=s+d
  while bd[t]==0:t+=d
  if bd[t]==(4 if by else -4):return 1
 for d in KO:
  t=s+d
  while bd[t]==0:t+=d
  if bd[t]==(5 if by else -5):return 1
 if by:return bd[s+9]==1 or bd[s+11]==1 or any(bd[s+d]==6 for d in KO)
 return bd[s-9]==-1 or bd[s-11]==-1 or any(bd[s+d]==-6 for d in KO)
def mvs(bd,w,cs,ep):
 out=[]
 for s in CS:
  p=bd[s]
  if p==0 or(p>0)is not w:continue
  a=p if p>0 else -p
  if a==1:
   d=-10 if w else 10;t=s+d
   if bd[t]==0:
    if t<31 or t>88:out+=s|t<<7|1<<14,
    else:
     out+=s|t<<7,
     if(s-21)//10==(6 if w else 1)and bd[s+2*d]==0:out.append(s|(s+2*d)<<7)
   for dd in(d-1,d+1):
    t=s+dd;q=bd[t]
    if q and q!=7 and(q>0)is not w:
     if t<31 or t>88:out+=s|t<<7|1<<14,
     else:out+=s|t<<7,
    elif t==ep:out+=s|t<<7|2<<14,
  elif a==6:
   for d in KO:
    t=s+d;q=bd[t]
    if q!=7 and(q==0 or(q>0)is not w):out+=s|t<<7,
   if w:
    if cs&1 and bd[96]==0 and bd[97]==0 and bd[98]==4 and not atk(bd,95,0)and not atk(bd,96,0)and not atk(bd,97,0):out+=95|97<<7|3<<14,
    if cs&2 and bd[94]==0 and bd[93]==0 and bd[92]==0 and bd[91]==4 and not atk(bd,95,0)and not atk(bd,94,0)and not atk(bd,93,0):out+=95|93<<7|3<<14,
   else:
    if cs&4 and bd[26]==0 and bd[27]==0 and bd[28]==-4 and not atk(bd,25,1)and not atk(bd,26,1)and not atk(bd,27,1):out+=25|27<<7|3<<14,
    if cs&8 and bd[24]==0 and bd[23]==0 and bd[22]==0 and bd[21]==-4 and not atk(bd,25,1)and not atk(bd,24,1)and not atk(bd,23,1):out+=25|23<<7|3<<14,
  else:
   of=NO if a==2 else BO if a==3 else RO if a==4 else KO
   for d in of:
    t=s+d
    while 1:
     q=bd[t]
     if q==7:break
     if q==0:out+=s|t<<7,
     else:
      if(q>0)is not w:out+=s|t<<7,
      break
     if a<3:break
     t+=d
 return out
CM={91:13,98:14,21:7,28:11,95:12,25:3};RC={97:(98,96),93:(91,94),27:(28,26),23:(21,24)}
def make(bd,w,cs,ep,m,un,wk,bk):
 f,t=m&127,(m>>7)&127;fl=(m>>14)&3;p=bd[f];vic=bd[t]
 un[:7]=(f,t,p,vic,cs,ep,fl);un[13]=wk;un[14]=bk
 nc=cs&CM.get(f,15)&CM.get(t,15);np=-1
 if fl==1:bd[t]=5 if w else -5
 elif fl==2:
  bd[t]=p;c=t+(10 if w else -10);bd[c]=0;un[7]=c
 elif fl==3:
  bd[t]=p;rf,rt=RC[t];bd[rf]=0;bd[rt]=4 if w else -4
 else:
  bd[t]=p
  if abs(t-f)==20:np=(f+t)//2
 bd[f]=0
 if p==6:un[13]=t
 elif p==-6:un[14]=t
 K=0;K^=ZO[p,IX[f]]
 if vic:K^=ZO[vic,IX[t]]
 K^=ZO[bd[t],IX[t]]
 if fl==2:K^=ZO[-1 if w else 1,IX[un[7]]]
 elif fl==3:K^=ZO[4 if w else -4,IX[RC[t][0]]]^ZO[4 if w else -4,IX[RC[t][1]]]
 if cs!=nc:K^=ZC[cs]^ZC[nc]
 if ep>=0:K^=ZE[ep]
 if np>=0:K^=ZE[np]
 K^=ZS;un[12]=K
 return nc,np,K
def unmk(bd,w,un):
 f,t,p,vic,cs,ep,fl=un[:7]
 if fl==1:bd[t]=vic
 elif fl==2:bd[t]=vic;bd[un[7]]=-1 if w else 1
 elif fl==3:bd[t]=0;bd[RC[t][0]]=4 if w else -4;bd[RC[t][1]]=0
 else:bd[t]=vic
 bd[f]=p
def ev(bd):
 sc=10;wpn=[];bpn=[]
 for s in CS:
  p=bd[s]
  if p==1:wpn.append(s)
  elif p==-1:bpn.append(s)
  if p:sc+=EW[p][s]if p>0 else-EB[-p][s]
 return sc
MA=30000;nd=0;TT={};KL=[0]*400;HI={};PK=set();US=[[0]*15 for _ in range(400)]
def qs(bd,w,cs,ep,a,b,pl,qd):
 global nd
 nd+=1
 if nd>N:raise A()
 if qd>=10:return ev(bd)if w else-ev(bd)
 k=bd.index(6 if w else -6)
 sc=ev(bd)if w else-ev(bd)
 if sc>=b:return sc
 if sc>a:a=sc
 for m in mvs(bd,w,cs,ep):
  vic=bd[(m>>7)&127];fl=(m>>14)&3
  if not vic and fl!=1 and fl!=2:continue
  if vic==6 or vic==-6:return MA-pl
  un=US[pl];nc,np,kk=make(bd,w,cs,ep,m,un,k,bd.index(-6 if w else 6))
  v=-qs(bd,not w,nc,np,-b,-a,pl+1,qd+1);unmk(bd,w,un)
  if v>=b:return v
  if v>a:a=v
 return a
def ab(bd,w,cs,ep,key,d,a,b,pl,wk,bk):
 global nd
 nd+=1
 if nd>N:raise A()
 if key in PK:return 0
 e=TT.get(key);mv=0
 if e is not None:mv=e[2]
 ic=atk(bd,wk if w else bk,not w)
 if ic and pl<24:d+=1
 if d<=0:return qs(bd,w,cs,ep,a,b,pl,0)
 ms=mvs(bd,w,cs,ep)
 def om(m):
  t=(m>>7)&127;s=0;vic=bd[t]
  if vic:s=100000+8*V[abs(vic)]-V[abs(bd[m&127])]
  if(m>>14)&1:s+=90000
  if m==mv:s=1000000+s
  elif m==KL[pl]:s=80000+s
  elif s==0:s=HI.get(bd[m&127],t,0)if 0 else HI.get((bd[m&127],t),0)
  return s
 ms.sort(key=om,reverse=True)
 best=-2*MA;bm=0;lg=0
 for m in ms:
  vic=bd[(m>>7)&127]
  if vic==6 or vic==-6:return MA-pl
  fl=(m>>14)&3;un=US[pl]
  nc,np,kk=make(bd,w,cs,ep,m,un,wk,bk)
  nk=key^kk
  PK.add(key);nwk,nbk=un[13],un[14]
  v=-ab(bd,not w,nc,np,nk,d-1,-b,-a,pl+1,nwk,nbk)
  PK.discard(key);unmk(bd,w,un)
  if v>best:best=v;bm=m
  if v>a:a=v
  lg+=1
  if a>=b:
   if not bd[(m>>7)&127] and not(m>>14)&3:
    KL[pl]=m;HI[(bd[m&127],(m>>7)&127)]=HI.get((bd[m&127],(m>>7)&127),0)+d*d
   break
 if not lg:return(-MA+pl)if ic else 0
 TT[key]=(d,best,bm)
 return best
class A(Exception):pass
def think(fen,lg,cap=N):
 global nd,TT,KL,HI,PK
 nd=0;TT={};KL=[0]*400;HI={};PK=set()
 bd,w,cs,ep=parse(fen)
 rw=bd.index(6);rb=bd.index(-6)
 key=0
 for s in CS:
  p=bd[s]
  if p:key^=ZO[p,IX[s]]
 if not w:key^=ZS
 key^=ZC[cs]
 if ep>=0:key^=ZE[ep]
 LS=set()
 for u in lg:LS.add((21+(ord(u[0])-97)+10*(8-int(u[1])))|((21+(ord(u[2])-97)+10*(8-int(u[3])))<<7))
 root=[m for m in mvs(bd,w,cs,ep)if(m&16383)in LS or(m>>14)&3]
 if not root:return lg[0]
 best=root[0];sc=[0]*len(root)
 try:
  for d in range(1,20):
   cb2=cb if d>1 else None
   cb,cv,a=None,-2*MA,-2*MA
   od=sorted(range(len(root)),key=lambda i:-sc[i])if d>1 else range(len(root))
   for ri,ix in enumerate(od):
    m=root[ix];un=US[0]
    nc,np,kk=make(bd,w,cs,ep,m,un,rw,rb)
    nk=key^kk
    PK.add(key)
    v=-ab(bd,not w,nc,np,nk,d-1,-2*MA,-a,1,un[13],un[14])
    PK.discard(key);unmk(bd,w,un);sc[ix]=v
    if v>cv:cv,cb=v,m
    if cv>a:a=cv
   if cb:best=cb
   if cv>MA-1000 or cv<-MA+1000:break
 except A:
  if cb2:best=cb2
  pass
 f,t=best&127,(best>>7)&127
 u=nm(f)+nm(t)
 if(best>>14)&3==1:u+="q"
 return u
def post(p,o):
 r=urllib.request.Request(U+p,data=json.dumps(o).encode(),headers={"content-type":"application/json"})
 return json.load(urllib.request.urlopen(r))
if __name__=="__main__":
 from time import perf_counter as pc
 while 1:
  g=post("/game",{})
  if g["status"]=="done":
   print("done: %s w, %s d, %s l"%(g["wins"],g["draws"],g["losses"]),file=sys.stderr);break
  while g["status"]=="your_move":
   t0=pc();u=think(g["fen"],g["legal_moves"]);dt=pc()-t0
   print("g%s %s p%s %.1fs %s n=%d"%(g["game"],g["opponent"],g["plies"],dt,u,nd),file=sys.stderr)
   g=post("/move",{"game":g["game"],"move":u})
  print("game %s: %s by %s"%(g["game"],g["outcome"],g["reason"]),file=sys.stderr)
