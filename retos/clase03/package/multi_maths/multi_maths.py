""" Multi_Maths file for Multi_Maths Package """
# __doc__ (Multi_Maths file for testing modules and packages)

import os
from multi_maths.core import Core
from multi_maths.info import Info


def print_examples(code_example, example, result):
    """
       Format the examples prints
    """

    print(f'{code_example} >>>{example} \n{result}\n')


def print_init_example(code_example_init, lang, response):
    """
       Format the inits for examples prints
    """

    result = f"{code_example_init}\n"
    result += "core = Core()\n"
    result += f"core.set_lang('{lang}')  # en, es\n"
    result += f"core.set_response('{response}')  # digit, text\n"
    print(result)


def main():  # pylint: disable=R0915
    """
       Main function, returns examples, info and more
    """

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print('-' * 49 + ' \n')
    print('              Multi Maths Package  \n')
    print('-' * 49 + ' \n')
    language = input('(1) English - (2) Español: ')

    if language == '2':
        language = 'es'
    else:
        language = 'en'

    core = Core()
    core.set_lang(language)  # Valid options: en, es
    core.set_response('digit')  # Valid options: digit, text

    code_example = core.lang["LANG"]["LANG_CODE_EXAMPLE"]
    code_example_init = core.lang["LANG"]["LANG_CODE_EXAMPLE_INIT"]

    print(f'\n>>> {core.lang["LANG"]["LANG_RESPONSE_ONLY_VALUE"]}')
    print_init_example(code_example_init, language, 'digit')
    print_examples(code_example, "core.run('ari', 'add', (2, 3, 4))",
                   core.run('ari', 'add', (2, 3, 4)))

    core.set_response('text')
    print_init_example(code_example_init, language, 'text')

    # MM_Arithmetic()
    print(f'\n>>> {core.lang["LANG"]["LANG_ARITH_TITLE"]}')
    print_examples(code_example, "core.run('ari', 'add', (2, 3, 4))",
                   core.run('ari', 'add', (2, 3, 4)))
    print_examples(code_example, "core.run('ari', 'sub', (4, 3))",
                   core.run('ari', 'sub', (4, 3)))
    print_examples(code_example, "core.run('ari', 'mul', (3, 3, 2))",
                   core.run('ari', 'mul', (3, 3, 2)))
    print_examples(code_example, "core.run('ari', 'div', (9, 3))",
                   core.run('ari', 'div', (9, 3)))
    print_examples(code_example, "core.run('ari', 'mod', (21, 200))",
                   core.run('ari', 'mod', (21, 200)))
    print_examples(code_example, "core.run('ari', 'mod', (32, 517))",
                   core.run('ari', 'mod', (32, 517)))
    print_examples(code_example, "core.run('ari', 'exp', (3, 3))",
                   core.run('ari', 'exp', (3, 3)))
    print_examples(code_example, "core.run('ari', 'flo', (9, 3))",
                   core.run('ari', 'flo', (9, 3)))

    # MM_Geometry()
    print(f'\n>>> {core.lang["LANG"]["LANG_GEOM_TITLE"]}')
    print_examples(code_example, "core.run('geo', 'ca', (4,))",
                   core.run('geo', 'ca', (4,)))
    print_examples(code_example, "core.run('geo', 'cc', (5,))",
                   core.run('geo', 'cc', (5,)))
    print_examples(code_example, "core.run('geo', 'ta', (5,5))",
                   core.run('geo', 'ta', (5, 5)))
    print_examples(code_example, "core.run('geo', 'tp', (5, 5, 5))",
                   core.run('geo', 'tp', (5, 5, 5)))
    print_examples(code_example, "core.run('geo', 'sa', (5, 5))",
                   core.run('geo', 'sa', (5, 5)))
    print_examples(code_example, "core.run('geo', 'sp', (5,))",
                   core.run('geo', 'sp', (5,)))
    print_examples(code_example, "core.run('geo', 'ra', (4, 2))",
                   core.run('geo', 'ra', (4, 2)))
    print_examples(code_example, "core.run('geo', 'rp', (4, 2))",
                   core.run('geo', 'rp', (4, 2)))
    print_examples(code_example, "core.run('geo', 'pa', (4, 3))",
                   core.run('geo', 'pa', (4, 3)))
    print_examples(code_example, "core.run('geo', 'pp', (4, 3))",
                   core.run('geo', 'pp', (4, 3)))

    # MM_Statistics()
    data_list = [8, 17, 41, 3, 21, 30, 11, 9]
    print(f'\n>>> {core.lang["LANG"]["LANG_STAT_TITLE"]}')
    print_examples(code_example, "core.run('stat', 'sd', (data_list,))",
                   core.run('stat', 'sd', (data_list,)))
    print_examples(code_example, "core.run('stat', 'sd', (data_list, 7))",
                   core.run('stat', 'sd', (data_list, 7)))
    print_examples(code_example, "core.run('stat', 'mean', (data_list,))",
                   core.run('stat', 'mean', (data_list,)))
    print_examples(code_example, "core.run('stat', 'med', (data_list,))",
                   core.run('stat', 'med', (data_list,)))
    print_examples(code_example, "core.run('stat', 'mode', (data_list,))",
                   core.run('stat', 'mode', (data_list,)))

    print('\n' + ('-' * 49) + '\n')
    view_credits = input(core.lang["LANG"]["LANG_CREDITS"])

    if view_credits.lower() == 'y':
        print('\n')
        Info().show_credits(True)
