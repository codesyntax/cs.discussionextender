from plone.app.discussion.browser.comments import CommentForm
from plone.app.discussion.browser.comments import CommentsViewlet as Base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CommentsViewlet(Base):
    form = CommentForm
    index = ViewPageTemplateFile('comments.pt')
