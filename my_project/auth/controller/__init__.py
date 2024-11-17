from my_project.auth.controller.orders.OrdersController import OrdersController
from my_project.auth.controller.orders.PizzaController import PizzaController
from my_project.auth.controller.orders.SaladController import SaladController
from my_project.auth.controller.orders.UsersController import UsersController
from my_project.auth.controller.orders.DrinksController import DrinksController
from my_project.auth.controller.orders.GenderController import GenderController
from my_project.auth.controller.orders.DeliveryOrdersController import DeliveryOrdersController
from my_project.auth.controller.orders.DeliveryPersonController import DeliveryPersonController
from my_project.auth.controller.orders.DeliveryStatusController import DeliveryStatusController
from my_project.auth.controller.orders.PizzaOrderController import PizzaOrderController
from my_project.auth.controller.orders.PaymentStatusController import PaymentStatusController
from my_project.auth.controller.orders.IngredientsController import IngredientsController

# Initialize controllers
orders_controller = OrdersController()
pizza_controller = PizzaController()
salad_controller = SaladController()
users_controller = UsersController()
drinks_controller = DrinksController()
gender_controller = GenderController()
delivery_orders_controller = DeliveryOrdersController()
delivery_person_controller = DeliveryPersonController()
delivery_status_controller = DeliveryStatusController()
pizza_order_controller = PizzaOrderController()
payment_status_controller = PaymentStatusController()
ingredients_controller = IngredientsController()
