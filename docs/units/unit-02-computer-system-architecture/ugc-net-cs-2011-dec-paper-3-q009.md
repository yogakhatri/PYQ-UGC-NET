# Question 9

*UGC NET CS · 2011 Dec Paper 3 · Digital Logic Circuits and Components · Master-Slave JK Flip-Flop*

Obtain the logic diagram of a master-slave JK flip flop with AND and NOR Gates, include provision for setting and clearing the flip flop asynchronously. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Use a clocked JK master latch feeding an oppositely clocked slave latch, with asynchronous preset and clear overriding both**

## Solution

Build two cross-coupled NOR SR latches. The master is open while CLK=1 and the slave is closed; the slave opens while CLK=0 and the master closes. Feed the master with AND-gated signals S_M=J·CLK·Q_bar and R_M=K·CLK·Q. The feedback terms give JK behaviour: J=K=0 holds, 1/0 sets, 0/1 resets and 1/1 makes the master capture the complement of the old output.

Let the master outputs be M and M_bar. Gate them into the slave with S_S=M·CLK_bar and R_S=M_bar·CLK_bar (swap names if the chosen NOR-latch polarity convention uses active-low inputs). Because the two latches are enabled on opposite clock levels, the externally visible Q changes only when control passes from master to slave, preventing the race-around that a level-triggered JK latch suffers when J=K=1.

Add asynchronous active-low PRE_bar and CLR_bar to the set and reset sides of both latches so they override the clock: PRE_bar=0 forces Q=1; CLR_bar=0 forces Q=0. The simultaneous asserted combination is forbidden. In a drawn circuit, show an inverter generating CLK_bar, the four clock/input AND gates, the two cross-coupled NOR pairs, feedback from final Q/Q_bar to the master gates, and preset/clear override lines.

## Key Points

- Opposite clock phases isolate master and slave; JK feedback enables toggling; asynchronous preset/clear override normal clocked operation.

## Common mistakes to avoid

Driving master and slave with the same clock phase makes them transparent together and permits race-around. Feeding J and K without Q/Q_bar feedback does not implement toggle behaviour. Asynchronous preset/clear must bypass clock gating and their illegal simultaneous state must be identified.
