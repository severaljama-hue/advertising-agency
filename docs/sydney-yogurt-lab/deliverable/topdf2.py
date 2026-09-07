import asyncio, pymupdf
from playwright.async_api import async_playwright
BASE="file:///tmp/claude-0/-home-user-advertising-agency/dd935f6d-907f-5cae-979f-5cdbb151d67e/scratchpad/deliverable/"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = await b.new_page(); await pg.goto(BASE+"print-cover.html", wait_until="load"); await pg.wait_for_timeout(600); await pg.emulate_media(media="print")
        await pg.pdf(path="cover.pdf", format="A4", print_background=True, prefer_css_page_size=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
        pg2 = await b.new_page(); await pg2.goto(BASE+"print-main.html", wait_until="load"); await pg2.wait_for_timeout(600); await pg2.emulate_media(media="print")
        footer = '<div style="width:100%;font-family:DejaVu Sans Mono,monospace;font-size:7.5px;color:#7A7F8E;padding:0 56px 22px 56px;display:flex;justify-content:space-between;letter-spacing:0.08em;"><span>SYDNEY YOGURT LAB · EXECUTION PLAN v1.0 · 2026.09.07</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
        await pg2.pdf(path="main.pdf", format="A4", print_background=True, prefer_css_page_size=True, display_header_footer=True, header_template='<div></div>', footer_template=footer, margin={"top":"0","bottom":"56px","left":"0","right":"0"})
        await b.close()
    out=pymupdf.open(); out.insert_pdf(pymupdf.open("cover.pdf")); out.insert_pdf(pymupdf.open("main.pdf"))
    out.set_metadata({"title":"시드니요거랩 브랜드·마케팅 실행안 v1.0","author":"[대행사명]","subject":"12개월 실행안"})
    out.save("시드니요거랩_실행안_v1.0.pdf", garbage=3, deflate=True); print("pages", len(out))
    d=pymupdf.open("시드니요거랩_실행안_v1.0.pdf")
    for i in [0,1,9,len(d)-1]: d[i].get_pixmap(dpi=60).save(f"pdf2-p{i+1:02d}.jpg")
asyncio.run(main())
