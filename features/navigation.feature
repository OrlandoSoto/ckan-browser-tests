Feature: verify the navigation links works according to test acceptance criteria
  As a first time visitor to the CKAN page
  I want to click on invidual links
  So that I can easily navigate the site


@smoke_testing @landing_page
Scenario Outline: Test links in the CKAN page
   Given I navigate to the CKAN Home page
   When I click on the "<link_name>" link
   Then I should see the "<expected_url>" URL in the address bar
   	And I should see "<page_title>" displayed in the page title

Examples:
  | link_name     | expected_url    | page_title      |
  | Datasets      | /dataset        | Datasets -      |
  | Organizations | /organization   | Organizations - |
  | Groups        | /group          | Groups -        |
  | About         | /about          | About -         |
