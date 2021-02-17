from driver_file import *
import time
from homerun_credentials import *
from homerun_cookies import cookies


def wait(t):
    time.sleep(t)


# Scroll till target
def scroll_till_target(target):
    driver.execute_script("arguments[0].scrollIntoView();", target)
    wait(5)


def login():
    driver.get("https://app.homerun.co/login?redirect=")
    print("Go to log in page")
    driver.maximize_window()

    # Find the email input field
    email = driver.find_element_by_xpath('//*[@id="email"]')

    # Find the password input field
    password = driver.find_element_by_xpath('//*[@id="password"]')

    # Send credentials to respective field
    email.send_keys(user_email)
    wait(2)
    password.send_keys(user_pass)

    # Wait for 2 seconds
    wait(2)

    # Find "Login with email" button and then click on it
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/form/button').click()
    print("Click on Login Button")

    # Wait for 10 seconds to load webpage properly
    wait(10)


# Compose mail function
def compose_mail(template):
    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Compose email" button
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div['
                                 '2]/div[1]/div/div/div/div[2]/div[1]/div').click()

    # Wait for 5 seconds to load webpage properly
    time.sleep(5)

    # Click on Insert Template button
    driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > div.Modal__wrapper__KPSjL > div > '
                                        'div.Modal__content__24RSX.Modal__content-medium__14IIQ > div > '
                                        'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                        'div.EmailComposer__content__vg85Z.types__body__3w21D > '
                                        'div.EmailComposer__subject-block__3zYUa > div.EmailComposer__insert__3rdIi > '
                                        'div > div:nth-child(1) > button').click()

    # Wait for 2 seconds
    time.sleep(2)

    # Search template input field
    search_template = driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > '
                                                          'div.Modal__wrapper__KPSjL > div > '
                                                          'div.Modal__content__24RSX.Modal__content-medium__14IIQ > '
                                                          'div > '
                                                          'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                                          'div.EmailComposer__content__vg85Z.types__body__3w21D > '
                                                          'div.EmailComposer__subject-block__3zYUa > '
                                                          'div.EmailComposer__insert__3rdIi > div > '
                                                          'div.BaseSelect__options__2HneA.BaseSelect__footer'
                                                          '-active__3iOCv > '
                                                          'div.BaseSelect__header__NNuta > div > span > div > input['
                                                          'type=text]')

    # Wait for 2 seconds
    time.sleep(2)

    # Send the template name
    search_template.send_keys(f'{template}')

    # Wait for 2 seconds
    time.sleep(2)

    # Click on the searched template
    driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > div.Modal__wrapper__KPSjL > div > '
                                        'div.Modal__content__24RSX.Modal__content-medium__14IIQ > div > '
                                        'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                        'div.EmailComposer__content__vg85Z.types__body__3w21D > '
                                        'div.EmailComposer__subject-block__3zYUa > div.EmailComposer__insert__3rdIi > '
                                        'div > div.BaseSelect__options__2HneA.BaseSelect__footer-active__3iOCv > '
                                        'div:nth-child(2) > div > div').click()

    # Wait for 2 seconds
    time.sleep(2)

    # Click on Send button
    driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > div.Modal__wrapper__KPSjL > div > '
                                        'div.Modal__content__24RSX.Modal__content-medium__14IIQ > div > '
                                        'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                        'div.EmailComposer__footer__3XZtc > '
                                        'div.EmailComposer__button-group__24mIi.general__align-items-right__1IeWz'
                                        '.general__align-items__2XcUs > '
                                        'button.Button__secondary__2J5xH.Button__button__3GlfL').click()

    # Wait for 4 seconds
    time.sleep(4)

    # Close the email popup window
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div[2]/div/div[2]/div/div[1]/div/div').click()

    # Wait for 2 seconds
    time.sleep(2)

    print("Mail send successfully")


# Move the candidate to desired stage
def move_candidate(stage):
    # Click on current stage
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div['
                                 '2]/div[1]/div/div/div/div[1]/div/div[1]/div').click()

    # Wait for 2 seconds
    time.sleep(2)

    # xpath of stage in which we want to move the candidate
    xpath2 = f'//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[' \
             f'1]/div/div/div/div[1]/div/div[2]/div/div/div[{stage}] '

    # Click on the stage to move candidate
    driver.find_element_by_xpath(xpath2).click()

    # Wait for 5 seconds
    time.sleep(5)

    print("Candidate moved successfully")


# Add Comment
def add_comment(content):
    # Add comments
    comment = driver.find_element_by_css_selector('#portal-mount > div > div > div.PageModal__wrapper__184dL > div > '
                                                  'div > div > div.CandidateModal__candidate-profile-wrapper__kT10d > '
                                                  'div > div.CandidateProfile__widgets__3PMIn > div > div > div > '
                                                  'div.CandidateWidgets__wrapper__3_j4m > span > '
                                                  'div.CandidateWidgets__notes__sLByP > div > div > '
                                                  'div.Notes__note-input-wrapper__1Y6BU > div > div > div > '
                                                  'div.TextEditor__editor__2HMtf.general__reset__1da_S > div > div')

    # Send comment content
    comment.send_keys(f'{content}')

    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Add" button to add comment
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div['
                                 '2]/div/div[2]/div/div/div/div[2]/span/div[2]/div/div/div['
                                 '1]/div/div[2]/div[2]/button').click()

    # Wait for 5 Seconds
    time.sleep(5)

    print("Successfully Add Comment")
    return 0


# Add candidate to Users in Proprofs
def addUser(candidate_email_address, candidate_full_name, first_name, last_name, encoded_quiz_url):
    try:
        # Add candidates to users
        add_new_user(candidate_email_address, first_name, last_name, encoded_quiz_url)

        # Shoot mail when candidate register as user successfully
        shoot_mail(subject=f'{candidate_full_name}', body="Successfully registered as user in proprofs")

    except Exception as addUserException:
        print(addUserException)

        # Shoot the error message via mail
        shoot_mail(subject=f'Error while adding {candidate_full_name}', body=f"{addUserException}")

        # Wait for 2 seconds
        time.sleep(2)


# Find Fullname and email address of candidate
def candidate_details():
    # Scrap full name of the candidate
    full_name = driver.find_element_by_xpath('.//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div['
                                             '2]/div/div[1]/div/div[2]/div[4]/div/div/div[1]/div[2]').text
    # Email Address
    candidate_email = ""
    for j in range(2, 5):
        try:
            # Scrap email address of the candidate
            candidate_email = driver.find_element_by_xpath(f'.//*[@id="portal-mount"]/div/div/div['
                                                           f'3]/div/div/div/div[2]/div/div[1]/div/div[2]/div['
                                                           f'4]/div/div/div[{j}]/div[2]/button/span').text
        except Exception as error_candidate_detail:
            print(f'Error - {error_candidate_detail}')

        if candidate_email:
            break

    return full_name, candidate_email
