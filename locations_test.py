import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from locations_po import LocationsPage
from locations_rest_api import create_location, delete_all_locations


@pytest.fixture
def driver():
    delete_all_locations()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    
    return driver


def test_create(driver: webdriver.Chrome):
    """Teszteset: location létrehozása"""

    page = LocationsPage(driver)
    # When
    page.click_on_create_location()
    page.fill_create_form("Home", "1,1")
    page.click_on_create_location_submit()

    # Then
    page.wait_for_message("Location has been created")
    
    name, coords = page.get_first_location()
    assert name == "Home"
    assert coords == "1, 1"

def test_create_invalid_name(driver: webdriver.Chrome):
    # Given
    page = LocationsPage(driver)

    # When
    page.click_on_create_location()
    page.click_on_create_location_submit()
    page.wait_for_name_message("Can not be empty name!")

    assert page.has_name_red_border()    
    page.wait_for_table_has_rows(0)


def test_edit(driver: webdriver.Chrome):
    # Given: legyen az adatbázisban egy Test... nevű location
    create_location("Test", "5,5")

    page = LocationsPage(driver)
    page.wait_for_table_has_rows(1)

    page.click_on_first_edit_button()
    page.fill_update_form("Test2", "8,8")
    page.click_on_update_location_submit()

    page.wait_for_message("Location has been modified")
    page.wait_for_table_has_rows(1)

    name, coords = page.get_first_location()
    assert name == "Test2"
    assert coords == "8, 8"
    

def test_delete(driver: webdriver.Chrome):
    create_location("Test", "5,5")

    page = LocationsPage(driver)
    page.wait_for_table_has_rows(1)
    
    page.click_on_first_delete_button()
    page.click_on_delete_confirm()
    page.wait_for_message("Location has been deleted")
    page.wait_for_table_has_rows(0)


