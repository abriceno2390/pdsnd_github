import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
#Refactoring change1
# Get user input for city.
    city = input("Please select city, Chicago, New York City or Washington\n")

    while city.lower() != "Chicago".lower() and city.lower() != "New York City".lower() and city.lower() != "Washington".lower():
          city.lower() == input("Please input, Chicago, New York City or Washington\n")

#print("Your selected city is:", city.upper())

# Get user input for months.

    month = input("Please select a month, all, january, february, march, april, may or june\n")

    while month.lower() != "all".lower() and month.lower() != "january".lower() and month.lower() != "february".lower() and month.lower() != "march".lower() and month.lower() != "april".lower() and month.lower() != "may".lower() and month.lower() != "june".lower():
        month.lower() == input("Please select a month, all, january, february, march, april, may or june\n") 
    
#print("Your selected month is:", month.upper()) 

# Get user input for day.

    day = input("Please select a day from this options, all, monday, tuesday, wednesday, thursday, wednesday, thursday, friday, saturday, sunday\n")   

    while day.lower() != "all".lower() and day.lower() != "sunday".lower() and day.lower() != "monday".lower() and day.lower() != "tuesday".lower() and day.lower() != "wednesday".lower() and day.lower() != "thursday".lower() and day.lower() != "friday".lower() and day.lower() != "saturday".lower() and day.lower() != "sunday".lower():
        day.lower() == input("Please select one of the following options, all, monday , tuesday, wednesday, thursday, wednesday, thursday, friday, saturday, sunday\n")
    
#print("Your selected day is:", day.upper())
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])

    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    
    #convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #creating a month column
    df['month'] = df['Start Time'].dt.month
     
    #creating a hour column
    
    df['hour'] = df['Start Time'].dt.hour
    
     #creating day of week column
    df['day_week'] = df['Start Time'].dt.day_name()
     #changing day_week column to lower case.
    df['day_week'] = df['day_week'].str.lower()
    
    #condition to check if a specific month was chosen.    
    if month.lower() != "all".lower():
        months = ['january','february','march','april','may','june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
        pop_month = month
    else:
        pop_month = df['month'].mode()[0]
        
        
    
    # TO DO: display the most common day of week
    
   
    
    #condition to check if a specific day was chosen.
    if day.lower() != "all".lower():
        df= df[df['day_week'] == day.lower()]
        pop_day = day
    else:
        pop_day = df['day_week'].mode()[0]

    # TO DO: display the most common start hour
            
    pop_hr = df['hour'].mode()[0]
    
        
    
    #return pop_month, pop_day, pop_hr,print("\nThis took %s seconds." % (time.time() - start_time)),print('-'*40)
    return pop_month,pop_day,pop_hr ,print("\nThis took %s seconds." % (time.time() - start_time)),print('-'*40)

def station_stats(df,month,day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #creating a month column
    df['month'] = df['Start Time'].dt.month
     
    #creating a hour column
    
    df['hour'] = df['Start Time'].dt.hour
    
     #creating day of week column
    df['day_week'] = df['Start Time'].dt.day_name()
     #changing day_week column to lower case.
    df['day_week'] = df['day_week'].str.lower()
    
    
    #condition to check if a specific month was chosen.
    if month.lower() != "all".lower():
        months = ['january','february','march','april','may','june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    
    #condition to check if a specific day was chosen.
    if day.lower() != "all".lower():
        df= df[df['day_week'] == day.lower()]

    # TO DO: display most commonly used start station
    pop_start = df['Start Station'].mode()[0]    


    # TO DO: display most commonly used end station
    pop_end = df['End Station'].mode()[0] 

    # TO DO: display most frequent combination of start station and end station trip

    # get duplicated records
    
    df = df.groupby('Start Station')['End Station'].value_counts().idxmax()



    return pop_start,pop_end, df,  print('-'*40), print("\nThis took %s seconds." % (time.time() - start_time))
    
def trip_duration_stats(df,month,day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    #creating a month column
    df['month'] = df['Start Time'].dt.month
     
    #creating a hour column
    
    df['hour'] = df['Start Time'].dt.hour
    
     #creating day of week column
    df['day_week'] = df['Start Time'].dt.day_name()
     #changing day_week column to lower case.
    df['day_week'] = df['day_week'].str.lower()
    
    
    
    #condition to check if a specific month was chosen.
    if month.lower() != "all".lower():
        months = ['january','february','march','april','may','june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    
    #condition to check if a specific day was chosen.
    if day.lower() != "all".lower():
       df= df[df['day_week'] == day.lower()]   


    # TO DO: display total travel time
    tot_trip = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    
    time_mean = df['Trip Duration'].mean()

    return  tot_trip,time_mean, print('-'*40),  print("\nThis took %s seconds." % (time.time() - start_time))    


def user_stats(df,city,month,day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #creating a month column
    df['month'] = df['Start Time'].dt.month
     
    #creating a hour column
    
    df['hour'] = df['Start Time'].dt.hour
    
     #creating day of week column
    df['day_week'] = df['Start Time'].dt.day_name()
     #changing day_week column to lower case.
    df['day_week'] = df['day_week'].str.lower()
    
    
    
    
    #condition to check if a specific month was chosen.
    if month.lower() != "all".lower():
        months = ['january','february','march','april','may','june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    
    #condition to check if a specific day was chosen.
    if day.lower() != "all".lower():
       df= df[df['day_week'] == day.lower()]   

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender

    try:
        file_gender = df['Gender'].value_counts()
    except city.lower() == 'washington'.lower():
        file_gender = 'Gender 0'
            
    # TO DO: Display earliest, most recent, and most common year of birth

    return user_types,file_gender, print("\nThis took %s seconds." % (time.time() - start_time)), print('-'*40)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(time_stats(df,month))
        
        print('The most frequent month, day and hour are: ',time_stats(df,month,day))
        
        print('The most frequent start station, the most frequent end station and the most common start and end station are respectively:',station_stats(df,month,day))
        print('Total trip duration and trip mean times are:', trip_duration_stats(df,month,day))
        print('Total User Type Counts are: ',user_stats(df,city,month,day))
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
