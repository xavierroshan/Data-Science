 use sql_cookbook
 WITH RECURSIVE x AS (
    SELECT 
        dy,
        DAY(dy) AS dm,
        MONTH(dy) AS mth,
        DAYOFWEEK(dy) AS dw,
        CASE 
            WHEN DAYOFWEEK(dy) = 1 
            THEN WEEK(dy, 3) - 1  -- Using mode 3 for ISO week calculation
            ELSE WEEK(dy, 3) 
        END AS wk
    FROM (
        SELECT DATE_SUB(CURRENT_DATE, INTERVAL (DAY(CURRENT_DATE) - 1) DAY) AS dy
        FROM t1
    ) AS init
    UNION ALL
    SELECT 
        DATE_ADD(dy, INTERVAL 1 DAY),
        DAY(DATE_ADD(dy, INTERVAL 1 DAY)),
        mth,
        DAYOFWEEK(DATE_ADD(dy, INTERVAL 1 DAY)),
        CASE 
            WHEN DAYOFWEEK(DATE_ADD(dy, INTERVAL 1 DAY)) = 1 
            THEN WEEK(DATE_ADD(dy, INTERVAL 1 DAY), 3) - 1
            ELSE WEEK(DATE_ADD(dy, INTERVAL 1 DAY), 3)
        END
    FROM x
    WHERE MONTH(DATE_ADD(dy, INTERVAL 1 DAY)) = mth
)


SELECT 
    MAX(CASE dw WHEN 2 THEN dm END) AS Mo,
    MAX(CASE dw WHEN 3 THEN dm END) AS Tu,
    MAX(CASE dw WHEN 4 THEN dm END) AS We,
    MAX(CASE dw WHEN 5 THEN dm END) AS Th,
    MAX(CASE dw WHEN 6 THEN dm END) AS Fr,
    MAX(CASE dw WHEN 7 THEN dm END) AS Sa,
    MAX(CASE dw WHEN 1 THEN dm END) AS Su
FROM x
GROUP BY wk
ORDER BY wk;