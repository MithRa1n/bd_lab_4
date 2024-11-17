from .orders.GenderService import GenderService
from .orders.UsersService import UserService
from .orders.DeliveryStatusService import DeliveryStatusService
from .orders.PaymentStatusService import PaymentStatusService
from .orders.PizzaService import PizzaService
from .orders.ToppingsService import ToppingsService
from .orders.IngredientsService import IngredientsService
from .orders.SaladService import SaladService
from .orders.DrinksService import DrinksService
from .orders.PizzaIngredientsService import PizzaIngredientsService
from .orders.DeliveryPersonService import DeliveryPersonService
from .orders.OrdersService import OrdersService
from .orders.PizzaOrderService import PizzaOrderService
from .orders.DeliveryOrdersService import DeliveryOrdersService


genderService = GenderService()
usersService = UserService()
deliveryStatusService = DeliveryStatusService()
paymentStatusService = PaymentStatusService()
pizzaService = PizzaService()
toppingsService = ToppingsService()
ingredientsService = IngredientsService()
saladService = SaladService()
drinksService = DrinksService()
pizzaIngredientsService = PizzaIngredientsService()
deliveryPersonService = DeliveryPersonService()
ordersService = OrdersService()
pizzaOrderService = PizzaOrderService()
deliveryOrdersService = DeliveryOrdersService()

