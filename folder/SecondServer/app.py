import sys
import time
from urllib.parse import unquote
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Add this import to the existing imports
import os
import pyautogui
import autoit
import requests


# Retrieve the data from the command line arguments
if len(sys.argv) > 1:
    firstname = sys.argv[1]
    lastname = sys.argv[2]
    henkilotunnus = sys.argv[3]
    address = sys.argv[4]
    postnumber = sys.argv[5]
    city = sys.argv[6]
    phone = sys.argv[7]
    email = sys.argv[8]
    start_date = sys.argv[9]
    end_date = sys.argv[10]
    nationality = sys.argv[11]
    education_level = sys.argv[12]
    language_of_service = sys.argv[13]
    school_id = sys.argv[14]
    gender = sys.argv[15]
    moveToCapitalArea = sys.argv[16]
    tulolaji = sys.argv[17]
    monthly_income = sys.argv[18]
    Varallisuutta = sys.argv[19]
    Varallisuusmaara = sys.argv[20]
    file_path  = sys.argv[21]
    lisatiedot = sys.argv[22]
    student_number = sys.argv[23]
    housingSituationSelect = sys.argv[24]
    applicationReasonSelect = sys.argv[25]
    accountOfService = sys.argv[26]
    Loginemail = sys.argv[27]
    Loginpassword = sys.argv[28]
    hometype = sys.argv[29]
    area = sys.argv[30]
    file_pathx = sys.argv[31]
    file_pathxxxx = sys.argv[32]
    input_birth_date = sys.argv[33]
    languageOfServicePass = sys.argv[34]
    applicationReasonHoaSelect = sys.argv[35]
    completeness = sys.argv[36]
    Makepassword = sys.argv[37]
    stateID = sys.argv[38]
    desired_rent = sys.argv[39]

else:
    firstname = ''
    lastname = ''
    henkilotunnus = ''
    address = ''
    postnumber = ''
    city = ''
    phone = ''
    email = ''
    start_date = ''
    end_date = ''
    nationality = ''
    education_level = ''
    language_of_service = ''
    school_id = ''
    gender = ''
    moveToCapitalArea = ''
    tulolaji = ''
    monthly_income = ''
    Varallisuutta = ''
    Varallisuusmaara = ''
    file_path = ''
    lisatiedot = '' 
    student_number = '' 
    housingSituationSelect = '' 
    applicationReasonSelect = '' 
    accountOfService = '' 
    Loginemail = ''
    Loginpassword = ''
    hometype = ''
    area = ''
    file_pathx = ''
    file_pathxxxx = ''
    input_birth_date = ''
    languageOfServicePass = '' 
    applicationReasonHoaSelect = ''
    completeness = ''
    Makepassword = '' 
    stateID = ''
    desired_rent = ''

#print('Received firstname from index.html:', firstname)
#print('Received firstname from index.html:', lastname)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--window-size=192,108")  # Adjust the size as needed #this for headles we need fileset so cant do

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Set the window size after initializing the driver
#driver.set_window_size(1920, 1080)  # Adjust the size as needed
#This camn fuckup your sripts&clicks and 

try:
     







    pyautogui.FAILSAFE = False
    # must automat3e setup so trt give user temp email for application bs login process
    # Locate the button






    # Define a mapping from variable values to corresponding dropdown options
    income_source_mapping = {
        "753": "salary",            # Map 753 to option value "salary"
        "754": "pension",           # Map 754 to option value "pension"
        "755": "entrepreneurship",  # Map 755 to option value "entrepreneurship"
        "756": "studying",          # Map 756 to option value "studying"
        "757": "unemployment",      # Map 757 to option value "unemployment"
        "758": "other"              # Map 758 to option value "other"
    }










    normalized_path = os.path.normpath(file_path)
    normalized_pathx = os.path.normpath(file_pathx)
    normalized_pathxxxx = os.path.normpath(file_pathxxxx)

    # Find the last occurrence of "uploads\\"
    last_uploads_index = normalized_path.rfind("uploads\\")
    last_uploads_indexx = normalized_pathx.rfind("uploads\\")
    last_uploads_indexxxxx = normalized_pathxxxx.rfind("uploads\\")

    if last_uploads_index != -1:
        # Remove everything after "uploads/"
        trypath_conversion = normalized_path[:last_uploads_index + len("uploads\\")]
    else:
        # "uploads\\" not found, return the original path
        trypath_conversion = normalized_path 
    # Find the last occurrence of "uploads\"
    last_uploads_index = normalized_path.rfind("uploads\\")

    if last_uploads_index != -1:
        # Extract everything after "uploads\"
        remaining_part = normalized_path[last_uploads_index + len("uploads\\"):]
        # Remove everything after "uploads\"
        #trimmed_path = normalized_path[:last_uploads_index + len("uploads\\")]


    if last_uploads_indexx != -1:
        trypath_conversionx = normalized_pathx[:last_uploads_indexx + len("uploads\\")]
    else:
        trypath_conversionx = normalized_pathx 
    last_uploads_indexx = normalized_pathx.rfind("uploads\\")

    if last_uploads_indexx != -1:
        remaining_partx = normalized_pathx[last_uploads_indexx + len("uploads\\"):]

    if last_uploads_indexxxxx != -1:
        trypath_conversionxxxx = normalized_pathxxxx[:last_uploads_indexxxxx + len("uploads\\")]
    else:
        trypath_conversionxxxx = normalized_pathxxxx 
    last_uploads_indexxxxx = normalized_pathxxxx.rfind("uploads\\")

    if last_uploads_indexxxxx != -1:
        remaining_partxxxx = normalized_pathxxxx[last_uploads_indexxxxx + len("uploads\\"):]




    if accountOfService=='0':
        # must automat3e setup so trt give user temp email for application bs login process
        driver.get("https://www.emailnator.com/10minutemail/")
        #time.sleep(1)
        # Locate the input field by its placeholder attribute
        email_input = driver.find_element(By.XPATH, '//input[@placeholder="Email Adress"]')
        # Retrieve the value attribute of the input field
        email_value = email_input.get_attribute('value')
        time.sleep(2)


        # Wait for "Manage options" to become visible and click
        manage_options_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[2]"))
        )
        manage_options_button.click()

        # Wait for "Confirm choices" to become visible and click
        confirm_choices_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[3]/div[2]/button[2]/p"))
        )
        confirm_choices_button.click()
        
        time.sleep(3)

        
        # Wait for the element to be clickable (up to 10 seconds)
        #reload_button = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, "//button[@name='reloadMail']"))
        #)
        # Scroll into view if necessary
        #driver.execute_script("arguments[0].scrollIntoView(true);", reload_button)
        # Click on the button
        #reload_button.click()

        #input("Press Enter to close the browser...")
    # Wait for the element with XPath to be clickable (up to 10 seconds)
        
        # Wait for the element to be clickable (up to 10 seconds)
        #reload_buttonx = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, "//button[@name='reloadMail']"))
        #)
        # Scroll into view if necessary
        #driver.execute_script("arguments[0].scrollIntoView(true);", reload_buttonx)
        # Click on the button
        #reload_buttonx.click()

        #input("Press Enter to close the browser...")
        # Wait for the element to be clickable (up to 10 seconds)
        #reload_buttonxx = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, "//button[@name='reloadMail']"))
        #)
        # Scroll into view if necessary
        #driver.execute_script("arguments[0].scrollIntoView(true);", reload_buttonxx)
        # Click on the button
        #reload_buttonxx.click()

        #time.sleep(4)
        #second_xpath = "//table[@class='table table-hover']/tbody/tr[2]"
        #first_xpath = "//table[@class='table table-hover']/tbody/tr[1]"

        #try:
            # Try clicking the second tr element
        #    second_tr_element = WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.XPATH, second_xpath))
        #    )
        #    second_tr_element.click()
        #except:
        #    # If the second tr element is not found, click the first tr element
        #    first_tr_element = WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.XPATH, first_xpath))
        #    )
        #    first_tr_element.click()


        # Navigate to the starting page // try if same mail -> it is but different user gets new mail try safe
        driver.get("https://domo.ayy.fi/")
        # Scroll to the element
        #driver.get("https://www.emailnator.com/10minutemail/")
        #time.sleep(5)

        #submit_buttontryx = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Luo Domo-tili']")
        #driver.execute_script("arguments[0].scrollIntoView(true);", submit_buttontryx)
        #submit_buttontryx.click()

        # Scroll to the element
        # Wait up to 10 seconds for the bars icon to be present
        #bars_iconx = driver.find_element(By.XPATH, "//i[@class='fa fa-bars']")
        #driver.execute_script("arguments[0].scrollIntoView(true);", bars_iconx)
        #bars_iconx.click()
        # Scroll into view and click the bars icon

        bars_iconx = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-bars']"))
        )
        # Scroll into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", bars_iconx)
        # Click on the button
        bars_iconx.click()
        time.sleep(3)
        makeaccountbtn = driver.find_element(By.XPATH, "//a[@class='invert-ghost-button' and @href='/customers/sign_up']")
        driver.execute_script("arguments[0].scrollIntoView(true);", makeaccountbtn)
        makeaccountbtn.click()
        
        time.sleep(1)
        # Set value for the firstname input field
        firstname_input = driver.find_element(By.ID, 'customer_first_name')
        firstname_input.send_keys(firstname)

        # Set value for the lastname input field
        lastname_input = driver.find_element(By.ID, 'customer_last_name')
        lastname_input.send_keys(lastname)

        
        if languageOfServicePass == '2':

            # try if no idnuym like foreiner then try input date 

            # Parse the input date string
            date_object = datetime.strptime(input_birth_date, '%d.%m.%Y')

            # Format the date to the desired output format
            output_date = date_object.strftime('%Y-%m-%d')
            time.sleep(2)

            dobtry = driver.find_element(By.XPATH, "//label[@for='dob']")
            driver.execute_script("arguments[0].scrollIntoView(true);", dobtry)
            dobtry.click()

            time.sleep(5)

            # Locate the input field
            birth_date_input = driver.find_element(By.ID, "customer_date_of_birth")

            # Remove the 'readonly' attribute using JavaScript
            ###driver.execute_script("arguments[0].removeAttribute('readonly')", birth_date_input)
            #birth_date_input.click()
            #time.sleep(1)
            #birth_date_input.click()
            #time.sleep(1)
            # Clear existing content (if any) and set the new value
            #birth_date_input.clear()
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(Keys.BACKSPACE)
            #birth_date_input.send_keys(input_birth_date)  # Replace this with the desired date








            # Assuming the date format is dd.mm.yyyy
            day, month, year = map(int, input_birth_date.split('.'))

            # Explicit wait for the datepicker to be clickable
            wait = WebDriverWait(driver, 10)
            date_picker = wait.until(EC.element_to_be_clickable((By.ID, "customer_date_of_birth")))

            # Click on the datepicker to open it
            date_picker.click()
            time.sleep(2)
            # Explicit wait for the datepicker to be clickable
            wait = WebDriverWait(driver, 10)
            date_picker = wait.until(EC.element_to_be_clickable((By.ID, "customer_date_of_birth")))

            # Click on the datepicker to open it
            date_picker.click()

            # Select Year
            year_dropdown = Select(driver.find_element(By.CLASS_NAME, "picker__select--year"))
            year_dropdown.select_by_visible_text(str(year))

            # Select Month
            month_dropdown = Select(driver.find_element(By.CLASS_NAME, "picker__select--month"))
            month_dropdown.select_by_index(month - 1)  # Index is zero-based

            # Select Day
            # Perform an action to open the dropdown (e.g., click on the input field)
            # Wait for the day element to be clickable
            day_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{day}']"))
            )

            # Click on the day element to select it
            day_element.click()

            # Optional:#### Print a message to confirm the selection
           #### print(f"Selected day: {day}")
            # Close the datepicker (assuming there is a "Close" button)
            #input("try")





            # Send an additional key (e.g., ENTER) to trigger any date picker updates
            pyautogui.hotkey('enter')
            #####
            #Bug need somekind of physuical calendar select seemsatfirst could also be enter orclick on box
            ##
        else:        
            # Assuming you have the value for henkitunnus in a variable called henkitunnus_value
            henkilotunnus_input = driver.find_element(By.ID, 'customer_identity_number')
            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView(true);", henkilotunnus_input)
            # Input the value into the field
            henkilotunnus_input.send_keys(henkilotunnus)


        #input("try")
        # Set value for the email input field
        email_input = driver.find_element(By.ID, 'customer_email')
        email_input.send_keys(email_value) #email is actual user using temp for acount verification

        # Set value for the email input field
        email_confirmation_input = driver.find_element(By.ID, 'customer_email_confirmation')
        email_confirmation_input.send_keys(email_value) #email is actual user using temp for acount verification

        # Set value for the phone input field
        phone_input = driver.find_element(By.ID, 'customer_phone_number')
        phone_input.send_keys(phone)
        
        # Find the label using the associated text
        checkbox_label = driver.find_element(By.XPATH, '//label[text()="Yhteystietojani ei saa luovuttaa seuraavalle vuokralaiselle"]')
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label)
        # Click the label to toggle the checkbox
        checkbox_label.click()

        if gender == '193':
            # Find the label using the associated text
            gender_checkboxx = driver.find_element(By.XPATH, '//label[text()="Mies"]')
            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView(true);", gender_checkboxx)
            # Click the label to toggle the checkbox
            gender_checkboxx.click()
        elif gender == '194':
            # Find the label using the associated text
            gender_checkboxxx = driver.find_element(By.XPATH, '//label[text()="Nainen"]')
            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView(true);", gender_checkboxxx)
            # Click the label to toggle the checkbox
            gender_checkboxxx.click()
        elif gender == '2199':
            # Find the label using the associated text
            gender_checkboxxxx = driver.find_element(By.XPATH, '//label[text()="Muu/En halua kertoa/Haen vain unisex-soluja"]')
            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView(true);", gender_checkboxxxx)
            # Click the label to toggle the checkbox
            gender_checkboxxxx.click()
            #<option value="193">Mies</option>
            #<option value="194">Nainen</option>
            #<option value="2199">Muu</option>
        

        # Locate the input fields
        address_input = driver.find_element(By.ID, 'customer_street')
        postnumber_input = driver.find_element(By.ID, 'customer_postal_code')
        city_input = driver.find_element(By.ID, 'customer_city')

        # Scroll into view for each input field
        driver.execute_script("arguments[0].scrollIntoView(true);", address_input)
        driver.execute_script("arguments[0].scrollIntoView(true);", postnumber_input)
        driver.execute_script("arguments[0].scrollIntoView(true);", city_input)

        # Input the values into the fields
        address_input.send_keys(address)
        postnumber_input.send_keys(postnumber)
        city_input.send_keys(city)

        # Assuming you have the country value in a variable
        ###country_value = "FI"
        # Locate the country dropdown
        country_dropdown = Select(driver.find_element(By.ID, 'customer_country_code'))
        # Scroll into view for the country dropdown
        #driver.execute_script("arguments[0].scrollIntoView(true);", country_dropdown)
        # Select the country from the dropdown by its value
        country_dropdown.select_by_value(nationality)

        # Define a mapping from variable values to corresponding dropdown options
        education_level_mapping = {
            '309': "1",  # Map 309 to option value "1"
            '310': "4",  # Map 310 to option value "2"
            '311': "2",  # Map 311 to option value "3"
            '2413': "3"  # Map 2413 to option value "4"
        }

        # Locate the education level dropdown
        education_level_dropdown = Select(driver.find_element(By.ID, 'customer_customer_type_id'))

        # Scroll into view for the education level dropdown
        #driver.execute_script("arguments[0].scrollIntoView(true);", education_level_dropdown)




        # Select the corresponding option based on the variable value
        education_level_dropdown.select_by_value(str(education_level_mapping.get(education_level, "1")))
        time.sleep(1)
        #try does he have student number if have give it only asked here if not then give first file
        if student_number != '':
            # Locate the input field
            student_number_input = driver.find_element(By.ID, 'customer_student_number')

            # Scroll into view for the input field
            driver.execute_script("arguments[0].scrollIntoView(true);", student_number_input)

            # Input the value into the field
            student_number_input.send_keys(student_number)
        else:
            # Locate the input field
            student_number_input = driver.find_element(By.XPATH, "//label[@for='student_number_exists_no']")

            # Scroll into view for the input field
            driver.execute_script("arguments[0].scrollIntoView(true);", student_number_input)

            # Input the value into the field
            student_number_input.click()
            time.sleep(1)

            driver.find_element(By.XPATH, '//*[@id="new_customer"]/div[2]/fieldset[4]/div[2]/div/label/div[2]').click()
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(1)
            pyautogui.write(trypath_conversion)
            pyautogui.hotkey('enter')
            time.sleep(1)
            pyautogui.hotkey('alt', 'n')
            time.sleep(1)
            pyautogui.write(remaining_part)
            time.sleep(1)
            pyautogui.hotkey('enter')
            time.sleep(5)
        
       #### print(student_number)
            
        #input("try")
        # Locate the input field
        monthly_income_input = driver.find_element(By.ID, 'customer_income')
        # Scroll into view for the input field
        #driver.execute_script("arguments[0].scrollIntoView(true);", monthly_income_input)
        # Input the value into the field
        monthly_income_input.clear()
        monthly_income_input.send_keys(Keys.BACKSPACE)
        monthly_income_input.send_keys(monthly_income)


        # Locate the "tulolaji" dropdown
        income_source_dropdown = Select(driver.find_element(By.ID, 'customer_income_source'))

        # Scroll into view for the "tulolaji" dropdown
        #driver.execute_script("arguments[0].scrollIntoView(true);", income_source_dropdown)

        # Select the corresponding option based on the variable value
        income_source_dropdown.select_by_value(income_source_mapping.get(tulolaji, ""))

        # Locate the input field
        varallisuusmaara_input = driver.find_element(By.ID, 'customer_wealth')
        # Scroll into view for the input field
        driver.execute_script("arguments[0].scrollIntoView(true);", varallisuusmaara_input)
        # Input the value into the field
        varallisuusmaara_input.clear()
        varallisuusmaara_input.send_keys(Keys.BACKSPACE)
        varallisuusmaara_input.send_keys(Varallisuusmaara)
        
        if nationality != 'FI':
            time.sleep(2)

            # Find the input field using the provided XPath
            region_input = driver.find_element(By.XPATH, '//*[@id="customer_region"]')

            # Send keys to the input field
            region_input.send_keys(stateID)
        # Assuming you have the password value in a variable
        password_value = "abcdefgh11"
        # Locate the password input field
        password_input = driver.find_element(By.ID, 'customer_password')
        # Scroll into view for the password input field
        driver.execute_script("arguments[0].scrollIntoView(true);", password_input)
        # Input the password value into the field
        password_input.send_keys("a", "b", "c", "d", "e", "f", "g", "h", "1", "1")

        # Locate the password confirmation input field
        password_confirmation_input = driver.find_element(By.ID, 'customer_password_confirmation')
        # Scroll into view for the password confirmation input field
        driver.execute_script("arguments[0].scrollIntoView(true);", password_confirmation_input)
        # Input the password confirmation value into the field
        password_confirmation_input.send_keys("a", "b", "c", "d", "e", "f", "g", "h", "1", "1")


       
        # Locate the checkbox using the associated label text
        checkbox_label = driver.find_element(By.XPATH, "//label[text()='Annan suostumuksen henkilötietojeni käsittelyä varten Domo-järjestelmässä']")
        #checkbox_input = checkbox_label.find_element(By.XPATH, "./preceding-sibling::input[@type='checkbox']")

        # Scroll into view for the checkbox
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label)
        
        time.sleep(1)
        # Check the checkbox
        checkbox_label.click()
        time.sleep(1)

        #time.sleep(4)
        # Scroll to the "Seuraava" button
        # Locate the button using its attributes
        # Assuming this is your second page with the button
        #input("try")
        submit_buttontryx = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Luo Domo-tili']")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_buttontryx)
        submit_buttontryx.click()
        time.sleep(5)

        driver.get("https://www.emailnator.com/10minutemail/")
        time.sleep(5)

        






        #driver.get("https://www.emailnator.com/10minutemail/")
        #time.sleep(10)

        reload_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@name='reloadMail']"))
        )
        # Scroll into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", reload_button)
        # Click on the button
        reload_button.click()
        time.sleep(5)
        #input("try")

        # tryopen mail
        # Wait for the element to be clickable
        # Find all <td> elements with the specified email address
        email_tds = driver.find_elements(By.XPATH, '//td[contains(text(), "domo-no-reply@ayy.fi")]')
        # Click the first found <td> element
        if email_tds:
            email_tds[0].click()
        time.sleep(2)
        #input("try")
        # Wait for the element to be clickable
        time.sleep(2)
        # Find the element by its text content
        # Wait for the element to be present on the page
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Vahvista tilisi tästä!')]"))
        )

        # Click the element
        element.click()

        time.sleep(5)
        #input("try")
        # try fill datanofic
        # Wait for the element to be clickable
        wait = WebDriverWait(driver, 10)
        a_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='large-default-button expand-button' and @id='close-personal-data-reminder']")))
        # Click on the element
        a_element.click()

        #try start form fill after try register
        # Wait for the element to be clickable
        wait = WebDriverWait(driver, 10)
        a_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='large-default-button expand-button' and @href='/applications/new']")))
        # Click on the element
        a_element.click()


    elif accountOfService=='1':

        driver.get("https://domo.ayy.fi/")
        # Locate the element
        time.sleep(2)
        bars_icon = driver.find_element(By.XPATH, "//i[@class='fa fa-bars']")
        # Click on the element
        bars_icon.click()

        time.sleep(1)
        login_button = driver.find_element(By.XPATH, "//a[@class='invert-ghost-button' and @href='/customers/sign_in']")
        # Click on the button
        login_button.click()
        time.sleep(1)

        # Input email
        email_input = driver.find_element(By.ID, "customer_email")
        email_input.clear()  # Clear any existing text in the field
        email_input.send_keys(Loginemail)

        # Input password
        password_input = driver.find_element(By.ID, "customer_password")
        password_input.clear()  # Clear any existing text in the field
        password_input.send_keys(Loginpassword)
        
        # Locate and click the "Kirjaudu sisään" button
        login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Kirjaudu sisään']")
        login_button.click()
        #trystartapplication
        wait = WebDriverWait(driver, 10)
        a_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='large-default-button expand-button' and @href='/applications/new']")))
        # Click on the element
        a_element.click()



    #this try start fill form after either signup or login 

    #try start form fill after try register
    # Wait for the element to be clickable
    ###Also press here to fill in details for mailing list, to gain early access to our upcoming new revolutionary social media app you don't want to miss this!!!!!
    # Wait for the checkbox "Haen yksin" to be clickable
    checkbox_haen_yksin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='applicationType0']"))
    )
    # Click on the checkbox
    checkbox_haen_yksin.click()

    
    # Wait for the checkbox to be clickable
    wait = WebDriverWait(driver, 10)
    checkbox_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='childrenNo']")))
    # Check the checkbox
    checkbox_element.click()
    # Wait for the checkbox to be clickable for 'Solu'
    # Find and click the checkbox using its associated label

    #try hometype
    #Solu Soluyksiö Solukaksio Yksiö Kaksio (oh + mh) Kaksio (2 x mh)
    if hometype == '193':
        # Find and click the checkbox using its associated label
        checkbox_label_text = "Solu"
        # Wait for the element to be present and visible
        checkbox_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//label[text()='Solu']"))
        )
        #Solu Soluyksiö Solukaksio Yksiö Kaksio (oh + mh) Kaksio (2 x mh)
        # Scroll into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label)
        # Click the label (which should click the associated checkbox)
        checkbox_label.click()
        # Wait for the element to be present and visible
        checkbox_label_soluyksio = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Soluyksiö']"))
        )
        # Scroll into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label_soluyksio)
        # Click the label (which should click the associated checkbox)
        checkbox_label_soluyksio.click()
        # Wait for the element to be present and visible
        checkbox_label_solukaksio = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Solukaksio']"))
        )
        # Scroll into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label_solukaksio)
        # Click the label (which should click the associated checkbox)
        checkbox_label_solukaksio.click()
        
        
        #elif hometype == '194':
        #try all are prechecked uncheck none to get all try
    elif hometype == '2199':
        checkbox_label_yksio = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//label[text()='Yksiö']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label_yksio)
        checkbox_label_yksio.click()

        checkbox_label_kaksio = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Kaksio (oh + mh)']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label_kaksio)
        checkbox_label_kaksio.click()

        checkbox_label_kaksiotwo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Kaksio (2 x mh)']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label_kaksiotwo)
        checkbox_label_kaksiotwo.click()



    # Wait for the element to be present and visible
    checkbox_label_helsinki = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Helsinki']"))
    )
    time.sleep(1)
    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_label_helsinki)
    # Click the label (which should click the associated checkbox)
    if area == '193':
        checkbox_label_helsinki.click()
    time.sleep(3)
    

    if hometype == '193' and area == '193':
        #apartment_selector_checkbox_label
        unchecklep0 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="31"]'))
        )
        unchecklep0.click()
                #apartment_selector_checkbox_label
        unchecklep1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="32"]'))
        )
        unchecklep1.click()


    elif hometype == '194' and area == '193':
        #apartment_selector_checkbox_label
        unchecklep0 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="29"]'))
        )
        unchecklep0.click()
        driver.execute_script("arguments[0].scrollIntoView(true);", unchecklep0)
        unchecklep1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="31"]'))
        )
        unchecklep1.click()
        #apartment_selector_checkbox_label
        unchecklep2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="32"]'))
        )
        unchecklep2.click()
    elif hometype == '2199' and area == '193':
        #apartment_selector_checkbox_label
        unchecklep0 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="29"]'))
        )
        unchecklep0.click()
        unchecklep1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="31"]'))
        )
        unchecklep1.click()
                #apartment_selector_checkbox_label
        unchecklep2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="32"]'))
        )
        unchecklep2.click()

        #18
        #17
        #67
        #66
        #107
        #81
        #80 # for these try not uncheck helsinki
    if hometype == '193' and area == '194':
            #apartment_selector_checkbox_label
        unchecklep0x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="18"]'))
        )
        unchecklep0x.click()        
        unchecklep1x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="17"]'))
        )
        unchecklep1x.click()   
        unchecklep2x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="67"]'))
        )
        unchecklep2x.click()   
        unchecklep3x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="66"]'))
        )
        unchecklep3x.click()     
        unchecklep4x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="107"]'))
        )
        unchecklep4x.click()   
        unchecklep5x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="81"]'))
        )
        unchecklep5x.click()   
        unchecklep6x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="80"]'))
        )
        unchecklep6x.click()   
    elif hometype == '194' and area == '194':
            #apartment_selector_checkbox_label
        unchecklep0x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="18"]'))
        )
        unchecklep0x.click()        
        unchecklep1x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="17"]'))
        )
        unchecklep1x.click()   
        unchecklep2x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="67"]'))
        )
        unchecklep2x.click()   
        unchecklep3x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="66"]'))
        )
        unchecklep3x.click()     
        unchecklep4x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="107"]'))
        )
        unchecklep4x.click()   
        unchecklep5x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="81"]'))
        )
        unchecklep5x.click()   
        unchecklep6x = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="80"]'))
        )
        unchecklep6x.click()   
        #try no unchecks
    #elif hometype == '2199' and area == '194':
        ##apartment_selector_checkbox_label
        #unchecklep0 = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="29"]'))
        #)
                
        #unchecklep1 = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="31"]'))
        #)
        #        #apartment_selector_checkbox_label
        #unchecklep2 = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="32"]'))
        #)
    
    #elif other no need to uncheck boxes we take all from helsinki espoo (no other areas like vantaa available atm 1/17/2024)


    #input("try")

    time.sleep(2)
    # Replace '520' with the desired rent value
    #desired_rent = 1250
    #en = driver.find_element(By.CLASS_NAME, "irs-slider.to")
    #move = ActionChains(driver)
    #trysmh = 420
    #trygit = int(420-(0.365*desired_rent)+38)
    #move.click_and_hold(en).move_by_offset(-trygit, 0).release().perform()
    #time.sleep(5)
    #move.click_and_hold(en).move_by_offset(trygit, 0).release().perform()
    #time.sleep(1)

    #desired_rent = 520
    desired_rent = int(desired_rent)
    en = driver.find_element(By.CLASS_NAME, "irs-slider.to")
    move = ActionChains(driver)
    trysmh = 420
    trygit = int(420-(0.365*desired_rent)+38)
    move.click_and_hold(en).move_by_offset(-trygit, 0).release().perform()
    time.sleep(5)
    ###move.click_and_hold(en).move_by_offset(trygit, 0).release().perform() ### Trytesting
    ###time.sleep(1)

    #desired_rent = 250
    #en = driver.find_element(By.CLASS_NAME, "irs-slider.to")
    #move = ActionChains(driver)
    #trysmh = 420
    #trygit = int(420-(0.365*desired_rent)+38)
    #move.click_and_hold(en).move_by_offset(-trygit, 0).release().perform()
    #time.sleep(5)
    #move.click_and_hold(en).move_by_offset(trygit, 0).release().perform()
    #ime.sleep(1)


    #move.click_and_hold(en).move_by_offset(-10, 0).release().perform()
    #time.sleep(5)

    #move.click_and_hold(en).move_by_offset(10, 0).release().perform()
    #time.sleep(5)

    input("try")
    #try accept user profile
    # Locate the button
    button = driver.find_element(By.XPATH, "//a[@class='large-default-button expand-button ng-binding ng-scope']")
    # Scroll to the button using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    # Click on the button
    button.click()
    # Wait for the element to be present and visible
    time.sleep(4)

    button = driver.find_element(By.XPATH, "//button[@class='large-default-button expand-button ng-binding']")
    # Wait for the button to be clickable
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='large-default-button expand-button ng-binding']")))
    # Click on the button
    button.click()
    time.sleep(1)

    #now newpage try select final info 
    # Locate the dropdown element
    dropdown = driver.find_element(By.NAME, "housingSituationSelect")
    # Create a Select object
    select = Select(dropdown)
    # Select the option by visible text
    select.select_by_value(housingSituationSelect)
    # Wait for the dropdown to be present
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "applicationReasonSelect"))
    )
    # Create a Select object
    selectx = Select(dropdown)
    # Select the option by visible text
    selectx.select_by_value(applicationReasonSelect)
    time.sleep(2)
    # Locate the textarea element
    textarea = driver.find_element(By.NAME, "urgentReasonNote")
    # Clear any existing text in the textarea
    textarea.clear()
    # Type the new text into the textarea
    textarea.send_keys(lisatiedot)
    time.sleep(2)

    #excuse try file might try need second
    # Find the file input element
    # Find the first file input field using its XPath
    # Locate the file input element
    # Wait for the file input to be present
    # Find the file input element
    #input("try coordinate")
    #print(cursor_position)
    # Get all iframes on the page
    # File path
    #file_path = "C:\\Users\\elias\\Desktop\\trytogroup\\uploads\\lataus_4.png"
    # Open the website with your file input (replace with your URL)
    # Make sure the file input is visible on the screen
    # (You may need to manually open the browser and navigate to the page before running this script)
    # Example:
    #pyautogui.click(239, 848)  # Click on the coordinates where the file input is located
    #
    # Wait for the file input to be ready
    #trypath_conversion = file_path.replace("\\", "/")
    # Use os.path.normpath to handle different path separators
    
    #else:
    #    # "uploads\" not found, return the original path as trimmed path and an empty string for remaining part
    #    return normalized_path, ""
   #### print(trypath_conversion)
   #### print(trypath_conversionx)
   #### print(trypath_conversionxxxx)

    time.sleep(3)  # Adjust the sleep time   based on your needs
    #input("try") 
    # Simulate the key press Ctrl+L to focus on the file path in the file manager
    #driver.find_element(By.XPATH, '//*[@id="ng-new-application"]/div/div/div[2]/form/div[1]/div/div/fieldset[2]/div[3]/div[1]/div/label/div').click()
    #time.sleep(1)
    #already gave this form
    #pyautogui.hotkey('ctrl', 'l')
    #time.sleep(1)
    #pyautogui.write(trypath_conversion)
    #pyautogui.hotkey('enter')
    #time.sleep(1)
    #pyautogui.hotkey('alt', 'n')
    #time.sleep(1)
    #pyautogui.write(remaining_part)
    #time.sleep(1)
    #pyautogui.hotkey('enter')
    #time.sleep(5)
    #input("try")
    driver.find_element(By.XPATH, '//*[@id="ng-new-application"]/div/div/div[2]/form/div[1]/div/div/fieldset[2]/div[3]/div[1]/div/label/div').click()
    #driver.find_element(By.XPATH, '//*[@id="ng-new-application"]/div/div/div[2]/form/div[1]/div/div/fieldset[2]/div[3]/div[1]/div/label/div').click()
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write(trypath_conversionx)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('alt', 'n')
    time.sleep(2)
    pyautogui.write(remaining_partx)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="ng-new-application"]/div/div/div[2]/form/div[1]/div/div/fieldset[2]/div[3]/div[1]/div/label/div').click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(4)
    pyautogui.write(trypath_conversionxxxx)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('alt', 'n')
    time.sleep(3)
    pyautogui.write(remaining_partxxxx)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(5)
    #input("try")
    #url = "https://domo.ayy.fi/customer_upload/extra_points"
    #file_path = "C:\\Users\\elias\\Desktop\\trytogroup\\uploads\\lataus_4.png"

    # Set the boundary string
    #boundary = '------WebKitFormBoundary7XkVEUQVtixSo0Mp'

    # Create the headers with the boundary
    #headers = {
    #    'Content-Type': f'multipart/form-data; boundary={boundary}',
    #}

    # Read the file content
    #with open(file_path, 'rb') as file:
    #    # Create the payload
    #    payload = (
    #        f'--{boundary}\r\n'
    #        f'Content-Disposition: form-data; name="attachment_type"\r\n\r\n'
    #        f'extra_points\r\n'
    #        f'--{boundary}\r\n'
    #        f'Content-Disposition: form-data; name="file"; filename="lataus_4.png"\r\n'
    #        f'Content-Type: image/png\r\n\r\n'
    #        f'{file.read()}\r\n'
    #        f'--{boundary}--\r\n'
    #    )

    #    # Send the POST request
    #    response = requests.post(url, headers=headers, data=payload)

    #print(response.status_code)
    #print(response.text)
    # Type the file path and press Enter
    #input("try coordinate")
    #cursor_position = pyautogui.position()
    #time.sleep(1)
    #pyautogui.click(806, 512)  # Click on the coordinates where the file input is located

    # Submit the form or perform any additional steps needed
    # (you may need to adjust the selector and method based on the actual website)
    #/html/body

    
    time.sleep(5)
    #After all updates/uploads and small waiting time try delete all files user security standard practices
    #try
    #input("try")
    # Click the first checkbox
    first_checkbox_label_text = "Olen lukenut ja hyväksyn asuntojen hakemiseen liittyvät ehdot."
    first_checkbox_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//label[text()='{first_checkbox_label_text}']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", first_checkbox_label)
    first_checkbox_label.click()
    time.sleep(2)
    #input("try")
    # Click the second checkbox with an additional wait
    # Press on the checkbox
    # Click the checkbox using JavaScript
    checkbox_idxxxx = "acceptedPrivacyTerms"
    checkbox_scriptxxxx = f"document.getElementById('{checkbox_idxxxx}').click();"
    driver.execute_script(checkbox_scriptxxxx)

    time.sleep(2)
    # Navigate to the webpage
    # Wait for the button to be clickable (you may adjust the timeout as needed)
    trysend_button_xpath = "//button[@class='large-default-button expand-button']"
    trysend_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, trysend_button_xpath)))
    ### tryatsnd
    ###trysend_button.click()

    # Perform other actions or interactions with the page as needed
    








    
    # try login and try change email and password to user request
    if accountOfService=='0':
        time.sleep(6)
        driver.get("https://google.fi/")
        time.sleep(6)
        driver.get("https://domo.ayy.fi/")
        

        # Locate the element
        time.sleep(2)
        bars_iconxx = driver.find_element(By.XPATH, "//i[@class='fa fa-bars']")
        # Click on the element
        bars_iconxx.click()

        time.sleep(1)
        login_button = driver.find_element(By.XPATH, "//a[@class='invert-ghost-button' and @href='/customers/sign_in']")
        # Click on the button
        login_button.click()
        time.sleep(1)

        # Input email
        email_input = driver.find_element(By.ID, "customer_email")
        email_input.clear()  # Clear any existing text in the field
        email_input.send_keys(email_value) #temnatorothermail ##email just temp

        # Input password
        password_input = driver.find_element(By.ID, "customer_password")
        password_input.clear()  # Clear any existing text in the field
        password_input.send_keys("abcdefgh1") #tempasswordgiven ## aaaabbbb1 just temp
        
        # Locate and click the "Kirjaudu sisään" button
        login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Kirjaudu sisään']")
        login_button.click()
        #trystartapplication
        time.sleep(2)
        bars_icon = driver.find_element(By.XPATH, "//i[@class='fa fa-bars']")
        # Click on the element
        bars_icon.click()
        
        time.sleep(1)
        edit_button = driver.find_element(By.XPATH, "//a[@class='invert-ghost-button' and @href='/customers/edit']")
        # Click on the button
        edit_button.click()
        time.sleep(1)

        # Set value for the email input field
        email_input = driver.find_element(By.ID, 'customer_email')
        email_input.clear()
        email_input.send_keys(email) #email is actual user using temp for acount verification

        # Set value for the email input field
        email_confirmation_input = driver.find_element(By.ID, 'customer_email_confirmation')
        email_confirmation_input.clear()
        email_confirmation_input.send_keys(email) #email is actual user using temp for acount verification

        # Set value for the email input field
        passwrd_input = driver.find_element(By.XPATH, '//*[@id="customer_password"]')
        email_confirmation_input.clear()
        passwrd_input.send_keys(Makepassword) #email is actual user using temp for acount verification

        #confitry
        #confitry = driver.find_element(By.XPATH, "//label[@for='customer_confidential_information']")
        #confitry.click()

        # Set value for the email input field
        passwrd_confirmation_input = driver.find_element(By.XPATH, '//*[@id="customer_password_confirmation"]')
        passwrd_confirmation_input.send_keys(Makepassword) #email is actual user using temp for acount verification

        time.sleep(2)
        # Set value for the email input field
        passwrd_try_input = driver.find_element(By.XPATH, '//*[@id="customer_current_password"]')
        passwrd_try_input.send_keys("abcdefgh11") #email is actual user using temp for acount verification
        
        income_source_dropdown = Select(driver.find_element(By.ID, 'customer_income_source'))

        # Scroll into view for the "tulolaji" dropdown
        #driver.execute_script("arguments[0].scrollIntoView(true);", income_source_dropdown)

        # Select the corresponding option based on the variable value
        income_source_dropdown.select_by_value(income_source_mapping.get(tulolaji, ""))

        time.sleep(1)
        #input("try")
        # Locate and click the "Kirjaudu sisään" button
        update_button = driver.find_element(By.XPATH, '//*[@id="edit_customer"]/div[3]/div/input')
        update_button.click()    
        time.sleep(1)
        #input("try")

        
















    # Navigate to the starting page
        # Navigate to the starting page



    

    driver.get("https://application.hoas.fi/")
    
    if area == '193':
        # Wait for the "Espoo" label to be present
        espoo_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_0"]'))
        )

        # Click the "Espoo" label
        espoo_label.click()

    elif area == '194':
        # Wait for the "Espoo" label to be present
        espoo_label0 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_0"]'))
        )

        # Click the "Espoo" label
        espoo_label0.click()
                # Wait for the "Espoo" label to be present
        espoo_label1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_1"]'))
        )

        # Click the "Espoo" label
        espoo_label1.click()
                # Wait for the "Espoo" label to be present
        espoo_label2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_2"]'))
        )

        # Click the "Espoo" label
        espoo_label2.click()
                # Wait for the "Espoo" label to be present
        espoo_label3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_3"]'))
        )

        # Click the "Espoo" label
        espoo_label3.click()
    elif area == '2199':
                # Wait for the "Espoo" label to be present
        espoo_label0 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_0"]'))
        )

        # Click the "Espoo" label
        espoo_label0.click()
                # Wait for the "Espoo" label to be present
        espoo_label1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_1"]'))
        )

        # Click the "Espoo" label
        espoo_label1.click()
                # Wait for the "Espoo" label to be present
        espoo_label2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_2"]'))
        )

        # Click the "Espoo" label
        espoo_label2.click()
                # Wait for the "Espoo" label to be present
        espoo_label3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunkiId_3"]'))
        )

        # Click the "Espoo" label
        espoo_label3.click()
    
    time.sleep(5)
    #needed loading time to try get
    #areas near campus
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_1
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_3
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_4
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_5
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_6
    #if area == '193':
    #    # Click the labels for "Otaniemi teekkarikylä" and "Otaniemi-Tapiola"
    #    otaniemi_teekkarikyla_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_5"]')
    #    driver.execute_script("arguments[0].scrollIntoView(true);", otaniemi_teekkarikyla_label)
    #    otaniemi_teekkarikyla_label.click()

        #otaniemi_tapiola_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_6"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", otaniemi_tapiola_label)
        #otaniemi_tapiola_label.click()
    #elif area == '194':
    #    # Click the labels for "Otaniemi teekkarikylä" and "Otaniemi-Tapiola" //Consider implementing name based if provider fcks settings
    #    trysend0 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_0"]')
    #    driver.execute_script("arguments[0].scrollIntoView(true);", trysend0)
    #    trysend0.click()

        #trysend1 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_2"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend1)
        #trysend1.click()

        #trysend2 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_5"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend2)
        #trysend2.click()

        #trysend3 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_8"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend3)
        #trysend3.click()

        #trysend4 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_10"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend4)
        #trysend4.click()

        #trysend5 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_11"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend5)
        #trysend5.click()

        #trysend6 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_12"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend6)
        #trysend6.click()

        #trysend7 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_14"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend7)
        #trysend7.click()

        #trysend8 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_16"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend8)
        #trysend8.click()

        #trysend9 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_17"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend9)
        #trysend9.click()

        #trysend10 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_21"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend10)
        #trysend10.click()

        #trysend11 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_23"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend11)
        #trysend11.click()

        #trysend12 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_24"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend12)
        #trysend12.click()

        #trysend13 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_25"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend13)
        #trysend13.click()

        #trysend14 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_28"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend14)
        #trysend14.click()

        #trysend15 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_30"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend15)
        #trysend15.click()

        #trysend16 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_33"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend16)
        #trysend16.click()

        #trysend17 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_34"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend17)
        #trysend17.click()

        #trysend18 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_35"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend18)
        #trysend18.click()

        #trysend19 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_36"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend19)
        #trysend19.click()

        #trysend20 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_39"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend20)
        #trysend20.click()

        #trysend21 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_41"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend21)
        #trysend21.click()

        #trysend22 = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_42"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend22)
        #trysend22.click()
    #elif area == '2199':
        #trysend = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_39"]')
        #driver.execute_script("arguments[0].scrollIntoView(true);", trysend)
        #trysend.click()
    #no cells
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_12
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_14
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_16
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_17
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_21
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_23
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_24
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_25
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_28
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_30
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_33
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_34
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_35
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_36
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_39
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_41
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_42

    area_selector_mapping = {
        '193': [5, 6],
        '194': [0, 2, 5, 8, 10, 11, 12, 14, 16, 17, 21, 23, 24, 25, 28, 30, 33, 34, 35, 36, 39, 41, 42],
        '2199': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]

    }

    if area in area_selector_mapping:
        for index in area_selector_mapping[area]:
            selector = f'MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_{index}'
            element = driver.find_element(By.CSS_SELECTOR, f'label[for="{selector}"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()


    if hometype == '193':
        # Click the labels for "Yksiö" and "Kaksio"
        yksio_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblHuoneistotyyppiId_1"]')
        yksio_label.click()

        kaksio_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblHuoneistotyyppiId_2"]')
        kaksio_label.click()
        #all types reasonable size
    elif hometype == '194':
        # Click the labels for "Yksiö" and "Kaksio"
        yksio_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblHuoneistotyyppiId_1"]')
        yksio_label.click()

        kaksio_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblHuoneistotyyppiId_2"]')
        kaksio_label.click()

        kaksio_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblHuoneistotyyppiId_0"]')
        kaksio_label.click()
        #only cells
    elif hometype == '2199':
        # Click the labels for "Yksiö" and "Kaksio"
        yksio_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucKohdehaku_cblHuoneistotyyppiId_0"]')
        yksio_label.click()

    #input("try")
    #areas near campus
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_1
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_3
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_4
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_5
    #MainPlaceHolder_ucKohdehaku_cblKaupunginosaId_6

    # Fill text into the first input element
    neliorajaus_min_input = driver.find_element(By.ID, 'MainPlaceHolder_ucKohdehaku_txtNeliorajausMin')
    neliorajaus_min_input.clear()
    neliorajaus_min_input.send_keys("8")

    # Fill text into the second input element
    vuokra_max_input = driver.find_element(By.ID, 'MainPlaceHolder_ucKohdehaku_txtVuokraMax')
    vuokra_max_input.clear()
    #vuokra_max_input.send_keys("599")
    vuokra_max_input.send_keys(desired_rent)
    time.sleep(2)

    # Click the "Seuraava" button
    seuraava_button = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_button)
    seuraava_button.click()

    # Click each checkbox with the specified characteristics
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'td[style="width:44px;"] input[type="checkbox"]')
    # Only for special cases
    for checkbox in checkboxes:
        checkbox.click()

    # Fill text into the first input element
    etu_nimi = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtEtunimet')
    etu_nimi.clear()
    etu_nimi.send_keys(firstname)

    # Fill text into the first input element
    etu_nimi = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtSukunimi')
    etu_nimi.clear()
    etu_nimi.send_keys(lastname)


    # Fill text into the first input element
    address_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtOsoite')
    address_input.clear()
    address_input.send_keys(address)

    # Fill text into the first input element
    postnumber_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtPostinumero')
    postnumber_input.clear()
    postnumber_input.send_keys(postnumber)

    # Fill text into the first input element
    city_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtPostitoimipaikka')
    city_input.clear()
    city_input.send_keys(city)

    # Fill text into the first input element
    phone_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtMatkapuhelin')
    phone_input.clear()
    phone_input.send_keys(phone)

    # Fill text into the first input element
    email_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtSahkoposti')
    email_input.clear()
    email_input.send_keys(email)

    # Fill text into the first input element
    email_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtSahkoposti')
    email_input.clear()
    email_input.send_keys(email)

    # Fill text into the first input element
    start_date_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtOppilaitosAlkaen')
    start_date_input.clear()
    start_date_input.send_keys(start_date)

    # Fill text into the first input element
    end_date_input = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtOppilaitosValmistuminen')
    end_date_input.clear()
    end_date_input.send_keys(end_date)

    # List of EU country codes
    eu_countries = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "GR", "HR", "HU", "IE", "IT", "LT", "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK"]

    # Mapping the selected nationality to the desired variable
    if nationality == "FI":
        narrow_nationality = "42"
    elif nationality in eu_countries:
        narrow_nationality = "195"
    else:
        narrow_nationality = "196"
    #Ayy uses wider mapping so try to bsfix by remaping to hoas narrows...

    # Now, 'narrow_nationality' contains the mapped value based on the selected nationality
   #### print(narrow_nationality)

    nationality_select = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlKansalaisuusId')
    nationality_select.send_keys(narrow_nationality)

    # Add these lines to select the values for the new dropdown fields
    education_level_select = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlOppilaitosTutkintoLinjaId')
    education_level_select.send_keys(education_level)

    school_id_select = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlOppilaitosId')
    school_id_select.send_keys(school_id)
    
    # Dropdown for Nationality
    nationality_select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlKansalaisuusId'))
    nationality_select.select_by_value(narrow_nationality)

    #try handle cases with no fin id also try other application giive just birth date
    if nationality != 'FI' and languageOfServicePass == '0':
        # Scroll to the specified label
        nonfinbutton = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucHakijat_Hakija1of4_rblTunnistautumistapa_2"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", nonfinbutton)
        time.sleep(2)
        nonfinbutton.click()
    elif nationality != 'FI' and languageOfServicePass == '2':
        # Scroll to the specified label
        nonfinbutton = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucHakijat_Hakija1of4_rblTunnistautumistapa_0"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", nonfinbutton)
        time.sleep(2)
        nonfinbutton.click()

    #input("try")
    # Fill text into the first input element
    if languageOfServicePass == '0':
        henkilo_tunnus = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtHenkilotunnus')
        time.sleep(2)
        henkilo_tunnus.clear()
        henkilo_tunnus.send_keys(henkilotunnus)
    elif languageOfServicePass == '2':
        pasportout_tunnus = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtPassinNumero')
        time.sleep(2)
        pasportout_tunnus.clear()
        pasportout_tunnus.send_keys(henkilotunnus)

        # Locate the input field
        birth_date_inputx = driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_txtSyntymaaika')

        # Remove the 'readonly' attribute using JavaScript
        driver.execute_script("arguments[0].removeAttribute('readonly')", birth_date_inputx)

        # Clear existing content (if any) and set the new value
        birth_date_inputx.clear()
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(Keys.BACKSPACE)
        birth_date_inputx.send_keys(input_birth_date)  # Replace this with the desired date

        # Send an additional key (e.g., ENTER) to trigger any date picker updates
        birth_date_inputx.send_keys(Keys.ENTER)

    # Dropdown for Education Level
    education_level_select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlOppilaitosTutkintoLinjaId'))
    education_level_select.select_by_value(education_level)

    # Dropdown for Language of Service
    language_of_service_select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlAsiointikieli'))
    language_of_service_select.select_by_value(language_of_service)
    #input("try")
    # Dropdown for School ID
    school_id_select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlOppilaitosId'))
    school_id_select.select_by_value(school_id)

    # Dropdown for Gender
    gender_select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlSukupuoliId'))
    gender_select.select_by_value(gender)
    time.sleep(10)

    # Add these lines to select the values for the new dropdown fields
    next_button = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    next_button.click()
    time.sleep(3)
    #input("try")
    # Scroll to the specified label
    ei_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucMuutHakijat_rblRaskaustodistus_0"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", ei_label)
    ei_label.click()
    time.sleep(4)

    # Scroll to the "Seuraava" button
    seuraava_buttonx = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_buttonx)
    seuraava_buttonx.click()
    #time.sleep(1)


# Scroll to the "Kyllä" label
    kylla_label = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucAsunnontarve_Hakija1of4_rblRESERVED_OnkoHakijallaAsuntoa_1"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", kylla_label)
    kylla_label.click()

    if moveToCapitalArea=='0':
        # Select "Ei"
        # Scroll to the "Ei" label
        kylla_labelx = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucAsunnontarve_Hakija1of4_rblMuuttoPaikkakunnalle_0"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", kylla_labelx)
        kylla_labelx.click()
        # OR
    else:
        # Select "Kyllä"
        ei_labelx = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucAsunnontarve_Hakija1of4_rblMuuttoPaikkakunnalle_1"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", ei_labelx)
        ei_labelx.click()

    # Get the current date in the desired format (dd.mm.yyyy)
    current_date = datetime.now().strftime("%d.%m.%Y")

    # Find the input field for "AsunnontarveAlkaen"
    asunnontarve_alkaen_input = driver.find_element(By.ID, 'MainPlaceHolder_ucAsunnontarve_Hakija1of4_txtAsunnontarveAlkaen')

    # Clear existing value and set the current date
    asunnontarve_alkaen_input.send_keys(current_date)
    asunnontarve_alkaen_input.clear()
    asunnontarve_alkaen_input.send_keys(current_date)



    # Get the current date
    current_date = datetime.now()

    # Format the current date as "dd.mm.YYYY"
    formatted_date = current_date.strftime("%d.%m.%Y")

    ##### Print the formatted date
   #### print("Current Date:", formatted_date)

    # Add 5 years to the current date
    future_date = current_date + timedelta(days=365 * 5)

    # Format the future date as "dd.mm.YYYY"
    formatted_future_date = future_date.strftime("%d.%m.%Y")

    # Fill text into the input element for start date
    start_date_inputx = driver.find_element(By.ID, 'MainPlaceHolder_ucAsunnontarve_Hakija1of4_txtAsunnontarvePaattyen')
    # Clear existing value and set the current date
    # Wait for the element to be present and clickable
    # Open the website
    # Find the input field by its ID
    # Click on the input field to activate it
    # Find the input field using XPath
    # Find the input field by its ID

    # Clear the input field using JavaScript
    driver.execute_script("arguments[0].value = '';", start_date_inputx)

    # Send new keys
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(Keys.BACKSPACE)
    start_date_inputx.send_keys(formatted_future_date)
    driver.execute_script("arguments[0].blur();", start_date_inputx)

    #input("try")
    # Locate the dropdown element by its id
    muuttovelvoite_dropdown = Select(driver.find_element(By.ID,'MainPlaceHolder_ucAsunnontarve_Hakija1of4_ddlMuuttovelvoiteId'))
    # Select the option by its value attribute
    muuttovelvoite_dropdown.select_by_value(applicationReasonHoaSelect)  # Assuming "2416" corresponds to "Nykyinen vuokra liian suuri"
    # Dropdown for Gender
    muuttovelvoite_dropdown = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucAsunnontarve_Hakija1of4_ddlMuuttovelvoiteId'))
    muuttovelvoite_dropdown.select_by_value(applicationReasonHoaSelect)
    #input("try")

    # Scroll to the "Seuraava" button
    seuraava_buttonxxxxx = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_buttonxxxxx)
    seuraava_buttonxxxxx.click()
    # Scroll to the "Seuraava" button
    time.sleep(1)   
    
    # Create a Select object
    select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucTulot_Hakija1of4_ddlTulolajit'))
    # Select an option by its value attribute
    select.select_by_value(tulolaji)  # Selects the option with value "753" (Palkka)
    
    # Dropdown for Gender
    #gender_select = Select(driver.find_element(By.ID, 'MainPlaceHolder_ucHakijat_Hakija1of4_ddlSukupuoliId'))
    #gender_select.select_by_value(gender)
    # Find the input fields by their IDs
    bruttotulot_input = driver.find_element(By.ID, 'MainPlaceHolder_ucTulot_Hakija1of4_txtBruttotulot')
    bruttotulot_input.clear()
    bruttotulot_input.send_keys(monthly_income)

    #opintolaina_input = driver.find_element(By.ID, 'MainPlaceHolder_ucTulot_Hakija1of4_txtOpintolaina')
    #opintolaina_input.clear()
    #opintolaina_input.send_keys(taken_studyloans)

    # Input the value 0 into the fields
    time.sleep(1) 

    # Scroll to the "Seuraava" button
    seuraava_buttonxxxxxxxxx = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_buttonxxxxxxxxx)
    seuraava_buttonxxxxxxxxx.click()
    time.sleep(1) 
    #input("try")
    if Varallisuutta=='0':
        # Select "Kyllä"
        Varallisuutta = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucVarallisuus_Hakija1of4_cblOmistuskohteet_3"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", Varallisuutta)
        Varallisuutta.click()
        # OR
    else:
        # Select "Ei"
        EiVarallisuutta = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_ucVarallisuus_Hakija1of4_cblOmistuskohteet_4"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", EiVarallisuutta)
        EiVarallisuutta.click()

    varallisuusarvo = driver.find_element(By.ID, 'MainPlaceHolder_ucVarallisuus_Hakija1of4_txtVarallisuusArvo')
    varallisuusarvo.clear()
    varallisuusarvo.send_keys(Varallisuusmaara)
    time.sleep(1) 

    # Scroll to the "Seuraava" button
    seuraava_buttonxxxxxxxxxx = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_buttonxxxxxxxxxx)
    seuraava_buttonxxxxxxxxxx.click()
    time.sleep(2)

    # Set the file path
    #file_path = os.path.abspath(file_path)

    # Locate the file input element by its ID
    #file_input = driver.find_element(By.ID, 'MainPlaceHolder_ucLiitteet_Hakija1of4_fileOpiskelutodistus_1')

    #file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    #driver.execute_script("arguments[0].scrollIntoView(true);", file_input)
    #file_input.send_keys("C:\\Users\\elias\\Desktop\\trytogroup\\uploads\\lataus_4.png")
    #driver.find_element(By.ID, "MainPlaceHolder_ucLiitteet_Hakija1of4_fileLblHuoltajansuostumus_0").click()
    #driver.find_element(By.XPath, "MainPlaceHolder_ucLiitteet_Hakija1of4_fileLblHuoltajansuostumus_0").send_keys(os.getcwd()+"/screenshot.png")
    #time.sleep(5)
    #driver.find_element(By.ID, "MainPlaceHolder_ucLiitteet_Hakija1of4_fileLblHuoltajansuostumus_0").click()
    #time.sleep(5)

    if file_path != '':
        buttonx = driver.find_element(By.ID, "MainPlaceHolder_ucLiitteet_Hakija1of4_fileOpiskelutodistus_0")
        buttonx.send_keys(file_path)
    time.sleep(1) 

    # Scroll to the "Seuraava" button
    seuraava_buttonxxxxxxxxxxxxx = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_buttonxxxxxxxxxxxxx)
    seuraava_buttonxxxxxxxxxxxxx.click()
    time.sleep(2)
    # Clear any existing text in the file input
    #file_input.clear()
    textareax = driver.find_element(By.ID, 'MainPlaceHolder_ucMuutTiedot_txtHakuMuuta')
    textareax.clear()
    textareax.send_keys(lisatiedot)

    # Scroll to the "Seuraava" button
    seuraava_buttonxxxxxxxxxxxxxxx = driver.find_element(By.ID, 'MainPlaceHolder_btnForward')
    driver.execute_script("arguments[0].scrollIntoView(true);", seuraava_buttonxxxxxxxxxxxxxxx)
    seuraava_buttonxxxxxxxxxxxxxxx.click()
    time.sleep(2)
    
    checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for="MainPlaceHolder_cbConfirmApplication"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    # Send keys (file path) to the file input
    #file_input.send_keys("C:\\Users\\elias\\Desktop\\trytogroup\\uploads\\lataus_4.png")
    #"MainPlaceHolder_ucMuutTiedot_txtHakuMuuta"

    # Rest of your script
    # Keep the browser open for a bit (adjust as needed)
    # Scroll to the element
    submit_button = driver.find_element(By.ID, 'MainPlaceHolder_btnSend')
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    ### maybe try submit the form
    ###submit_button.click()

    time.sleep(5)








    
    ###
    input("Press Enter to close the browser...")
    ###time.sleep(5)


finally:
    # Close the browser window
    driver.quit()
 