# coding: utf-8
from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.text.stringcontains import contains_string
from decorators import *

from pages.groups import Groups
from pages.base import Base


@given(u'I enter "{search_term}" in the "Search groups" field')
@when(u'I enter "{search_term}" in the "Search groups" field')
@handle_error
def step(context, search_term):
    context.groups.enter_search_term(search_term)


@given(u'I click the search groups button')
@when(u'I click the search groups button')
@handle_error
def step(context):
    context.groups.click_btn_search_datasets()


@when(u'I select Groups Order By "{sort_order}"')
@handle_error
def step(context, sort_order):
    context.groups.set_sort_order(sort_order)


@then(u'I should see the Groups Order By option set to "{selected_option}"')
@handle_error
def step(context, selected_option):
    actual_selection = context.groups.get_sort_order()
    assert_that(actual_selection, equal_to(selected_option))


@then(u'I should see "{search_term}" in the Groups URL query string')
def step(context, search_term):
    actual_url = context.base.get_current_url()
    assert_that(actual_url, contains_string(search_term))
