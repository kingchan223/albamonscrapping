from albamon import extract_jobs as get_albamon_jobs

from save import save_to_file

albamon_jobs = get_albamon_jobs()

jobs = albamon_jobs

save_to_file(jobs)
