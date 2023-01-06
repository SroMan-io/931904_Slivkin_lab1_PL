import sys
import time
from urllib import request
from urllib import parse

local_file=''
#'https://tolstoy.ru/upload/iblock/519/voina-i-mir.pdf'

def reporthook(count, block_size, total_size):
    global start_time
    global visualization_time
    if count == 0:
        start_time = time.time()
        visualization_time = 0
        sys.stdout.write(f"Progress: 0% || 0/{total_size} bytes, 0 secs \n")
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)   
    percent = min(int(count*block_size*100/total_size),100)

    if int(visualization_time)!=int(duration):      
        sys.stdout.write(f"Progress: {percent}% || {progress_size}/{total_size} bytes, {round(duration)} secs \n")
        #sys.stdout.flush()
        visualization_time=duration

    if progress_size>=total_size:
         sys.stdout.write(f"Progress: {percent}% || {total_size}/{total_size} bytes, {round(duration,2)} secs\nFile {local_file} is successful downloaded!\n")

def main( argv ):
    remote_url = argv[1]   
    unquoted_url = parse.unquote(remote_url)
    path = parse.urlparse(unquoted_url).path
    global local_file 
    local_file = path.rstrip("/").split("/")[-1]

    request.urlretrieve(remote_url, local_file, reporthook)
    
if __name__ == '__main__':
    main( sys.argv )