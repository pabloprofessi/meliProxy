import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_time(): 
	print "pablo kapo cada 5 segundos"
	print_some_times()
	print "asdasdas"	

def print_some_times():
   
   
   s.enterabs(time.time() + 5, 1, print_time, ())
   s.run()
   pass

print_some_times()
print "asdasdas"