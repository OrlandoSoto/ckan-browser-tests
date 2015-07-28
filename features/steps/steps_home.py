from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.text.stringcontains import contains_string
from decorators import *

from pages.home import Home
from pages.base import Base


@given(u'I navigate to the Home page')
@handle_error
def step(context):
    context.base.go()


@then(u'I should see "{link_name}" displayed in the page title')
@handle_error
def step(context, link_name):
    # Verify that the page title matches the link we clicked
    page_title = context.base.get_page_title()
    assert_that(page_title, contains_string(link_name))
