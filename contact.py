from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import time


while True:
    try:
        loops = int(input("Please enter how many data to add (number only) : "))
    except:
        print("Not a number, please try again!")
        continue
    else:
        print("Website loading, please wait...")
        break

contactlist = webdriver.Chrome()
contactlist.get("https://thinking-tester-contact-list.herokuapp.com/")
#contactlist.quit()

signup = contactlist.find_element(By.ID,"signup")
signup.click()
catcher = "Pass0"

#Add User
try:
    
    catcher = "Pass1"
    signupform = WebDriverWait(contactlist, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "main-content"))
    )
    catcher = "Pass2"


    adduser = signupform.find_element(By.ID,"firstName")
    adduser.send_keys("Chesnut")

    adduser = signupform.find_element(By.ID,"lastName")
    adduser.send_keys("Tanjiro")

    emailrandom = "".join(random.choices(string.ascii_lowercase,k=7))
    adduser = signupform.find_element(By.ID,"email")
    adduser.send_keys(emailrandom + "@yahoo.com")

    adduser = signupform.find_element(By.ID,"password")
    adduser.send_keys("abc123456")

   
    submit = signupform.find_element(By.ID,"submit")
    submit.click()

    
except:
    print("FAILED")
    print(catcher)

counter = 0

for x in range(int(loops)):
    try:
        counter += 1
        AddNewContactPage = WebDriverWait(contactlist, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='add-contact']"))
        )
        AddNewContactPage.click()

        
        AddContactPage = WebDriverWait(contactlist, 10).until(
            EC.presence_of_element_located((By.TAG_NAME,"form"))
        )

        firstname = AddContactPage.find_element(By.ID,"firstName")
        lastname = AddContactPage.find_element(By.ID,"lastName")
        dateofbirth = AddContactPage.find_element(By.ID,"birthdate")
        email = AddContactPage.find_element(By.ID,"email")
        phone = AddContactPage.find_element(By.ID,"phone")
        address1 = AddContactPage.find_element(By.ID,"street1")
        address2 = AddContactPage.find_element(By.ID,"street2")
        city = AddContactPage.find_element(By.ID,"city")
        prov = AddContactPage.find_element(By.ID,"stateProvince")
        code = AddContactPage.find_element(By.ID,"postalCode")
        country = AddContactPage.find_element(By.ID,"country")


        firstnamerandom = "".join(random.choices(string.ascii_lowercase,k=5))
        lastnamerandom = "".join(random.choices(string.ascii_lowercase,k=8))
        emailrandom = "".join(random.choices(string.ascii_lowercase,k=7))
        phonerandom = "".join(random.choices(string.digits,k=9))
        add1random = "".join(random.choices(string.ascii_letters,k=5))
        add2random = "".join(random.choices(string.ascii_letters,k=5))
        cityrandom = "".join(random.choices(string.ascii_letters,k=6))
        provrandom = "".join(random.choices(string.ascii_letters,k=7))
        coderandom = "".join(random.choices(string.digits,k=4))
        countryrandom = "".join(random.choices(string.ascii_letters,k=7))

        
        firstname.send_keys(firstnamerandom)
        lastname.send_keys(lastnamerandom)
        yearrandom = random.randint(1900,2024)
        monthrandom = random.randint(1,12)
        dayrandom = random.randint(1,28)
        if(monthrandom < 10):
            monthrandom = ("0" + str(monthrandom))

        if(dayrandom < 10):
            dayrandom = ("0" + str(dayrandom))
        dateofbirth.send_keys(str(yearrandom) + "-" +str(monthrandom) + "-" +str(dayrandom))
        email.send_keys(emailrandom + "@email.com") 
        phone.send_keys( "09" + str(phonerandom))
        address1.send_keys(add1random)
        address2.send_keys(add2random)
        city.send_keys(cityrandom)
        prov.send_keys(provrandom)
        code.send_keys(coderandom)
        country.send_keys(countryrandom)

        #contactlist.implicitly_wait(10)
        

        button1 = WebDriverWait(contactlist, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[form='add-contact']"))
        )
        button1.click()
        print("Data added succesfully: " + str(counter))
        
        if (counter == loops):
            print(str(loops)+" data has been added succesfully!")
    
    except Exception as e:
        print(counter)
        print("failed to add data : ", e)
    

        

time.sleep(1000)
