from __future__ import absolute_import, unicode_literals

from home.models import HomePage
from standard_page.models import StandardPage


class AnotherHomePage(HomePage):
    content_panels = HomePage.content_panels


class AnotherStandardPage(StandardPage):
    content_panels = StandardPage.content_panels
