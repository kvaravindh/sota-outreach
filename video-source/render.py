import os, sys, time
from playwright.sync_api import sync_playwright

W, H, FPS = 1920, 1080, 25
OUT = "/home/claude/video/frames"
os.makedirs(OUT, exist_ok=True)

probe = len(sys.argv) > 1 and sys.argv[1] == "probe"

with sync_playwright() as p:
    b = p.chromium.launch(args=["--force-color-profile=srgb", "--font-render-hinting=none"])
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    pg.goto("file:///home/claude/video/video.html")
    pg.wait_for_timeout(1200)          # let the woff2 faces land
    pg.evaluate("document.fonts.ready")
    dur = pg.evaluate("window.DURATION")

    if probe:
        for t in [0.9, 11.0, 14.0, 22.0, 29.0, 36.0, 47.0, 60.0, 69.0]:
            pg.evaluate("window.seek(%f)" % t)
            pg.wait_for_timeout(45)
            pg.screenshot(path="/home/claude/video/probe_%05.1f.png" % t)
        print("probe frames written")
    else:
        total = int(dur * FPS)
        t0 = time.time()
        for i in range(total):
            pg.evaluate("window.seek(%f)" % (i / FPS))
            pg.screenshot(path="%s/f%05d.jpg" % (OUT, i), type="jpeg", quality=94)
            if i % 250 == 0:
                el = time.time() - t0
                print("frame %d/%d  %.0fs elapsed" % (i, total, el), flush=True)
        print("done %d frames in %.0fs" % (total, time.time() - t0))
    b.close()
