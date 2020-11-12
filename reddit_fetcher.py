# -*- coding: utf-8 -*-
import praw
import json
from praw.models import MoreComments
from config import API
from config import extras
import re

def find_hyperlink(submiss) :
    start = submiss.find('[')
    end  = submiss.find(']')
    if (start > -1 and end > -1 and end > start) :
        if (submiss[end + 1] == '('):
            start2 = end + 1
            end2 = submiss.find(')', start2)
            if (end2 > start2) :
                submiss = submiss[0: start2] + submiss[end2 + 1::]
                submiss = submiss.replace('[', '')
                submiss = submiss.replace(']', '')
                find_hyperlink(submiss)
    return (submiss)

def edit_special_chars(submiss) :
    var = submiss
    var = var.upper()
    index = var.find('EDIT')
    if (index > 0):
        submiss = submiss[:index]
    submiss = submiss.replace('by', '')
    submiss = submiss.replace(' ', '+')
    return (submiss)

def add_to_list(submission, list):
    if (submission.find('\n') > 0 and len(submission.split('\n')) > 3):
        for word in submission.split('\n'):
            if word:
                list.append(word)
    else:
        index = submission.find('\n')
        if (index > 0):
            submission = submission[:index]
    if (submission.find('+or+') > 0):
        for word in submission.split('+or+'):
            if word:
                list.append(word)
    if (submission.find('+and+') > 0):
        for word in submission.split('+and+'):
            if word:
                list.append(word)
    elif (submission.find('+or+') == -1 and submission.find('+and+') == -1) :
        list.append(submission)

reddit = praw.Reddit(
    user_agent= API["user_agent"],
    client_id= API["client_id"],
    client_secret= API["client_secret"],
    username=   API["username"],
    password= API["password"],
)
submission = reddit.submission(id=extras["reddit_url_id"])
submission.comment_sort = 'best'
filteredlist = []
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    var = top_level_comment.body.encode('utf-8')
    if not b'removed' in var :
        var = var.decode('utf-8')
        var = find_hyperlink(var)
        var = (''.join(ch for ch in var if ch.isalnum() or ch.isspace()))
        var = edit_special_chars(var)
        add_to_list(var, filteredlist)
with open('data', 'w', encoding='utf8') as outfile:
    json.dump(filteredlist, outfile)