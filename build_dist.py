"""Builds dist/ for Vercel: index.html + styles.css + assets/ + case-studies/ (keeps dist/.vercel link)."""
import io, os, shutil
here = os.path.dirname(os.path.abspath(__file__)); d = os.path.join(here, "dist")
os.makedirs(d, exist_ok=True)
for sub in ("assets", "case-studies"):
    shutil.copytree(os.path.join(here, sub), os.path.join(d, sub), dirs_exist_ok=True)
shutil.copy(os.path.join(here, "styles.css"), d)
html = io.open(os.path.join(here, "index.html"), encoding="utf-8").read()
io.open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html.replace("https://fluycomedia.com/", "https://fluycomedia.vercel.app/"))
print("dist ready")
