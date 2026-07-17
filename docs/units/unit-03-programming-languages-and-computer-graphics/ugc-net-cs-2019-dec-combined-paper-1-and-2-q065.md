# Question 65

*UGC NET CS · 2019 Dec Paper 1 And 2 · Object-Oriented Programming · Protected Inheritance and Access Control*

Let A be the base class in C++ and B be the derived class from A with protected inheritance. Which of the following statement is false for class B?

- **1.** Member function of class B can access protected data of class A
- **2.** Member function of Class B can access public data of class A
- **3.** Member function of class B cannot access private data of class A
- **4.** Object of derived class B can access public base class data

> [!TIP]
> **Correct answer: 4. Object of derived class B can access public base class data**

## Solution

Inside B, the inherited public and protected members of A are accessible, so statements 1 and 2 are true. A's private members remain inaccessible directly to B, so statement 3 is also true. Under protected inheritance, A's public and protected members become protected members of B; outside code using a B object cannot access them. Therefore statement 4 is false, making option 4 correct.

## Key Points

- Protected inheritance maps base public/protected members to protected in the derived class; base private members stay inaccessible.

## Why the other options are incorrect

Options 1–3 describe the correct access rules for B's member functions. Protected inheritance changes the outside visibility of inherited public members; it does not prevent B's own member functions from using the base's public or protected members, and it never grants direct access to base private data.
