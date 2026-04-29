#!/usr/bin/env python3
"""
Create NotebookLM notebooks from YouTube URL lists.
Creates one notebook per course and registers each in the library.

Usage:
  python scripts/run.py create_notebooks.py --courses '[{"name": "Course Name", "urls": ["url1", "url2"]}]'
"""

import sys
import json
import argparse
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from patchright.sync_api import sync_playwright
from config import BROWSER_PROFILE_DIR, STATE_FILE, BROWSER_ARGS, USER_AGENT, PAGE_LOAD_TIMEOUT
from browser_utils import BrowserFactory, StealthUtils


def wait_for_processing(page):
    """Wait for NotebookLM to finish processing sources"""
    time.sleep(3)
    try:
        page.wait_for_function(
            "() => document.querySelectorAll('mat-progress-bar, mat-spinner, mat-progress-spinner').length === 0",
            timeout=180000
        )
    except Exception:
        pass
    time.sleep(3)


def create_notebook(context, course_name, youtube_urls):
    """
    Create a single NotebookLM notebook with the given YouTube URLs.
    Returns the notebook URL.
    """
    stealth = StealthUtils()
    page = context.new_page()

    try:
        print(f"\n📓 Creating notebook: '{course_name}' ({len(youtube_urls)} URLs)...")

        # Navigate to NotebookLM home
        page.goto("https://notebooklm.google.com", wait_until="domcontentloaded", timeout=PAGE_LOAD_TIMEOUT)

        if "accounts.google.com" in page.url:
            raise RuntimeError("Not authenticated. Run: python scripts/run.py auth_manager.py setup")

        stealth.random_delay(1500, 2500)

        # Click "Create new notebook"
        page.wait_for_selector('[aria-label="Create new notebook"]', timeout=10000)
        stealth.realistic_click(page, '[aria-label="Create new notebook"]')
        stealth.random_delay(1500, 2500)

        # Click "Websites" button in the Add Sources dialog
        page.wait_for_selector('button:has-text("Websites")', timeout=10000)
        stealth.realistic_click(page, 'button:has-text("Websites")')
        stealth.random_delay(800, 1200)

        # Fill in the URL textarea
        url_input_selector = 'textarea[placeholder*="links" i], textarea[placeholder*="paste" i]'
        page.wait_for_selector(url_input_selector, timeout=10000)
        page.fill(url_input_selector, '\n'.join(youtube_urls))
        stealth.random_delay(500, 800)

        # Click Insert
        page.wait_for_selector('button:has-text("Insert")', timeout=10000)
        stealth.realistic_click(page, 'button:has-text("Insert")')

        print("  ⏳ Waiting for sources to process (this may take a minute)...")
        wait_for_processing(page)

        notebook_url = page.url
        print(f"  ✅ Done: {notebook_url}")

        return notebook_url

    finally:
        page.close()


def register_in_library(skill_dir, notebook_url, course_name):
    """Add notebook to the library so it can be queried via the skill"""
    import subprocess
    run_py = skill_dir / "scripts" / "run.py"
    topics = "claude,anthropic,ai,course"
    result = subprocess.run(
        [
            sys.executable, str(run_py), "notebook_manager.py", "add",
            "--url", notebook_url,
            "--name", course_name,
            "--description", f"YouTube video lessons from the '{course_name}' course",
            "--topics", topics
        ],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"  📚 Registered in library as '{course_name}'")
    else:
        print(f"  ⚠️  Could not register in library (you can add it manually): {result.stderr.strip()}")


def main():
    parser = argparse.ArgumentParser(description="Create NotebookLM notebooks from YouTube URL lists")
    parser.add_argument(
        "--courses",
        required=True,
        help='JSON array: [{"name": "Course Name", "urls": ["url1", "url2"]}, ...]'
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (default: visible)"
    )
    args = parser.parse_args()

    try:
        courses = json.loads(args.courses)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in --courses: {e}")
        sys.exit(1)

    if not courses:
        print("❌ No courses provided.")
        sys.exit(1)

    skill_dir = Path(__file__).parent.parent
    results = []

    with sync_playwright() as p:
        context = BrowserFactory.launch_persistent_context(p, headless=args.headless)

        try:
            for course in courses:
                name = course.get("name", "Untitled")
                urls = [u for u in course.get("urls", []) if "youtube.com" in u]

                if not urls:
                    print(f"\n⚠️  Skipping '{name}' — no YouTube URLs found")
                    continue

                notebook_url = create_notebook(context, name, urls)
                register_in_library(skill_dir, notebook_url, name)
                results.append({"name": name, "url": notebook_url})

        finally:
            context.close()

    print("\n" + "="*60)
    print("✅ All notebooks created!\n")
    for r in results:
        print(f"  {r['name']}")
        print(f"  {r['url']}\n")
    print("You can now query any of these in Claude Code by saying:")
    print('  "Query my [course name] notebook: [your question]"')
    print("="*60)


if __name__ == "__main__":
    main()
