import info
import timeTable
import time

def joinEnglish():
    driver.get(english)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinPhysics():
    driver.get(physics)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinChem():
    driver.get(chemistry)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinMaths():
    driver.get(maths)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def joinBio():
    driver.get(biology)
    time.sleep(60) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()

def dummy():
    driver.get(dummy)
    time.sleep(1) #seconds
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(1800)
    driver.quit()
