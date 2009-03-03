#!/usr/bin/python
# For some PL workloads (read attacks) the cache-reclaiming policy of Linux is not
# aggressive enough to avert OOMs when low-memory is running out. Examples of this
# were seen on MLAB when TCP flooding attacks would lead to a sudden burst in kernel-memory 
# utilization.
#
# This script is for scenarios of that type. We monitor our memory reserves and empty all
# caches if we find that they are critically low.

import os
import time
import re

lmthreshold = 200000

while (1):
    meminfo=open('/proc/meminfo').read();
    m=re.search(r'LowFree:\s+(\d+)\s+kB',meminfo);
    lowfree=int(m.group(1))

    if (lowfree<200000):
        os.system('echo 3 > /proc/sys/vm/drop_caches')

    time.sleep(60)
