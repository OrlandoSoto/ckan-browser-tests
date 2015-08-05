# coding: utf-8
from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.text.stringcontains import contains_string
from decorators import *

from pages.datasets import Datasets
from pages.base import Base


@Given(u'I enter "{search_term}" in the "Search datasets" field')
@When(u'I enter "{search_term}" in the "Search datasets" field')
@handle_error
def step(context, search_term):
    context.datasets.enter_search_term(search_term)


@Given(u'I click the search datasets button')
@When(u'I click the search datasets button')
@handle_error
def step(context):
    context.datasets.click_btn_search_datasets()


@When(u'I select Order By "{sort_order}"')
@handle_error
def step(context, sort_order):
    context.datasets.set_sort_order(sort_order)


@Then(u'I should see the Order By option set to "{selected_option}"')
@handle_error
def step(context, selected_option):
    actual_selection = context.datasets.get_sort_order()
    assert_that(actual_selection, equal_to(selected_option))


@Then(u'I should see "{search_term}" in the URL query string')
def step(context, search_term):
    actual_url = context.base.get_current_url()
    assert_that(actual_url, contains_string(search_term))
