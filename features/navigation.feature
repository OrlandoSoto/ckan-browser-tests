Feature: verify the navigation links works according to test acceptance criteria
  As a first time visitor to the CKAN page
  I want to click on invidual links
  So that I can easily navigate the site

Background:
   Given I navigate to the CKAN Home page

@smoke @navigation
Scenario Outline: Smoke test links in the CKAN page
   When I click on the "<link_name>" link
   Then I should see the "<expected_url>" URL in the address bar
   	And I should see "<expected_page_title>" displayed in the page title

Examples:
  | link_name                 | expected_url    | expected_page_title |
  | Datasets                  | /dataset        | Datasets -          |


@navigation
Scenario Outline: Regression test links in the CKAN page
   When I click on the "<link_name>" link
   Then I should see the "<expected_url>" URL in the address bar
   	And I should see "<expected_page_title>" displayed in the page title

Examples:
  | link_name                 | expected_url    | expected_page_title |
  | Organizations             | /organization   | Organizations -     |
  | Groups                    | /group          | Groups -            |
  | About                     | /about          | About -             |
  | Log in                    | /user/login     | Login -             |
  | CKAN API                  | /docs.ckan.org/ | API guide           |
  | Open Knowledge Foundation | /okfn.org       | Open Knowledge      |
  | CKAN                      | /ckan.org/      | ckan                |
