# Testing

Execute tests with `python test_polly.py`. 

Your output should have no failures and exit with `OK`.

## Location
Either in the course materials folder in sciebo or at https://github.com/Wegi/hhu-advanced-programming-exercise-01-polly online

# Practical Exercise 01
(Due to 06.11.2019)

## Po(l)lymorphism wants a biscuit

In this exercise, we develop a bunch of object oriented parrots. The `polly.py` file contains
two classes: `Parrot` and `ParrotType`. 

`ParrotType` is just an `Enum` to enumerate all possible parrot types.

`Parrot` is the class representing the actual parrot. They all have certain
properties, since they are electronic parrots.
Every parrot has a `type` the `number_of_coconuts` it is carrying and a `voltage`
on which it runs. They are also either nailed down `is_nailed = True` or not.

At the beginning, you will be only able to get the parrots speed. You will change 
that during the exercise. The `Parrot` has also a method that is annotated with
`@staticmethod`. We will talk about static methods and annotations later on. 
For now, you just need to now, that static methods are called on the class
rather than on an instantiated object.

### Your Tasks
During all the tasks, regularly re-run the tests to see if you broke some functionality.


* 1: Download the project and open it in an IDE. (Use `git` if you are familiar or download
the `practical_exercise_polly.zip` archive in the sciebo folder)
* 2: Run all tests in the `test_polly.py` file. They should all pass initially.
* 3:The `Parrot` class is not implemented very cleverly. Rewrite the class with the things
in mind that you learned up to date. Extract other classes, where needed. (Tip: Inheritance and Polymorphism)
* 4:The Parrots should now be additionally initialized with an optional List of Strings `messages` that contains
messages the parrot can repeat. If no message is passed an instantiation, give it any default String.
* 5: Develop a method `speak()` for the parrots, that returns any message that the parrot has learned.
(Try your hand at random functions if you like)
* 6: Develop tests for the new functionality. 
* 7: Find out how you can overload the `+` sign in python.
* 8: Overload the + sign for any Parrot. When you add two parrots (`polly + jacky`),
the result will be another parrot that has the type mixed and is capable of speaking
the message of both "parent" Parrots. (The parrots have no gender, they are electronic ;))
* 9: Implement a class `ParrotCage` which can be initialized with any number of parrots.
The cage shall have a method to
    * Add parrots
    * Remove parrots
    * Listen to the cage (repeat a random phrase of a random parrot)
    * Any fun method you can think of
* 10: Write Tests for the `ParrotCage`


------------------
Credit: Exercise inspired by Christian Meter (@n2o)