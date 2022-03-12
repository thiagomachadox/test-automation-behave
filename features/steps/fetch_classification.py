from behave import *
from datetime import datetime

from bs4 import BeautifulSoup

base_url = 'https://www.nba.com/standings'
today_date = datetime.today().strftime('%Y-%m-%d')

table_selector = '.relative.my-4'

@given(u'I access nba standings page')
def step_impl(context):
    context.web.get(base_url)


@when(u'The page is loaded')
def step_impl(context):
    context.element_tables = context.web.find_elements_by_css_selector(table_selector)
    if not context.element_tables:
        raise Exception('Table element not found')

@then(u'I should know who is the first place in each conference and have it recorded into a txt file')
def step_impl(context):


    for html in context.element_tables:
        html_code = html.get_attribute('innerHTML')
        soup = BeautifulSoup(html_code, 'html.parser')
        conference_name = soup.find('h5').text # only h5 element

        table = soup.find('table')
        row = table.tbody.find('tr')
        team_name = row.text.strip()
        row = f'{today_date} : 1st in {conference_name} conference: {team_name}'

        # Save standings into txt
        file = open('results.txt', 'a')
        file.write(row, '\n')
        file.close()
