Error detected during execution are called exceptions. exceptions comes in different types and 
the types is printed as part of the message.
Base exception is the common base class of all exceptions. exception can be used as a wildcard
that cathes (almosta) everything. however, it is good practice to be as specific as possible 
with the types of exceptions that we intend to handle, and to allow any unexcepted exceptions
to propagate on.
an error refers to a situation where the execution of a program encounters an unexpected condition or situation that prevents 
it from running correctly.
to handle errors or exceptions in python, you can use the try and except statements.
when error occurs within the try block, python looks for a corresponding except block that can handle that specific type of error. 
if a matching except block is found, its code is executed. if no matching block is found, the error propagates to the next level of exception handling.
the else block is exceptional and executes only if no exceptions were raised in the try block. the finally block is also optional typically used to
perform cleanup tasks such as closing files or releasing resources.
UTF-8 (Unicode transformation format-8 is an encoding scheme used and is the preferred encoding for text on the internet and in most modern software systems.
