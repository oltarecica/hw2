#7
def total_registered_cases(data, country):
    return sum(data.get(country, []))
#8
def total_registered_cases_per_country(data):
    totals= {}
    for country, cases in data.items():
        totals[country] = sum(cases)
    return totals
#9
def country_with_most_cases(data):
    totals = total_registered_cases_per_country(data)
    return max(totals, key=totals.get)
