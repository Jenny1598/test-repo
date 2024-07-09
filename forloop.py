from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import string
import random
import time

contactlist = webdriver.Chrome()
contactlist.get("https://thinking-tester-contact-list.herokuapp.com/")
# contactlist.quit()

signup = contactlist.find_element(By.ID, "signup")
signup.click()
catcher = "Pass0"

# Add User
try:
    catcher = "Pass1"
    signupform = WebDriverWait(contactlist, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "main-content"))
    )
    catcher = "Pass2"

    adduser = signupform.find_element(By.ID, "firstName")
    adduser.send_keys("Chesnut")

    adduser = signupform.find_element(By.ID, "lastName")
    adduser.send_keys("Tanjiro")

    emailrandom = "".join(random.choices(string.ascii_lowercase, k=7))
    adduser = signupform.find_element(By.ID, "email")
    adduser.send_keys(emailrandom + "@yahoo.com")

    adduser = signupform.find_element(By.ID, "password")
    adduser.send_keys("abc123456")

    submit = signupform.find_element(By.ID, "submit")
    submit.click()

except Exception as e:
    print("FAILED")
    print(catcher)
    print(str(e))

# Contact List

# Add Contact Page
for x in range(10):  
    try:
        time.sleep(1)
        print(f"Starting iteration {x + 1}")  # Print statement to track iterations
        
       
        try:
            AddNewContactPage = WebDriverWait(contactlist, 10).until(
                EC.presence_of_element_located((By.ID, "add-contact"))
            )
        except TimeoutException as e:
            print(f"TimeoutException on iteration {x + 1} while waiting for 'add-contact'")
            continue
        
        AddNewContactPage.click()

        
        try:
            AddContactPage = WebDriverWait(contactlist, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "main-content"))
            )
        except TimeoutException as e:
            print(f"TimeoutException on iteration {x + 1} while waiting for 'main-content'")
            continue
        
        firstnamerandom = "".join(random.choices(string.ascii_lowercase, k=5))
        lastname = "".join(random.choices(string.ascii_lowercase, k=8))
        yearrandom = random.randint(1900, 2000)
        monthrandom = f"{random.randint(1, 12):02}"
        dayrandom = f"{random.randint(1, 28):02}"
        emailrandom = "".join(random.choices(string.ascii_lowercase, k=7))
        phonerandom = "".join(random.choices(string.digits, k=9))
        add1random = "".join(random.choices(string.ascii_letters, k=5))
        add2random = "".join(random.choices(string.ascii_letters, k=5))
        cityrandom = "".join(random.choices(string.ascii_letters, k=6))
        provrandom = "".join(random.choices(string.ascii_letters, k=7))
        coderandom = "".join(random.choices(string.digits, k=4))
        countryrandom = "".join(random.choices(string.ascii_letters, k=7))

        try:
            AddContactPage.find_element(By.ID, "firstName").send_keys(firstnamerandom)
            AddContactPage.find_element(By.ID, "lastName").send_keys(lastname)
            AddContactPage.find_element(By.ID, "birthdate").send_keys(f"{yearrandom}-{monthrandom}-{dayrandom}")
            AddContactPage.find_element(By.ID, "email").send_keys(emailrandom + "@email.com")
            AddContactPage.find_element(By.ID, "phone").send_keys("09" + str(phonerandom))
            AddContactPage.find_element(By.ID, "street1").send_keys(add1random)
            AddContactPage.find_element(By.ID, "street2").send_keys(add2random)
            AddContactPage.find_element(By.ID, "city").send_keys(cityrandom)
            AddContactPage.find_element(By.ID, "stateProvince").send_keys(provrandom)
            AddContactPage.find_element(By.ID, "postalCode").send_keys(coderandom)
            AddContactPage.find_element(By.ID, "country").send_keys(countryrandom)
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException on iteration {x + 1}")
            continue

        time.sleep(1)
        
        submitcontact = AddContactPage.find_element(By.ID, "submit")
        submitcontact.click()
        print(f"Iteration {x + 1} passed")  

    except Exception as e:
        print(f"Iteration {x + 1} did not finish")  
        print(str(e))

time.sleep(1000)