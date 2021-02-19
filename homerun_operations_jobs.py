from homerun_functions import *
from mail import *


# Automation on candidates which are in "Selected for 2nd round"
def selected_for_1st_or_2nd_or_3rd_round(job_url, email_template_name, j, k):
    # Initialising variable i if any error occurs then move to next candidate
    i = 1

    # xpath of candidate in "Selected to be sent quiz" link
    xpath = f"/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div[{j}]/div/div/div[{i}]/a/div"

    try:
        while driver.find_element_by_xpath(xpath):
            # Click on the candidate
            driver.find_element_by_xpath(xpath).click()

            # Wait for 15 seconds to load Candidate modal properly
            time.sleep(15)

            # Call candidate_details function to find fullname and email address of candidate
            candidate_full_name, candidate_email_address = candidate_details()
            print(candidate_full_name)
            print(candidate_email_address)

            try:
                # Compose mail
                compose_mail(email_template_name)

                # Wait
                time.sleep(2)

            except Exception as ex:
                print(ex)

                # shoot mail
                shoot_mail(subject=f'Error while sending mail to {candidate_full_name}', body=f'{ex}')

            try:
                # move candidate to Second Round
                move_candidate(k)

                # Wait for 5 seconds
                time.sleep(5)

                # Shoot mail
                shoot_mail(subject=f'{candidate_full_name}', body="Successfully moved to automatically to Second Round")

                # Go to job
                driver.get(job_url)

                # Wait for 10 seconds to load page properly
                time.sleep(10)

            except Exception as exp:
                print(exp)

                # Shoot error mail
                shoot_mail(subject=f'Error while changing stage of {candidate_full_name}', body=f'{exp}')

                # Increase value of i by 1 to move to the next candidate
                i += 1

                # xpath of candidate in "Selected to be sent quiz" link
                xpath = f"/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div[{j}]/div/div/div[{i}]/a/div"

    except Exception as e:
        print(e)


# Selected for 1st round Product Manager
def selected_for_first_round(job_url, email_template_name, k):
    # Initialising variable i if any error occurs then move to next candidate
    i = 1

    # xpath of candidate in "Selected for 1st round" stage
    xpath = f"/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[{i}]/a/div"

    try:
        while driver.find_element_by_xpath(xpath):
            # Click on the candidate
            driver.find_element_by_xpath(xpath).click()

            # Wait for 15 seconds to load Candidate modal properly
            time.sleep(15)

            # Call candidate_details function to find fullname and email address of candidate
            candidate_full_name, candidate_email_address = candidate_details()
            print(candidate_full_name)
            print(candidate_email_address)

            try:
                # Compose mail
                compose_mail(email_template_name)

                # Wait
                time.sleep(2)

            except Exception as ex:
                print(ex)

                # shoot mail
                shoot_mail(subject=f'Error while sending mail to {candidate_full_name}', body=f'{ex}')

            try:
                # move candidate to Second Round
                move_candidate(k)

                # Wait for 5 seconds
                time.sleep(5)

                # Shoot mail
                shoot_mail(subject=f'{candidate_full_name}', body="Successfully moved to automatically to Second Round")

                # Go to job
                driver.get(job_url)

                # Wait for 10 seconds to load page properly
                time.sleep(10)

            except Exception as exp:
                print(exp)

                # Shoot error mail
                shoot_mail(subject=f'Error while changing stage of {candidate_full_name}', body=f'{exp}')

                # Increase value of i by 1 to move to the next candidate
                i += 1

                # xpath of candidate in "Selected for 1st round" stage
                xpath = f"/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[{i}]/a/div"

    except Exception as e:
        print(e)


# Check candidates in "Send rejection mail" stage
def send_rejection_mail(job_url, rejection_mail_template, j, k):
    try:
        print("Checking Send rejection mail stage")
        i = 1
        xpath = f'/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div[{j}]/div/div/div[{i}]/a/div'
        while driver.find_element_by_xpath(xpath):
            driver.find_element_by_xpath(xpath).click()

            # Wait for 15 seconds to load candidate modal properly
            time.sleep(15)

            # Call candidate_details function to find fullname and email address of candidate
            candidate_full_name, candidate_email_address = candidate_details()
            print(candidate_full_name)
            print(candidate_email_address)

            # Try if Compose mail function is working properly or not
            try:
                # Send email with disqualified template
                compose_mail(rejection_mail_template)

            except Exception as mail_exception:
                print(mail_exception)

                # Shoot the Error mail
                shoot_mail(subject=f'Error while sending rejection mail',
                           body=f'Error - {mail_exception}')

                # Close the browser
                driver.quit()
                break

            # Try if move_candidate function is working properly or not
            try:
                # Move the candidate to "Rejected" Stage
                move_candidate(k)

                # Wait for 5 seconds
                time.sleep(5)

                # Message body
                message = f'Candidate Name - {candidate_full_name}\nSuccessfully moved ' \
                          f'automatically to Rejected Stage'

                # Shoot mail
                shoot_mail(subject=f'{candidate_full_name}', body=message)

                # Click on the job to
                driver.get(job_url)

                # Wait for 15 seconds to load job page page properly
                time.sleep(15)

            except Exception as moving_exception:
                print(moving_exception)

                # Shoot error mail
                shoot_mail(subject=f'Error while changing stage of {candidate_full_name}', body=f'{moving_exception}')

                # Increase value of i by 1 to move to the next candidate
                i += 1

                # Change the xpath to next candidate
                xpath = f'/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div[7]/div/div/div[{i}]/a/div'

                # Go to the job page
                driver.get(job_url)
                time.sleep(15)


    except Exception as send_rejection_mail_error:
        print(send_rejection_mail_error)


# Recruiter
def recruiter():
    xpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/span[2]/a"

    # Click on the job
    driver.find_element_by_xpath(xpath).click()

    # Wait for 10 seconds to load job page properly
    time.sleep(10)

    # Job page url
    job_url = driver.current_url

    # Selected for 1st round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "1st round selection - Tejasvi", 2, 4)

    # Wait for 2 seconds
    time.sleep(2)

    # Selected for 2nd round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "2nd round selection - Akshit", 4, 6)

    # wait for 2 seconds
    time.sleep(2)

    # Selected for 3rd round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "3rd round selection - Varun", 6, 8)

    # Send rejection mail
    send_rejection_mail(job_url, "Rejection - General", 9, 11)


# Accountant
def accountant():
    xpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/span[2]/a"

    # Click on the job
    driver.find_element_by_xpath(xpath).click()

    # Wait for 10 seconds to load job page properly
    time.sleep(10)

    # Job page url
    job_url = driver.current_url

    # Selected for 1st round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "1st round selection - Akshit", 2, 4)

    # wait for 2 seconds
    time.sleep(2)

    # Send rejection mail
    send_rejection_mail(job_url, "Rejection - General", 7, 9)


# Accountant
def automation():
    xpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/span[2]/a"

    # Click on the job
    driver.find_element_by_xpath(xpath).click()

    # Wait for 10 seconds to load job page properly
    time.sleep(10)

    # Job page url
    job_url = driver.current_url

    # Selected for 1st round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "1st round selection - Rishabh", 2, 4)

    # Wait for 2 seconds
    time.sleep(2)

    # Selected for 2nd round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "2nd round selection - Varun", 4, 6)

    # Send rejection mail
    send_rejection_mail(job_url, "Rejection - General", 7, 9)


# Product Manager
def product_manager():
    xpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/span[2]/a"

    # Click on the job
    driver.find_element_by_xpath(xpath).click()

    # Wait for 15 seconds to load job page properly
    time.sleep(15)

    # Job page url
    job_url = driver.current_url

    # Selected for 1st round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "1st round selection - Anupam", 2, 4)

    # Wait for 2 second
    time.sleep(2)

    # Selected for 2nd round
    selected_for_1st_or_2nd_or_3rd_round(job_url, "2nd round selection - Akshit", 4, 6)

    # wait for 2 seconds
    time.sleep(2)

    # Send rejection mail
    send_rejection_mail(job_url, "Rejection - General", 7, 9)
