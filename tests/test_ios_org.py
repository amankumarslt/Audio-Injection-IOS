from appium.webdriver.common.appiumby import AppiumBy
import time

def test_audio_recording(driver):
    # Wait for app to load
    time.sleep(5)
    
    # Click mic button
    
    # Inject audio
    if hasattr(driver, 'media_url'):
        driver.execute_script(f"lambda-audio-injection={driver.media_url}")

        el1 = driver.find_element(by=AppiumBy.XPATH,
            value='//*[@name="mic.fill" and @type="XCUIElementTypeButton"]')
        el1.click()
        time.sleep(10)
        el2 = driver.find_element(
            by=AppiumBy.XPATH,
            value='//*[@type="XCUIElementTypeButton"]')
        el2.click()
        time.sleep(25)

        el3 = driver.find_element(by=AppiumBy.XPATH,
            value='//*[@name="Recordings"]')
        el3.click()
        time.sleep(10)

        el4 = driver.find_element(by=AppiumBy.XPATH,
            value='//*[@type="XCUIElementTypeButton"]')
        el4.click()
        time.sleep(10)
    time.sleep(10)

    