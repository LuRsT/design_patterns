# Abstract Factory pattern


## What is it?

Abstract factory pattern is a way to encapsulate a group of factories that
share a common theme amongst them, without specifying their classes.

Factory of factories


## What does it solve

- How to specify related objects in a way that is independent to the way they
are created.


## Advantages

- Single point of creation of objects for those types. Like the factory method pattern
- Helps testing because the creted objects can be easily replaced with mocks


## Examples

An ice cream shop that has multiple types of ice creams. If we create an
abstract factory, we can create an object that has flavour of Strawberry and
Texture of sorbet.

So we could have a top class called Icecream that has a two factories, one that
gets a Flavour class and another for texture class. So to build our icecream,
the factory for texture would give us a SorbetTexture class and the factory for
flavour would give us a StrawberryFlavour, so we end up with a composite object
that is made out of two other objects made from different factories.
