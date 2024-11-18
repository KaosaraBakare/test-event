from ga4mp import GtagMP
from ga4mp.store import DictStore

# Create a DictStore
my_store = DictStore(data={
  # "client_id": "35d78b41-b82f-4ba5-adde-49b0f34960d7",
  # "non_personalized_ads": false,
  "events": [
    {
      "name":"purchase",
      "params":{
      "category":"phone",
      "description":"water resistant",
        "name":"Samsung A13"}
    }
  ]
})

# Create an instance of GA4 object using gtag, including the new DictStore.
gtag_tracker = GtagMP(api_secret="CmzwujFrRcGObV4U9OsSp", measurement_id="G-12TBLX9LCD",
client_id="35d78b41-b82f-4ba5-adde-49b0f34960d7")


# Create a new event for purchase.
purchase_event = gtag_tracker.create_new_event(name="purchase")

# Set transaction_id, value, and currency.
purchase_event.set_event_param(name="transaction_id", value="T_12345")
purchase_event.set_event_param(name="currency", value="USD")
purchase_event.set_event_param(name="value", value=12.21)

# Create an item and add details about the item.
shirt = purchase_event.create_new_item(item_id="SKU_12345", item_name="Stan and Friends Tee")
shirt.set_parameter("price", 9.99)
shirt.set_parameter("quantity", 1)
shirt.set_parameter("item_category", "Apparel")

# Add the item to the purchase event.
purchase_event.add_item_to_event(shirt)

# Add a user property based on what you know about the user.
gtag_tracker.store.set_user_property(name="shirt_wearer", value="yes")

# Send the event to GA4 immediately.
event_list = [purchase_event]
print(event_list)