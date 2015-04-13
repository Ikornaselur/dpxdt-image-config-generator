# dpxdt image config generator

This script takes in paths to a before and after folder with images to use with [dpxdt](https://github.com/bslatkin/dpxdt). 

## Example
```
ᐅ tree before after
before
├── about_page.png
└── front_page_login.png
after
├── about_page.png
└── front_page_login.png

0 directories, 4 files
ᐅ python genconfig.py before after
ᐅ cat before.json
[
    {
        "name": "Front Page Login",
        "run_failed": false,
        "image_path": "/home/axel/Projects/generate_dpxdt_config/before/front_page_login.png",
        "log_path": "/home/axel/Projects/generate_dpxdt_config/before/front_page_login.txt"
    },
    {
        "name": "About Page",
        "run_failed": false,
        "image_path": "/home/axel/Projects/generate_dpxdt_config/before/about_page.png",
        "log_path": "/home/axel/Projects/generate_dpxdt_config/before/about_page.txt"
    }
]
ᐅ cat after.json 
[
    {
        "name": "Front Page Login",
        "run_failed": false,
        "image_path": "/home/axel/Projects/generate_dpxdt_config/after/front_page_login.png",
        "log_path": "/home/axel/Projects/generate_dpxdt_config/after/front_page_login.txt"
    },
    {
        "name": "About Page",
        "run_failed": false,
        "image_path": "/home/axel/Projects/generate_dpxdt_config/after/about_page.png",
        "log_path": "/home/axel/Projects/generate_dpxdt_config/after/about_page.txt"
    }
]
```
