import resource
import time

time_start = time.perf_counter()
list = [1,2,3,4,5,6.6,7,7,7,7,65,4]
a = 3
n = 4
#run your code
t = (time.perf_counter() - time_start)

m=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%5.1f secs %5.1f MByte" % (t,m))
