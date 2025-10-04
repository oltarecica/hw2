#ANSWER 4
def has_experience_as(cvs, job_title):
    experienced_users=[]
    for cv in cvs:
        if job_title in cv['jobs']:
            experienced_users.append(cv['user'])
    return experienced_users


#ANSWER 5
def job_counts(cvs):
    job_count_dict={}
    for cv in cvs:
        for job in cv['jobs']:
            if job in job_count_dict:
                job_count_dict[job]+=1
            else:
                job_count_dict[job]=1
    return job_count_dict


#ANSWER 6
def most_popular_job(cvs):
    job_count_dict = job_counts(cvs)
    most_popular = None
    highest_count = 0

    for job, count in job_count_dict.items():
        if count > highest_count:
            most_popular = job
            highest_count = count
    return (most_popular, highest_count)


