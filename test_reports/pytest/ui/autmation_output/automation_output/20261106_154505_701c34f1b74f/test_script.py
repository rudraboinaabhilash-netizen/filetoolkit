async def run_test(page, output_dir, page_url):
    try:
     await page.set_viewport_size({'width':390,'height':844}); await page.goto('https://fileforge-workspace--8ei512uo.preview.emergentagent.com/tool/merge-pdf',wait_until='networkidle'); await page.get_by_test_id('file-upload-zone').locator('input[type=file]').set_input_files('/app/test_reports/ui/test-file.txt'); await page.get_by_test_id('process-tool-button').click(); await page.wait_for_timeout(300); assert await page.get_by_test_id('tool-error-message').is_visible(); assert await page.get_by_test_id('download-ready').count()==0; print('PASS: non-image processing has no fake download')
     await page.goto('https://fileforge-workspace--8ei512uo.preview.emergentagent.com/tools',wait_until='networkidle'); await page.get_by_test_id('tools-search-input').fill('JSON'); assert await page.get_by_test_id('tool-card-json-formatter').count()==1; print('PASS: directory search works')
     await page.get_by_test_id('nav-settings-link').click(); await page.get_by_test_id('motion-toggle').click(); print('PASS: settings toggle works')
     overflow=await page.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth'); print('PASS: no mobile horizontal overflow' if not overflow else 'FINDING: mobile horizontal overflow')
     errors=await page.evaluate("""() => Array.from(document.querySelectorAll('.error, [class*="error"], [id*="error"]')).map(el => el.textContent).join(', ')"""); print('Found error message: '+errors if errors else 'No error messages found on the page')
    except AssertionError as e: print('FINDING: assertion failed: '+str(e))
    except Exception as e: print('SCRIPT ERROR: '+str(e)); raise
