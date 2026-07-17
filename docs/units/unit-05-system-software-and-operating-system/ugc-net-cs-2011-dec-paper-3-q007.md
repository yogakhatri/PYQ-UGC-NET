# Question 7

*UGC NET CS · 2011 Dec Paper 3 · CPU Scheduling · Starvation Detection and Prevention*

Can a system detect that some of its processes are starving ? If yes, then explain how it can ? If no, then explain how the system can deal with starvation problem. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Starvation cannot be proved from a finite wait, but prolonged lack of progress can be monitored and starvation should be prevented with fairness or aging**

## Solution

Starvation means a ready process is postponed indefinitely while others continue. At any finite instant, a scheduler generally cannot know whether the process will wait forever—the next scheduling decision might run it—so exact detection of the infinite property is impossible without a specified waiting bound or fairness rule.

A practical system can nevertheless detect symptoms. Record each process's ready-queue entry time, number of bypasses, CPU share and lock-wait duration. If waiting exceeds a policy threshold, flag the process as at risk. This is operational detection of excessive delay, not a proof of infinite starvation.

Prevention is stronger: use aging to increase a waiting process's priority; use round-robin or weighted fair queuing; bound the number of times a newcomer may bypass an older waiter; use FIFO/ticket locks or fair semaphores; periodically boost priorities in multilevel feedback queues; and prevent unbounded priority inversion with priority inheritance or priority ceiling. These mechanisms establish a finite service guarantee under stated assumptions.

## Key Points

- A finite observation cannot prove indefinite delay; fairness, bounded waiting and aging turn starvation into a preventable scheduling property.

## Common mistakes to avoid

Simply increasing a fixed priority once may still permit starvation under continuous higher-priority arrivals. Deadlock detection is not starvation detection: a starving process may remain ready and the system as a whole continues making progress.
