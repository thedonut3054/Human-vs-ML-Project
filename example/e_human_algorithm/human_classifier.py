def human_classify(petal_width):
    if petal_width < 0.6:
        return 'Iris-setosa'
    elif petal_width < 1.6:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'
