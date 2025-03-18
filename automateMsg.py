# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.common.keys import Keys
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
#
# # Open WhatsApp Web
# driver.get("https://web.whatsapp.com/")
# print("Scan the QR Code and press Enter after logging in.")
# input("Press Enter after logging in...")  # Wait for manual login
# time.sleep(10)
# # List of contacts and messages
# contacts = [
#     "+9779842724655",
#     "+9779862012325"
# ]
# message = "Hello! This is an automated message sent using Selenium. h2"
#
# # Send messages to each contact
# def sendMsg(phone_number,message):
#         print(f"Sending message to {phone_number}...")
#
#
#         try:
#             driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
#             time.sleep(5)
#             # Wait for the input box
#             wait = WebDriverWait(driver, 5)
#             input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')))
#             print("msg typed")
#             # Type the message
#             input_box.send_keys(message)
#             time.sleep(3)
#             print("sending")
#             input_box.send_keys(Keys.ENTER)
#             print(f"sent to {phone_number}")
#
#
#             print(f"Message sent to {phone_number} successfully!")
#             time.sleep(2)  # Wait before sending the next message
#
#         except Exception as e:
#             print(f"Failed to send message to {phone_number}: {e}")
# for phone_number in contacts:
#     sendMsg(phone_number,message)
#     time.sleep(10)  # Wait before sending the next message
# # Close the browser
# print("All messages sent. Closing browser...")
# time.sleep(5)
# driver.quit()


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

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Scan the QR Code and press Enter after logging in.")



# List of contacts and messages
contacts = [
    "+9779862012325",
    "+9779842724655",
    # "+9779862012325"
]
message = "Hello! This is an automated message sent using Selenium. h2"


# Send messages to each contact
def sendMsg(phone_number, message):
    print(f"Sending message to {phone_number}...")

    try:
        driver.get(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")

        # Wait for the input box to load
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )

        # Clear the input box (if any pre-filled text exists)
        input_box.clear()

        # Type the message into the input box
        input_box.send_keys(message)

        # Wait for the Send button to be clickable
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
        )

        # Click the Send button
        send_button.click()

        print(f"Message sent to {phone_number} successfully!")
        time.sleep(5)  # Wait for the message to be sent

    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")

# Wait for the chat list to load
try:

    print("Logged in successfully!")
    for phone_number in contacts:
        sendMsg(phone_number, message)
        time.sleep(10)
        print("All messages sent. Closing browser...")

except Exception as e:
    print("Login timeout or failed:", e)
    driver.quit()
    exit()

