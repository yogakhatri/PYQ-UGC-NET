# Question 73

*UGC NET CS · 2019 June Paper 1 And 2 · Object-Oriented Programming · Method overloading and overriding*

In Java, class Good has private int m, constructor Good(int m){this.m=m;}, and overloaded method Boolean equals(Good n){return n.m==m;}. In main: Good m1=new Good(22); Good m2=new Good(22); Object s1=new Good(22); Object s2=new Good(22); then print m1.equals(m2), s1.equals(s2), m1.equals(s2), and s1.equals(m2). What is the output?

- **1.** True, True, False, False
- **2.** True, False, True, False
- **3.** True, True, False, True
- **4.** True, False, False, False

> [!TIP]
> **Correct answer: 4. True, False, False, False**

## Solution

Good declares equals(Good), which overloads rather than overrides Object.equals(Object). For m1.equals(m2), both static types are Good, so equals(Good) is selected and returns true because both m values are 22. Variables s1 and s2 have static type Object, so s1.equals(s2) and s1.equals(m2) call Object.equals, which tests identity and returns false for different objects. In m1.equals(s2), the argument's static type Object prevents selection of equals(Good), so inherited equals(Object) is used and is also false.

## Key Points

- To override Object.equals in Java, the signature must be equals(Object); equals(Good) is only an overload.

## Why the other options are incorrect

Options 1–3 treat equals(Good) as though it overrode equals(Object), or ignore compile-time overload selection. Only the first comparison invokes the custom method.

## Additional Information

Using @Override would expose this mistake at compile time because equals(Good) does not match the superclass method.
