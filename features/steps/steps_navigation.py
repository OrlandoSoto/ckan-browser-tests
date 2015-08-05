# coding: utf-8
from behave import given, when, then
from hamcrest.core import assert_that, equal_to
from hamcrest.library.text.stringcontains import contains_string
from decorators import *

from pages.home import Home
from pages.base import Base
from pages.utils import Utils


@given(u'I navigate to the CKAN Home page')
@handle_error
def step(context):
    context.base.go()


@given(u'I navigate to the Datasets page')
@handle_error
def step(context):
    context.base.go('/dataset')


@when(u'I click on the "{link_name}" link')
@handle_error
def step(context, link_name):
    context.navigation.click_link(link_name)


@then(u'I should see the "{relative_url}" URL in the address bar')
@handle_error
def step(context, relative_url):
    actual_url = context.base.get_current_url()
    assert_that(actual_url, contains_string(relative_url))
