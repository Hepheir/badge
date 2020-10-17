from python.download import save_at

from python.acmicpc.net import problem

for problem_id in range(1000, 1010 +1):
    url = problem(problem_id)
    file_path = f'svg/acmicpc.net/{problem_id}.svg'
    save_at(url, file_path)
