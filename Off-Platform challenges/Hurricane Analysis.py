# names of hurricanes

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


def update_damage(list_of_damage):
    damages_update = []
    for entry in list_of_damage:
        if 'M' in entry:
            entry = entry.replace('M', '')
            entry_to_float = float(entry) * (conversion['M'])
            damages_update.append(entry_to_float)
        elif 'B' in entry:
            entry = entry.replace('B', '')
            entry_to_float = float(entry) * (conversion['B'])
            damages_update.append(entry_to_float)
        else:
            damages_update.append(entry)

    return damages_update


# test function by updating damages
damages = update_damage(damages)


# 2
# Create a Table
def create_dictionary(hurr_names, hurr_months, hurr_years, hurr_max_sustained_winds,
                      hurr_areas_affected, hurr_damages, hurr_deaths):
    hurricans = {}
    hurricans_len = len(hurr_names)
    for i in range(hurricans_len):
        hurricans[hurr_names[i]] = {
            "Name": hurr_names[i],
            "Month": hurr_months[i],
            "Year": hurr_years[i],
            "Max Sustainled Wind": hurr_max_sustained_winds[i],
            "Areas Affected": hurr_areas_affected[i],
            "Damage": hurr_damages[i],
            "Deaths": hurr_deaths[i]
        }
    return hurricans


# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages,
                               deaths)
print(hurricanes)


# 3
# Organizing by Year
def create_year_dictionary(hurricanes):
    """Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary."""
    hurricanes_by_year = dict()
    for cane in hurricanes:
        current_year = hurricanes[cane]['Year']
        current_cane = hurricanes[cane]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year


# create a new dictionary of hurricanes with year and key
hurricanes_by_year = create_year_dictionary(hurricanes)
print(hurricanes_by_year[1932])


# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes):
    """Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys."""
    affected_areas_count = {}
    for cane in hurricanes:
        for area in hurricanes[cane]['Areas Affected']:
            if area not in affected_areas_count:
                affected_areas_count[area] = 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count


# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_affected_areas(hurricanes)
print(affected_areas_count)

# 5
# Calculating Maximum Hurricane Count
def calculate_most_affected_area(affected_areas):
    max_area = "Louisiana America"
    max_count = 1
    for affected_area in affected_areas:
        if affected_areas.get(affected_area) > max_count:
            max_area = affected_area
            max_count = affected_areas.get(affected_area)
    return max_area, max_count

most_affected_area = calculate_most_affected_area(affected_areas_count)
print(most_affected_area)
# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
def calculate_max_vixtims(list_of_hurricanes):
    max_mortality_cane = "Cuba I"
    max_mortality = 0
    for cane in list_of_hurricanes:
        if hurricanes[cane]['Deaths'] > max_mortality:
            max_mortality_cane = cane
            max_mortality = hurricanes[cane]['Deaths']
    return max_mortality_cane, max_mortality

# find highest mortality hurricane and the number of deaths
most_victims_hurricane = calculate_max_vixtims(hurricanes)
print(most_victims_hurricane)
# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
