# Singleton

It's a pattern where a class can only be instantiated once and that instance is
used anytime the class gets instanciated again.


## What does it solve

- Having only one instance of a class in your application.
- Having global variables that are "hidden" since you're just "instantiating" a
class


## Disadvantages

It basically makes a global object


## Example

With the ice cream shop, we can make an ice cream maker a singleton, so we can
have a class IceCreamMaker that will return itself if it's already instanciated
so they can keep state like how many ice creams they made or if they're making
an ice cream at the moment
