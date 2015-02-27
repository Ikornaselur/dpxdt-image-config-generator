from re import sub
from os import listdir


def generate_title_from_file_name(file_name):
    """Replace all symbols with spaces and "titleize" the file name

    `foo-bar_baz.png` would become `Foo Bar Baz`
    """
    no_symbols = sub('[^a-zA-Z]', ' ', file_name)
    return no_symbols.title()


def writeline(string, f):
    """Wrapper for writing the a string with newline to file"""
    f.write(string + '\n')


def lookahead(iterable):
    """A for loop wrapper to check return if the item is the last item"""
    it = iter(iterable)
    last = it.next()
    for val in it:
        yield last, False
        last = val
    yield last, True


def get_pngs(path):
    """Return a list of all the png image files within the given path"""
    return [png for png in listdir(path) if png.endswith('png')]
