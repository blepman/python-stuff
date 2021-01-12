#! usr/bin/env python
class Variables:
    """ A way to make variables from dict keys.

    dict = {"hello": "world", "one":1, "foo_list":["elem0", "elem1", 2], "bar_dict":{"etc":"etc", "randint":randint(0,100)}}

    from_dict = Variables(dict)
    from_dict.hello     >>> 'world'
    from_dict.one       >>> 1
    from_dict.foo_list  >>> ['elem0', 'elem1', 2]
    from_dict.bar_dict  >>> {'etc': 'etc', 'randint': 31} """

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)
