#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error)
    """

    cleaned_data = []

    ### your code goes here
    for prediction, age, net_worth in zip(predictions, ages, net_worths):
        age = age[0]
        net_worth = net_worth[0]
        error = (prediction[0] - net_worth)**2

        cleaned_data.append((age, net_worth, error))

    cleaned_data.sort(key = lambda val: val[2])

    from math import floor
    top90 = int(floor(len(cleaned_data) * 0.9))
    cleaned_data = cleaned_data[0:top90]

    return cleaned_data
