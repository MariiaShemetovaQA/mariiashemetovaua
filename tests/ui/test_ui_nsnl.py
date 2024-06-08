from modules.ui.page_object.nsnl import HomePage
import pytest
import time

@pytest.mark.ui_ind
def test_find_route():
    home_page = HomePage()
    home_page.go_to()
    time.sleep(2)
    home_page.find_route("Leiden Centraal", "Amsterdam Centraal")
    time.sleep(3)
    assert home_page.check_route_title("Reisplanner | Plan je reis | NS")
    time.sleep(2)
    home_page.close()
    #home_page.buy_ticket()
    #time.sleep(3)
    #assert home_page.check_route_title("Koop kaartijes | NS")
    #time.sleep(2)
    #home_page.close()

