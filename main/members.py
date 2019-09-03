from .models import GroupTask


class Members(object):
    def all_members(self):
        GroupTask.member.all()
