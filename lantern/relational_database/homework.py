from typing import List
import psycopg2


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    cur = con.cursor()
    cur.execute(
        '''
        INSERT INTO customers(customerid, customername, contactname, address, city, postalcode, country)
        VALUES(92, 'Thomas', 'David', 'Some Address', 'London', '774', 'Singapore')
        RETURNING customers;
        '''
    )
    return cur.fetchall()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute(
        '''
        SELECT * 
        FROM customers
        '''
    )
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute(
        '''
        SELECT * 
        FROM customers 
        WHERE country='Germany';
        '''
    )
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    cur = con.cursor()
    cur.execute(
        '''
        UPDATE customers
        SET customername = 'Johnny Depp'
        WHERE customerid = 1
        RETURNING customers;
        '''
    )
    return cur.fetchall()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    cur = con.cursor()
    cur.execute(
        '''
        DELETE FROM customers
        WHERE customerid = 91
        RETURNING customers;
        '''
    )
    return cur.fetchall()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute(
        '''
        SELECT country 
        FROM suppliers;
        '''
    )
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute(
        '''
        SELECT country FROM suppliers
        ORDER BY country DESC;
        '''
    )
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute(
        '''
        SELECT COUNT(city), city 
        FROM customers
        GROUP BY city
        ORDER BY COUNT DESC;
        '''
    )
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute(
        '''
        SELECT COUNT(country), country
        FROM customers
        GROUP BY country
        HAVING COUNT(country) > 10;
        '''
    )
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute(
        '''
        SELECT * FROM customers
        FETCH first 10 row only;    
        '''
    )
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute(
        '''
        SELECT * FROM customers
        OFFSET 11 rows
        FETCH FIRST 80 row only;
        '''
    )
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute(
        '''
        SELECT supplierid, suppliername, contactname, city, country
        FROM suppliers
        WHERE country in ('USA', 'UK', 'Japan');
        '''
    )
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute(
        '''
        SELECT productname 
        FROM products
        WHERE supplierid in (SELECT supplierid FROM suppliers WHERE country='Sweden');
        '''
    )
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute(
        '''
        SELECT p.productid, p.productname, p.unit, p.price,
        s.country, s.city, s.suppliername
        FROM products as p
        INNER JOIN suppliers as s
        ON p.supplierid = s.supplierid;
        '''
    )
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute(
        '''
        SELECT c.customername, c.contactname, c.country, o.orderid
        FROM customers as c
        LEFT JOIN orders as o
        ON c.customerid = o.customerid
        '''
    )
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute(
        '''
        SELECT c.customername, c.address, c.country as customercountry, s.country as suppliercountry, s.suppliername
        FROM customers as c
        FULL OUTER JOIN suppliers as s
        ON c.country = s.country
        ORDER BY customercountry, suppliercountry;
        '''
    )
    return cur.fetchall()
