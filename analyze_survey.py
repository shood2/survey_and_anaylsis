import json
import survey

def get_survey_data():
    file = open("dump.json", "r")
    survey_results = json.load(file)
    file.close()
    return survey_results

def average_age(survey_results):
    sum = 0
    for result in survey_results:
        sum += int(result['age'])

    return sum / len(survey_results)

data = get_survey_data()
print(average_age(data))
conduct_survey()
