class MyConfig:

    environments_URLS = {
        "dev": ["https://path/to/dev/env/", "https://path/to/dev/env/admin/"],
        "stage": ["https://path/to/stage/env/", "https://path/to/dev/stage/admin/"],
        "prod": ["https://www.ebay.com/", "https://www.ebay.com/admin/"],
    }

    ENV_in_use = "prod"

    wait_timeout = 45
