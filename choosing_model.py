# Code written by Umolu John Chukwuemeka
# import libraries
import JUStat as js
import pandas as pd

# create an empty dataframe
df = pd.DataFrame()


def suggest_model():
    # make dataframe accessible from outside
    global df

    # enter the target columns name
    target_variable = input('Please enter the target column name: ')

    # ensure that the target column is in the dataset columns
    if target_variable not in df.columns:
        # display error message
        print('\nError: Please enter a valid target column name to proceed.')

        # call last text input function
        suggest_model()

    # do this instead
    else:
        # check the best model to use
        result = js.best_model(df, target_variable)

        # display best model result
        print(result)


def enter_filename():
    # make dataframe accessible from outside
    global df

    # enter the target columns name
    filename = input('Please enter the CSV dataset filename: ')

    try:
        # read CSV file to dataframe
        df = pd.read_csv(filename) if '.csv' in filename else pd.read_csv(f'{filename}.csv')

        # call the next text input function
        suggest_model()

    except BaseException as error:
        # display error message
        print('\nError: Please enter a valid CSV dataset filename: {}'.format(error))

        # call last text input function
        enter_filename()


# call the first text input function
enter_filename()


