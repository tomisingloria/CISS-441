import sqlite3

DB_FILE = 'payroll_dc_small.db'
conn = sqlite3.connect(DB_FILE)


def main():
    print('a6 - standard report 2')
    strsql = """select
                    loct,
                    max(salary),
                    avg(salary),
                    min(salary),
                    max(los),
                    avg(los) los_avg,
                    count(loct)
                        select agelvlt, max(salary), avg(los)
                        from agelvl, factdata_mar2016
                        where factdata_mar2016.agelvl = agelvl.agelvl
                        group by agelvlt
                        limit 10;


        """
    cursor = conn.execute(strsql)
    # the formating string for each row of the report
    report_string_format = '{0:<40}\t{1:<15}{2:<15}{3:<15}{4:<15}'
    # printing the header of the report.
    print(
        report_string_format.format(
           'agelvl', 'agelvlt'
            )
        )

    for row in cursor: 
        agelvl, agelvlt = row
        print(
            report_string_format.format(
                agelvl, agelvlt
                )
            )

    cursor.close()        # close cursor
    conn.close()        # close connection to the db

if __name__ == "__main__":
    main()
