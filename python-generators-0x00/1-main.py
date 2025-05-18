from itertools import islice
# stream_users = __import__('0-stream_users')


# for user in islice(stream_users.stream_users(), 6):
#     print(user)

# import sys
# processing = __import__('1-batch_processing')

# ##### print processed users in a batch of 50
# try:
#     processing.batch_processing(50)
# except BrokenPipeError:
#     sys.stderr.close()



seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows




# (venv) faithokoth@Faiths-MacBook-Pro python-generators-0x00 % cat 3-main.py

import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_pagination


try:
    for page in lazy_paginator(100):
        for user in page:
            print(user)

except BrokenPipeError:
    sys.stderr.close()