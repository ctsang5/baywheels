import pandas as pd

def get_words_to_search_with(station_names: list):
    """
    Analyze station names to find key words for matching based on the word "AT". 
    """
    pattern_pairs = []
    missing_AT_string = []

    for station in station_names:
        words = station.split()

        if 'AT' not in words:
            missing_AT_string.append(station)
            longest_words = sorted(words, key = len, reverse = True)[:2]
            first_longest_word = longest_words[0] if longest_words else None
            second_longest_word = longest_words[1] if len(longest_words) > 1 else None
            pattern_pairs.append((first_longest_word,second_longest_word))

        else:
            AT_position = words.index('AT')
            before = max(words[:AT_position], key = len) if AT_position > 0 else None           
            after = max(words[AT_position + 1:], key = len) if AT_position + 1 < len(words) else None      
            pattern_pairs.append((before,after))

    return pattern_pairs, missing_AT_string


def standardize_stations(pair_pattern: list, station_name: str, station_id: str, ride_time, station_lat: str, station_lng: str, df: pd.DataFrame): 
    
    df = df.copy()
    df[station_name] = df[station_name].astype('string[pyarrow]')
    
    slow_functions_first_df = df.sort_values(ride_time, ascending = False).drop_duplicates(subset = [station_id, station_name])
    fast_series = slow_functions_first_df[station_name]

    LATITUDE_THRESHOLD = 0.03
    same_station_name_same_station_id_list = []
    different_station_name_list = []
    different_latitude_list = []

    for street_word_one, street_word_two in pair_pattern:
        pattern_one = rf"\b{street_word_one}\b"      
        pattern_two = rf"\b{street_word_two}\b"

        mask = fast_series.str.contains(pattern_one) & fast_series.str.contains(pattern_two)            
        check_df = slow_functions_first_df.loc[mask].copy()

        if check_df[station_name].nunique() != 1: 
            if not check_df.empty:                                                              
                different_station_name_list.append(check_df)

        elif check_df[station_lat].diff().abs().gt(LATITUDE_THRESHOLD).any():
            different_latitude_list.append(check_df)

        else: 
            check_df[station_id] = check_df[station_id].iat[0]                                 
            check_df[station_lat] = check_df[station_lat].iat[0]                               
            check_df[station_lng] = check_df[station_lng].iat[0]

            same_station_name_same_station_id_list.append(check_df)    

    fixed_different_station_id_list = fix_mismatched_stations(different_station_name_list, station_name, station_id)
    standardized_station_id_list = fixed_different_station_id_list + same_station_name_same_station_id_list

    return standardized_station_id_list, same_station_name_same_station_id_list, different_station_name_list, different_latitude_list 


def create_station_dictionary(station_df_list: list, station_name: str, station_id: str):
    df = pd.concat(station_df_list, ignore_index = True)
    return df.set_index(station_name)[station_id].to_dict()


def fix_mismatched_stations(mismatched_station: list, station_name: str, station_id: str):     
    for station in mismatched_station:  
        station[station_id] = station[station_id].iat[0]                                        
    return mismatched_station 


