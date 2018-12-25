from Iris import Iris

def normalizeData(iris_data):

    min_sep_len = iris_data[0].sepal_length
    max_sep_len = iris_data[0].sepal_length
    min_sep_wid = iris_data[0].sepal_width
    max_sep_wid = iris_data[0].sepal_width
    min_pet_len = iris_data[0].pedal_length
    max_pet_len = iris_data[0].pedal_length
    min_pet_wid = iris_data[0].pedal_width
    max_pet_wid = iris_data[0].pedal_width

    for iris in iris_data:
        if min_sep_len > iris.sepal_length:
            min_sep_len = iris.sepal_length
        elif max_sep_len < iris.sepal_length:
            max_sep_len = iris.sepal_length

        if min_sep_wid > iris.sepal_width:
            min_sep_wid = iris.sepal_width
        elif max_sep_wid < iris.sepal_width:
            max_sep_wid = iris.sepal_width

        if min_pet_len > iris.pedal_length:
            min_pet_len = iris.pedal_length
        elif max_pet_len < iris.pedal_length:
            max_pet_len = iris.pedal_length

        if min_pet_wid > iris.pedal_width:
            min_pet_wid = iris.pedal_width
        elif max_pet_wid < iris.pedal_width:
            max_pet_wid = iris.pedal_width

    for iris in iris_data:
        iris.sepal_length = (iris.sepal_length - min_sep_len) / (max_sep_len - min_sep_len)
        iris.sepal_width = (iris.sepal_width - min_sep_wid) / (max_sep_wid - min_sep_wid)
        iris.pedal_length = (iris.pedal_length - min_pet_len) / (max_pet_len - min_pet_len)
        iris.pedal_width = (iris.pedal_width - min_pet_wid) / (max_pet_wid - min_pet_wid)

    max = [max_sep_len, max_sep_wid, max_pet_len, max_pet_wid]
    min = [min_sep_len, min_sep_wid, min_pet_len, min_pet_wid]

    return iris_data, max, min
