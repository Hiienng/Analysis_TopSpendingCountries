#######################################################
#OWNER: Hiennpd3
#######################################################
import pyodbc
import pandas as pd
import pyodbc

# def SQL_DEPS_MOVEMENT_01(Month_start,server,database):
#     connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes'
#     conn = pyodbc.connect(connection_string)
#     cursor = conn.cursor()
#     sql_query = '''
#     USE RB_DATA
#     GO

#     IF OBJECT_ID ('TEMPDB..#DATE') IS NOT NULL DROP TABLE #DATE

#     SELECT T.PERIOD_CLOSE_DATE AS BUSINESS_DATE INTO #DATE 
#     FROM MASTER_DATA.DBO.DIM_PERIOD T 
#     WHERE YEAR (T.PERIOD_CLOSE_DATE) = '2023'
#     AND T.PERIOD_CLOSE_DATE = '2023-11-30' /*LẤY NGÀY CUỐI PERIOD*/


#     WHILE((SELECT COUNT(1) FROM #DATE T) > 0)
#     BEGIN
#     DECLARE @CURRDATE   DATE 
#     SELECT @CURRDATE = (SELECT TOP 1 T.BUSINESS_DATE FROM #DATE T)
#     DECLARE @CURRDATE1   DATE = DATEADD (DD, -DAY (@CURRDATE)+1, @CURRDATE) /*LẤY NGÀY ĐẦU PERIOD*/
#     DECLARE @LASTDATE   DATE = DATEADD (DD, -1, @CURRDATE1) /*LẤY NGÀY CUỐI PERIOD TRƯỚC*/
#     DECLARE @LASTDATE1   DATE =DATEADD (DD, -DAY (@LASTDATE)+1, @LASTDATE) /*LẤY NGÀY ĐẦU PERIOD TRƯỚC*/
#     DECLARE @PERIOD   VARCHAR (255) = CONVERT(VARCHAR(7),@CURRDATE,121) /*LẤY PERIOD*/
#     DECLARE @PERIODLM   VARCHAR (255) = CONVERT(VARCHAR(7),DATEADD (MM, -1, @CURRDATE),121) /*LẤY PERIOD TRƯỚC*/

#     IF OBJECT_ID ('TEMPDB..#EPOLM_CM') IS NOT NULL DROP TABLE #EPOLM_CM

#     SELECT 	T.BUSINESS_DATE, T.CONTRACT_NO,	T.CUSTOMER_ID, T.PRODUCT_GROUP
#     ,	CASE WHEN T.BUSINESS_DATE = @LASTDATE THEN 'LM' WHEN T.BUSINESS_DATE = @CURRDATE THEN 'CM'END AS HEADING
#     ,	T.TERM
#     ,	T.CURRENCY
#     ,	T.MIS_TERM
#     ,	T.VALUE_DATE, T.CREATE_DATE, T.MATURITY_DATE
#     , SUM(T.AMOUNT_LCY) AS EOP 
#     , MAT_INSTRUCTION
#     INTO #EPOLM_CM 
#     FROM [FIN_WHR].[DBO].[PIS_DEPOSIT_ALL] T
#     WHERE (T.BUSINESS_DATE BETWEEN @LASTDATE AND @CURRDATE)	
#     AND MIS_SEGMENT IN ('KHCN','RB','AF','MAF','HH') 
#     /*AND BOOK_CODE <> 'TMO' AND BOOK_CODE <> 'I2B'*/ /*--TU THANG 11/2020, TOAN BO BOOK CODE I2B VA TMO VE RB--*/
#     AND (PRODUCT_GROUP LIKE 'TD%' OR PRODUCT_GROUP LIKE '%TERM%DEPOSIT')
#     AND CUSTOMER_ID !='7403752' --(ADJ LOẠI TRỪ THÁNG 01.2023, NC SỬ DUNG SOURCE RB_DATA)
#     GROUP BY T.BUSINESS_DATE, T.CONTRACT_NO, T.CUSTOMER_ID, T.PRODUCT_GROUP
#     , CASE WHEN T.BUSINESS_DATE = @LASTDATE THEN 'LM' WHEN T.BUSINESS_DATE = @CURRDATE THEN 'CM' END
#     , T.TERM, T.CURRENCY, T.MIS_TERM, T.VALUE_DATE, T.CREATE_DATE, T.MATURITY_DATE, MAT_INSTRUCTION

#     /*BẢNG TRUNG GIAN #PIVOT_DATA TẠO */
#     IF OBJECT_ID ('TEMPDB..#PIVOT_DATA') IS NOT NULL DROP TABLE #PIVOT_DATA

#     SELECT T.CONTRACT_NO, T.PRODUCT_GROUP
#         , CONVERT(FLOAT,SUM(ISNULL (T.LM, 0)) /1E9) AS EOP_LM
#         , CONVERT(FLOAT,SUM(ISNULL (T.CM, 0)) /1E9) AS EOP_CM
#         , CONVERT(FLOAT,SUM(ISNULL (T.CM, 0) - ISNULL (T.LM, 0)) /1E9) AS NET
#         , CAST (NULL AS VARCHAR (255)) TERM
#         , CAST (NULL AS VARCHAR (255)) CURRENCY
#         , CAST (NULL AS VARCHAR (255)) STATUS_LM
#         , CAST (NULL AS VARCHAR (255)) STATUS_CM
#         , CAST (NULL AS DATE) VALUE_DATE_LM
#         , CAST (NULL AS DATE) VALUE_DATE_CM
#         , CAST (NULL AS DATE) CREATE_DATE_LM
#         , CAST (NULL AS DATE) CREATE_DATE_CM
#         , CAST (NULL AS DATE) MATURITY_DATE_LM
#         , CAST (NULL AS DATE) MATURITY_DATE_CM
#         , CAST (NULL AS VARCHAR (255)) BIG_TD_LM
#         , CAST (NULL AS VARCHAR (255)) BIG_TD_CM
#         , CAST (NULL AS VARCHAR (255)) CUSTOMER_ID_LM
#         , CAST (NULL AS VARCHAR (255)) CUSTOMER_ID_CM
#         , CAST (NULL AS DATE) MAXDATE
#         , CAST (NULL AS VARCHAR (255)) MOVEMENT_TYPE 
#         , MAT_INSTRUCTION
#     INTO #PIVOT_DATA FROM #EPOLM_CM PIVOT (SUM (EOP) FOR HEADING IN ([LM], [CM])) T
#     GROUP BY T.CONTRACT_NO, T.PRODUCT_GROUP, MAT_INSTRUCTION

#     UPDATE T SET T.TERM = V.TERM
#     , T.CURRENCY = V.CURRENCY 
#     , T.STATUS_CM = V.MIS_TERM
#     , T.VALUE_DATE_CM = V.VALUE_DATE
#     , T.CREATE_DATE_CM = V.CREATE_DATE
#     , T.MATURITY_DATE_CM = V.MATURITY_DATE
#     , T.CUSTOMER_ID_CM = V.CUSTOMER_ID 
#     FROM #PIVOT_DATA T, #EPOLM_CM V 
#     WHERE T.CONTRACT_NO = V.CONTRACT_NO 
#     AND V.BUSINESS_DATE = @CURRDATE

#     UPDATE T 
#     SET T.CURRENCY = CASE WHEN T.CURRENCY IS NULL THEN V.CURRENCY ELSE T.CURRENCY END
#     , T.TERM = CASE WHEN T.TERM IS NULL THEN V.TERM ELSE T.TERM END
#     , T.STATUS_LM = V.MIS_TERM
#     , T.VALUE_DATE_LM = V.VALUE_DATE
#     , T.CREATE_DATE_LM = V.CREATE_DATE
#     , T.MATURITY_DATE_LM = V.MATURITY_DATE
#     , T.CUSTOMER_ID_LM = V.CUSTOMER_ID 
#     FROM #PIVOT_DATA T, #EPOLM_CM V  
#     WHERE T.CONTRACT_NO = V.CONTRACT_NO 
#     AND V.BUSINESS_DATE = @LASTDATE 

#     /*UPDATE DANH SACH BIG_TD VAO BANG #BIG_TD*/
#     IF OBJECT_ID ('TEMPDB..#BIG_TD') IS NOT NULL DROP TABLE #BIG_TD

#     SELECT BUSINESS_DATE, CUSTOMER_ID
#             , CASE WHEN SUM(EOP)/1E9 > 100 THEN 'BIG_TD' ELSE 'MASS' END AS BIG_TD 
#     INTO #BIG_TD
#     FROM #EPOLM_CM
#     GROUP BY BUSINESS_DATE, CUSTOMER_ID ORDER BY BUSINESS_DATE, CUSTOMER_ID

#     UPDATE T 
#     SET T.BIG_TD_CM = V.BIG_TD 
#     FROM #PIVOT_DATA T, #BIG_TD V 
#     WHERE T.CUSTOMER_ID_CM = V.CUSTOMER_ID 
#     AND V.BUSINESS_DATE = @CURRDATE

#     UPDATE T 
#     SET T.BIG_TD_LM = V.BIG_TD 
#     FROM #PIVOT_DATA T, #BIG_TD V 
#     WHERE T.CUSTOMER_ID_LM = V.CUSTOMER_ID 
#     AND V.BUSINESS_DATE = @LASTDATE 

#     /*UPDATE BANG #MAXDATE NGÀY TỒN TẠI CUỐI CÙNG CỦA HỢP ĐỒNG*/
#     IF OBJECT_ID ('TEMPDB..#MAXDATE') IS NOT NULL DROP TABLE #MAXDATE

#     SELECT CONTRACT_NO, MAX(BUSINESS_DATE) AS MAXDATE INTO #MAXDATE 
#     FROM #EPOLM_CM
#     GROUP BY CONTRACT_NO ORDER BY CONTRACT_NO

#     UPDATE T 
#     SET T.MAXDATE = V.MAXDATE 
#     FROM #PIVOT_DATA T, #MAXDATE V 
#     WHERE T.CONTRACT_NO = V.CONTRACT_NO

#     UPDATE T 
#     SET T.MOVEMENT_TYPE = CASE WHEN EOP_CM = EOP_LM AND MAT_INSTRUCTION <> 'AUTOMATIC ROLLOVER' AND MAT_INSTRUCTION <> 'Automatic Rollover Only Principal' THEN '0UNCHANGED_NOTROLL' 
#                             WHEN (CREATE_DATE_CM BETWEEN @CURRDATE1 AND @CURRDATE) AND MAT_INSTRUCTION <> 'AUTOMATIC ROLLOVER' AND MAT_INSTRUCTION <> 'Automatic Rollover Only Principal' AND MAT_INSTRUCTION IS NOT NULL
#                                         THEN '1NEW_NOTROLL' 
#                             WHEN (EOP_CM = 0 AND EOP_LM <> 0) AND MAT_INSTRUCTION <> 'AUTOMATIC ROLLOVER' AND MAT_INSTRUCTION <> 'Automatic Rollover Only Principal' AND MAT_INSTRUCTION IS NOT NULL 
#                                         THEN CASE WHEN MATURITY_DATE_LM <= MAXDATE THEN '2SCHE_NOTROLL'
#                                                 WHEN MATURITY_DATE_LM > MAXDATE THEN  '3PREMATURE_NOTROLL' END
#                             WHEN EOP_CM = EOP_LM AND (MAT_INSTRUCTION = 'AUTOMATIC ROLLOVER' OR MAT_INSTRUCTION = 'Automatic Rollover Only Principal') 
#                                         THEN '4UNCHANGED_AUTOROLL' 
#                             WHEN (CREATE_DATE_CM BETWEEN @CURRDATE1 AND @CURRDATE) AND (MAT_INSTRUCTION = 'AUTOMATIC ROLLOVER' OR MAT_INSTRUCTION = 'Automatic Rollover Only Principal') 
#                                         THEN '5NEW_AUTOROLL' 
#                             WHEN (VALUE_DATE_CM BETWEEN @CURRDATE1 AND @CURRDATE) AND CREATE_DATE_CM < VALUE_DATE_CM AND (MAT_INSTRUCTION = 'AUTOMATIC ROLLOVER' OR MAT_INSTRUCTION = 'Automatic Rollover Only Principal') AND EOP_CM <> 0
#                                         THEN '6ROLL_AUTOROLL' 
#                             WHEN (EOP_CM = 0 AND EOP_LM <> 0) AND (MAT_INSTRUCTION = 'AUTOMATIC ROLLOVER' OR MAT_INSTRUCTION = 'Automatic Rollover Only Principal')
#                                         THEN '7PREMATURE_AUTOROLL' 
#                             ELSE '9OTHERS' END
#     FROM #PIVOT_DATA T

#     DELETE T
#     FROM USER_DATA.VYTT11.FCST_EOP_TD_MOVEMENT_MAT_TEST2 T
#     WHERE T.PERIOD = @PERIOD

#     INSERT INTO USER_DATA.VYTT11.FCST_EOP_TD_MOVEMENT_MAT_TEST2
#     SELECT @PERIOD AS PERIOD , T.PRODUCT_GROUP, T.TERM, T.CURRENCY, T.STATUS_LM, T.STATUS_CM
#     , T.MOVEMENT_TYPE, T.BIG_TD_CM, T.BIG_TD_LM, T.EOP_LM, T.EOP_CM, T.NET, T.MATURITY_DATE_CM, MAT_INSTRUCTION
#     FROM #PIVOT_DATA T


#     DELETE  T
#     FROM #DATE T
#     WHERE T.BUSINESS_DATE = @CURRDATE

#     END 
#     '''
#     cursor.execute(sql_query, Month_start)
#     rows = cursor.fetchall()

#     columns = [column[0] for column in cursor.description]
#     df = pd.DataFrame.from_records(rows, columns=columns)

#     cursor.close()
#     conn.close()

#     print('Completed fetch SQL_DEPS_MOVEMENT')
#     return df

#########################################################################################################
#########################################################################################################
def SQL_DEPS_MOVEMENT_11(Month_start, Month_end, server, database):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    sql_query = '''
    SELECT PERIOD, PRODUCT_GROUP, TERM, CURRENCY, STATUS_LM, STATUS_CM, MOVEMENT_TYPE, BIG_TD_CM, BIG_TD_LM, SUM(EOP_LM) AS EOP_LM, SUM(EOP_CM) AS EOP_CM, SUM(NET) AS NET, MAT_INSTRUCTION
    FROM [USER_DATA].[vytt11].[FCST_EOP_TD_MOVEMENT_MAT_TEST2]
    WHERE PERIOD >= ? AND PERIOD <= ?
    GROUP BY PERIOD, PRODUCT_GROUP, TERM, CURRENCY, STATUS_LM, STATUS_CM, MOVEMENT_TYPE, BIG_TD_CM, BIG_TD_LM, MAT_INSTRUCTION
    ORDER BY PERIOD, PRODUCT_GROUP, TERM, CURRENCY, STATUS_LM, STATUS_CM, MOVEMENT_TYPE, BIG_TD_CM, BIG_TD_LM, MAT_INSTRUCTION  
    '''
    cursor.execute(sql_query, Month_start, Month_end)
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)

    cursor.close()
    conn.close() 

    print(f'Completed fetch SQL_DEPS_MOVEMENT: {len(df)} rows')
    return df

###
"""
Hàm dưới đang xây dựng để optimize trọng tải / lần quét server cho hàm SQL_DEPS_MOVEMENT_11-> Giảm thời gian quyét dữ liệu và hiệu suất server 
Bằng cách sử dụng pagination truy vấn phân trang, sau đó chạy vòng lặp và lưu dữ liệu caching
"""
# def SQL_DEPS_MOVEMENT_11_v2(Month_start, server, database):
#     connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes'
    
#     with pyodbc.connect(connection_string) as conn:
#         cursor = conn.cursor()
#         sql_query = '''
#         SELECT PERIOD, PRODUCT_GROUP, TERM, CURRENCY, STATUS_LM, STATUS_CM, MOVEMENT_TYPE, BIG_TD_CM, BIG_TD_LM, SUM(EOP_LM) AS EOP_LM, SUM(EOP_CM) AS EOP_CM, SUM(NET) AS NET, MAT_INSTRUCTION
#         FROM [USER_DATA].[vytt11].[FCST_EOP_TD_MOVEMENT_MAT_TEST2]
#         WHERE PERIOD >= ?
#         GROUP BY PERIOD, PRODUCT_GROUP, TERM, CURRENCY, STATUS_LM, STATUS_CM, MOVEMENT_TYPE, BIG_TD_CM, BIG_TD_LM, MAT_INSTRUCTION
#         ORDER BY PERIOD, PRODUCT_GROUP, TERM, CURRENCY, STATUS_LM, STATUS_CM, MOVEMENT_TYPE, BIG_TD_CM, BIG_TD_LM, MAT_INSTRUCTION  
#         '''
#         cursor.execute(sql_query, Month_start)
        
#         # Khởi tạo danh sách rỗng để lưu trữ các phần dữ liệu
#         data_parts = []
        
#         # Sử dụng vòng lặp để truy vấn và gom các phần dữ liệu
#         while True:
#             rows = cursor.fetchmany(1000)  # Số lượng hàng trên mỗi trang
            
#             if not rows:
#                 break
            
#             data_parts.append(rows)
        
#         # Gom các phần dữ liệu thành một DataFrame
#         columns = [column[0] for column in cursor.description]
#         df = pd.DataFrame.from_records(data_parts, columns=columns)

#     cursor.close()
#     conn.close()
#     print(f'Completed fetch SQL_DEPS_MOVEMENT : {len(df)} rows' )
#     return df


def SQL_DEPS_MOVEMENT_GROUPTERM(dataframe):
    mapping_table = {
        '10M': '10-11M','11M': '10-11M',
        '12M': '12-18M','13M': '12-18M', '14M': '12-18M', '16M': '12-18M', '18M': '12-18M','17M': '12-18M',
        '1M': '1-3M', '2M': '1-3M', '3M': '1-3M','4M': '4-5M','5M': '4-5M',
        '6M': '6-9M', '7M': '6-9M', '8M': '6-9M','9M': '6-9M',
        '100M': 'From 18M',  '108M': 'From 18M',   '120M': 'From 18M', '144M': 'From 18M',
        '150M': 'From 18M','156M': 'From 18M', '168M': 'From 18M', '180M': 'From 18M',
        '183M': 'From 18M', '20M': 'From 18M', '22M': 'From 18M', '244M': 'From 18M',
        '24M': 'From 18M',   '25M': 'From 18M', '30M': 'From 18M','33M': 'From 18M',
        '34M': 'From 18M', '35M': 'From 18M', '36M': 'From 18M','38M': 'From 18M',
        '40M': 'From 18M', '42M': 'From 18M',  '48M': 'From 18M','50M': 'From 18M',
        '54M': 'From 18M',  '57M': 'From 18M','59M': 'From 18M', '60M': 'From 18M',
        '63M': 'From 18M',  '72M': 'From 18M', '75M': 'From 18M','80M': 'From 18M',
        '84M': 'From 18M',  '92M': 'From 18M','96M': 'From 18M','123M': 'From 18M',
        '37M': 'From 18M',  '43M': 'From 18M','109M': 'From 18M', '121M': 'From 18M',
        '134M': 'From 18M',  '146M': 'From 18M','158M': 'From 18M',  '170M': 'From 18M',
        '182M': 'From 18M',  '19M': 'From 18M','243M': 'From 18M',  '55M': 'From 18M',
        '58M': 'From 18M',  '73M': 'From 18M','85M': 'From 18M',  '97M': 'From 18M',   '98M': 'From 18M', '26M': 'From 18M',
        '89M': 'From 18M',  '45M': 'From 18M','167M': 'From 18M','56M': 'From 18M','66M': 'From 18M',
        '90M': 'From 18M','101M': 'From 18M','32M': 'From 18M','62M': 'From 18M',  '99M': 'From 18M',
        '253M': 'From 18M','23M': 'From 18M','36M': 'From 18M',
        '48M': 'From 18M',  '46M': 'From 18M',
        '0M': 'less than 1M','1W': 'less than 1M','2W': 'less than 1M',   '3W': 'less than 1M',
        '02W': 'less than 1M', '03W': 'less than 1M',
        'OTHERS': 'Special payment',
        'less than 1M':'less than 1M', # related to Term_CM. Term_LM
        'NEW':'NEW' # related to Term_LM
    }
    
    mapping_type = {
        'Payment to nominated account' : 'NOT_ROLL',
        'PAYMENT TO NOMINATED ACCOUNT' : 'NOT_ROLL', 
        'AUTOMATIC ROLLOVER' : 'AUTOROLL',
        'Automatic Rollover' : 'AUTOROLL',
        'Automatic Rollover Only Principal' : 'AUTOROLL',
        None: 'NOT_ROLL'
    }

    # Áp dụng ánh xạ vào cột "Term_CM" của DataFrame
    dataframe['Term_CM'] = dataframe.apply(lambda row: row['STATUS_LM'] if row['STATUS_LM'] is not None else (row['STATUS_CM'] if row['STATUS_CM'] is not None else 'less than 1M'), axis=1)
    dataframe['Term_CM'] = dataframe['Term_CM'].map(mapping_table)

    # Áp dụng ánh xạ vào cột "Term_LM" của DataFrame
    dataframe['Term_LM'] = dataframe.apply(lambda row: 'NEW' if (row['STATUS_LM'] is None and row['MOVEMENT_TYPE'] in ["NEW", "5NEW_AUTOROLL"]) else ( 'less than 1M' if row['STATUS_LM'] is None else row['STATUS_LM']), axis=1)
    dataframe['Term_LM'] = dataframe['Term_LM'].map(mapping_table)

    # Áp dụng ánh xạ vào cột "Currency" của DataFrame
    dataframe['Currency_2'] = dataframe['CURRENCY'].apply(lambda value: 'VND' if value in ['VND', None] else 'Non-VND')
    dataframe['TYPE'] = dataframe['MAT_INSTRUCTION'].map(mapping_type)
    
    return dataframe

#########################################################################################################
#########################################################################################################

def SQL_SD_OTHER_14(server, database):
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    sql_query = '''
    select * from USER_DATA.HIENNPD3.FCST_NII_TD_ALL
    '''
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)

    cursor.close()
    conn.close() 

    print(f'Completed fetch SQL_DEPS_MOVEMENT: {len(df)} rows')
    return df
