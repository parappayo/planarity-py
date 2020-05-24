
# planarity-py

[Planarity](https://en.wikipedia.org/wiki/Planarity) is a graph geometry game, [originally implemented in Flash](http://planarity.net/) by John Tantalo, based on a concept by Mary Radcliffe. This version is implemented in [PyGame](https://www.pygame.org/).

There is an [elegant implementation](https://www.jasondavies.com/planarity/) in JavaScript by Jason Davies, as well as a GTK+ [desktop version](http://web.mit.edu/xiphmont/Public/gPlanarity.html) by Chris Montgomery of Xiph.org.

![Screenshot](./screenshot.png)

## Setup

Assuming you have [Python 3](https://www.python.org/) and [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) installed,

* `pipenv install`
* `pipenv run python3 planarity.py`

If you have already installed PyGame into your global environment, then you probably just want,

* `python3 planarity.py`

On Windows, `python3` is often aliased as `py` so try,

* `py planarity.py`

## Further Considerations

I'm working on other Planarity implementations.

* [planarity-qt](https://github.com/parappayo/planarity-qt)

I'm also working on other game clones.

* [hex-py](https://github.com/parappayo/hex-py)

There are alternative tech choices worth considering:

* [pyglet](http://pyglet.org/) adheres more to OpenGL than PyGame
