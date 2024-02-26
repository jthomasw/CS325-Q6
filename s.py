class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

    def get_customer_info(self):
        return self.customer_info

    def get_items(self):
        return self.items

    def get_shipping_address(self):
        return self.shipping_address


class OrderCostCalculator:
    TAX_RATE = 0.1
    DISCOUNT_RATE = 0.05

    def calculate_total_order_cost(self, items):
        subtotal = sum(item['price'] for item in items)
        total_tax = subtotal * self.TAX_RATE
        total_discount = subtotal * self.DISCOUNT_RATE
        total_cost = subtotal + total_tax - total_discount
        return total_cost


class OrderValidator:
    def validate_order_data(self, items, shipping_address):
        if not items:
            raise ValueError("No items in the order.")
        if not shipping_address:
            raise ValueError("Shipping address is missing.")


class EmailSender:
    def send_order_confirmation_email(self, customer_email, order_details):

        print(f"Sending order confirmation email to {customer_email}...")
      


class InventoryUpdater:
    def update_inventory_levels(self, items):
      
        print("Updating inventory levels after order processing...")
       


def main():
    customer_info = {'name': 'Jack Woodward', 'email': 'jackWood@gmail.com'}
    items = [{'name': 'Apple', 'price': 10}, {'name': 'Orange', 'price': 20}]
    shipping_address = '123 Jack Ave, St.louis, St.Louis County'

    order_details = OrderDetails(customer_info, items, shipping_address)
    order_cost_calculator = OrderCostCalculator()
    order_validator = OrderValidator()
    email_sender = EmailSender()
    inventory_updater = InventoryUpdater()

    total_cost = order_cost_calculator.calculate_total_order_cost(items) #calc cost
    print("Total order cost:", total_cost)

    order_validator.validate_order_data(items, shipping_address)

    email_sender.send_order_confirmation_email(customer_info['email'], order_details)

    
    inventory_updater.update_inventory_levels(items)


if __name__ == "__main__":
    main()