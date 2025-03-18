from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(15) #wait for browser to load
# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Scan the QR Code and press Enter after logging in.")

# List of contacts and messages
contacts = [
    "+9779862012325",
    # "+9779865054974",
    "+9779842724655",
]
failed_contacts = []
message = "Hello! This is an automated message sent using Selenium."

# Send messages to each contact
def sendMsg(phone_number, message):
    print(f"Sending message to {phone_number}...")

    try:
        driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
        time.sleep(5)
        print("Number Found")
        try:
            confirm_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "OK")]'))
            )
            confirm_button.click()
            print("Popup handled successfully!")
        except:
            print("No popup found or already dismissed.")
            pass
        # Wait for the input box to load
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        print("Input box loaded successfully!")
        # Clear the input box (if any pre-filled text exists)
        input_box.clear()

        # Type the message into the input box
        input_box.send_keys(message)
        print("Message Typed")

        # Wait for the Send button to be clickable
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
        )
        # Click the Send button
        send_button.click()
        print(f"Message sent to {phone_number} successfully!")
        time.sleep(5)  # Wait for the message to be sent
        return True

    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
        return False

# Wait for the chat list to load
try:
    print("Logged in successfully!")
    for phone_number in contacts:
        success=sendMsg(phone_number, message)
        if not success:
            failed_contacts.append(phone_number)
        time.sleep(5)
    if failed_contacts:
        print("Retrying failed numbers...")
        for phone_number in failed_contacts:
            success=sendMsg(phone_number, message)
            if not success:
                print(f"Failed to send message to {phone_number}")
    print("All messages sent. Closing browser...")
    time.sleep(5)
    driver.quit()

except Exception as e:
    print("Login timeout or failed:", e)
    driver.quit()
    exit()

