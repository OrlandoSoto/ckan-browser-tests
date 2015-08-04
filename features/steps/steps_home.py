# coding: utf-8
from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.text.stringcontains import contains_string
from decorators import *

from pages.home import Home
from pages.base import Base


@given(u'I navigate to the CKAN Home page')
@handle_error
def step(context):
    context.base.go()


@When(u'I enter "{search_term}" in the "Search data" field')
@handle_error
def step(context, search_term):
	context.home.enter_search_term(search_term)

@When(u'I click the search data button')
@handle_error
def step(context):
	context.home.click_btn_search_data()

@then(u'I should see "{expected_page_title}" displayed in the page title')
@handle_error
def step(context, expected_page_title):
    # Verify that the actual page title matches the expected title
    actual_title = context.base.get_page_title(expected_page_title)
    assert_that(actual_title, contains_string(expected_page_title))
