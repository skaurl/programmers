SET @HOUR := -1;
SELECT
    (@HOUR := @HOUR + 1),
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR)
FROM ANIMAL_OUTS
WHERE @HOUR < 23