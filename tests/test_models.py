from config.models import Customer


def test_customer_model():
    customer = Customer(
        id="123",
        name="John",
        email="john@example.com"
    )

    assert customer.id == "123"
    assert customer.name == "John"
    assert customer.email == "john@example.com"