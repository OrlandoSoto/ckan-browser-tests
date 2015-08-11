# coding: utf-8
from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.text.stringcontains import contains_string
from decorators import *

from pages.organizations import Organizations
from pages.base import Base


@given(u'I enter "{search_term}" in the "Search organizations" field')
@when(u'I enter "{search_term}" in the "Search organizations" field')
@handle_error
def step(context, search_term):
    context.organizations.enter_search_term(search_term)


@given(u'I click the search organizations button')
@when(u'I click the search organizations button')
@handle_error
def step(context):
    context.organizations.click_btn_search_datasets()


@when(u'I select Organizations Order By "{sort_order}"')
@handle_error
def step(context, sort_order):
    context.organizations.set_sort_order(sort_order)


@then(u'I should see the Organizations Order By option set to "{selected_opt}"')
@handle_error
def step(context, selected_opt):
    actual_selection = context.organizations.get_sort_order()
    assert_that(actual_selection, equal_to(selected_opt))


@then(u'I should see "{search_term}" in the Organizations URL query string')
def step(context, search_term):
    actual_url = context.base.get_current_url()
    assert_that(actual_url, contains_string(search_term))
