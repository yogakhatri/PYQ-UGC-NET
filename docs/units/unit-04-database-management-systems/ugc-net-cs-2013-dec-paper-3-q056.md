# Question 56

*UGC NET CS · 2013 Dec Paper 3 · Relational Model and Algebra · Selection Followed by Projection*

Consider the following schemas : Branch = (Branch-name, Assets, Branch-city) Customer = (Customer-name, Bank name, Customer-city) Borrow = (Branch-name, loan number, customer account-number) Deposit = (Branch-name, Account- number, Customer-name, Balance) Using relational Algebra, the Query that finds customers who have balance more than 10,000 is _______

- **A.** πcustomer-name (σbalance > 10000(Deposit)
- **B.** σcustomer-name (σbalance > 10000(Deposit)
- **C.** πcustomer-name (σbalance > 10000(Borrow)
- **D.** σcustomer-name (πbalance > 10000(Borrow)

> [!TIP]
> **Correct answer: A. πcustomer-name (σbalance > 10000(Deposit)**

## Solution

Balance and Customer-name are attributes of Deposit, so that is the required relation. First select tuples satisfying Balance>10000: sigma_(Balance>10000)(Deposit). Then project Customer-name from the selected tuples: pi_(Customer-name)(sigma_(Balance>10000)(Deposit)). This is exactly the operation sequence represented by option A.

## Key Points

- Selection filters rows; projection chooses columns.
- Filter Deposit by balance, then project customer names.

## Why the other options are incorrect

B incorrectly uses selection with Customer-name as though it were a Boolean condition; retrieving columns requires projection. C and D use Borrow, which does not contain Balance in the stated schema. D also reverses/misuses selection and projection.
