# Question 52

*UGC NET CS · 2017 Jan Paper 3 · Process Management · Fair-Share Scheduling Priorities*

Some of the criteria for calculation of priority of a process are : a. Processor utilization by an individual process. b. Weight assigned to a user or group of users. c. Processor utilization by a user or group of processes In fair share scheduler, priority is calculated based on :

- **1.** only (a) and (b)
- **2.** only (a) and (c)
- **3.** (a), (b) and (c)
- **4.** only (b) and (c)

> [!TIP]
> **Correct answer: 3. (a), (b) and (c)**

## Solution

Fair-share scheduling adjusts a process's priority using both its own recent processor consumption and the recent consumption of its user or group, preventing a user from gaining extra CPU merely by launching more processes. It also uses an assigned user/group weight to represent that group's entitled share. Therefore individual-process utilization, group weight, and user/group utilization all participate: a, b, and c, giving option 3.

## Key Points

- Fair-share priority combines process usage with weighted aggregate user/group usage.

## Why the other options are incorrect

Options 1, 2, and 4 each omit one component needed by the standard fair-share priority formula. Process history controls local behavior, group history enforces aggregate fairness, and weight defines the intended allocation.
