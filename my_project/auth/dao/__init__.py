

# Orders DB imports for DAOs corresponding to each entity
from .orders.GenderDao import GenderDAO
from .orders.OrdersDAO import OrdersDAO
from .orders.PizzaDAO import PizzaDAO
from .orders.SaladDAO import SaladDAO
from .orders.UsersDAO import UsersDAO
from .orders.DrinksDAO import DrinksDAO
from .orders.DeliveryOrdersDAO import DeliveryOrdersDAO
from .orders.DeliveryPersonDAO import DeliveryPersonDAO
from .orders.DeliveryStatusDAO import DeliveryStatusDAO
from .orders.PizzaOrderDAO import PizzaOrderDAO
from .orders.PaymentStatusDAO import PaymentStatusDAO
from .orders.ToppingsDAO import ToppingsDAO
from .orders.PizzaIngredientsDAO import PizzaIngredientsDAO
from .orders.IngredientsDAO import IngredientsDAO

# Initialize DAOs for each entity
gender_dao = GenderDAO()
orders_dao = OrdersDAO()
pizza_dao = PizzaDAO()
salad_dao = SaladDAO()
users_dao = UsersDAO()
drinks_dao = DrinksDAO()
delivery_orders_dao = DeliveryOrdersDAO()
delivery_person_dao = DeliveryPersonDAO()
delivery_status_dao = DeliveryStatusDAO()
pizza_order_dao = PizzaOrderDAO()
payment_status_dao = PaymentStatusDAO()
toppings_dao = ToppingsDAO()
pizza_ingredients_dao = PizzaIngredientsDAO()
ingredients_dao = IngredientsDAO()
