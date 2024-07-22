from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def order_food(username, password, food_choice):
    # Set up the WebDriver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Open Sweetgreen website for Hadrian
        driver.get("https://order.sweetgreen.com/account/menu")

        # Log in
        login_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Join or sign in"))
        )
        login_button.click()

        email_input = wait.until(EC.element_to_be_clickable((By.NAME, "Email Address")))
        email_input.send_keys(username)

        continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        continue_button.click()

        # get one-time password from email
        time.sleep(10)
        print("Waiting for email...")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        time.sleep(5)
        driver.quit()
