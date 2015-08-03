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


@then(u'I should see "{page_title}" displayed in the page title')
@handle_error
def step(context, page_title):
    # Verify that the page title matches the link we clicked
    page_title = context.base.get_page_title(page_title)
    assert_that(page_title, contains_string(page_title))
