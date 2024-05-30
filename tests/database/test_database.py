import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    
    assert user [0][0] == 'Maydan Nezalezhnosti 1'
    assert user [0][1] == 'Kyiv'
    assert user [0][2] == '3127'
    assert user [0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

@pytest.mark.database
def test_table_schema():
    db = Database()
    schema = db.get_table_schema('customers')
    print(schema)

@pytest.mark.database
def test_add_new_customer():
    db = Database()
    db.add_new_customer(2, 'Mariia', 'Parallelweg 1', 'Noordwijk', 'Netherlands')
    customers = db.get_all_users()
    print(customers)

@pytest.mark.database
def test_add_random_customer():
    db = Database()
    db.add_random_customer()
    customers = db.get_all_users()
    assert len(customers) > 0
    print(customers[-1])

@pytest.mark.database
def test_error_message_for_unsupported_data_type():
    db = Database()
    with pytest.raises(ValueError) as excinfo:
        db.add_only_name_to_customers(True)
    assert "Name must be a string" in str(excinfo.value)
    print(excinfo.value)

@pytest.mark.database
def test_get_customers_with_any_empty_field():
    db = Database()
    results = db.get_customers_with_empty_field()
    assert len(results) > 0
    for result in results:
        assert (result[0] is None or
                result[1] is None or
                result[2] is None or
                result[3] is None or
                result[4] is None)
    print(results)            
