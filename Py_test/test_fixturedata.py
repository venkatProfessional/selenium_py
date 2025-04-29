import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_edit_profile(self, dataLoad):
        print("Inside test_edit_profile")
        # print a specific data
        print(dataLoad[0])
#         print a full data
        print(dataLoad)

    def test_crossBrowser(self,crossBrowser):
        print(crossBrowser)

    def test_calculate_shipping(shippingData):
        location = shippingData["location"]
        weight = shippingData["weight"]
        print(f"Calculating shipping for {location} with weight {weight}kg")

        # Example logic (could be replaced with real function)
        base_cost = 10
        cost_per_kg = 2
        total_cost = base_cost + (weight * cost_per_kg)

        assert total_cost > base_cost  # Simple check
