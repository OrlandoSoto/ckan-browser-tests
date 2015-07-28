Feature: verify the Home page works according to the test acceptance criteria
As a first time visitor to the CKAN page
I want to navigate the home page
So that I can find the information I'm looking for

Background:
   Given I navigate to the Home page

@smoke_testing @landing_page
Scenario: Testing landing page
  Then I should see "Welcome - Data Catalog" displayed in the page title
