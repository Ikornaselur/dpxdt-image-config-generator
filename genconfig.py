import sys
from os.path import abspath
from os import listdir
from re import sub


BEFORE_CONF = 'before.json'
AFTER_CONF = 'after.json'


def generate_title_from_file_name(file_name):
    """Replace all symbols with spaces and "titleize" the file name

    `foo-bar_baz.png` would become `Foo Bar Baz`
    """
    no_ext = '.'.join(file_name.split('.')[:-1])
    no_symbols = sub('[^a-zA-Z]', ' ', no_ext)
    return no_symbols.title()


def config_entry(name, path):
    """Return a string with the configuration entry based on name and path"""
    tab = '    '
    string = tab + '{\n'
    string += 2*tab + '"name": "{}",\n'.format(
        generate_title_from_file_name(name))
    string += 2*tab + '"run_failed": false,\n'
    string += 2*tab + '"image_path": "{}/{}"\n'.format(path, name)
    string += tab + '}'
    return string


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


def get_images(path):
    """Return a list of all the png image files within the given path"""
    return [png for png in listdir(path) if png.endswith('png')]


def generate_config(conf, path, images):
    """Generate the actual json config file based on images found"""
    with open(conf, 'w') as f:
        writeline('[', f)
        for i, last in lookahead(images):
            entry = config_entry(i, path)
            if not last:
                entry += ','
            writeline(entry, f)
        writeline(']', f)


def main(before_path, after_path):
    abs_before_path = abspath(before_path)
    abs_after_path = abspath(after_path)

    before_images = get_images(abs_before_path)
    after_images = get_images(abs_after_path)

    generate_config(BEFORE_CONF, abs_before_path, before_images)
    generate_config(AFTER_CONF, abs_after_path, after_images)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Needs exactly two arguments!'
        print 'First: relative path to the before images folder'
        print 'Second: relative path to the after images folder'
        exit(1)

    # Send all the arguemnts to the main function
    main(sys.argv[1], sys.argv[2])
