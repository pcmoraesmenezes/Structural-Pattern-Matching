def execute_command(command):

    if command == 'ls':
        print('$ listing files')

    elif command == 'cd':
        print('$ Changing directory')

    else:
        print('$ command not implemented')


def execute_command_using_match_case(command: str):
    match command:
        case 'ls':
            print('$ listing files')

        case 'cd':
            print('$ changing directory')

        case _:
            print('$ command not implemented')


def execute_command_using_avanced_match_case(command: str):
    match command.split():
        case ['ls', path, *_]:
            print('$ listing files from ', path)

        case ['cd', path]:
            print('$ changing directory to ', path)

        case _:
            print('$ command not implemented')


execute_command_using_avanced_match_case('ls /desktop --force')


def execute_command_using_advanced_match_case(command):
    match command.split():
        case['ls' | 'list', *directories]:
            for directory in directories:
                print('$ listing directory from ', directory)

        case ['cd', path]:
            print('$ changing directory to ', path)

        case _:
            print('$ command not implemented')


print()

execute_command_using_advanced_match_case('cd home')
execute_command_using_advanced_match_case('ls home')


def execute_command_using_match_and_guard(command):
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from ', directory)

        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from ', directories[0])

        case ['cd', path]:
            print('$ changing directory to ', path)

        case _:
            print('$ command not implemented')


print()

execute_command_using_match_and_guard('ls /home/desktop /etc')


def execute_command_using_as_and_match_and_guard(command):
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:  # noqa
            for directory in directories:
                print('$ listing ALL directories from ', directory)

            print(f'{the_command=}, {the_list=}')

        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from ', directories[0])

        case ['cd', path]:
            print('$ changing directory to ', path)

        case _:
            print('$ command not implemented')


def execute_command_using_dict(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            for directory in command['directories']:
                print('$ listing ALL directories from ', directory)

        case _:
            print('$ command not implemented')


print()

execute_command_using_dict({'command': 'ls', 'directories': ['/user', '/home']})  # noqa


from dataclasses import dataclass  # noqa


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command_object(command):
    match command:
        case Command(command='ls'):
            for directory in command.directories:
                print('$ listing ALL directories from ', directory)

        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to ', directory)

        case _:
            print('$ Command not implemented')


command1 = Command('ls', ['/users'])
command2 = Command('cd', ['/Users'])

print()

execute_command_object(command1)
execute_command_object(command2)
