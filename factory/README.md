# Factory Method pattern


## What is it?

It's a pattern that allows you to create objects without specifying it's class.


## What does it solve

- Reducing complexity of creating objects since the code to create them can be complex.
- Reducing duplication of code when creating objects, since it may require:
    - Another level of abstraction
    - Code that is not part of the object's concern
    - May require information not accessible to the composing object


## Advantages

- Allows us to change the factory without changing code on other places to get the correct object
- There's one and only one place that produces the objects in the code. OCP Principle.

## Examples of uses

Imagine that we have a Product factory, where we pass an ID and according to
that ID, we return an object with two different subclasses. One Sofa and one
Bed, which having their own special properties.
