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
                        select patcot, max(salary) max_salary, max(los)
                        from patco, factdata_mar2016
                        where factdata_mar2016.patco = patco.patco
                        order by max_salary desc
                        limit 20;


        """
    cursor = conn.execute(strsql)
    # the formating string for each row of the report
    report_string_format = '{0:<40}\t{1:<15}{2:<15}{3:<15}{4:<15}'
    # printing the header of the report.
    print(
        report_string_format.format(
           'patco', 'patcot'
            )
        )

    for row in cursor: 
        patco, patcot = row
        print(
            report_string_format.format(
                patco, patcot
                )
            )

    cursor.close()        # close cursor
    conn.close()        # close connection to the db

if __name__ == "__main__":
    main()
