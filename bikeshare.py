import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    city = ''
    while city.lower() not in cities:
        city = str(input('Please choose city from Chicago, New York City or Washington:')).lower()
        if city in cities:
            break
        else:
            print('Wrong input,please try again.\n')
    #print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month = ''
    while month.lower() not in months:
        month = str(input('Please input month from January to June or all:')).lower()
        print(month)
        if month in months:
            break
        else:
            print('Wrong input,please try again.\n')
    #print(month)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    day = ''
    while day.lower() not in days:
        day = str(input('Please enter a day from Monday to Sunday or all:')).lower()
        if day in days:
            break
        else:
            print('Wrong input,please try again.\n')
    #print(day)

    print('-'*40)
    #print(city, month, day)
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

    files_dic = {'chicago':'chicago.csv',
                 'new york city':'new_york_city.csv',
                 'washington':'washington.csv'}
    filename = files_dic.get(city)
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if month != 'all':#filter a specific month
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month]
        
    if day != 'all':#filter a specific day
        df = df[df['Start Time'].dt.day_name() == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #convert to date time
    df['Month'] = df['Start Time'].dt.month
    common_month = df['Month'].mode()[0]
    print('Common month is: ',months[common_month-1].title())
 

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #print(df['day_of_week'])
    common_day = df['day_of_week'].mode()[0]
    print('Common day is: ',common_day)

    # TO DO: display the most common start hour
    df['hour_of_day'] = df['Start Time'].dt.hour
    #print(df['hour_of_day'])
    common_hour = df['hour_of_day'].mode()[0]
    print('Common hour is: ',common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Common start station is: ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Common end station is: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End Station'] = df['Start Station'] +' to '+ df['End Station']
    common_strt_end_station = df['Start_End Station'].mode()[0]
    print('Common trip is from',common_strt_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('Total trips duration:',total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average trips duration:',mean_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    if city =='washington':
        return
    else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print('user_types:\n',user_types)

        # TO DO: Display counts of gender
        users_gender = df['Gender'].value_counts()
        print('users_gender:\n',users_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
    
    print('earliest_year :',earliest_year)
    print('recent_year :',recent_year)
    print('common_year :',common_year)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while (view_data.lower() == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
