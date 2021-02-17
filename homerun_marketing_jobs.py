from homerun_functions import *
from mail import *


# Automation on candidates which are in "Selected for 2nd round"
def selected_for_1st_or_2nd_round(job_url, email_template_name, j, k):
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
                # move candidate to First Round or Second Round
                move_candidate(k)

                # Wait for 5 seconds
                time.sleep(5)

                if k == 4:
                    # Shoot mail
                    shoot_mail(subject=f'{candidate_full_name}',
                               body="Successfully moved to automatically to First Round")
                else:
                    # Shoot mail
                    shoot_mail(subject=f'{candidate_full_name}',
                               body="Successfully moved to automatically to Second Round")

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


# Inside Sales
def insideSales():
    xpath = "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/span[2]/a"

    # Click on the job
    driver.find_element_by_xpath(xpath).click()

    # Wait for 10 seconds to load job page properly
    time.sleep(10)

    # Job page url
    job_url = driver.current_url

    # Selected for 1st round
    selected_for_1st_or_2nd_round(job_url, "1st round selection - Denny", 2, 4)

    # Wait for 2 seconds
    time.sleep(2)

    # Selected for 2nd round
    selected_for_1st_or_2nd_round(job_url, "2nd round selection - Varun", 4, 6)

    # wait for 2 seconds
    time.sleep(2)

    # Send rejection mail
    # send_rejection_mail(job_url, "Rejection - General")
