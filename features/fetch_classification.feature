Feature: Fetch NBA classification

    '''As a user, I want to access NBA Standings page to
    see the first place in each conference
    '''

    Scenario: Fetch first place in NBA Standings
    Given I access nba standings page
    When The page is loaded
    Then I should know who is the first place in each conference and have it recorded into a txt file