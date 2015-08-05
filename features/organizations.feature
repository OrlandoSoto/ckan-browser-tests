Feature: verify the Organizations page works according to the test acceptance criteria
As a first time visitor to the CKAN page
I want to search inside the Organizations page
So that I can find the Organizations I'm looking for

Background:
   Given I navigate to the Organizations page


@smoke
Scenario Outline: Search in the Organizations page
  When I enter "<search-term>" in the "Search organizations" field
  	And I click the search organizations button
  Then I should see "Organizations - " displayed in the page title

Examples:
   | search-term |
   | qu          |


@search
Scenario Outline: Verify that search term appears in URL query string
  When I enter "<search-term>" in the "Search organizations" field
  	And I click the search organizations button
  Then I should see "q=<search-term>" in the Organizations URL query string

Examples:
   | search-term |
   | qu          |

@search
Scenario Outline: Verify that sort order appears in URL query string
  Given I enter "qu" in the "Search organizations" field
  	And I click the search organizations button
  When I select Organizations Order By "<sort-order>"
  Then I should see the Organizations Order By option set to "<sort-order>"
  	And I should see "sort=<sort-parameter>" in the Organizations URL query string

Examples:
   | sort-order      | sort-parameter |
   | Name Ascending  | name+asc       |
   | Name Descending | name+desc      |
