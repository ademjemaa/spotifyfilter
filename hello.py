# -*- coding: utf-8 -*-
import praw
from praw.models import MoreComments
from config import API

reddit = praw.Reddit(
    user_agent= API["user_agent"],
    client_id= API["client_id"],
    client_secret= API["client_secret"],
    username=   API["username"],
    password= API["password"],
)
print(reddit.user.me())
submission = reddit.submission(id="jq53sv")
submission.comment_sort = 'best'
filteredlist = []
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    str = top_level_comment.body
    if not "removed" in str :
        filteredlist.append(str)
for i in filteredlist:
    print(i)