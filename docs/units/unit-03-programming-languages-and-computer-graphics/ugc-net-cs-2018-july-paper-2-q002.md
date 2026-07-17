# Question 2

*UGC NET CS · 2018 July Paper 2 · Web Programming · JavaScript `this` and Lexical Scope*

Consider the non-strict browser JavaScript: `var y="12"; function f(){ var y="6"; alert(this.y); function g(){ alert(y); } g(); } f();` If M is the number of alert boxes and D1,…,DM are their displayed contents, which result occurs?

- **1.** M=3; D1 displays ”12”; D2 displays ”6”; D3 displays ”12”.
- **2.** M=3; D1 displays ”6”; D2 displays ”12”; D3 displays ”6”.
- **3.** M=2; D1 displays ”6”; D2 displays ”12”.
- **4.** M=2; D1 displays ”12”; D2 displays ”6”.

> [!TIP]
> **Correct answer: 4. M=2; D1 displays ”12”; D2 displays ”6”.**

## Solution

The script calls `f()` as a plain function in a classic non-strict browser script. In that setting, `this` inside `f` is the global object, and the global `var y="12"` is its `y` property; the first alert therefore shows 12. The nested function `g` resolves the unqualified name `y` lexically and finds `f`'s local `y="6"`, so the second alert shows 6. There are exactly two alerts, giving option 4.

## Key Points

- `this.y` depends on the call receiver; bare `y` in a nested function follows lexical scope.

## Why the other options are incorrect

Options 1 and 2 invent a third alert. Option 3 reverses dynamic `this.y` lookup and lexical variable lookup. In strict mode, a plain call would make `this` undefined and the code would fail at `this.y`; the exam's use of browser `alert` and global `var` indicates the classic non-strict interpretation.
