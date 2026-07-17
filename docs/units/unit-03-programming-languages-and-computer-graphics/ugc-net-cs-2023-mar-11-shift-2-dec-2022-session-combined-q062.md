# Question 62

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Web Programming · Scripting*

Which one of the following allows the session to continue?

- **1.** When a user quits a browser
- **2.** When the user logs out and is invalidated by the servlet
- **3.** When the session is timed out due to inactivity
- **4.** When the user refreshes the browser and there is a persistent cookie

> [!TIP]
> **Correct answer: 4. When the user refreshes the browser and there is a persistent cookie**

## Solution

Refreshing a browser normally sends the same persistent session cookie back to the server, so the server can associate the new request with the existing session and continue it. The other events explicitly end or invalidate the client/server session association.

## Key Points

- HTTP is stateless; a session continues across requests only while its identifier remains valid on both client and server.

## Why the other options are incorrect

Closing the browser can discard a nonpersistent session cookie. Logging out commonly invalidates the server-side session, and an inactivity timeout expires it. A refresh with a persistent cookie does none of those things.
