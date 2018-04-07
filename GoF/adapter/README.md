# Adapter pattern


## What is it?

It's a way to make two incompatible interfaces work with each other, like the
name suggests.


## What does it solve

- How to use a class in a way that it was not designed to be used.
- Making a class work with others nicely without modifying it's code.


## Examples

Let's say there are two types of cones for the ice creams, one is a waffle that
will just be wrapped by the person, and a normal cone that will be fetch from
the plastic cone holder.
So we want to add that to our ice cream the same way, but they have different
ways of working, so an adapter comes into play offering the same interface to
the cone as the waffle.
