# AirBnB clone - The console
This is the console project.
Concepts used in this project include:
- OOP - Object Oriented Programming
- Python packaging
- cmd module - the command interpreter module
- args/kwargs - arguments and keyworded arguments
- Python unittest
- UUID - For assigning unique user id to objects

## Models
- [BaseModel](models/base_model.py)
- [City](models/city.py)
- [Place](models/place.py)
- [User](models/user.py)
- [State](models/state.py)
- [Amenity](models/amenity.py)
- [Review](models/review.py)

## The console
The [console](console.py) is a command interpreter just like a shell but with limited use-case.
The console is able to manage the objects of the project:
* Create a new object
* Retieve an object from file or database etc
* Do operations on objects
* Update attributes of an object
* Destroy an object
### Usage
On a terminal, run the command:
```
$ ./console.py
(hbnb)
```

The command interpreter commands:
- `help`
Type `help` for a list of a list of all the available commands
```
(hbnb) help

Documented commands (help <topic>):
===================================
EOF  all  count  destroy  help  quit  show  update

(hbnb)
```

- `EOF` - End Of File
```
(hbnb) help EOF

	Exits the console when CTRL+D is entered

(hbnb)
```

- `all`
```
(hbnb) help all

	Prints all string representation of all instances based
	or not on the class name

	Usage: all [<class name>]

(hbnb)
```

- `create`
```
(hbnb) help create

	Creates an instance

	Usage: create <class name>

(hbnb)
```

- `destroy`
```
(hbnb) help destroy

	Deletes an instance based on the class name and id

	Usage: destroy <class name> <id>

(hbnb)
```

- `quit`
```
(hbnb) help quit

	Quits the console

	Usage: Quit

(hbnb)
```

- `show`
```
(hbnb) help show

	Prints the string representation
	of an instance based on the class name

	Usage: show <class name> <id>

(hbnb)
```

- `update`
```
(hbnb) help update

	Updates an instance based on the class name and id
	by adding or updating attribute

	Usage: update <class name> <id> <attribute name> "<attribute value>"

(hbnb)
```
