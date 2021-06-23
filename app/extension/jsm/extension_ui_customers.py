from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jsm.pages.customer_pages import Login, FavfjsmCustomerVoteList
from util.conf import JSM_SETTINGS


def favfjsm_customer_vote_list(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        custom_request_key = datasets['custom_issue_key']
        custom_service_desk_id = datasets['custom_service_desk_id']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action

    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_customer_favfjsm_customer_vote_list")
    def measure():
        customer_vote_list_page = FavfjsmCustomerVoteList(webdriver,
                                                          datasets['random_favfjsm_service_desk_project_id'])

        @print_timing("selenium_customer_favfjsm_customer_vote_list:view_customer_vote_list")
        def sub_measure():
            customer_vote_list_page.go_to()
            customer_vote_list_page.wait_for_page_loaded()
        sub_measure()
    measure()
