# Code written by Umolu John Chukwuemeka
def treat_outliers(df, columns):
    try:
        # create an empty list to store values
        column_names = []
        total_outliers = []
        percentage = []
        least_outlier = []

        # loop through all column list
        for column in columns:
            # finding the 1st quartile
            q1 = df[column].quantile(0.25)

            # finding the 3rd quartile
            q3 = df[column].quantile(0.75)

            # get the column mean and median values
            mean = df[column].mean()
            # median = df[column].median()

            # finding the iqr region
            iqr = q3 - q1

            # finding upper and lower whiskers
            upper_bound = q3 + (1.5 * iqr)
            lower_bound = q1 - (1.5 * iqr)

            # Get the array data for column
            arr1 = df[column]

            # Get the outliers using the upper and lower whiskers
            outliers = arr1[(arr1 <= lower_bound) | (arr1 >= upper_bound)]

            # get the min value of the outliers found
            min_value = round(min(outliers.values)) if len(outliers.values) > 0 else 0

            # calculate the percentage of the outliers found
            percentage_value = round((len(outliers.values) / len(arr1)) * 100, 2) if len(outliers.values) > 0 else 0

            # add values to the list
            column_names.append(column)
            total_outliers.append(len(outliers.values))
            least_outlier.append(min_value)
            percentage.append(f'{percentage_value}%')

            # do this if outliers is less than or equal to 5%
            if round(percentage_value) <= 5 and len(outliers.values) > 0:
                # capping Outliers using IQR Ranges
                df.loc[(df[column] <= lower_bound), column] = lower_bound
                df.loc[(df[column] >= upper_bound), column] = upper_bound

            # do this if outliers is greater than 5%
            elif round(percentage_value) > 5 and len(outliers.values) > 0:
                # replacing outlier values with the mean or median value
                df.loc[(df[column] <= lower_bound), column] = mean
                df.loc[(df[column] >= upper_bound), column] = mean

        # create a new dictionary
        table_dict = {'Column Name': column_names, 'Number of Outliers': total_outliers, 'Least Value': least_outlier,
                      'Percentage Value': percentage}

        # return the table dictionary
        return table_dict, df[columns]

    except BaseException as error:
        print('\nPlease ensure the dataframe name is correct and the target column is entered correctly: {}'.format(error))


def best_model(df, column):
    # ensure that the target column is in the dataset columns
    if column not in df.columns:
        print('\nError: Please enter a valid dataframe column name to proceed.')
    else:
        try:
            # list of numerical data types to look out for
            numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

            # suggest regression model
            if df[column].dtype in numerics and len(df[column].unique()) >= len(df[column]) / 100:
                return f"\nModel Suggestion:\nUse Regression Model => Numerical: {df[column].dtype}," \
                    f" Categorical: {df[column].dtype == 'category'}," \
                    f" Unique Values: {len(df[column].unique())}, Total Value: {len(df[column])}"

            # suggest classification model
            else:
                return f"\nModel Suggestion:\nUse Classification Model => Numerical: {df[column].dtype}," \
                    f" Categorical: {df[column].dtype == 'category'}," \
                    f" Unique Values: {len(df[column].unique())}, Total Value: {len(df[column])}"

        except BaseException as error:
            print('\nError: Please enter a valid dataframe column name to proceed: {}'.format(error))



