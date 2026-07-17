# Question 18

*UGC NET CS · 2016 July Paper 2 · Data Modeling · NULL Values and Entity Integrity*

In a relational database model, NULL values can be used for all but which one of the following ?

- **1.** To allow duplicate tuples in the table by filling the primary key column(s) with NULL.
- **2.** To avoid confusion with legitimate data values such as 0 for integer columns and the empty string for string columns.
- **3.** To mark a column as unknown when its actual value is unknown.
- **4.** To mark a column as not applicable when that attribute does not exist for the particular tuple.

> [!TIP]
> **Correct answer: 1. To allow duplicate tuples in the table by filling the primary key column(s) with NULL.**

## Solution

A NULL can represent an unknown value or a value that is inapplicable, and it prevents those meanings from being confused with legitimate values such as numeric zero or an empty string. It cannot be placed in a primary-key column to manufacture duplicate tuples: entity integrity forbids NULL in every primary-key component, and a relation cannot contain duplicate tuples.

## Key Points

- NULL means missing/unknown/inapplicable; it is not a wildcard for bypassing keys or duplicate elimination.

## Why the other options are incorrect

Options 2–4 describe the standard motivations for a null marker: distinguish missingness from real values, record 'unknown', or record 'not applicable'. Only option 1 conflicts with primary-key and relational-set semantics.
