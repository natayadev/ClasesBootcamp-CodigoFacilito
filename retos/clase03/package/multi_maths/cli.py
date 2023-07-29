""" Cli file for Multi_Maths Package """
# __doc__ (Cli file for testing modules and packages)

import argparse
from typing import Sequence

from multi_maths.core import Core
from multi_maths.__version__ import __version__


def main(argv: Sequence[str] | None = None) -> int:
    """
       Main function, prepare console arguments and args,
       returns functions values
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('module', type=str, help='')
    parser.add_argument('submodule', type=str, help='')
    parser.add_argument('data', nargs='+', type=int, help='')
    parser.add_argument('-l', '--language', default='en', help='')
    parser.add_argument('-r', '--response', default='text', help='')
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args_values = parser.parse_args(argv)

    core = Core()  # noqa: F405

    if args_values.language.lower() == 'es':
        core.set_lang('es')
    else:
        core.set_lang('en')

    if args_values.response.lower() == 'text':
        core.set_response('text')
    else:
        core.set_response('digit')

    data_list = list(args_values.data)

    try:
        return core.run(args_values.module.lower(),
                        args_values.submodule.lower(),
                        data_list)
    except ValueError as error:
        print(error)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
