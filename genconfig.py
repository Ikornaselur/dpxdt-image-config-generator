import sys
from os.path import abspath

from utils import (
    generate_title_from_file_name, writeline, lookahead, get_pngs)


BEFORE_CONF = 'before.json'
AFTER_CONF = 'after.json'


def config_entry(name, path):
    """Return a string with the configuration entry based on name and path"""
    tab = '    '
    no_ext = '.'.join(name.split('.')[:-1])
    fancy_title = generate_title_from_file_name(no_ext)

    string = tab + '{\n'
    string += 2*tab + '"name": "{}",\n'.format(fancy_title)
    string += 2*tab + '"run_failed": false,\n'
    string += 2*tab + '"image_path": "{}/{}.png",\n'.format(path, no_ext)
    string += 2*tab + '"log_path": "{}/{}.txt"\n'.format(path, no_ext)
    string += tab + '}'
    return string


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

    before_images = get_pngs(abs_before_path)
    after_images = get_pngs(abs_after_path)

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
