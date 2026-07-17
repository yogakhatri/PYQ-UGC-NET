# Question 38

*UGC NET CS · 2015 June Paper 3 · Web Programming · ServletResponse API and Content Type*

The Servlet Response interface enables a servlet to formulate a response for a client using the method __________.

- **1.** void log(Exception e, String s)
- **2.** void destroy( )
- **3.** int getServerPort()
- **4.** void setContextType(String type)

> [!TIP]
> **Correct answer: No option is exactly valid. Option 4 is clearly intended, but the ServletResponse method is `void setContentType(String type)`, not `setContextType`.**

## Solution

`ServletResponse.setContentType(String)` tells the container the MIME type of the response, such as `text/html`, and therefore helps formulate the client response. The printed option inserts `Context` instead of `Content`. This is an API-name error in the source, not merely a formatting choice.

## Key Points

- The exact ServletResponse API call is `setContentType(String type)`; method spelling matters in Java.

## Why the other options are incorrect

`log(Exception,String)` belongs to logging facilities such as ServletContext in older APIs, `destroy()` is a servlet lifecycle method, and `getServerPort()` belongs to ServletRequest. None is a ServletResponse method for setting response content.
