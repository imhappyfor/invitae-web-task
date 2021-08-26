from datetime import timedelta
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class HomePageTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(HomePageTests, cls).setUpClass()
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(HomePageTests, cls).tearDownClass()

    def test_home_page_content(self):
        """Test that the home page renders the task description"""
        self.browser.get(self.live_server_url)
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Task Description', page_heading)

        requirements = self.browser.find_elements_by_css_selector('#task-requirements li')
        self.assertEqual(len(requirements), 3)
        self.assertIn('BED file to database', requirements[0].text)
        self.assertIn('graphical summary', requirements[1].text)
        self.assertIn('well tested', requirements[2].text)

    def test_nav_links(self):
        """Test that navigation links to expected pages"""
        self.browser.get(self.live_server_url)

        # Test that the home page links to the BED upload page
        navbar = self.browser.find_element_by_id('navbar')
        bed_upload_nav_link = navbar.find_element_by_xpath("//a[text()='Upload BED File']")
        bed_upload_nav_link.click()
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Upload BED File', page_heading)

        # Test that the submit rejects empty uploads
        submitButton = self.browser.find_element_by_id('submitBtn')
        submitButton.click()
            # set timer for for 3 seconds or until the element is found
        wait = WebDriverWait(self.browser, 3)
            # validate the errors existence.
        sweetAlertError = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.swal2-container.swal2-center.swal2-backdrop-show')))
        self.assertEqual(True, sweetAlertError.is_displayed())
            # get the button to exit error and click it.
        sweetAlertErrorBtn = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[6]/button[1]')
        sweetAlertErrorBtn.click()
        
        # Test that the home page links to the View Page upload page
        navbar = self.browser.find_element_by_id('navbar')
        bed_upload_nav_link = navbar.find_element_by_xpath("//a[text()='View Genome Data']")
        bed_upload_nav_link.click()
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('View Genome Data', page_heading)
        
        # check for tabContainer element which may or may not retrieve data.

        tabContainer = wait.until(EC.visibility_of_element_located((By.ID, 'tab-container')))
        self.assertEqual(True, tabContainer.is_displayed())


        #  TODO: 
        # Test model for the data entry
        # Test 
            # Test that bootstrap tabs loaded properly based upon previous load
            # tableTab = self.browser.find_element_by_xpath("//body/div/div/ul/li[1]/a").text
            # self.assertAlmostEqual('Genome Data Table', tableTab)

            # Test that bootstrap tabs loaded properly based upon previous load
            # tableTab = self.browser.find_element_by_xpath("//body/div/div/ul/li[2]/a").text
            # self.assertAlmostEqual('Genome Box Plot', tableTab)



        #  return home to valid it it's existence.
        navbar = self.browser.find_element_by_id('navbar')
        home_nav_link = navbar.find_element_by_xpath("//a[text()='Home']")
        home_nav_link.click()
        page_heading = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Task Description', page_heading)
