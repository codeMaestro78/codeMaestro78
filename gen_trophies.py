#!/usr/bin/env python3
"""Generate an animated, self-hosted trophy strip (trophies.svg) from the GitHub GraphQL API.
Usage: GITHUB_TOKEN=... python gen_trophies.py [username] [output.svg]
With no token / on failure it writes a placeholder card set ("-") so the image never breaks."""
import os, sys, json, urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "codeMaestro78"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "trophies.svg"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
FONT = "ui-monospace,'JetBrains Mono',SFMono-Regular,Menlo,Consolas,monospace"

QUERY = """query($u:String!){user(login:$u){
 followers{totalCount}
 repositories(ownerAffiliations:OWNER,isFork:false,first:100){totalCount nodes{stargazerCount}}
 pullRequests{totalCount}
 issues{totalCount}
 contributionsCollection{totalCommitContributions}
 repositoriesContributedTo(contributionTypes:[COMMIT,PULL_REQUEST],first:1){totalCount}}}"""

def fetch():
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"u": USER}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    u = json.load(urllib.request.urlopen(req, timeout=30))["data"]["user"]
    return {
      "Stars":   sum(n["stargazerCount"] for n in u["repositories"]["nodes"]),
      "Commits": u["contributionsCollection"]["totalCommitContributions"],
      "PRs":     u["pullRequests"]["totalCount"],
      "Issues":  u["issues"]["totalCount"],
      "Repos":   u["repositories"]["totalCount"],
      "Followers": u["followers"]["totalCount"],
    }

# thresholds for C, B, A, S, SSS
TH = {"Stars":[1,10,50,200,1000],"Commits":[1,100,500,1500,5000],"PRs":[1,10,50,150,500],
      "Issues":[1,10,40,120,400],"Repos":[1,10,30,60,120],"Followers":[1,10,50,200,1000]}
RANKS = ["C","B","A","S","SSS"]
COL = {"-":"#484F58","C":"#8B949E","B":"#CD7F32","A":"#58A6FF","S":"#E3B341","SSS":"#BC8CFF"}

def rank(k, v):
    r = "-"
    for t, name in zip(TH[k], RANKS):
        if v is not None and v >= t: r = name
    return r

try:
    if not TOKEN: raise RuntimeError("no token")
    stats = fetch()
except Exception as e:
    print("fallback placeholder:", e, file=sys.stderr)
    stats = {k: None for k in TH}

W, CARD, GAP = 860, 128, 18
x0 = (W - (6*CARD + 5*GAP)) / 2
cards = []
for i, (k, v) in enumerate(stats.items()):
    r = rank(k, v); c = COL[r]; x = x0 + i*(CARD+GAP)
    val = "–" if v is None else f"{v:,}"
    cards.append(f'''<g transform="translate({x:.1f},14)"><g class="card" style="animation-delay:{i*0.12:.2f}s">
<rect width="{CARD}" height="150" rx="12" fill="#0D1117" stroke="{c}" stroke-opacity=".55"/>
<rect width="{CARD}" height="150" rx="12" fill="url(#g{i})" opacity=".5"/>
<g transform="translate({CARD/2},52)"><g class="cup" style="animation-delay:{i*0.4:.1f}s">
 <path d="M-18-26h36v14c0 12-8 20-18 20s-18-8-18-20z" fill="{c}"/>
 <path d="M-18-22h-10c0 12 6 16 12 16M18-22h10c0 12-6 16-12 16" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>
 <rect x="-3" y="8" width="6" height="12" fill="{c}"/><rect x="-14" y="20" width="28" height="6" rx="2" fill="{c}"/>
 <text y="-4" text-anchor="middle" fill="#0D1117" font-size="12" font-weight="800">{r}</text>
</g></g>
<text x="{CARD/2}" y="104" text-anchor="middle" fill="#8B949E" font-size="12">{k}</text>
<text x="{CARD/2}" y="130" text-anchor="middle" fill="#C9D1D9" font-size="20" font-weight="700">{val}</text>
<rect class="shine" x="-60" y="0" width="40" height="150" fill="url(#sh)" style="animation-delay:{i*0.5+1:.1f}s" clip-path="url(#cl)"/>
</g></g>''')
defs = "".join(f'<linearGradient id="g{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{COL[rank(k,v)]}" stop-opacity=".18"/><stop offset="1" stop-color="{COL[rank(k,v)]}" stop-opacity="0"/></linearGradient>' for i,(k,v) in enumerate(stats.items()))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="178" viewBox="0 0 {W} 178" role="img" aria-label="GitHub trophies for {USER}">
<style>
text{{font-family:{FONT}}}
@keyframes rise{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:none}}}}
@keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
@keyframes shine{{0%,70%{{transform:translateX(0)}}100%{{transform:translateX(230px)}}}}
.card{{opacity:0;animation:rise .6s ease-out forwards}}
.cup{{animation:bob 3s ease-in-out infinite}}
.shine{{animation:shine 4.5s linear infinite}}
</style>
<defs>{defs}
<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".14"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cl"><rect width="{CARD}" height="150" rx="12"/></clipPath></defs>
{"".join(cards)}
</svg>'''
open(OUT, "w", encoding="utf-8").write(svg)
print("wrote", OUT, stats)
