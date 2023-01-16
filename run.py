import asyncio
from pyppeteer import launch

async def main():
    # Launch a new browser instance
    browser = await launch(headless=True)
    # Create a new page
    page = await browser.newPage()
    # Set the user agent
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')
    # Navigate to the website
    await page.goto("https://bingotingo.com/best-social-media-platforms/")
    # Wait for the element with the text "Free Guide" to load
    await page.waitForXPath("//h2[text()='Free Guide']")
    # Scroll down until the element with the text "Script link" is found
    await page.xpath("//h2[text()='Free Guide']")
    # Wait for the button to appear and be clickable
    print("Trying to find canva pro for you! Please wait 60s...")
    await page.waitForXPath("//*[@id='download']", {'visible': True, 'timeout': 70000})
    button = await page.xpath("//*[@id='download']")
    # Click the button that opens the new tab
    await button[0].click()
    # Wait for the new tab to open
    await asyncio.sleep(5)
    # Get the handle of the new tab
    new_tab = (await browser.pages())[-1]
    # Switch to the new tab
    await new_tab.bringToFront()
    # Extract the href link from the button
    href_link = await new_tab.xpath("//a[text()='GET HERE']")
    href_link = await (await href_link[0].getProperty('href')).jsonValue()
    #Print the link of canva pro in a text file
    with open("canva_pro_link.txt", "w") as f:
        f.write(href_link)
        print("Canva Pro Found!")

    # Close the browser instance
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
