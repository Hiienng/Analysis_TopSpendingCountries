##################################################################
# (3:38) 
# EOP: Tính các chỉ số tỷ trọng
##################################################################
import datetime

def calculate_value(row):
    mappings_1 = {
        'Rate_NotRoll_Pre': '2.1 Not-roll: Premature',
        'Rate_NotRoll_NewSales': '2.1 Not-roll: New sales',
        'Rate_NotRoll_Sche': '2.1 Not-roll: Schedule on system',
        'Rate_Roll_Pre': '2.2 Autoroll: Premature',
        'Rate_Roll_NewSales': '2.2 Autoroll: New sales',
        'Rate_Roll_Auto': '2.2 Autoroll: Roll'
    } 
    indicator = row['INDICATORS']
    mappings_2 = {
        'Rate_NotRoll_Pre': '2.1 Not-roll',
        'Rate_NotRoll_NewSales': '2.1 Not-roll',
        'Rate_NotRoll_Sche': '2.1 Not-roll',
        'Rate_Roll_Pre': '2.2 Autoroll',
        'Rate_Roll_NewSales': '2.2 Autoroll',
        'Rate_Roll_Auto': '2.2 Autoroll'
    } 

    if row['PERIOD'] == '2023-01':
        return row['VALUE']
    else:
        target_indicator = mappings_1[indicator]
        current_period = datetime.datetime.strptime(row['PERIOD'], '%Y-%m')
        previous_period = (current_period.replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m')
        numerator  = df_8.loc[
            (df_8['INDICATORS'] == row['INDICATORS']) 
            & (df_8['PERIOD'] == row['PERIOD'])
            & (df_8['TYPE'] == row['TYPE'])
            & (df_8['Term_CM'] == row['Term_CM'])
            & (df_8['Currency_2'] == 'VND')
            , 'VALUE'
        ]
        if not numerator.empty:
            numerator = numerator.values[0]
        else:
            numerator = 123

        denominator_NR = df_8.loc[
            (df_8['INDICATORS'] == '2.1 Not-roll') 
            & (df_8['PERIOD'] == previous_period)
            & (df_8['TYPE'] == row['TYPE'])
            & (df_8['Term_CM'] == row['Term_CM'])
            & (df_8['Currency_2'] == 'VND')
        ]
        if not denominator_NR.empty:
            denominator_NR = denominator_NR['VALUE'].values[0]
        else:
            denominator_NR = 456  
        denominator_R = df_8.loc[
            (df_8['INDICATORS'] == '2.2 Autoroll') 
            & (df_8['PERIOD'] == previous_period)
            & (df_8['TYPE'] == row['TYPE'])
            & (df_8['Term_CM'] == row['Term_CM'])
            & (df_8['Currency_2'] == 'VND')
        ]
        if not denominator_R.empty:
            denominator_R = denominator_R['VALUE'].values[0]
        else:
            denominator_R = 789

        if (numerator*denominator_NR != 0) & (row['INDICATORS'] in List_rate_Level3_NR):
                return numerator
        elif  (numerator*denominator_R != 0) & (row['INDICATORS'] in List_rate_Level3_R):
                return numerator
        else:
            return row['VALUE']# Trả về giá trị ban đầu nếu không phải 'Rate_NotRoll_Pre'
          
df_9 = df_8
df_9['VALUE'] = df_8.apply(calculate_value, axis=1)
