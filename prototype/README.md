# Prototype

A pattern that describes an object being able to create a true copy of itself.

## What does this solve

- This is helpful for use cases where re-creating an object is expensive, so rather than using a constructor, we just use a method called clone() to get a true copy of the object instead.

## Example

Keeping with the ice cream theme, the exapmle would be that an ice cream object would be able to create a copy of itself with a method called copy() that would return `deepcopy` on itself.
