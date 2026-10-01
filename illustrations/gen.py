# Flat "cut paper" illustrations, 400x400
INK="#313131"; SKIN="#f8d3af"
Y=("#fffbed","#fff6b6","#ffdc4a","#af7e04")
B=("#f0f5fd","#c6dcff","#659df2","#305bab")
G=("#eaf9ef","#adf0c7","#2dc75c","#067429")
O=("#fff5ed","#f8d3af","#fe9f4d","#9b4a08")
R=("#fff0f0","#ffc6c6","#ff6464","#bd0a0a")
P=("#f4f2fd","#dedaff","#8f7fee","#6631d7")

def wrap(bg, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">
<rect width="400" height="400" rx="40" fill="{bg}"/>
<g stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>'''

def person(x, y, c, s=1.0, smile=True):
    # x,y = head center
    r=28*s
    body=f'<path d="M{x-48*s},{y+110*s} Q{x-48*s},{y+40*s} {x},{y+40*s} Q{x+48*s},{y+40*s} {x+48*s},{y+110*s} Z" fill="{c}"/>'
    head=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}"/>'
    eyes=f'<circle cx="{x-9*s}" cy="{y-3*s}" r="{3*s}" fill="{INK}"/><circle cx="{x+9*s}" cy="{y-3*s}" r="{3*s}" fill="{INK}"/>'
    mouth=f'<path d="M{x-9*s},{y+9*s} Q{x},{y+17*s} {x+9*s},{y+9*s}" fill="none" stroke="{INK}" stroke-width="{3*s}"/>' if smile else ''
    return body+head+eyes+mouth

def bubble(x,y,w,h,c,tail="left"):
    tx = x+30 if tail=="left" else x+w-30
    d = -1 if tail=="left" else 1
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{c}"/>'
            f'<path d="M{tx-12},{y+h-2} L{tx+d*-14},{y+h+24} L{tx+12},{y+h-2} Z" fill="{c}"/>')

def dots(x,y,c):
    return ''.join(f'<circle cx="{x+i*22}" cy="{y}" r="6" fill="{c}"/>' for i in range(3))

def arrow_circle(cx,cy,r,c,w=12):
    # cycle: top arc left->right, bottom arc right->left, arrowheads at ends
    g=18
    top=f'<path d="M{cx-r},{cy-g} A{r},{r} 0 0 1 {cx+r},{cy-g}" fill="none" stroke="{c}" stroke-width="{w}"/>'
    th=f'<path d="M{cx+r-18},{cy-g-14} L{cx+r},{cy-g+6} L{cx+r+18},{cy-g-14}" fill="none" stroke="{c}" stroke-width="{w}"/>'
    bot=f'<path d="M{cx+r},{cy+g} A{r},{r} 0 0 1 {cx-r},{cy+g}" fill="none" stroke="{c}" stroke-width="{w}"/>'
    bh=f'<path d="M{cx-r-18},{cy+g+14} L{cx-r},{cy+g-6} L{cx-r+18},{cy+g+14}" fill="none" stroke="{c}" stroke-width="{w}"/>'
    return top+th+bot+bh

def check(x,y,s,c,w=12):
    return f'<path d="M{x-20*s},{y} L{x-5*s},{y+16*s} L{x+24*s},{y-18*s}" fill="none" stroke="{c}" stroke-width="{w}"/>'

def laptop(x,y,w,c_screen,c_body):
    h=w*0.62
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{INK}"/>'
            f'<rect x="{x+12}" y="{y+12}" width="{w-24}" height="{h-24}" rx="6" fill="{c_screen}"/>'
            f'<rect x="{x-24}" y="{y+h}" width="{w+48}" height="18" rx="9" fill="{c_body}"/>')

def gear(cx,cy,r,c,hole):
    import math
    teeth=''.join(f'<rect x="{cx-10}" y="{cy-r-14}" width="20" height="28" rx="4" fill="{c}" transform="rotate({i*45} {cx} {cy})"/>' for i in range(8))
    return teeth+f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/><circle cx="{cx}" cy="{cy}" r="{r*0.42}" fill="{hole}"/>'

ills = {}

# V1 個人と対話
ills["v1"]=wrap(B[0], person(120,220,B[2])+person(280,220,G[2])
    +bubble(50,70,130,80,B[1],"left")+dots(93,110,B[3])
    +bubble(220,90,130,80,G[1],"right")+dots(263,130,G[3]))

# V2 動くソフトウェア
ills["v2"]=wrap(G[0],
    # stack of documents (behind)
    '<rect x="248" y="70" width="110" height="140" rx="10" fill="#e7e7e7"/>'
    '<rect x="236" y="82" width="110" height="140" rx="10" fill="#ffffff" stroke="#b0b0b0" stroke-width="4"/>'
    + ''.join(f'<line x1="256" y1="{110+i*22}" x2="326" y2="{110+i*22}" stroke="#b0b0b0" stroke-width="6"/>' for i in range(4))
    + laptop(60,150,220,G[1],"#595959")
    + gear(130,215,26,G[2],G[1]) + f'<path d="M190,195 L230,220 L190,245 Z" fill="{G[3]}"/>')

# V3 顧客との協調 (puzzle pieces joining)
ills["v3"]=wrap(Y[0], person(95,170,Y[2])+person(305,170,B[2])
    + f'<rect x="150" y="270" width="60" height="60" rx="8" fill="{Y[2]}"/><circle cx="210" cy="300" r="16" fill="{Y[2]}"/>'
    + f'<rect x="196" y="270" width="60" height="60" rx="8" fill="{B[2]}"/><circle cx="210" cy="300" r="15" fill="{B[2]}"/>'
    + f'<rect x="150" y="270" width="60" height="60" rx="8" fill="{Y[2]}"/><circle cx="210" cy="300" r="16" fill="{Y[2]}"/>'
    + f'<path d="M140,90 Q200,40 260,90" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="2 14"/>'
    + '<path d="M200,100 C185,80 160,95 200,125 C240,95 215,80 200,100 Z" fill="#ff6464"/>')

# V4 変化への対応 (winding path with arrow, a plan line crossed)
ills["v4"]=wrap(O[0],
    f'<line x1="60" y1="320" x2="340" y2="80" stroke="#b0b0b0" stroke-width="8" stroke-dasharray="4 20"/>'
    f'<path d="M60,320 C140,320 100,200 180,210 C260,220 220,110 320,90" fill="none" stroke="{O[2]}" stroke-width="16"/>'
    f'<path d="M300,70 L340,86 L310,118" fill="none" stroke="{O[2]}" stroke-width="16"/>'
    f'<circle cx="60" cy="320" r="16" fill="{O[3]}"/>'
        f'<path d="M250,280 q20,-20 40,0 q20,20 40,0" fill="none" stroke="{B[2]}" stroke-width="8"/>'
    f'<path d="M230,310 q20,-20 40,0 q20,20 40,0" fill="none" stroke="{B[1]}" stroke-width="8"/>')

# P1 顧客満足・早く継続的に提供 (gifts flowing to happy customer)
ills["p01"]=wrap(Y[0],
    ''.join(f'<rect x="{40+i*70}" y="{250-i*10}" width="52" height="46" rx="6" fill="{c}"/><rect x="{40+i*70+22}" y="{250-i*10}" width="8" height="46" fill="{Y[3]}"/>' for i,c in enumerate([Y[2],Y[2],Y[2]]))
    + f'<path d="M50,330 L250,330" stroke="{INK}" stroke-width="6"/><path d="M235,318 L252,330 L235,342" fill="none" stroke="{INK}" stroke-width="6"/>'
    + person(310,170,G[2],1.0)
    + f'<path d="M262,96 l5,13 l13,5 l-13,5 l-5,13 l-5,-13 l-13,-5 l13,-5 z" fill="{Y[2]}"/><path d="M352,84 l5,13 l13,5 l-13,5 l-5,13 l-5,-13 l-13,-5 l13,-5 z" fill="{Y[2]}"/>')

# P2 変更を歓迎 (person with open arms, circular arrows)
ills["p02"]=wrap(G[0],
    arrow_circle(200,215,140,G[1],14)
    + f'<path d="M150,250 L95,180" stroke="{G[2]}" stroke-width="22"/><path d="M250,250 L305,180" stroke="{G[2]}" stroke-width="22"/>'
    + person(200,190,G[2],1.1)
    + f'<rect x="300" y="110" width="52" height="52" rx="10" fill="{Y[2]}" transform="rotate(15 326 136)"/>'
    + f'<path d="M318,136 l8,8 l14,-16" fill="none" stroke="{Y[3]}" stroke-width="6"/>')

# P3 短い間隔でリリース (calendar + repeating releases)
ills["p03"]=wrap(B[0],
    f'<rect x="70" y="80" width="190" height="180" rx="16" fill="#ffffff" stroke="{B[3]}" stroke-width="6"/>'
    f'<rect x="70" y="80" width="190" height="44" rx="16" fill="{B[2]}"/><rect x="70" y="104" width="190" height="20" fill="{B[2]}"/>'
    + ''.join(f'<rect x="{88+(i%4)*42}" y="{140+(i//4)*38}" width="28" height="24" rx="4" fill="{B[1] if i not in (1,5,9) else G[2]}"/>' for i in range(12))
    + f'<rect x="100" y="64" width="12" height="34" rx="6" fill="{INK}"/><rect x="218" y="64" width="12" height="34" rx="6" fill="{INK}"/>'
    + ''.join(f'<path d="M{220+i*45},330 l18,-36 l18,36 z" fill="{G[2]}"/>' for i in range(3))
    + f'<path d="M60,310 L200,310" stroke="{B[3]}" stroke-width="6" stroke-dasharray="2 14"/>')

# P4 ビジネス側と開発者が日々一緒に (two people at shared table, sun)
ills["p04"]=wrap(Y[0],
    f'<circle cx="200" cy="80" r="34" fill="{Y[2]}"/>'
    + ''.join(f'<line x1="200" y1="80" x2="{200+60*__import__("math").cos(a)}" y2="{80+60*__import__("math").sin(a)}" stroke="{Y[2]}" stroke-width="6" stroke-dasharray="0 44 16 100"/>' for a in [i*3.14159/4 for i in range(8)])
    + person(110,190,B[2]) + f'<path d="M110,232 l-8,12 l8,40 l8,-40 z" fill="{B[3]}"/>'
    + person(290,190,G[2])
    + f'<rect x="40" y="290" width="320" height="22" rx="8" fill="{O[2]}"/>'
    + laptop(250,240,70,G[1],"#595959")
    + f'<rect x="80" y="254" width="60" height="36" rx="4" fill="#ffffff" stroke="#b0b0b0" stroke-width="4"/>')

# P5 意欲に満ちた人々・信頼 (team inside a shield with heart)
ills["p05"]=wrap(P[0],
    f'<path d="M200,40 L340,90 L340,200 C340,290 270,340 200,365 C130,340 60,290 60,200 L60,90 Z" fill="{P[1]}"/>'
    + person(140,190,P[2],0.8)+person(260,190,P[2],0.8)+person(200,170,O[2],0.9)
    + '<path d="M200,95 C188,78 162,90 200,122 C238,90 212,78 200,95 Z" fill="#ff6464"/>')

# P6 フェイス・トゥ・フェイス (two big faces)
def face(x,y,c,flip):
    s=-1 if flip else 1
    return (f'<circle cx="{x}" cy="{y}" r="80" fill="{SKIN}"/>'
            f'<path d="M{x-80},{y-10} Q{x},{y-130} {x+80},{y-10} Q{x+40*s},{y-60} {x-80},{y-10}" fill="{c}"/>'
            f'<circle cx="{x+30*s}" cy="{y+5}" r="7" fill="{INK}"/>'
            f'<path d="M{x+20*s},{y+40} Q{x+40*s},{y+55} {x+55*s},{y+35}" fill="none" stroke="{INK}" stroke-width="5"/>')
ills["p06"]=wrap(O[0], face(110,210,O[3],False)+face(290,210,"#595959",True)
    + f'<path d="M180,140 q20,-20 40,0" fill="none" stroke="{O[2]}" stroke-width="8"/><path d="M170,115 q30,-30 60,0" fill="none" stroke="{O[2]}" stroke-width="8"/>')

# P7 動くソフトウェアが進捗の尺度 (progress bar + gear)
ills["p07"]=wrap(G[0],
    f'<rect x="50" y="250" width="300" height="44" rx="22" fill="#ffffff" stroke="{G[3]}" stroke-width="6"/>'
    f'<rect x="58" y="258" width="210" height="28" rx="14" fill="{G[2]}"/>'
    + gear(150,140,46,G[2],G[0]) + gear(250,120,30,B[2],G[0])
    + check(305,330,0.9,G[3],10))

# P8 持続可能な一定のペース (steady heartbeat line + steps)
ills["p08"]=wrap(R[0],
    f'<path d="M30,200 L110,200 L130,160 L150,240 L170,200 L230,200 L250,160 L270,240 L290,200 L370,200" fill="none" stroke="{R[2]}" stroke-width="10"/>'
    + ''.join(f'<circle cx="{60+i*70}" cy="300" r="14" fill="{B[2]}"/>' for i in range(5))
    + f'<line x1="60" y1="300" x2="340" y2="300" stroke="{B[1]}" stroke-width="6"/>'
    + ''.join(f'<circle cx="{60+i*70}" cy="300" r="14" fill="{B[2]}"/>' for i in range(5))
    + '<path d="M200,100 C185,78 150,92 200,135 C250,92 215,78 200,100 Z" fill="#ff6464"/>')

# P9 技術的卓越性と優れた設計 (gem on blueprint)
ills["p09"]=wrap(B[0],
    f'<rect x="50" y="210" width="300" height="140" rx="10" fill="{B[2]}"/>'
    + ''.join(f'<line x1="{50+i*30}" y1="210" x2="{50+i*30}" y2="350" stroke="{B[1]}" stroke-width="2"/>' for i in range(1,10))
    + ''.join(f'<line x1="50" y1="{210+i*28}" x2="350" y2="{210+i*28}" stroke="{B[1]}" stroke-width="2"/>' for i in range(1,5))
    + f'<rect x="90" y="250" width="100" height="70" fill="none" stroke="#ffffff" stroke-width="4"/><circle cx="260" cy="285" r="34" fill="none" stroke="#ffffff" stroke-width="4"/>'
    + f'<path d="M140,90 L260,90 L300,130 L200,230 L100,130 Z" fill="{P[2]}"/>'
    + f'<path d="M100,130 L300,130 M140,90 L170,130 L200,230 L230,130 L260,90" fill="none" stroke="{P[1]}" stroke-width="5"/>'
    + f'<path d="M320,60 l6,16 l16,6 l-16,6 l-6,16 l-6,-16 l-16,-6 l16,-6 z" fill="{Y[2]}"/>')

# P10 シンプルさ (many cluttered blocks crossed vs one clean block)
ills["p10"]=wrap(Y[0],
    ''.join(f'<rect x="{x}" y="{y}" width="34" height="34" rx="4" fill="#e7e7e7" transform="rotate({r} {x+17} {y+17})"/>' for x,y,r in [(40,120,10),(84,100,-15),(60,170,25),(110,150,5),(40,220,-20),(100,210,15),(140,110,30),(150,190,-10)])
    + f'<line x1="40" y1="100" x2="190" y2="260" stroke="{R[2]}" stroke-width="10"/>'
    + f'<path d="M205,180 L240,180" stroke="{INK}" stroke-width="8"/><path d="M228,166 L244,180 L228,194" fill="none" stroke="{INK}" stroke-width="8"/>'
    + f'<rect x="270" y="140" width="80" height="80" rx="12" fill="{Y[2]}"/>'
    + check(310,180,0.9,Y[3],10)
    + f'<path d="M60,320 L340,320" stroke="#b0b0b0" stroke-width="6"/>')

# P11 自己組織的なチーム (network of people)
nodes=[(200,110,G[2]),(100,210,B[2]),(300,210,Y[2]),(140,320,B[2]),(260,320,G[2])]
edges=[(0,1),(0,2),(1,3),(2,4),(3,4),(1,2),(0,3),(0,4)]
ills["p11"]=wrap(G[0],
    ''.join(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" stroke="#b0b0b0" stroke-width="6"/>' for a,b in edges)
    + ''.join(f'<circle cx="{x}" cy="{y}" r="44" fill="#ffffff" stroke="{c}" stroke-width="8"/><circle cx="{x}" cy="{y-10}" r="14" fill="{SKIN}"/><path d="M{x-22},{y+28} Q{x},{y-2} {x+22},{y+28} Z" fill="{c}"/>' for x,y,c in nodes))

# P12 ふりかえりと調整 (cycle arrows with lightbulb + magnifier)
ills["p12"]=wrap(P[0],
    arrow_circle(200,200,140,P[1],14)
    + f'<circle cx="200" cy="180" r="50" fill="{Y[2]}"/><rect x="178" y="226" width="44" height="34" rx="6" fill="#595959"/>'
    + f'<path d="M185,190 l15,-20 l15,20" fill="none" stroke="{Y[3]}" stroke-width="6"/><line x1="200" y1="170" x2="200" y2="226" stroke="{Y[3]}" stroke-width="6"/>'
    + f'<circle cx="285" cy="285" r="30" fill="#ffffff" stroke="{INK}" stroke-width="10"/><line x1="307" y1="307" x2="335" y2="335" stroke="{INK}" stroke-width="14"/>')

for k,v in ills.items():
    open(f"{k}.svg","w").write(v)
print(len(ills))
