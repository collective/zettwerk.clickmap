from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from zettwerk.clickmap import clickmapMessageFactory as _


class IclickmapView(Interface):
    """
    clickmap view interface
    """

class clickmapView(BrowserView):
    """
    clickmap browser view
    """
    implements(IclickmapView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()


    def getLoggedPagesOverview(self):
        """ """
        return [self.context.getLoggedPageOverview(page) for page in self.context.pages]
