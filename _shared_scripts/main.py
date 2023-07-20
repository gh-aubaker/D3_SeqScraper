import time
import JSONscrub

if __name__ == '__main__':
    start = time.time()
    JSONscrub.execute()
    print("done. it took ", time.time()-start, " to run")