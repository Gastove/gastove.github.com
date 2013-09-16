import os
from time import localtime, strftime
import re
import sys

from fabric.api import local, lcd, settings, task
from fabric.utils import puts
from blog_config import INPUT_PATH, OUTPUT_PATH

SETTINGS_FILE = 'blog_config'

# Load paths
ABS_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_SETTINGS_FILE = os.path.join(ABS_DIR_PATH, SETTINGS_FILE)
# ABS_OUTPUT_PATH = os.path.join(ABS_DIR_PATH, os.path.normpath(OUTPUT_PATH))
ABS_INPUT_PATH = os.path.normpath(os.path.join(ABS_DIR_PATH, INPUT_PATH))

__all__ = ['generate_new_post']

@task(alias="np")
def generate_new_post(name = "", extension = ".md",
                      should_open = True, list_existing = False):
    """ Make a new post """
    if list_existing:
        path = _post_path()
        existing_files = os.listdir(path)
        puts("Files in today's folder already:")
        for n in existing_files:
            puts("\t" + n)
    if not name:
        puts("Enter a post name, or 'quit' to exit':")
        name = raw_input("\t:")
    if name == "quit":
        puts("Done!")
        sys.exit(0)
    path = _post_path()
    file_name = _post_name(name) + extension
    full_post_uri = os.path.join(path, file_name)
    if not _name_is_unique(full_post_uri):
        puts("Name not unique!")
        generate_new_post(list_existing = True)
        sys.exit(0)
    puts("Generated new post: ", file_name)
    puts("Stored it in: ", path)
    puts("Adding default metadata")
    _write_default_metadata(name, full_post_uri)
    if should_open:
        puts("Opening new post")
        _open_file(full_post_uri)
    else:
        puts("Complete.")
        sys.exit(0)


def _write_default_metadata(post_real_name, post_full_path):
    # Control structure for metadata order
    def load_config_or_else(key, default):
        """ Try to load a value from config; if not found, return default  """
        try:
            val = getattr(__import__(SETTINGS_FILE, globals(),
                                     locals(), key.upper()), key.upper())
            return val
        except AttributeError:
            return default

    metadata_keys = [
        "Title", "Author", "Date", "Slug", "Category", "Tags", "Summary", "status"
    ]
    metadata_defaults = {
        "Title": post_real_name,
        "Date": strftime("%Y-%m-%d %H:%M", localtime()),
        "Category": "",
        "Tags": "",
        "Slug": os.path.basename(post_full_path[:-3]),
        "Author": "",
        "Summary": "",
        "status": "draft"
    }
    for key in metadata_keys:
        metadata_defaults[key] = load_config_or_else(key, metadata_defaults[key])

    with open(post_full_path, 'w') as pointer:
        for key in metadata_keys:
            pointer.write("%s: %s\n" % (key, metadata_defaults[key]))


def _name_is_unique(candidate_path):
        """ Check if the generated path name is unique or not  """
        return False if os.path.isfile(candidate_path) else True


def _post_path():
    """ Generate the correct post path and make sure it exists  """
    date_string_pieces = strftime("%Y,%m,%d", localtime()).split(",")
    path = "/".join(date_string_pieces)
    abs_path = os.path.join(ABS_INPUT_PATH, 'posts', path)
    if not os.path.exists(abs_path):
        local("mkdir -p %s" % abs_path)
    return abs_path


def _post_name(input_string):
    """ Generate a valid post name  """
    def is_not_empty(entry): return True if entry else False
    first_pass = re.sub("\s", "_", input_string.lower())
    second_pass = "".join(filter(is_not_empty, re.findall("\w", first_pass)))
    third_pass = re.search("([a-z0-9]*_){,4}[a-z0-9]*", second_pass).group()
    timestamp = strftime("%Y-%m-%d", localtime())
    return "_".join([timestamp, third_pass])


def _open_file(filepath):
    """ Open the given file for editing  """
    cmd = "$EDITOR " + filepath
    local(cmd)
