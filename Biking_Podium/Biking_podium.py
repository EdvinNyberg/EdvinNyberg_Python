import datetime

def convert_time(seconds): # Function that converts time in seconds to a string in the format HH:MM:SS
    return str(datetime.timedelta(seconds=seconds)) # Return the time in the format HH:MM:SS as a string

def read_csv(file_path): # Function that reads a csv file and returns a list of lines
    with open(file_path, 'r') as file: # Open the file in read mode and assign it to the variable file
        lines = file.readlines() # Read all lines in the file and store them in a list
    return lines # Return the list of lines

def parse_csv(lines): # Function that parses the csv file and returns a list of tuples
    data: list = [] # Create an empty list to store the data
    for line in lines[0:]: # Iterate over the lines in the file
        name, country, time = line.strip().split(',') # Split the line by comma and unpack the values into name, country and time
        data.append((name, country, float(time))) # Append a tuple with the name, country and time to the data list
    return data # Return the list of tuples

def get_top_3_times(data): # Function that returns the top 3 times
    sorted_data: list = sorted(data, key=lambda x: x[2]) # Sort the data by the time in ascending order
    return sorted_data[:3] # Return the top 3 times

def main(): # Main function that reads the csv file, parses the data, gets the top 3 times and prints them
    file_path = r'C:\Users\Edvin\Python Projects\Lektioner\Lektion_5\Biking_Podium\TT_Olympic_2024_Men.csv' # Path to the csv file
    lines = read_csv(file_path) # Read the csv file and get a list of lines
    data: list = parse_csv(lines) # Parse the data from the csv file
    top_3: list = get_top_3_times(data) # Get the top 3 times from the data
    
    print("These are the top 3 contenders:")
    for name, country, time in top_3: # Iterate over the top 3 times and print them in the correct format
        formatted_time: str = convert_time(time) # Convert the time to a string in the format HH:MM:SS
        print(f'{name} ({country}): {formatted_time}') # Print the name, country and time in the format "Name (Country): HH:MM:SS"

if __name__ == "__main__":
    main()