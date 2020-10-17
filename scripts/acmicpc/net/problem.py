from . import BASE_URL, LOGO

from ...shields.io import makeurl

def problem(problem_id:int):
    problem_id = str(problem_id)
    options = [('style', 'flat-square'),
               ('labelColor', 'E0E0E4'),
               ('link', BASE_URL),
               ('link', f'{BASE_URL}/problem/{problem_id}'),
               ('logo', LOGO)]
    return makeurl('BAEKJOON', problem_id, '428bca', options)