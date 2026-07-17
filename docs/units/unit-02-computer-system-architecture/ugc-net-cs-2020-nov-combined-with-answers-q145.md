# Question 145

*UGC NET CS · 2020 Nov With Answers · Memory Hierarchy · Disk Transfer Rate*

If one track of data can be transferred per revolution, then what is the data transfer rate?

- **1.** 2,850 KBytes/second
- **2.** 4,500 KBytes/second
- **3.** 5,700 KBytes/second
- **4.** 2,250 KBytes/second

> [!TIP]
> **Correct answer: 4. 2,250 KBytes/second**

## Solution

A track holds 25 KBytes. The rotation speed is 5,400 rpm = 5,400/60 = 90 revolutions per second. If one track is transferred per revolution, the rate is 25 KBytes/revolution ×90 revolutions/second = 2,250 KBytes/second. This is option 4.

## Key Points

- Transfer rate = data per revolution × revolutions per second.

## Why the other options are incorrect

Options 1–3 do not equal track capacity multiplied by revolutions per second. Using rpm directly without dividing by 60 would also give a rate 60 times too large.
