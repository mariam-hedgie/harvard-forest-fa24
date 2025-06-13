#PURPOSE: Analyze eddy flux data from Harvard Forest

#Required libraries
import numpy as np
import matplotlib.pyplot as plt


def is_leap_year(year):
    '''
    determines if a year is a leap year or not:
    a year is a leap year if it is divisible by 4 but not 100
    or divisible by 400

    parameters: year(int): year to be checked
    returns: boolean: True if leap year, False if not
    '''
    if (year % 100 != 0 and year % 4 == 0): #if yr is divisible by 4 but not by 100
        return True
    elif (year%400 == 0): #if yr is divisible by 400
        return True
    else:
        return False #if neither condition are satisfied it is not a leap yr
    

def readdata(filename):
    '''
    Read in Harvard Forest data
    Parameters: filename (str): name of file to be read
    Returns: data (NumPy Array): array containing data 
    '''
    # Purpose: Read in Harvard Forest data

    #reads CSV file into a NumPy array, skipping the 1st row (header)
    data = np.genfromtxt(filename, delimiter= ',', skip_header=1)
    return data


def fractional_years(hf):
    '''
    calculates fractional years from a given dataset.
    Parameters: 
    hf (NumPy array): 2D Array of csv file that was read
    Returns: 
    fractional_years_array (NumPy array): 1D Array of fractional years
    '''

    #extract year and day from csv file
    year = hf[:, 0]
    day = hf[:, 2]   

    #create an empty np array to store fractional years    
    fractional_years_array = np.empty(len(year))

    #calculate fractional year by iterating over each year
    for i in range(len(year)):

        #determine total number of days for a leap year and non-leap year
        if is_leap_year(year[i]):
            total_days = 366
        elif is_leap_year(year[i]) == False:
            total_days = 365
        
        #calculate fractional year as sum of year and days as a fraction of all the days in the year
        fractional_years_array[i] = year[i] + ((day[i] - 1)/total_days)

    #return the array of fractional years
    return fractional_years_array

def summarizedata(hf):
    '''
    creates a plot of the CO2 data as a time series and calculates summary statistics about the data
    parameters: 
    hf (NumPy array): 2D Array of csv file that was read
    returns: 
    observation_array (NumPy array): a 1d array containing the summary statistics
    '''
    # Read in data from the Harvard Forest
    co2_flux = hf[:, 3]

    #calculate the fractional years for the time series plot
    fractional_year = fractional_years(hf)

    # Create a time series scatter plot of the co2 flux data
    plt.figure(figsize = (12, 6))
    plt.scatter(fractional_year, co2_flux, color = 'b', s=8)
    plt.xlabel('Year as Fraction')
    plt.ylabel('CO2 Flux')
    plt.title('CO2 Flux Data as Time Series for Harvard Forest')
    plt.savefig('timeseries.png')
    
    plt.show() #comment out before submitting

    # Find the number of data points
    total_points = len(co2_flux)

    #Find the mean of the data
    mean = np.round(np.mean(co2_flux), 3)

    # Find the 25th percentile of the data points
    q_25 = np.round(np.quantile(co2_flux, 0.25), 3)

    # Find the 75th percentile of the data points
    q_75 = np.round(np.quantile(co2_flux, 0.75), 3)

    #create an array of all the summary statistics
    observation_array = np.array([total_points, mean, q_25, q_75])

    # Return the number of data points, the mean, 
    # the 25th percentile, and the 75th percentile
    return observation_array

def missingdata(hf):
    '''
    finds the percentage of missing data points in each year
    parameters:
    hf (NumPy array): 2D Array of csv file that was read
    returns:
    percentages (list): list of percentages of missing days per year
    '''
    
    # Read in the data from the Harvard Forest
    year = list(hf[:,0])

    #creates a list of all years from min to max 
    years = [i for i in range(int(min(year)), int(max(year)+1))]

    # Find the percentage of data in each year that are missing

    #creates an empty list to store percentage of data in each year that are missing
    percentages =[]

    #calculates missing data percent per eyar
    for j in years:
        #only look at data for the current year
        current_year_data = [hf[i] for i in range(len(hf)) if hf[i][0]== j]
        no_of_days = len(current_year_data)

        #determine total days in the year if leap year or not
        total_days = 366 if is_leap_year(j) else 365

        #calculation for missing percentage of days rounded to 3 decimal places
        missing_percentages = (1-(no_of_days/total_days))*100

        #add the percent for the current year to the list of all percentages
        percentages.append(round(missing_percentages, 3))

    # Create a bar plot showing the percentage of data that are
    # missing in each year
    plt.figure(figsize = (12, 6))
    plt.bar(years, percentages, color = 'b')
    plt.xlabel('Year')
    plt.ylabel('Percentage of Missing Days')
    plt.xticks(years, rotation = 45)
    plt.title('Percentage of Days Missing Data per Year')
    plt.savefig('missingdata.png')    

    # Display the plot
    plt.show() #comment out when submitting

    # Return the list of percentages of missing days in each year
    return percentages
    
def seasonalcycle(hf):
    '''
    calculates average co2 fluc per month for each year and plots it for 1995 to 2000
    parameters:
    hf (NumPy array): 2D Array of csv file that was read
    returns:
    average_flux_array (NumPy array): 2d array of years and average co2 flux per month
    '''
   
    # Read in the data from the Harvard Forest
    year = list(hf[:, 0])
    #creates a list of all years from min to max 
    years = [i for i in range(int(min(year)), int(max(year)+1))]
    #creates a list of months
    months = list(range(1, 13))

    #creates a list to store average co2 flux per month for each year
    total_average_flux = []

    #calculates average co2 flux per month for each year
    for j in years:
        #use data for current year
        current_average_flux = []
        current_year_data = np.array([hf[i] for i in range(len(hf)) if hf[i][0] == j])

        for month in months:
            #use data for current month
            current_month_data = np.array([current_year_data[i][3] for i in range(len(current_year_data)) if current_year_data[i][1] == month])

            #calculate the average flux per month and add nan for missing data
            if len(current_month_data) != 0:
                current_average_flux.append(np.mean(current_month_data))
            else:
                current_average_flux.append(np.nan)
        
        #add averages for current year to the main list of averages
        total_average_flux.append(current_average_flux)

    #convert the list of averages into a np array
    average_flux_array = np.array(total_average_flux)


    # Plot the average fluxes by month in several different years
    plt.figure(figsize = (12,10))
    for i, year in enumerate(years):
        if year >= 1995.0 and year <= 2000.0:
            plt.plot(months, average_flux_array[i], label = f'{int(year)}')
            plt.xlabel('Month')
            plt.ylabel('Average CO2 Flux')
            plt.title('Average CO2 Flux per Month (1995-2000)')
            plt.xticks(range(1, 13))
            plt.legend(title="Year")
            plt.savefig('monthlyflux.png')
    
    # Display the plot
    plt.show()

    # Return the array of average co2 flux per month for each year
    return average_flux_array


def HFregression(hf):
    '''
    creates a regression model for co2 flux and visualizes the outputs and variable contributions
    parameters:
    hf (NumPy array): 2D Array of csv file that was read
    returns:
    list: list of regression coefficients (B) and model estimates of co2 flux values (estimate_flux)
    '''
 
    # Read in the data from the Harvard Forest
    co2_flux = hf[:,3]
    co2_flux_array = np.array(hf[:, 3])

    #create a matrix with a constant term of 1 and all the contributing variables
    X = np.array([[1, hf[i][4], hf[i][5], hf[i][6], hf[i][7]] for i in range(len(hf))])

    #calculate the regression coefficients using the equation given
    B = X.T@X
    B = np.linalg.inv(B)
    B = B @ X.transpose()
    B = B @ co2_flux_array

    #estimate the co2 flux using the model
    estimate_flux = X@B
    
    #calculate the fractional year using the year and day data from the file
    year = hf[:, 0]
    day = hf[:, 2]
    fractional_year = year + (day/365)
    
    #plot the time series of observed vs. model estimate co2  flux
    plt.figure(figsize=(12,10))
    plt.subplot(2, 1, 1)
    plt.plot(fractional_year, co2_flux_array)
    plt.plot(fractional_year, estimate_flux)
    plt.title('Time Series of Model Fit')
    plt.xlabel('Date')
    plt.ylabel('CO2 Flux')
    plt.legend(['Data', 'Model'])

    #calculate the correlation coefficient and display it on the graph
    r = np.corrcoef(co2_flux, estimate_flux)
    plt.text(2007, 15, f'r = {round(r[0][1], 2)}')
    
    #calculate the contribution of each variable and store it in lists
    all_variable_contributions = [[] for _ in range(5)]  
    for i in range(len(X)):
        for j in range(5):  
            all_variable_contributions[j].append(X[i][j] * B[j])
    
    #assign all variable contributions from the above calculations
    intercept, net_radiation, air_temp, water_vapor, wind_speed = all_variable_contributions

    #plot contributions of each variable with time
    plt.subplot(2, 1, 2)
    plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
    plt.plot(fractional_year, intercept)
    plt.plot(fractional_year, net_radiation)
    plt.plot(fractional_year, air_temp)
    plt.plot(fractional_year, water_vapor)
    plt.plot(fractional_year, wind_speed)
    plt.title('Contribution of Each Variable over time')
    plt.xlabel('Date')
    plt.ylabel('CO2 flux')
    plt.legend(['Intercept', 'Net Radiation', 'Air Temperature', 'Water Vapor', 'Wind Speed'])
    plt.savefig('modelcomparison.png')
    plt.show()

    #return the regression coefficients and the mdoel estimate of co2 flux
    return [B, estimate_flux]


def averagecarbon(hf, modelest):
    '''
    calculate the average carbon flux from the model for each year of the simulations.
    Create a time series plot showing carbon flux per year

    parameters:
    hf (NumPy array): 2D Array of csv file that was read
    modelest (NumPy array): 1D array of model estimates of co2 flux

    returns:
    averages(list): list of co2 average values per year
    '''

    #Read in the data from the Harvard Forest
    year = hf[:, 0]
    years = range(int(np.min(year)),int(np.max(year)+1))

    #create a list to store averages per year
    averages = []

    #calculate the average co2 flux per year
    for j in years:
        #gives indices where year from dataet matches current year
        index   = np.where(year==j)
        #calculates the average co2 flux of the current year
        meanco2 = np.mean(modelest[index])
        averages.append(round(meanco2,3))

    #plot the averages per year as a time series
    plt.figure()
    plt.scatter(years, averages, color = 'b')
    plt.title('Time Series of Model Averages')
    plt.xlabel('Date')
    plt.ylabel('Model CO2 Flux Averages')
    plt.axhline(y=0, color = 'black')
    plt.savefig('avgflux.png')

    plt.show()

    #returns a list of averages per year of co2 flux
    return averages

#filename = '/Users/mariamhusain/Desktop/harvard_forest.csv'
#hf = readdata(filename)



if __name__ == "main":
    filename = 'harvard_forest.csv'
    hf = readdata(filename)
    ndata,hfmean,hf25,hf75 = summarizedata(hf)
    missing_data = missingdata(hf)
    month_means = seasonalcycle(hf)
    betas, modelest = HFregression(hf)
    means = averagecarbon(hf, modelest)

