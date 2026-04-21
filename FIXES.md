state the file name
the line number
whta the problem was
what you changed


File_name: main.py
 line 1:PROBLEM: httpstatus was missing. FIXES:added httpstatus {HTTPStatus}.
 line 8:PROBLEM: no hardcoded reddis host,in cloud/container environment this will fail. FIXES:added a hardcoded reddis host, this will Read Redis host from environment variable, fallback to localhost {redis_host = os.getenv("REDIS_HOST", "localhost")}
 line 9:FIXES. Added decode_responses=True to avoid manual .decode() calls.
 line 22:PROBLEM: get-job returns ["error": "not found"] with a default 200 OK status. Should return 404 Not Found. FIXES:Added [HTTPStatus.NOT_FOUND] to returned 404 status when job not found instead of 200. 
 line 23:PROBLEM: noticed a potential decoding issues with status.decode(). FIXES:changed it from status.decode to status.

file_name:worker/worker.py
 line 5: FIXES:added import sys to allow clean exit with sys.exit when receiving termination signal.
 line 8: FIXES:added the same reddis host as our main.py to avoid connecting to other reddis host.
    
