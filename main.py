import os
from datetime import date
import re
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Function to extract numbers from the link
def extract_numbers_from_link(link):
    match = re.search(r',(-?\d+),(-?\d+)', link)
    if match:
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        return number1, number2
    else:
        return None

# Function to find matching files in the download folder
def find_matching_files(download_folder, number1, number2):
    matching_files = []
    for filename in os.listdir(download_folder):
        match = re.search(fr'^pixelplanet-{number1}-{number2}', filename)
        if match:
            matching_files.append(filename)
    return matching_files


# Create a new instance of the Chrome driver 
link = input("Link for the location you want recorded")
initial_date = input("Date from which you want to start (in yyyy-mm-dd format):")  # Replace with the desired initial date

# Specify the path to the download folder
download_folder = "insert path to where your download files go"

today = date.today()
folder_name = initial_date + today.strftime("%Y-%m-%d")

# Create a new instance of the browser driver
driver = webdriver.Chrome()

driver.maximize_window()

# Open the web page
driver.get(link)

# Simulate pressing the 'h' key
actions = ActionChains(driver)
actions.send_keys('h').perform()

# Wait for the input element to be visible
wait = WebDriverWait(driver, 10)
date_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#historyselect input[type='date']")))

# Set the initial date value
date_input.clear()
date_input.send_keys(initial_date)
date_input.send_keys(Keys.RETURN)

# Function to handle the process from a specific date
def process_from_date(date):
    # Loop until the current date is reached
    current_date = time.strftime("%Y-%m-%d")
    while date != current_date:
        try:
            # Wait for the menu button to be clickable
            menu_button = wait.until(EC.element_to_be_clickable((By.ID, "menubutton")))
            menu_button.click()
            
            # Wait for the download button to be clickable
            download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "downloadbutton")))
            download_button.click()

            # Click the next button
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#historyselect .hsar:last-child")))
            next_button.click()

            # Get the updated date value
            date = driver.execute_script("return arguments[0].value;", date_input)

        except:
            # If an error occurs, print the error message and retry from the current date
            print("Error occurred. Retrying from current date:", date)
            process_from_date(date)
            break

# Process from the initial date input
process_from_date(initial_date)

# Extract numbers from the link
numbers = extract_numbers_from_link(link)
if numbers:
    number1, number2 = numbers
    print("Extracted numbers:", number1, number2)

    # Find matching files in the download folder
    matching_files = find_matching_files(download_folder, number1, number2)

    if matching_files:
        # Create a folder with the current date in the root directory

        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True)

        print("Created folder:", folder_name)

        # Move matching files to the new folder
        for filename in matching_files:
            src_path = os.path.join(download_folder, filename)
            dst_path = os.path.join(folder_path, filename)
            shutil.move(src_path, dst_path)

            print("Moved file:", filename)
    else:
        print("No matching files found.")
else:
    print("No numbers found in the link.")


# Close the browser window
driver.quit()
