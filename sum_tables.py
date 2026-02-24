from playwright.sync_api import sync_playwright

seeds = list(range(82, 92))

total = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)

        # wait for JS table to render
        page.wait_for_selector("table")

        # grab all numbers in table cells
        cells = page.locator("td").all_text_contents()

        for c in cells:
            c = c.strip()
            if c.replace(".", "", 1).isdigit():
                total += float(c)

    browser.close()

print("FINAL_TOTAL =", total)
