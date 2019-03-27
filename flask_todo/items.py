import datetime

class Item(object):


    def __init__(self, job, is_complete = False, timestamp = '', due_date = ''):
        # timestamp of when it was created
        if timestamp == '':
            self.timestamp = datetime.datetime.now()
        else:
            self.timestamp = timestamp
        # boolean marking the item as complete/not completed (false to begin)
        self.is_complete = is_complete
        # text of the actual to-do item
        self.job = job
        # optional attribute which defines the time/date an item is due.
        # should be in YYYY-MM-DD HH format, can also be in HH:MM:SS format perhaps
        self.due_date = due_date
