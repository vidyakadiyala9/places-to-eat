[![Build Status](https://travis-ci.org/TheCognizantFoundry/places-to-eat.svg?branch=master)](https://travis-ci.org/TheCognizantFoundry/places-to-eat)

# Where to Eat?

Places at which we like to eat :knife_fork_plate:

This repository has places to eat for the following cities:

* [Boulder, CO](/locations/boulder)
* [Chicago, IL](/locations/Chicago)
* [Hyderabad, Telangana](/locations/Hyderabad)
* [Newport Beach, CA](/locations/Newport Beach)
* [Orlando, FL](/locations/Orlando)
* [The Woodlands, TX](/locations/The Woodlands)
* [Vernon Hills, IL](/locations/Vernon Hills)

## Contributing

If you would like to add a place to eat, please ensure you follow the following instructions.

* Your addition should be a Markdown text file with the extension `.md`.
* Your addition should be located somewhere within the
  [./locations](/locations/) directory.
* Your addition should be in the format specified by the
  [`PLACE_TO_EAT_TEMPLATE.md`](./PLACE_TO_EAT_TEMPLATE.md) template.

## Linting

To run the linter locally, use the following command:

  ```sh
  python lint_markdown_files.py PLACE_TO_EAT_TEMPLATE.md locations/
  ```
