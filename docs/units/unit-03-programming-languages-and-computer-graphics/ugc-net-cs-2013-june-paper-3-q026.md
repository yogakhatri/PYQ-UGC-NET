# Question 26

*UGC NET CS · 2013 June Paper 3 · Computer Animation · Actors and Per-Frame Updates*

An actor in an animation is a small program invoked _______ per frame to determine the characteristics of an object in the animation.

- **A.** once
- **B.** twice
- **C.** 30 times
- **D.** 60 times

> [!TIP]
> **Correct answer: A. once**

## Solution

In this actor-based animation model, an actor is a behavior program associated with an object. The animation system invokes it once for each generated frame so it can update or determine that object's current position, appearance or other characteristics before the frame is rendered.

## Key Points

- Frame rate says how many frames occur per second; an actor update runs once within each frame.

## Why the other options are incorrect

Twice per frame has no general role, and 30 or 60 are frame rates measured per second, not the number of times one actor runs within each frame. The per-frame update count is one.
