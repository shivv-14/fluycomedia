"""Builds the case-study web pages (replacing the old Wix PDFs).
Run:  python build_case_studies.py   -> writes case-studies/<slug>.html
Content below is transcribed word-for-word from the Fluyco case-study PDFs."""
import html, io, os

CAL = "https://cal.com/fluycomedia/30min"
E = html.escape

STUDIES = [
  dict(
    slug="robert-coronado", name="Robert Frank Coronado", role="Founder · Coronado Media",
    photo="../assets/img/cs-robert.jpg",
    title="How a LA videographer went from buried in editing to 34K followers and a growing client roster",
    intro="Robert Frank Coronado was a videographer in Glendale with a real problem. He had clients, he had a camera, and he had talent. What he didn't have was time. Every hour after the shoot was going into editing — for himself, and for the clients who hired him. This is the story of what changed when post-production was no longer his problem.",
    stats=[("1500+","Videos Delivered"),("24-48 hrs","Average Turnaround"),("5M+ views","In the past 7 months"),("34K+","Followers - built by Robert, freed by us")],
    situation=[
      "By November 2024, Robert was at a ceiling that had nothing to do with his skill as videographer. He had built a client base in Los Angeles, was producing content for multiple clients, and was growing his own personal brand alongside it. But every project he completed created a new editing backlog. The more he shot, the more time he spent at a desk — not on set.",
      "He couldn't take on new clients because there was no capacity left. He couldn't grow his own following consistently because the pipeline kept choking. Quality was slipping under the volume. The bottleneck wasn't opportunity. It was bandwidth. And the bottleneck was him.",
      "On November 13, 2024, Robert brought in FLUYCO MEDIA to handle post-production. <b>His job from that point:</b> handle production. <b>Our job:</b> handle everything after."],
    problems_title="The Three Problems",
    problems=[
      ("Time — editing was consuming his day","Robert was spending the bulk of his hours in post-production, for himself and for his clients. Time that should have gone toward shooting, pitching, and signing new work was stuck inside the timeline."),
      ("Capacity — he couldn't take on more clients","Every new project meant more editing, which meant less room for growth. His ceiling wasn't talent or opportunity — it was bandwidth. The business couldn't scale while he was the bottleneck."),
      ("Consistency — quality at volume was breaking down","Maintaining a consistent standard across multiple client deliverables — while also managing his own content output — was becoming unsustainable. Something always had to give.")],
    context=None,
    did_intro="The engagement was simple by design. Robert hands off raw footage. We return polished, client-ready edits. We learned his style early, held that standard across every deliverable, and gave him back the one thing no agency can manufacture for a client — time.",
    did=[
      ("Edited all client deliverables — end to end","Every video Robert's clients needed, we handled. He shoots, we edit, the client receives. The workflow that used to jam his schedule now runs without him in the middle of it."),
      ("Delivered within 24 hours, consistently","Speed was non-negotiable. We built a workflow that returns every file within 24 hours regardless of volume — the kind of turnaround that keeps clients loyal and pipelines moving."),
      ("Maintained quality at scale across 1,500+ videos","Over 7+ months and more than 1,500 videos, every deliverable met the standard Robert's clients expect. No drops, no shortcuts, no excuses on volume days."),
      ("Freed him entirely to focus on production","With post-production off his plate, Robert shifted his energy entirely to shooting, client management, and growing his brand. The ceiling that editing had created was gone.")],
    result=[
      "With client post-production fully handled, Robert's calendar opened up. He went after new clients — and signed them. He focused on his own content — and grew to 34K followers. The videos tied to his work generated millions of views. He liked what we delivered for his clients so much that he referred us to people in his network, unprompted.",
      "None of that was the plan on paper. It was just what happened when the hardest, most time-consuming part of his workload stopped being his problem."],
    table=[("Client videos edited by us","0","1500+"),("Turnaround on client work","Days","Under 24 hrs"),("Robert's followers","Stagnant","34K"),("Views across clients content","—","3 Millions+"),("New clients signed","Capped by bandwidth","Actively growing"),("Referrals to FLUYCO MEDIA","0","Multiple - unprompted")],
    closing=None, closing_img=None),
  dict(
    slug="tyler-mclellan", name="Tyler McLellan", role="Mortgage Agent · Advisory X",
    photo="../assets/img/cs-tyler.jpg",
    title="How a mortgage broker went from DIY editing to owning his market",
    intro="Tyler McLellan was already the top mortgage broker in Prince Edward Island. He had the clients, the reputation, and the results. What he didn't have was content that looked the part. He was shooting videos, editing them himself, and posting content that didn't reflect the standard of his actual work. That changed when he found FLUYCO MEDIA.",
    stats=[("15+","Videos Delivered"),("24-48 hrs","Average Turnaround"),("100K+","Views Generated"),("0","Competitors at his Content Level")],
    situation=[
      "Prince Edward Island is a small market. That cuts both ways. There's less competition — but there's also less room to hide when your content doesn't match your reputation. Tyler McLellan had already built one of the most trusted mortgage practices in PEI, with access to over 70 lenders across Canada and a client list that reflected it. But his social content told a different story.",
      "He was shooting educational mortgage tips and short-form reels — the right content strategy for a broker trying to build authority online. The problem was execution. Tyler was editing the videos himself, and the output wasn't matching the standard of his brand. The content looked like it was produced by someone who was also managing 70 lenders, client files, and a growing brokerage — because it was.",
      "There was also a timing problem. Tyler wanted to post the same day or the day after a shoot. That kind of turnaround requires a dedicated post-production system. Doing it yourself while running a brokerage isn't a system — it's a gamble.",
      "Tyler found FLUYCO MEDIA and reached out. The brief was clear: professional quality, fast turnaround, no compromise on either."],
    problems_title="The Two Problems",
    problems=[
      ("Quality — the content wasn't reflecting the brand","Tyler was editing his own videos. For a mortgage broker managing dozens of client files, that meant rushed cuts, inconsistent style, and a final product that didn't communicate the authority his business had actually earned. In a trust-based industry, the way your content looks is part of what clients use to decide whether to pick up the phone."),
      ("Speed — he needed same-day or next-day delivery","Short-form content is a timing game. Shoot today, post tomorrow — that's the window when momentum is highest and the algorithm rewards fresh uploads. Tyler needed a partner who could match that pace without cutting corners. Waiting three days for an edit doesn't work when the content strategy depends on consistency.")],
    context="<b>The market context:</b> PEI is a small, tight-knit market where most mortgage brokers aren't producing video content at all. Tyler already had no competition on expertise. With the right post-production, he'd have no competition on content quality either — and that's exactly what happened.",
    did_intro="The model was simple. Tyler shoots. We edit and deliver within 24 hours — consistently, every time, with no drop in quality regardless of volume or deadline pressure. Educational talking-head videos and short-form reels, both cut to the standard his brand deserved.",
    did=[
      ("Took the edit entirely off his plate","Tyler stopped spending evenings cutting videos and started spending that time on his business. Post-production became someone else's problem — ours — and it stopped being a source of stress or delay in his content calendar."),
      ("Delivered within 24 hours, every single time","Same-day and next-day delivery — matched every time. Tyler shoots, we return a finished edit before the next shoot. The content pipeline that he needed to build authority in PEI now runs without friction."),
      ("Elevated the quality to match his market position","Professional cuts, clean pacing, consistent style — the kind of editing that makes a mortgage broker look like the most credible voice in the room. In a market where most brokers aren't producing video at all, the quality gap became a competitive moat.")],
    result=["Tyler's videos began performing in a market that had no precedent for mortgage content at this production level. Over 100,000 views generated across his educational tips and reels — in PEI, a province with a total population under 180,000. That's not a small number in context. That's saturation."],
    table=[("Video editing","Done by Tyler himself","Fully handled by us"),("Content quality","Unprofessional","Brand-level standard"),("Turnaround time","Weeks (self-edited)","Under 24-48 hours"),("Total views generated","—","100K+"),("Competitors at his content quality","Unknown","Zero")],
    closing="Tyler McLellan was already the best mortgage broker in PEI. Now his content reflects that. In a province where most brokers aren't publishing video at all — and none at this production level — the gap between his brand and the competition isn't just about expertise anymore. It's visible every time someone scrolls past one of his reels.",
    closing_img="../assets/img/cs-tyler-reels.jpg"),
  dict(
    slug="steph-dorworth", name="Steph Dorworth", role="Founder · Speaker Société",
    photo="../assets/img/steph.jpg",
    title="Steph Dorworth × Fluyco Media",
    intro="Steph Dorworth is the founder of Speaker Société and one of the agents and founders who trust Fluyco Media with their post-production.",
    stats=[], situation=[], problems_title="", problems=[], context=None, did_intro=None, did=[], result=[], table=[],
    closing=None, closing_img=None, pending=True),
]

CSS = r"""
:root{color-scheme:dark;--bg:#000;--card:#0d0d0d;--text:#fff;--muted:#9a9a9a;--soft:#c9c9c9;--border:rgba(255,255,255,.16);--border-soft:rgba(255,255,255,.10);--up:#7dff6b;
--font:"Inter",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;--serif:"Instrument Serif","Times New Roman",Times,serif;--ease:cubic-bezier(.16,1,.3,1)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--font);-webkit-font-smoothing:antialiased;line-height:1.55;overflow-x:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid #fff;outline-offset:3px;border-radius:6px}
.wrap{max-width:1040px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.top{position:sticky;top:0;z-index:20;background:rgba(0,0,0,.7);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid var(--border-soft);padding-top:env(safe-area-inset-top,0px)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;height:68px}
.logo{display:inline-flex;align-items:center;gap:10px;font-weight:700;font-size:17px;letter-spacing:-.045em}
.logo svg{width:30px;height:auto}
.back{font-size:14px;color:var(--muted);display:inline-flex;gap:6px;align-items:center}.back:hover{color:#fff}
.btn{position:relative;overflow:hidden;isolation:isolate;display:inline-flex;align-items:center;justify-content:center;gap:8px;height:42px;padding:0 18px;border-radius:6px;font-size:14px;font-weight:500;letter-spacing:-.02em;white-space:nowrap;transition:box-shadow .35s,border-color .35s,background .35s}
.btn::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(115deg,transparent 20%,rgba(255,255,255,.45) 48%,transparent 76%);transform:translateX(-130%);transition:transform .65s ease}
.btn:hover::after{transform:translateX(130%)}
.btn-solid{background:linear-gradient(180deg,#fff 0%,#e7e7e7 48%,#cfcfcf 100%);color:#111;border:1px solid #fff}
.btn-solid:hover{box-shadow:0 0 22px rgba(186,208,255,.35),0 8px 18px rgba(255,255,255,.12)}
.btn-ghost{background:linear-gradient(135deg,rgba(255,255,255,.12),rgba(0,0,0,.5) 46%,rgba(150,170,200,.1));color:#fff;border:1px solid rgba(198,198,198,.55)}
.btn-ghost:hover{border-color:rgba(220,230,255,.8);box-shadow:0 0 24px rgba(170,200,255,.28)}
.btn-lg{height:50px;padding:0 24px;font-size:15px}
.tabs{display:flex;justify-content:center;gap:8px;margin:56px 0 48px}
.tabs span{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 18px;border-radius:999px;font-size:14px;font-weight:600;letter-spacing:-.03em}
.tabs .a{background:#fff;color:#111}.tabs .b{background:linear-gradient(90deg,#2a2a2a,#111);border:1px solid var(--border-soft)}
.hero{display:grid;grid-template-columns:260px 1fr;gap:48px;align-items:center}
.photo{border-radius:18px;padding:8px;background:linear-gradient(160deg,#2a2a2a,#0a0a0a);border:1px solid var(--border-soft)}
.photo img{display:block;width:100%;aspect-ratio:1;object-fit:cover;border-radius:12px}
h1{font-size:clamp(32px,5vw,52px);font-weight:600;letter-spacing:-.05em;line-height:1.04;text-wrap:balance}
.lead{margin-top:20px;padding-left:18px;border-left:1px solid rgba(255,255,255,.6);color:var(--soft);font-size:17.5px;max-width:62ch}
.stats{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:640px;margin:96px auto 0}
.stat{padding:28px;border-radius:16px;background:linear-gradient(135deg,#1e1e1e,#0e0e0e 60%,#1a1a1a);border:1px solid var(--border-soft)}
.stat b{display:block;font-size:clamp(30px,4vw,40px);font-weight:600;letter-spacing:-.05em;line-height:1}
.stat span{display:block;margin-top:8px;color:var(--soft);font-size:15px}
section{padding-top:112px}
h2{font-size:clamp(30px,4vw,44px);font-weight:600;letter-spacing:-.05em;line-height:1.05;margin-bottom:24px}
h2 em{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--muted)}
.prose p{color:var(--soft);font-size:17px;max-width:68ch}
.prose p+p{margin-top:18px}
.prose b{color:#fff}
.rule{padding-left:18px;border-left:1px solid rgba(255,255,255,.6)}
.items{display:grid;gap:28px;margin-top:8px}
.item{display:grid;grid-template-columns:auto 1fr;gap:18px}
.item .n{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:#1c1c1c;border:1px solid var(--border-soft);font-size:13px;font-variant-numeric:tabular-nums;margin-top:2px}
.item h3{font-size:18px;font-weight:600;letter-spacing:-.03em}
.item p{color:var(--soft);font-size:16.5px;margin-top:4px;max-width:68ch}
.check{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;background:linear-gradient(180deg,#fff,#cfcfcf);color:#111;margin-top:2px}
.context{margin-top:40px}
.tbl{overflow-x:auto;margin-top:8px}
table{width:100%;border-collapse:collapse;min-width:520px}
th{text-align:left;font-size:14px;font-weight:600;letter-spacing:.02em;text-transform:uppercase;padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.4)}
td{padding:16px;border-bottom:1px solid var(--border);font-size:15px;color:var(--soft)}
td.up{color:var(--up);font-weight:500}
.closing{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.closing p{font-size:19px;color:#e5e5e5;letter-spacing:-.02em;line-height:1.5}
.closing img{width:100%;border-radius:14px;display:block}
.cta{margin-top:120px;text-align:center;padding:88px 24px;border-radius:24px;border:1px solid var(--border);background:radial-gradient(70% 90% at 50% 0%,rgba(255,255,255,.14),transparent 70%),linear-gradient(180deg,#111,#030303)}
.cta p{color:var(--muted);margin:0 auto 28px;max-width:46ch}
.more{margin-top:72px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.more a{display:flex;gap:14px;align-items:center;padding:16px;border-radius:14px;border:1px solid var(--border-soft);background:var(--card);transition:border-color .3s}
.more a:hover{border-color:rgba(255,255,255,.35)}
.more img{width:52px;height:52px;border-radius:50%;object-fit:cover}
.more small{display:block;color:var(--muted);font-size:12.5px}
.more b{font-weight:500;letter-spacing:-.02em}
footer{margin-top:96px;border-top:1px solid var(--border-soft);padding-block:28px;color:var(--muted);font-size:13px}
footer .wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
.pending{margin-top:56px;padding:28px;border-radius:16px;border:1px dashed var(--border);color:var(--soft);max-width:640px}
.reveal{animation:up .9s var(--ease) both}
@keyframes up{from{opacity:0;transform:translateY(18px)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
body{padding-bottom:calc(34px + env(safe-area-inset-bottom,0px))}
.credit-bar{position:fixed;left:0;right:0;bottom:0;z-index:95;display:flex;align-items:center;justify-content:center;gap:8px;min-height:34px;padding:0 16px env(safe-area-inset-bottom,0px);background:rgba(0,0,0,.72);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-top:1px solid var(--border-soft);font-size:12.5px;color:var(--muted)}
.credit-bar a{color:#f3f3f3;font-weight:500;text-underline-offset:3px}.credit-bar a:hover{color:#fff;text-decoration:underline}
@media (max-width:760px){.hero{grid-template-columns:1fr;gap:28px}.photo{max-width:220px}.closing{grid-template-columns:1fr}section{padding-top:80px}.stats{margin-top:64px}.stat{padding:20px}.back span{display:none}}
"""

LOGO = '<svg viewBox="0 0 100 84" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#8a8a8a"/></linearGradient><mask id="lm"><rect width="100" height="84" fill="#fff"/><circle cx="62" cy="58" r="25" fill="#000"/></mask></defs><path mask="url(#lm)" fill="url(#lg)" d="M34 6h48c10 0 15 8 11 17l-9 22c-4 9-11 13-20 13H16C6 58 1 50 5 41l11-25C20 9 26 6 34 6z"/><circle cx="62" cy="58" r="19" fill="url(#lg)"/></svg>'
CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 84'%3E%3Cpath fill='%23ddd' d='M34 6h48c10 0 15 8 11 17l-9 22c-4 9-11 13-20 13H16C6 58 1 50 5 41l11-25C20 9 26 6 34 6z'/%3E%3Ccircle cx='62' cy='58' r='19' fill='%23fff' stroke='%23000' stroke-width='6'/%3E%3C/svg%3E"

def page(s):
    first = s["name"].split()[0]
    p = []
    a = p.append
    a(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(s["name"])} Case Study — Fluyco Media</title>
<meta name="description" content="{E(s["intro"][:155])}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(s["title"])}">
<meta property="og:description" content="{E(s["intro"][:155])}">
<link rel="canonical" href="https://fluycomedia.vercel.app/case-studies/{s["slug"]}">
<link rel="icon" href="{FAV}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900&family=Instrument+Serif:ital@1&display=swap">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="logo" href="../index.html" aria-label="Fluyco Media home">{LOGO}fluyco media</a>
  <div style="display:flex;gap:16px;align-items:center">
    <a class="back" href="../index.html#case-studies">← <span>All case studies</span></a>
    <a class="btn btn-solid" href="{CAL}" target="_blank" rel="noopener">Book a call</a>
  </div>
</div></header>
<main class="wrap">
  <div class="tabs reveal"><span class="a">Case Study</span><span class="b">{E(s["name"])}</span></div>
  <div class="hero reveal">
    <div class="photo"><img src="{s["photo"]}" alt="{E(s["name"])}" width="260" height="260"></div>
    <div><h1>{E(s["title"])}</h1><p class="lead">{s["intro"]}</p>
    <p style="margin-top:14px;color:var(--muted);font-size:14px">{E(s["role"])}</p></div>
  </div>''')
    if s["stats"]:
        a('<div class="stats">' + "".join(f'<div class="stat"><b>{E(v)}</b><span>{E(l)}</span></div>' for v, l in s["stats"]) + '</div>')
    if s["situation"]:
        a('<section><h2>The Situation</h2><div class="prose rule">' + "".join(f"<p>{x}</p>" for x in s["situation"]) + '</div></section>')
    if s["problems"]:
        a(f'<section><h2>{E(s["problems_title"])}</h2><div class="items">' + "".join(
            f'<div class="item"><span class="n">{i+1}</span><div><h3>{E(h)}</h3><p>{E(t)}</p></div></div>' for i, (h, t) in enumerate(s["problems"])) + '</div>')
        if s["context"]:
            a(f'<div class="prose rule context"><p>{s["context"]}</p></div>')
        a('</section>')
    if s["did"]:
        a(f'<section><h2>What We Did</h2><div class="prose" style="margin-bottom:36px"><p>{E(s["did_intro"])}</p></div><div class="items">' + "".join(
            f'<div class="item"><span class="check">{CHECK}</span><div><h3>{E(h)}</h3><p>{E(t)}</p></div></div>' for h, t in s["did"]) + '</div></section>')
    if s["result"]:
        a('<section><h2>The Result</h2><div class="prose">' + "".join(f"<p>{E(x)}</p>" for x in s["result"]) + '</div></section>')
    if s["table"]:
        a('<section><h2>Before <em>&amp;</em> after</h2><div class="tbl"><table><thead><tr><th>Metric</th><th>Before</th><th>After</th></tr></thead><tbody>' + "".join(
            f'<tr><td style="color:#fff">{E(m)}</td><td>{E(b)}</td><td class="up">{E(af)}</td></tr>' for m, b, af in s["table"]) + '</tbody></table></div></section>')
    if s["closing"]:
        a(f'<section class="closing"><p>{E(s["closing"])}</p><img src="{s["closing_img"]}" alt="Tyler McLellan reels with view counts: 15.3K, 11.8K, 37.9K, 25.6K and 18.2K" loading="lazy"></section>')
    if s.get("pending"):
        a('<div class="pending"><b style="color:#fff">Full case study coming soon.</b><p style="margin-top:8px">We\'re putting together the numbers and the story behind Steph\'s content. In the meantime, see how we work with Robert and Tyler below — or book a call to talk about your own content.</p></div>')
    a(f'''<div class="cta"><h2>Want results like <em>{E(first)}'s</em>?</h2><p>Book a free 30-minute call. You record, we handle everything after.</p>
    <a class="btn btn-solid btn-lg" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div>''')
    others = [o for o in STUDIES if o["slug"] != s["slug"]]
    a('<div class="more">' + "".join(
        f'<a href="{o["slug"]}.html"><img src="{o["photo"]}" alt="" loading="lazy"><span><small>Next case study</small><b>{E(o["name"])}</b></span></a>' for o in others) +
      '<a href="../index.html"><span style="width:52px;height:52px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--border)">←</span><span><small>Back to</small><b>Fluyco Media home</b></span></a></div>')
    a('''</main>
<footer><div class="wrap"><span>© Fluyco Media</span><a href="https://www.instagram.com/fluycomedia/" target="_blank" rel="noopener">Instagram @fluycomedia</a></div></footer>
<div class="credit-bar" role="contentinfo">Developed by <a href="https://www.linkedin.com/in/brungi-shiva-ganesh" target="_blank" rel="noopener">Brungi Shiva Ganesh</a></div>
</body>
</html>
''')
    return "\n".join(p)

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "case-studies"); os.makedirs(out, exist_ok=True)
    for s in STUDIES:
        io.open(os.path.join(out, s["slug"] + ".html"), "w", encoding="utf-8").write(page(s))
        print("wrote case-studies/" + s["slug"] + ".html")
