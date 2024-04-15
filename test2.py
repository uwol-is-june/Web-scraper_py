from playwright.sync_api import sync_playwright
import time
import playwright

p = sync_playwright().start()

# headless True면 브라우저 안보이고 프로세스만 실행
browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://storycloud.kr/705")
time.sleep(3)

while(True):
  page.keyboard.down("End")
  time.sleep(3)
  button_exists = page.locator('.btn._more_btn.more_btn').first.is_visible()

  if button_exists:
      page.click('.btn._more_btn.more_btn')
      time.sleep(3)
  else:
      break

time.sleep(3)
