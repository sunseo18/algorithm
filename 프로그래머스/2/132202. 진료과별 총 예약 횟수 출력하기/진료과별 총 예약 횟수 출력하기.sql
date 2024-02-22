SELECT MCDP_CD as "진료과코드", count(*) as "5월예약건수"
FROM 
    (SELECT MCDP_CD, APNT_YMD
    FROM APPOINTMENT
     WHERE YEAR(APNT_YMD) = "2022" and MONTH(APNT_YMD) like "%5" ) as GROUPED_MCDP_CD
group by MCDP_CD
order by 5월예약건수, MCDP_CD;