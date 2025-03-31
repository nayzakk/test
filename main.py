from playwright.sync_api import sync_playwright

def run_headless():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Run in headless mode
        page = browser.new_page()
        page.goto("https://google.com")
        print(page.title())  # examplemplelehe page title
        browser.close()

if __name__ == "__main__":
    run_headless()
