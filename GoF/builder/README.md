# Builder

Similar to the Factory, but it's used for more complex objects that requires
data from potentially multiple places and/or multiple steps to create it.


## What does it solve

- Creating objects that require multiple parameters
- As a way to create objects separate to the constructor, as a wrapper or
replacement.

## Disadvantages

- Dependency injection can be harder to implement

## Example

If you want an ice cream object that has 2 scoops of strawberry and 1 of
chocolate, and if each of those are an object, you could create a builder where
you pass in how many scoops of a flavour the object Icecream has and the builder
will build the object with those parameters.
