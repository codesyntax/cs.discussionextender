"""

This comment-form extensions follows the recomendations at:
  https://github.com/collective/example.commentextender/

"""
from zope.interface import Interface, implements
from zope import schema

from zope.component import adapts
from zope.annotation import factory
from plone.z3cform.fieldsets import extensible

from plone.app.discussion.browser.comments import CommentForm
from plone.app.discussion.comment import Comment

from persistent import Persistent


from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IUserEmail(Interface):
    pass

from cs.discussionextender import discussionMessageFactory as _

# Interface to define the fields we want to add to the comment form.                        
class ICommentExtenderFields(Interface):
    
    url = schema.TextLine(title=_(u'Website'), 
                          required=False)
    
    email = schema.TextLine(title=_(u'Email'),
                            description=_(u'The e-mail address will not be shown, it is just to contact you if requried'),
                            required=True)


class CommentExtenderFields(Persistent):
    implements(ICommentExtenderFields)
    adapts(Comment)
    url = u''
    email = u''

# CommentExtenderFields factory
CommentExtenderFactory = factory(CommentExtenderFields)


# Extending the comment form with the fields defined in the
# ICommentExtenderFields interface.
class CommentExtender(extensible.FormExtender):
    adapts(Interface, IDefaultBrowserLayer, CommentForm)

    def __init__(self, context, request, form):
        self.context = context
        self.request = request
        self.form = form

    def update(self):
        # Add the fields defined in ICommentExtenderFields to the form.
        self.add(ICommentExtenderFields, prefix="")
        # Move the url and email fields to the top of the comment form.
        self.move('url', before='text', prefix="")
        self.move('email', before='url', prefix="")
