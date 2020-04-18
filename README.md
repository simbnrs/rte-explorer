# Installation

Simply git clone, cd into the `rte-explorer` directory and `pip install -e .`

# Usage
To use this package, you will need to add your API keys in a .env fil, encoded in base64.

You will need one key per datasource, on one line each. Example:
```buildoutcfg
PWR_GEN_KEY='YzVmYjhiYTk56h4jNC00ZGFjLTkxNTEtZmNiM597fmNhMjI0OmYyZTdhZjc3Lfgrz4D3Ftnb35DiN2FlLTM2ZDUxMzM0Mzk5Yg=='
```

This package is really early stage, thus only the power generation is available.
The data is retrieved via the `get_data.get_ressource` function, which will be made into a class when other APIs are added.

Don't hesitate to explore the content of the html error if it doesn't work!