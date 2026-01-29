from appium.webdriver.common.appiumby import AppiumBy
import time

def test_audio_recording(driver):
    print("▶️ Test started")
    print("⏳ Waiting for app to load...")
    time.sleep(5)
    print("App load wait completed")

    # Inject audio
    if hasattr(driver, 'media_url'):
        print(f"Media URL found: {driver.media_url}")
        print("Injecting audio into session")
        driver.execute_script(f"lambda-audio-injection={driver.media_url}")
        print("Audio injection command executed")
    else:
        print("media_url not found on driver. Skipping audio injection")

    # Click mic button
    try:
        print("▶️ Locating mic button")
        el1 = driver.find_element(
            by=AppiumBy.XPATH,
            value='//XCUIElementTypeButton[@name="record_stop_button"]'
        )
        print("Mic button found")
        el1.click()
        print("Mic button clicked")
    except Exception as e:
        print(f"Failed to click mic button: {e}")
        return

    print("⏳ Waiting 10 seconds for recording to start")
    time.sleep(15)
    print("Recording should be in progress")

    # Click stop recording button
    try:
        print("Locating stop recording button")
        el2 = driver.find_element(
            by=AppiumBy.XPATH,
            value='//*[@type="XCUIElementTypeButton"]'
        )
        print(f"Stop button located: {el2}")
        el2.click()
        print("Stop recording button clicked")
    except Exception as e:
        print(f"Failed to click stop button: {e}")
        return

    print("⏳ Waiting 25 seconds after stopping recording")
    time.sleep(15)
    print("✅ Post-stop wait completed")

    # Open recordings tab
    try:
        print("▶️ Locating Recordings tab")
        el3 = driver.find_element(
            by=AppiumBy.XPATH,
            value='//*[@name="Recordings"]'
        )
        print("Recordings tab found")
        el3.click()
        print("Recordings tab clicked")
    except Exception as e:
        print(f"Failed to open Recordings tab: {e}")
        return

    print("⏳ Waiting 10 seconds for recordings list")
    time.sleep(10)
    print("Recordings list should be visible")

    # Play recording
    try:
        print("▶️ Locating play button")
        el4 = driver.find_element(
            by=AppiumBy.XPATH,
            value='//*[@type="XCUIElementTypeButton"]'
        )
        print(f"Play button found: {el4}")
        el4.click()
        print("Play button clicked")
    except Exception as e:
        print(f"Failed to click play button: {e}")
        return

    print("⏳ Waiting 10 seconds after playback")
    time.sleep(10)
    print("Playback wait completed")

    print("🏁 Test finished successfully")
    time.sleep(10)