from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

#Counter metrics (Counters go up, and reset when the process restarts)
c = Counter('my_failures', 'Description of counter')
c.inc()     # Increment by 1
c.inc(1.6)  # Increment by given value

#There are utilities to count exceptions raised:
@c.count_exceptions()
def f():
  pass

with c.count_exceptions():
  pass

# Count only one type of exception
with c.count_exceptions(ValueError):
  pass
###

#Gauge metrics (Gauges can go up and down)
g = Gauge('my_inprogress_requests', 'Description of gauge')
g.dec(10)    # Decrement by given value
g.inc()      # Increment by 1
g.set(4.2)   # Set to a given value

#There are utilities for common use cases:
g.set_to_current_time()   # Set to current unixtime

# Increment when entered, decrement when exited.
@g.track_inprogress()
def f():
  pass

with g.track_inprogress():
  pass

#A Gauge can also take its value from a callback:
d = Gauge('data_objects', 'Number of objects')
my_dict = {}
d.set_function(lambda: len(my_dict))
###

#Summary (Summaries track the size and number of events.)
s = Summary('request_latency_seconds', 'Description of summary')
s.observe(4.7)    # Observe 4.7 (seconds in this case)

#There are utilities for timing code:
@s.time()
def f():
  pass

with s.time():
  pass
###

#Histogram (Histograms track the size and number of events in buckets. This allows for aggregatable calculation of quantiles)
#h = Histogram('request_latency_seconds', 'Description of histogram')
#h.observe(4.7)    # Observe 4.7 (seconds in this case)

#There are utilities for timing code:
#@h.time()
#def f():
#  pass

#with h.time():
#  pass
###

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())