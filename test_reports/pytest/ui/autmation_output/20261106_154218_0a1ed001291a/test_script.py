async def run_test(page, output_dir, page_url):
    import json
    from pathlib import Path

    try:
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto("https://fileforge-workspace--8ei512uo.preview.emergentagent.com/", wait_until="networkidle")
        assert await page.locator('[data-testid="brand-home-link"]').is_visible()
        assert await page.locator('text=Everything you need').is_visible()
        assert await page.locator('[data-testid="stats-section"]').is_visible()
        print("PASS: home branding, hero, upload zone, and stats loaded")

        await page.locator('[data-testid="nav-tools-link"]').click()
        await page.wait_for_url("**/tools")
        cards = page.locator('[data-testid^="tool-card-"]')
        count = await cards.count()
        assert count == 33, f"expected 33 cards, got {count}"
        print("PASS: all tools directory shows 33 cards")

        await page.locator('[data-testid="filter-pdf-tools"]').click()
        assert await page.locator('[data-testid^="tool-card-"]').count() == 10
        await page.locator('[data-testid="filter-image-&-video"]').click()
        assert await page.locator('[data-testid^="tool-card-"]').count() == 8
        await page.locator('[data-testid="filter-converters-&-utilities"]').click()
        assert await page.locator('[data-testid^="tool-card-"]').count() == 15
        print("PASS: category filters return expected tool counts")

        await page.locator('[data-testid="tools-search-input"]').fill("JSON")
        assert await page.locator('[data-testid="tool-card-json-formatter"]').is_visible()
        assert await page.locator('[data-testid^="tool-card-"]').count() == 1
        print("PASS: directory search filters correctly")

        await page.locator('[data-testid="global-search-input"]').fill("password")
        await page.locator('[data-testid="search-result-password-generator"]').click()
        await page.wait_for_url("**/tool/password-generator")
        assert await page.locator('[data-testid="utility-run-button"]').is_visible()
        await page.locator('[data-testid="utility-input-0"]').fill("24")
        await page.locator('[data-testid="utility-run-button"]').click()
        result = await page.locator('[data-testid="utility-result"]').inner_text()
        assert len(result) >= 24
        print("PASS: global search routes to independent password tool and utility runs")

        utility_cases = [
            ("word-counter", lambda: page.locator('[data-testid="utility-text-input"]').fill("one two three"), "3 words"),
            ("json-formatter", lambda: page.locator('[data-testid="utility-text-input"]').fill('{"a":1}'), '"a": 1'),
            ("base64-encoder", lambda: page.locator('[data-testid="utility-text-input"]').fill("hello"), "aGVsbG8="),
            ("percentage-calculator", lambda: (page.locator('[data-testid="utility-input-0"]').fill("200"), page.locator('[data-testid="utility-input-1"]').fill("10")), "20"),
            ("emi-calculator", lambda: (page.locator('[data-testid="utility-input-0"]').fill("100000"), page.locator('[data-testid="utility-input-1"]').fill("12"), page.locator('[data-testid="utility-input-2"]').fill("1")), "Monthly EMI"),
            ("bmi-calculator", lambda: (page.locator('[data-testid="utility-input-0"]').fill("180"), page.locator('[data-testid="utility-input-1"]').fill("80")), "BMI"),
        ]
        for slug, fill, expected in utility_cases:
            await page.goto(f"https://fileforge-workspace--8ei512uo.preview.emergentagent.com/tool/{slug}", wait_until="networkidle")
            await fill()
            await page.locator('[data-testid="utility-run-button"]').click()
            assert expected in await page.locator('[data-testid="utility-result"]').inner_text(), slug
        print("PASS: word, JSON, Base64, percentage, EMI, and BMI utilities produce results")

        await page.goto("https://fileforge-workspace--8ei512uo.preview.emergentagent.com/tool/merge-pdf", wait_until="networkidle")
        await page.locator('[data-testid="process-tool-button"]').click()
        await page.wait_for_timeout(700)
        assert "Choose a file" in await page.locator('[data-testid="download-ready"]').inner_text()
        print("PASS: processing without a file remains non-successful and does not fake readiness")

        await page.goto("https://fileforge-workspace--8ei512uo.preview.emergentagent.com/history", wait_until="networkidle")
        assert await page.locator('text=Your history is clear').is_visible()
        print("PASS: history empty state is available")

        await page.goto("https://fileforge-workspace--8ei512uo.preview.emergentagent.com/settings", wait_until="networkidle")
        toggle = page.locator('[data-testid="motion-toggle"]')
        before = await toggle.get_attribute("class")
        await toggle.click()
        after = await toggle.get_attribute("class")
        assert before != after
        await page.locator('[data-testid="background-intensity-slider"]').fill("40")
        print("PASS: settings toggle and slider are interactive")

        await page.set_viewport_size({"width":390,"height":844})
        await page.goto("https://fileforge-workspace--8ei512uo.preview.emergentagent.com/", wait_until="networkidle")
        await page.locator('[data-testid="mobile-menu-button"]').click()
        assert await page.locator('[data-testid="mobile-all-tools-link"]').is_visible()
        await page.locator('[data-testid="mobile-all-tools-link"]').click()
        await page.wait_for_url("**/all-tools")
        print("FINDING: mobile All Tools link navigates to /all-tools, but app only defines /tools")

    except AssertionError as e:
        print(f"FINDING: {e}")
    except Exception as e:
        print(f"SCRIPT ERROR: {e}")

    error_text = await page.evaluate("""() => {
    const errorElements = Array.from(document.querySelectorAll('.error, [class*="error"], [id*="error"]'));
    return errorElements.map(el => el.textContent).join(", ");
    }""")
    if error_text:
        print(f"Found error message: {error_text}")
    else:
        print("No error messages found on the page")

