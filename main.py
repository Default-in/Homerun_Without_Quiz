from homerun_operations_jobs import *
from homerun_marketing_jobs import *


# Call homeurl
def home(home_url):
    # Wait for 2 seconds
    time.sleep(2)

    # Open homepage
    driver.get(home_url)

    # Wait for 15 seconds to load homepage
    time.sleep(15)


try:
    # Login in to homerun
    login()

    # Dashboard url
    url = driver.current_url

    print("Start Check recruiter job")
    # Go to recruiter job
    recruiter()

    # GO back to dashboard
    home(url)

    print("Start Check accountant job")
    # Go to accountant Job
    accountant()

    # GO back to dashboard
    home(url)

    print("Start Check Automation job")
    # Go to automation job
    automation()

    # GO back to dashboard
    home(url)

    print("Start Check Inside Sales job")
    # Go to inside sales job
    insideSales()

    # Close the window
    driver.close()

    # Shoot mail
    shoot_mail("Success", "Automation Complete")

except Exception as e:
    print(e)
    # Shoot error mail
    shoot_mail("Error", e)
