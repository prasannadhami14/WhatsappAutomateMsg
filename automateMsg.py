river = webdriver.Chrome(executable_path="C:/path_to_chromedriver/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
input("Scan the QR Code and press Enter")

for number in numbers:
    driver.get(f"https://web.whatsapp.com/send?phone={number}&text=")
    time.sleep(10)  # Wait for chat to load

    # Click on the attachment button (paperclip icon)
    attach_button = driver.find_element("xpath", '//div[@title="Attach"]')
    attach_button.click()
    time.sleep(2)

    # Click on the gallery (video) button
    video_upload = driver.find_element("xpath", '//input[@accept="video/*"]')
    video_upload.send_keys(video_path)
    time.sleep(5)  # Wait for the upload to complete

    # Click the send button
    send_button = driver.find_element("xpath", '//span[@data-icon="send"]')
    send_button.click()
    time.sleep(5)

print("Videos sent successfully!")
driver.quit()