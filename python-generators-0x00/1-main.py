from itertools import islice
# stream_users = __import__('0-stream_users')


# for user in islice(stream_users.stream_users(), 6):
#     print(user)

import sys
processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    processing.batch_processing(50)
except BrokenPipeError:
    sys.stderr.close()