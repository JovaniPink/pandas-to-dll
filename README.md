# pandas-to-dll

[![Build Status](https://github.com/measuredstudios/pandas-to-dll/workflows/test/badge.svg?branch=master&event=push)](https://github.com/measuredstudios/pandas-to-dll/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/measuredstudios/pandas-to-dll/branch/master/graph/badge.svg)](https://codecov.io/gh/measuredstudios/pandas-to-dll)
[![Python Version](https://img.shields.io/pypi/pyversions/pandas-to-dll.svg)](https://pypi.org/project/pandas-to-dll/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

> Supply a Pandas DataFrame and we return a DLL string.

## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Add yours!

## Installation

```bash
pip install pandas-to-dll
```

## Example

Showcase how your project can be used:

```python
from pandas_to_dll.example import some_function

print(some_function(3, 4))
# => 7
```

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Lots of items! :)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

1. Fork this repository;
2. Create your branch: `git checkout -b my-new-feature`;
3. Commit your changes: `git commit -m 'Add some feature'`;
4. Push to the branch: `git push origin my-new-feature`.

**After your pull request is merged**, you can safely delete your branch.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more information.

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [de63faa912eb36309c37c94bced64bd2cf3584a3](https://github.com/wemake-services/wemake-python-package/tree/de63faa912eb36309c37c94bced64bd2cf3584a3). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/de63faa912eb36309c37c94bced64bd2cf3584a3...master) since then.

Also inspired by: Pandas github code comments [pandas/io/sql.py](https://github.com/pandas-dev/pandas/blob/master/pandas/io/sql.py#L649). Gist [build_hive_ddl.py](https://gist.github.com/apeletz512/0addbfd698f355828a370a71a7218b9b) by apeletz512. Feature Request [pd.DataFrame.schema iterable](https://github.com/pandas-dev/pandas/issues/28022).
