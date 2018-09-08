Title: Unified Python
Author: Marc
Date: 2011-06-25 01:19:00
Slug: unified-python
Tags: Python

After all these days at EuroPython, there is a thought that keep me thinking. It is about how Python have different ways to represent what it could be considered the same thing.

On today's talk, Alex Martelli pointed out that "def" and "lambda" are actually the same concept. This was part of a more complete idea about that both of them have the wrong name ("function" should be the right), and that lambda actually should disappear, but that's another question.

Also, yesterday, Raymond Hettinger reminded that class are actually dictionaries, something that most Pythonistas know, but which also made me thought.

Then, there is something that I never saw very clearly, and it is the subtle difference between an instance and a dictionary, and how trivial it can be in some case, the difference between person['name'] and person.name.

So, I wanted to do an experiment on how it could look Python, if it would try to merge all this entities in ones single format, and even some other things like avoiding assignments that doesn't follow the assignment pattern (I mean class or function definition here, where instead of _my_func = [...]_ it's used _def my_func[...]_).

Next, there is how the most stupid example I could invent looks like, but first some definitions to make it easier to understand the idea.

**map**: could be also "class", "dict", "obj", "hash",... and it's the structure for dictionaries, classes and instances.
**seq**: a list or tuple, any linear sequence of values.
**func**: a function or callable, that in Python is defined by "def" or "lambda".

<code>
foods = seq:
    "meat"
    "milk"
    "bread"

sounds = map:
    "bark" = "woof woof"
    "mew" = "meow meow"

animal = map:
    "step_size" = None
    "sound" = None

    "move" = func(self, num_steps):
        print("I've moved {} units".format(num_steps * self.step_size))

    "talk" = func(self):
        print(sounds.{self.sound})

    "eat" = func(self, food):
        print("I'm eating {}".format(food))

cat = map(animal):
    "step_size" = 80
    "sound" = "mew"

    "eat" = func(self, food):
        print("I only eat {} if I want to".format(food))


azrael = map(cat):
    "owner_name" = "Gargamel"

azrael.move(5)
for food in foods:
    azrael.eat(food)
</code>

Of course, there are too many things that should be considered before being able to implement this syntax, but can give an idea on how it could look a more _unified_ approach of Python syntax.

See how the syntax for "sounds", which would be a dictionary, "cat", which would be a class, and "azrael", which would be a instance, is exactly the same.

Being used to Python syntax, it's difficult to say if this syntax could be readable, so far I just find it weird. But what looks clear, is that this syntax would make the language simpler, from the implementation point of view, and probably from the programmer point of view, who would probably need to forget some OP concepts first.

Whatever is the conclusion the reader can get from this example, I think it's quite interesting seeing how a class can look exactly the same way as a dictionary, and how an instance can look exactly as a subclass of the base class.