IF OBJECT_ID ('TEMPDB..#A') IS NOT NULL    DROP TABLE #A
IF OBJECT_ID ('TEMPDB..#C') IS NOT NULL    DROP TABLE #C
IF OBJECT_ID ('TEMPDB..#D') IS NOT NULL    DROP TABLE #D
IF OBJECT_ID ('TEMPDB..#E') IS NOT NULL    DROP TABLE #E
IF OBJECT_ID ('TEMPDB..#STANDARD') IS NOT NULL    DROP TABLE #STANDARD

DECLARE @ENDDATE   DATE
SET @ENDDATE = '2023-11-30'		
DECLARE @BEGDATE   DATE = DATEADD(DAY, -DAY(@ENDDATE) + 1, @ENDDATE)
DECLARE @PERIOD   VARCHAR (7)
SET @PERIOD = LEFT (@ENDDATE, 7)

SELECT @BEGDATE, @ENDDATE, @PERIOD
---------------------------------------------------------------------------------------------------------------------------------------------------------

---/*ADB OF TD BY CURRENCY, BY TERM*/---
SELECT PRODUCT_GROUP AS PRODUCT,
       CURRENCY,
       MIS_TERM,
       SUM (AMOUNT_AVG) / 1E9 AS AMOUNT,
       CASE WHEN (CURRENCY = 'VND' OR CURRENCY IS NULL) THEN 'VND' ELSE 'NON-VND' END CURRENCY_REFINE,
       'ADB' CODE
  INTO #A
  FROM [RB_DATA].[DBO].[REPORT_BALANCE_DEPOSIT_DAILY] WITH (NOLOCK)
 WHERE     BUSINESS_DATE = @ENDDATE
       AND PRODUCT_GROUP = 'TD'
       AND MIS_SEGMENT IN ('RB', 'AF', 'MAF', 'HH')
	   AND CUSTOMER_ID ! =  '7403752'
GROUP BY PRODUCT_GROUP, CURRENCY, MIS_TERM, CASE WHEN (CURRENCY = 'VND' OR CURRENCY IS NULL) THEN 'VND' ELSE 'NON-VND' END


--UPDATE T
--   SET CURRENCY_REFINE =
--          CASE
--             WHEN (CURRENCY = 'VND' OR CURRENCY IS NULL) THEN 'VND'
--             ELSE 'NON-VND'
--          END
--  FROM #A T

--UPDATE #A
--   SET CODE = 'ADB'
---------------------------------------------------------------------------------------------------------------------------------------------------------

---/*NII OF TD*/---
SELECT ID,
       ITEM_CODE,
       PRODUCT_GROUP AS PRODUCT,
       CURRENCY,
       SUM (AMOUNT_LCY) / 1E9 AS AMOUNT,
       CAST (NULL AS VARCHAR (6)) AS MIS_TERM
  INTO #C
  FROM [RB_DATA].[DBO].[RB_PNL_DATA] WITH (NOLOCK)
 WHERE     PERIOD = @PERIOD
       AND (MIS_SEGMENT = 'RB' OR MIS_SEGMENT = 'AF' OR MIS_SEGMENT = 'MAF' OR MIS_SEGMENT = 'HH')
       AND ITEM_CODE IN ('35',
                         '20',
                         '21',
                         '25',
                         '31',
                         '33',
                         '34',
                         '27')
       AND (SUB_SEGMENT = 'STANDARD' OR SUB_SEGMENT LIKE '%AF%' OR SUB_SEGMENT LIKE '%HH%') ---- TEST HAÌNG THAÌNG
       AND PRODUCT_GROUP = 'TD'
       AND PRODUCT <> 'CASA' --- PRODUCT_GROUP = 'TD',PRODUCT = CASA -> CASA - NON-VND
GROUP BY ID,
         PRODUCT_GROUP,
         CURRENCY,
         ITEM_CODE

/*Update mis term cho pnl*/
SELECT BUSINESS_DATE, CONTRACT_NO, MIS_TERM
  INTO #D
  FROM [FIN_WHR].[DBO].[PIS_DEPOSIT_ALL] WITH (NOLOCK)
 WHERE     BUSINESS_DATE BETWEEN DATEADD (DD, -31, @BEGDATE) AND @ENDDATE
       AND [MIS_SEGMENT] IN ('KHCN', 'RB', 'AF','MAF','HH')
       AND CKH_KKH = 'CKH'
GROUP BY BUSINESS_DATE, CONTRACT_NO, MIS_TERM
ORDER BY CONTRACT_NO, MIS_TERM, BUSINESS_DATE DESC

UPDATE #C
   SET #C.MIS_TERM = ISNULL(#D.MIS_TERM,'OTHERS')
  FROM #C LEFT JOIN #D ON #C.ID = #D.CONTRACT_NO

SELECT PRODUCT,
       ITEM_CODE,
       CURRENCY,
       MIS_TERM,
       SUM (AMOUNT) AS AMOUNT,
       CASE WHEN ITEM_CODE = '27' THEN 'VOF' ELSE 'CIE' END CODE,
       CASE WHEN CURRENCY = 'VND' THEN 'VND' ELSE 'NON-VND' END
          CURRENCY_REFINED
  INTO #E
  FROM #C
GROUP BY PRODUCT,
         CURRENCY,
         MIS_TERM,
         ITEM_CODE


--UPDATE #E
--   SET MIS_TERM = 'OTHERS'
-- WHERE MIS_TERM IS NULL
---------------------------------------------------------------------------------------------------------------------------------------------------------

---/*RESULT*/---
SELECT CODE,
	   @PERIOD AS PERIOD,
       PRODUCT,
       MIS_TERM,
	   CURRENCY_REFINE,
	   '' VINTAGE,
       AMOUNT
  INTO #STANDARD
  FROM #A
UNION ALL
SELECT CODE,
       @PERIOD AS PERIOD,
       PRODUCT,
       MIS_TERM,
       CURRENCY_REFINED,
	   '' VINTAGE,
	   AMOUNT
  FROM #E


SELECT *
  FROM #STANDARD
ORDER BY CODE,
         PRODUCT,
         CURRENCY_REFINE,
         MIS_TERM