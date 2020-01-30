from __future__ import print_function

import basc_py4chan
import random
import requests

def webm():
    
    # grab the first thread on the board by checking first page
    board = basc_py4chan.Board('wsg')
    all_thread_ids = board.get_all_thread_ids()
    number = random.randint(1, 16)
    first_thread_id = all_thread_ids[number]
    thread = board.get_thread(first_thread_id)

    # file information
    webmlist = []
    for f in thread.file_objects():
        if f.file_extension == ".webm":
            webmlist.append(f.file_url)
    return random.choice(webmlist)
