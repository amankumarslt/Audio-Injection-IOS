import pytest
import requests
import os
from appium import webdriver
from appium.options.common import AppiumOptions

def finalize_driver(request, driver):
    def fin():
        if request.node.rep_call.failed:
            driver.execute_script('lambda-status=failed')
        else:
            driver.execute_script('lambda-status=passed')
        driver.quit()
    request.addfinalizer(fin)

def upload_media(username, access_key):
    url = "https://api.lambdatest.com/mfs/v1.0/media/upload"
    file_path = "harvard.wav"
    
    if not os.path.exists(file_path):
        # Create a dummy wav file if it doesn't exist
        with open(file_path, "wb") as f:
            f.write(b"dummy audio content")
            
    import time
    files = {
        'media_file': ('harvard.wav', open(file_path, 'rb'), 'audio/wav'),
        'type': (None, 'audio'),
        'custom_id': (None, f'SampleAudio_{int(time.time())}')
    }
    
    response = requests.post(url, files=files, auth=(username, access_key))
    
    if response.status_code == 200:
        return response.json().get("media_url")
    else:
        raise Exception(f"Failed to upload media: {response.text}")

@pytest.fixture(scope="function")
def driver(request):
    username = "Username"
    access_key = "AccessKey"
    
    # Upload media first
    media_url = "lt://MEDIA850bab5183614cd8a3efa9f5283455e6"
    
    caps = {
        "app": "lt://APP10160341531766398674076768",
        "lt:options": {
            "w3c": True,
            "isRealMobile": True,
            "deviceName": "iPhone 16",
            "build": "Audio Injection Demo on iOS RD",
            "name": "Audio Injection Demo on iOS RD",
            "platformVersion": "18",
            "platformName": "ios",
            "visual": True,
            "video": True,
            "network": True,
            "enableAudioInjection": True,
            "media": media_url,
            "iosLiveInteraction":True,
        }
    }

    options = AppiumOptions()
    options.load_capabilities(caps)

    url = f"https://{username}:{access_key}@mobile-hub.lambdatest.com/wd/hub"
    
    driver = webdriver.Remote(url, options=options)
    
    # Store media_url in driver for test access
    driver.media_url = media_url
    
    yield driver
    
    finalize_driver(request, driver)
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)