# Flyweight

Flyweight is an object that tries to minimize memory usage by sharing data with
other related objects that require an object which could be potentially
duplicated.

# What does it solve

- Having an object that can be shared between others so that memory usage is kept at a minimum.

## Example

In the ice cream shop, we have plenty of flavours, so instead of creating
multiple scoop objects (each with a flavour) for each ice cream, we can use a
flyweight to have the same instance representing the flavour in the scoop.
