import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         if login_page.is_first_login():
    #             login_page.first_login_setup()
    #         if login_page.is_first_login_second_page():
    #             login_page.first_login_second_page_setup()
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    # def measure():
    #     @print_timing("selenium_app_custom_action:view_issue")
    #     def sub_measure():
    #         page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
    #         page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
    #         page.wait_until_visible((By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
    #     sub_measure()

    def measure():
        @print_timing("selenium_app_custom_action:Story_custom_fields")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/VERADCCERT-1022")
            page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "customfieldmodule"))  # Wait for you app-specific UI element by ID selector
            # Wait for you Veracode specific UI element by ID selector
            page.wait_until_visible((By.ID, "customfield_11100-val")) # Vera_Comm_ApplicationName
            page.wait_until_visible((By.ID, "customfield_11101-val")) # Vera_Comm_AppID
            page.wait_until_visible((By.ID, "customfield_11104-val")) # Vera_SCA_Comp_ComponentID
            page.wait_until_visible((By.ID, "customfield_11105-val")) # Vera_SCA_Comp_MaxCVSSScore
        sub_measure()

        @print_timing("selenium_app_custom_action:Task_custom_fields")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/VERADCCERT-830")
            page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "customfieldmodule"))  # Wait for you app-specific UI element by ID selector
            # Wait for you Veracode specific UI element by ID selector
            page.wait_until_visible((By.ID, "customfield_11100-val")) # Vera_Comm_ApplicationName
            page.wait_until_visible((By.ID, "customfield_11101-val")) # Vera_Comm_AppID
            page.wait_until_visible((By.ID, "customfield_11102-val")) # Vera_Static_BuildID
            page.wait_until_visible((By.ID, "customfield_11103-val")) # Vera_Static_FlawID
        sub_measure()

        @print_timing("selenium_app_custom_action:Sub_Task_custom_fields")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/VERADCCERT-1023")
            page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "customfieldmodule"))  # Wait for you app-specific UI element by ID selector
            # Wait for you Veracode specific UI element by ID selector
            page.wait_until_visible((By.ID, "customfield_11100-val"))  # Vera_Comm_ApplicationName
            page.wait_until_visible((By.ID, "customfield_11101-val"))  # Vera_Comm_AppID
            page.wait_until_visible((By.ID, "customfield_11106-val"))  # Vera_SCA_Vuln_CVEID
            page.wait_until_visible((By.ID, "customfield_11107-val"))  # Vera_SCA_Vuln_CVSSscore
        sub_measure()

        @print_timing("selenium_app_custom_action:Bug_custom_fields")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/VERADCCERT-1087")
            page.wait_until_visible((By.ID, "summary-val"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "customfieldmodule"))  # Wait for you app-specific UI element by ID selector
            # Wait for you Veracode specific UI element by ID selector
            page.wait_until_visible((By.ID, "customfield_11100-val"))  # Vera_Comm_ApplicationName
            page.wait_until_visible((By.ID, "customfield_11101-val"))  # Vera_Comm_AppID
            page.wait_until_visible((By.ID, "customfield_11102-val"))  # Vera_Static_BuildID
            page.wait_until_visible((By.ID, "customfield_11103-val"))  # Vera_Static_FlawID
            page.wait_until_visible((By.ID, "customfield_11104-val"))  # Vera_SCA_Comp_ComponentID
            page.wait_until_visible((By.ID, "customfield_11105-val"))  # Vera_SCA_Comp_MaxCVSSScore
            page.wait_until_visible((By.ID, "customfield_11106-val"))  # Vera_SCA_Vuln_CVEID
            page.wait_until_visible((By.ID, "customfield_11107-val"))  # Vera_SCA_Vuln_CVSSscore
        sub_measure()

    measure()