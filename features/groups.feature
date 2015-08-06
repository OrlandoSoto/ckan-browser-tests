Feature: verify the Groups page works according to the test acceptance criteria
As a first time visitor to the CKAN page
I want to search inside the Groups page
So that I can find the Organizations I'm looking for

Background:
   Given I navigate to the Groups page


@smoke
Scenario Outline: Search in the Groups page
  When I enter "<search-term>" in the "Search groups" field
  	And I click the search groups button
  Then I should see "Groups - " displayed in the page title

Examples:
   | search-term |
   | qu          |


@search
Scenario Outline: Verify that search term appears in URL query string
  When I enter "<search-term>" in the "Search groups" field
  	And I click the search groups button
  Then I should see "q=<search-term>" in the Groups URL query string

Examples:
   | search-term |
   | qu          |

@search
Scenario Outline: Verify that sort order appears in URL query string
  Given I enter "qu" in the "Search groups" field
  	And I click the search groups button
  When I select Groups Order By "<sort-order>"
  Then I should see the Groups Order By option set to "<sort-order>"
  	And I should see "sort=<sort-parameter>" in the Groups URL query string

Examples:
   | sort-order      | sort-parameter  |
   | Name Ascending  | title+asc       |
   | Name Descending | title+desc      |
