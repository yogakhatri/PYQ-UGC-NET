# Question 68

*UGC NET CS · 2016 July Paper 3 · Unix and Linux · cron Daemon and User Crontabs*

Which of the following statement is not correct with reference to cron daemon in UNIX O.S. ?

- **1.** The cron daemon is the standard tool for running commands on a pre-determined schedule.
- **2.** It starts when the system boots and runs as long as the system is up.
- **3.** Cron reads configuration files that contain list of command lines and the times at which they invoked.
- **4.** Crontab for individual users are not stored.

> [!TIP]
> **Correct answer: 4. Crontab for individual users are not stored.**

## Solution

cron is a long-running scheduling daemon. It starts as part of system initialization, reads scheduling configuration, and runs commands at their prescribed times. Individual users can install personal crontab entries, and those crontabs are stored in an implementation-specific spool or service database. Consequently the claim that individual-user crontabs are not stored is false; option 4 is the requested answer.

## Key Points

- cron is the scheduler daemon; crontab is the stored schedule submitted by a system administrator or an individual user.

## Why the other options are incorrect

Options 1, 2, and 3 describe the ordinary cron model: scheduled command execution, a daemon available while the system runs, and configuration containing command/time specifications.
