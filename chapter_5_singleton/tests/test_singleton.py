from singleton import db_connection,ExistingConnectionError
import pytest



def test_if_singleton_can_be_used_to_create_only_one_instance():
    new_conn=db_connection.get_instance()
    new_conn2=db_connection.get_instance()
    assert new_conn==new_conn2
    assert new_conn2.get_connection()=='this is db connection'
    with pytest.raises(RuntimeError):
        new_conn3=db_connection()