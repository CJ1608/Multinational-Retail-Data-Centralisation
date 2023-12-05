from datetime import datetime
import calendar
import pandas as pd
import string 


class DataCleaning():
    """
    Methods to clean data from each of the data sources. 
    Please see main.py to see how and when these methods are called. 
    """
    def __init__(self, table):
        """
        Initalise each table to be cleaned, passed in from DataExtractor class instance. 

        Args:
            table(pd.dataframe): dataframe that is being cleaned. 
        """
        self.table = table
    
    def __clean_nulls(self, max_null_number):
        """
        If have more than specified number of blank/null entries, drop the row. 

        Args:
            max_null_number: maximum number of null entries a row can have before it is dropped. 
        Returns:
            table (pd.dataframe): dataframe with specific rows removed
        """
        #drop rows that have more than specified number of null values
        self.table.dropna(axis=0, thresh=max_null_number, inplace=True)
        return self.table
    
    def __check_code(self, column_name, code_list, number):
        """
        Check which rows in specified column have values in them that aren't right for that column. Removed unwanted characters from 
        beginning of string and if the row content still isn't in the list of accepted values, drop that row. 

        Args:
            column_name (literal): column to check
            code_list(list[str]): list of accepted values for that column
            number (int): number of str characters to ignore when checking if row contents is in the code_list of accepted values
        Returns:
            table (pd.dataframe): dataframe with specific rows removed. 
        """
        #sort rows in ascending order to tidy up
        self.table.sort_values(by=['index'], inplace=True)
        #initalise empty lists for incorrect values to be added to, used later in method to insert correct details back in
        drop_rows = list()
        index_location = list()
        new_values = list()
        #check if country code is in accepted list
        for index, row in self.table.iterrows():
            if row[column_name] not in code_list:
                # print('Not in codes:', index, row)
                #gets rid of specified number of letters from start of value and check if in accepted list
                if row[column_name][number:] in code_list:
                    # print('In codes:', index, row)
                    index_location.append(index)
                    new_values.append(row[column_name][number:])
                #if still not in accepted list, then add index to drop the row later
                else:
                    # print('Nope', index, row)
                    drop_rows.append(index)
        #update specific rows with new information 
        for i in range(len(index_location)):
            # print('To drop', index_location[i], new_values[i])
            self.table.at[index_location[i], column_name] = new_values[i]       
        # print(drop_rows)
        #drop the rows with incorrect info in
        self.table.drop(drop_rows, axis=0, inplace=True)
        return self.table

    def __check_location(self, column_name, location_list, number):
        """
        Check which rows in specified column have values in them that aren't right for that column. Removed unwanted characters from 
        beginning of string and if the row content still isn't in the list of accepted values, drop that row.

        Args:
            column_name (literal): column to check
            code_list(list[str]): list of accepted values for that column
            number (int): number of str characters to ignore when checking if row contents is in the code_list of accepted values
        Returns:
            table (pd.dataframe): dataframe with specific rows removed. 
        """
        #initalise empty lists for incorrect values to be added to, used later in method to insert correct details back in
        index_location = list()
        new_values = list()
        #check if location in accepted list
        for index, row in self.table.iterrows():
            if row[column_name] not in location_list: 
                # print('Not in locations:', row[column_name])
                #pops first 2 letters off, deals with eeNAME
                if row[column_name][number:] in location_list:
                    # print('In location list:', row[column_name][number:])
                    index_location.append(index)
                    new_values.append(row[column_name][number:])
            else:
                pass
        #update specific rows with new information 
        for i in range(len(index_location)):
            # print(index_location[i], new_values[i])
            self.table.at[index_location[i], column_name] = new_values[i] 
        return self.table

    def __drop_column(self, column_name):
        """
        Drop a named row from table. 

        Args:
            column_name(literal): name of column to be dropped.
        Returns:
            table (pd.dataframe): dataframe with specific column removed. 
        """
        self.table.drop(labels=column_name, axis=1, inplace=True)
        return self.table

    def __clean_card_number(self, column_name):
        """
        Clean specified characters from card number strs, then if str is not numeric, drop the row. 

        Args:
            column_name(literal): name of column to be cleaned.
        Returns:
            table (pd.dataframe): dataframe with specific rows removed. 
        """
        #covert all to string and replace all ?
        self.table[column_name] = self.table[column_name].astype(str)
        self.table[column_name] = self.table[column_name].str.replace('?', '')
        #if row contains text, add index to list
        drop_rows = list()
        for index, row in self.table.iterrows():
            if row[column_name].isnumeric() == False:
                drop_rows.append(index)  
        #drop rows with indices returned in list from for loop
        self.table.drop(drop_rows, axis=0, inplace=True) 
        #check all values are numeric(will get error in code if not)
        self.table[column_name] = pd.to_numeric(self.table[column_name])
        return self.table

    def __clean_date(self, column_name):
        """
        Check if date is in valid format, if not split the str into list of strs and convert written months to numbers and rearrange list elements to match specific format. 

        Args:
            column_name(literal): name of column to be cleaned.
        Returns:
            table (pd.dataframe): dataframe with specific rows removed. 
        """
        #initalise empty lists for incorrect values to be added to, used later in method to insert correct details back in
        index_location = list()
        values = list()
        new_values = list()
        # go through all rows for column, see which are okay and which need amending, check if is a valid date format, if not add index and value to lists
        pattern = "%Y-%m-%d"
        for index, row in self.table.iterrows():
            try:
                res = bool(datetime.strptime(row[column_name], pattern))
            except ValueError:
                index_location.append(index)
                values.append(row[column_name])
                # print('HOW SHOULD BE', index, row[column_name])
        # go through date values in values list, split each one into 3, replace written month with numerical month then reorder
        for date in values:
            date = date.replace("/", " ")
            date = date.split(" ")  
            month_list = list(calendar.month_name) 
            found_month = False
            for i in range(len(date)):
                element = date[i]
                if element in month_list:
                    month_number = str(list(calendar.month_name).index(element))
                    #change order of dates to Y-M-D
                    if len(month_number) == 1:
                        month_number = '0' + month_number
                    # print('before', date)
                    if i == 0:
                        # format =  MM YYYY DD to YMD
                        date = str(date[1]) + "-" + str(month_number) + "-" + str(date[2])
                        found_month = True
                        # print('after 1', date)
                    elif i == 1:
                        # format =  YYYY MM DD to YMD
                        date = str(date[0]) + "-" + str(month_number) + "-" + str(date[2])
                        found_month = True
                        # print('after 2', date)
                    break
            # assume it's format YYYY MM DD with no month conversion
            if not found_month:
                # print(date)
                date = str(date[0]) + "-" + str(date[1]) + "-" + str(date[2])
            #add updated values to list to be added to table
            new_values.append(date)
        # print((new_values))
        # print(index_location)
        #update row content based on location from index_location list and updated strings from new_values list
        for i in range(len(index_location)):
            self.table.at[index_location[i], column_name] = new_values[i]
        #convert all updated info to datetime, if get an error then something gone wrong
        self.table[column_name] = pd.to_datetime(self.table[column_name], format='%Y-%m-%d', errors='raise') 
        return self.table

    def __convert_weight(self, item, index):
        """
        Called in clean_weight method, does unit conversion and returns result as a float. 

        Args:
            item: numeric weight value to be converted
            index: row index of value to be converted
        Returns:
            result(float): weight value converted to kg
        """
        #initalise empty float value to be used
        result = float()
        #if kg ignore, already right units
        if item[-2:] == 'kg' or item[1] == 'kg':
            result = item[:-2]
        #if ml convert
        elif item[-2:] == 'ml': 
            # print('start ml', item[:-2], 'should be: ', float(item[:-2]) / 1000)
            result = float(item[:-2]) / 1000
        #if g and not kg 
        elif item[-1:] == 'g' and item[-2:] != 'kg': 
            # print('start g', item[:-1], 'should be: ', float(item[:-1]) / 1000)
            result = float(item[:-1]) / 1000
        #if oz, not ml or kg
        elif item[-2:] == 'oz': 
            # print('start oz', item[:-2], 'should be: ', float(item[:-2]) * 0.283)
            result = float(item[:-2]) * 0.283
        else:
            print('Error at index:', index)
        return float(result)

    def __clean_weight(self, column_name):
        """
        Format strs so in a useable format for weight conversion, get result from convert weight method and update specific row until all rows in
        table have been converted to kg units. 

        Args:
            column_name (literal): specific column to be cleaned
            result (float): weight in kg units from convert_weight method
        Returns:
            table (pd.dataframe): converted weight column
        """
        #initalise empty float value to be used
        result = float()
        for index, row in self.table.iterrows():
            row[column_name] = row[column_name].replace(' .', '')
            #if is multiple items of one weight, split and convert last part of str
            if 'x' in row[column_name]:
                multi_item = row[column_name].split('x')
                # print('     multiitem', row[column_name], multi_item[0], '*', multi_item[1])
                # print('Multi item going to convert weight', multi_item[1], 'index', index)
                result = self.__convert_weight(multi_item[1], index) * float(multi_item[0])
            else:
                # print(row[column_name], 'going to convert weight', row[column_name], 'index', index)
                result = self.__convert_weight(row[column_name], index)
            #update table
            # print('INPUT: ', row[column_name], '\tRESULT:', result)
            self.table.at[index, column_name] = result
        return self.table

    def __clean_number(self, column_name):
        """
        Cleans alphabetical characters for rows in specified column.

        Args:
            column_name (literal): specific column to be cleaned.
        Returns:
            table (pd.dataframe): cleaned column. 
        """
        #get lowercase letters to check against
        letters = string.ascii_lowercase
        #intialise empty lists for index locations and incorrect values which will be used later in method to update column
        to_clean = list()
        index_location = list()
        cleaned = list()
        #find strs with letters in
        for index, row in self.table.iterrows():
            if row[column_name].isnumeric() == False:
                print('Letter at', row[column_name])
                index_location.append(index)
                to_clean.append(row[column_name])
            else:
                pass   
        #go through each str in list, convert it to lowercase, then convert it to a list
        for element in to_clean:
            #convert string to lowercase and then to list
            element = element.lower()
            element = list(element)
            # print(element)
            for i in element:
                #go through every element in the list and get the index positions of the letters
                if i in letters:
                    # print(i)
                    #replace letter, join list back into string and return it
                    element = [item.replace(i, '') for item in element]
                    element = ''.join(element)
                    cleaned.append(element)
        #update new values at specific locations and return table 
        for i in range(len(index_location)):
            self.table.at[index_location[i], column_name] = cleaned[i]
        return self.table

    #T3- 'CONTAINER' FOR ALL METHODS USED ON LEGACY USER DATA TABLE FROM AMAZON DATABASE
    def clean_user_data(self):
        """
        Clean legacy user data from database- task3. Keep clean date methods as last ones. 
        """
        print(self.table)
        self.__clean_nulls(3)
        self.__check_code(number=1, column_name='country_code', code_list=['GB', 'DE', 'US'])
        self.__check_location(number=2, column_name='country', location_list=['United Kingdom', 'United States', 'Germany'])
        self.__clean_date('date_of_birth')
        self.__clean_date('join_date')
        print(self.table)
        return self.table
    
    #T4-'CONTAINER' FOR ALL METHODS USED ON CARD DATA FROM PDF
    def clean_card_details(self):
        """
        Clean card details from pdf- task4. Keep clean date method as last one. 
        """ 
        print(self.table)
        self.__clean_card_number('card_number')
        self.__clean_date('date_payment_confirmed')
        print(self.table)
        return self.table

    #T5-'CONTAINER' FOR ALL METHODS USED ON STORES DATA FROM API    
    def clean_stores(self):
        """
        Clean store data from API- task5. Keep clean date method as last one. 
        """ 
        print(self.table)
        self.__clean_nulls(3)
        self.__check_code(number=1, column_name='country_code', code_list=['GB', 'DE', 'US'])
        self.__drop_column('lat')
        self.__check_location(number=2, column_name='continent', location_list=['Europe', 'America'])
        self.__clean_date('opening_date') 
        self.__clean_number('staff_numbers')
        self.table = self.table.reindex(columns=['index', 'address', 'longitude', 'latitude', 'locality', 'store_code', 'staff_numbers', 'opening_date', 'store_type', 'country_code', 'continent'])  
        print(self.table)
        return self.table
    
    #T6- 'CONTAINER' FOR ALL METHODS USED ON PRODUCTS DATA FROM AWS S3
    def clean_products(self):
        """
        Clean products data and convert weights to kgs. Keep clean date method as last one. 
        """
        print(self.table)
        self.table = self.table.rename(columns={"Unnamed: 0": "index" , "removed": "availability"})
        self.__clean_nulls(3)
        self.__check_code(number=1, column_name='availability', code_list=['Still_avaliable', 'Removed'])
        self.__clean_date('date_added')
        self.__clean_weight('weight')
        print(self.table)
        return self.table

    #T7- 'CONTAINER' FOR ALL METHODS USED ON ORDER TABLE DATA
    def clean_order_table(self):
        """
        Clean order data. Used as source of truth and central point for star based schema so do not do much cleaning. 
        """
        print(self.table)
        self.__drop_column('first_name')
        self.__drop_column('last_name')
        self.__drop_column('1')
        self.__drop_column('level_0') 
        print(self.table)
        return self.table

    #T8- 'CONTAINER' FOR ALL METHODS USED ON JSON DATE DETAILS FILE
    def clean_date_details(self):
        """
        Clean date details. 
        """
        print(self.table)
        self.table = self.table.reindex(columns=['index', 'timestamp', 'month', 'year', 'day', 'time_period', 'date_uuid'])  
        self.__check_code(number=1, column_name='time_period', code_list=['Evening', 'Morning', 'Midday', 'Late_Hours'])
        print(self.table)
        return self.table