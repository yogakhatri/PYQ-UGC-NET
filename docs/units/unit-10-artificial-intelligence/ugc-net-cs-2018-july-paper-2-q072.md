# Question 72

*UGC NET CS · 2018 July Paper 2 · Intelligent Agents · Simple Reflex Agents*

In Artificial Intelligence (AI), a simple reflex agent selects actions on the basis of_________.

- **1.** current percept, completely ignoring rest of the percept history.
- **2.** rest of the percept history, completely ignoring current percept.
- **3.** both current percept and complete percept history.
- **4.** both current percept and just previous percept.

> [!TIP]
> **Correct answer: 1. current percept, completely ignoring rest of the percept history.**

## Solution

A simple reflex agent applies condition-action rules directly to the current percept. It maintains no internal state representing earlier percepts, so the rest of the percept history is ignored. Therefore option 1 is correct.

## Key Points

- Simple reflex: action=current-percept rule; model-based reflex: action uses an updated internal state.

## Why the other options are incorrect

Options 2–4 all require some use of percept history. That belongs to a model-based reflex agent, which updates an internal state when the current percept alone is insufficient.
