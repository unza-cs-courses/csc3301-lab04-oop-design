import pytest
import math

class TestShapes:
    def test_circle_area(self):
        from src.task1_shapes import Circle
        c = Circle(5)
        assert abs(c.area() - 78.54) < 0.01

    def test_rectangle_area(self):
        from src.task1_shapes import Rectangle
        r = Rectangle(4, 3)
        assert r.area() == 12

    def test_square_inherits_rectangle(self):
        from src.task1_shapes import Square, Rectangle
        s = Square(5)
        assert isinstance(s, Rectangle)
        assert s.area() == 25

    def test_total_area_polymorphism(self):
        from src.task1_shapes import Circle, Rectangle, total_area
        shapes = [Circle(1), Rectangle(2, 3)]
        total = total_area(shapes)
        expected = math.pi + 6
        assert abs(total - expected) < 0.01

    def test_circle_perimeter(self):
        from src.task1_shapes import Circle
        c = Circle(3)
        expected = 2 * math.pi * 3
        assert abs(c.perimeter() - expected) < 0.01

    def test_rectangle_perimeter(self):
        from src.task1_shapes import Rectangle
        r = Rectangle(4, 3)
        assert r.perimeter() == 14

    def test_square_perimeter(self):
        from src.task1_shapes import Square
        s = Square(5)
        assert s.perimeter() == 20


class TestPaymentStrategy:
    def test_payment_strategy_abc_enforcement(self):
        """PaymentStrategy should not be instantiable."""
        try:
            from src.task2_payment import PaymentStrategy
            with pytest.raises(TypeError):
                PaymentStrategy()
        except ImportError:
            pytest.skip("task2_payment not yet implemented")

    def test_credit_card_payment_processing(self):
        """Test credit card payment with fee."""
        try:
            from src.task2_payment import CreditCardPayment
            strategy = CreditCardPayment(2.5)
            final_amount = strategy.process_payment(100.0)
            assert final_amount == 102.5
        except ImportError:
            pytest.skip("task2_payment not yet implemented")

    def test_paypal_payment_processing(self):
        """Test PayPal payment with fee."""
        try:
            from src.task2_payment import PayPalPayment
            strategy = PayPalPayment(3.0)
            final_amount = strategy.process_payment(100.0)
            assert final_amount == 103.0
        except ImportError:
            pytest.skip("task2_payment not yet implemented")

    def test_crypto_payment_discount(self):
        """Test cryptocurrency payment with discount."""
        try:
            from src.task2_payment import CryptoPayment
            strategy = CryptoPayment(5.0)
            final_amount = strategy.process_payment(100.0)
            assert final_amount == 95.0
        except ImportError:
            pytest.skip("task2_payment not yet implemented")

    def test_payment_processor_strategy_swapping(self):
        """Test PaymentProcessor can swap strategies."""
        try:
            from src.task2_payment import PaymentProcessor, CreditCardPayment, CryptoPayment
            processor = PaymentProcessor(CreditCardPayment(2.5))
            amount1 = processor.checkout(100.0)
            assert amount1 == 102.5

            processor.set_strategy(CryptoPayment(5.0))
            amount2 = processor.checkout(100.0)
            assert amount2 == 95.0
        except ImportError:
            pytest.skip("task2_payment not yet implemented")


class TestComposition:
    def test_vehicle_with_features(self):
        """Test vehicle composition with features."""
        try:
            from src.task3_composition import Vehicle, Engine, Wheels
            vehicle = Vehicle("Car", [Engine(), Wheels()])
            descriptions = vehicle.describe()
            assert len(descriptions) == 2
            assert "Engine started" in descriptions
            assert "Wheels rolling" in descriptions
        except ImportError:
            pytest.skip("task3_composition not yet implemented")

    def test_vehicle_feature_independence(self):
        """Test that features are independent."""
        try:
            from src.task3_composition import Vehicle, Engine, Propeller, Wings
            boat = Vehicle("Boat", [Engine(), Propeller()])
            plane = Vehicle("Plane", [Engine(), Wings()])

            boat_features = boat.describe()
            plane_features = plane.describe()

            assert "Propeller spinning" in boat_features
            assert "Wings deployed" in plane_features
            assert "Propeller spinning" not in plane_features
            assert "Wings deployed" not in boat_features
        except ImportError:
            pytest.skip("task3_composition not yet implemented")

    def test_has_feature_method(self):
        """Test has_feature method."""
        try:
            from src.task3_composition import Vehicle, Engine, Wheels, Wings
            vehicle = Vehicle("Plane", [Engine(), Wings()])

            assert vehicle.has_feature(Engine) is True
            assert vehicle.has_feature(Wings) is True
            assert vehicle.has_feature(Wheels) is False
        except ImportError:
            pytest.skip("task3_composition not yet implemented")


class TestObserver:
    def test_event_emitter_on_emit(self):
        """Test basic event emitter on/emit functionality."""
        try:
            from src.task4_observer import EventEmitter
            emitter = EventEmitter()
            results = []

            def callback(value):
                results.append(value)

            emitter.on("test", callback)
            emitter.emit("test", 42)
            assert results == [42]
        except ImportError:
            pytest.skip("task4_observer not yet implemented")

    def test_event_emitter_off(self):
        """Test unregistering callbacks."""
        try:
            from src.task4_observer import EventEmitter
            emitter = EventEmitter()
            results = []

            def callback(value):
                results.append(value)

            emitter.on("test", callback)
            emitter.off("test", callback)
            emitter.emit("test", 42)
            assert results == []
        except ImportError:
            pytest.skip("task4_observer not yet implemented")

    def test_event_emitter_once(self):
        """Test one-time event listener."""
        try:
            from src.task4_observer import EventEmitter
            emitter = EventEmitter()
            results = []

            def callback(value):
                results.append(value)

            emitter.once("test", callback)
            emitter.emit("test", 1)
            emitter.emit("test", 2)
            assert results == [1]
        except ImportError:
            pytest.skip("task4_observer not yet implemented")

    def test_event_emitter_multiple_listeners(self):
        """Test multiple callbacks for same event."""
        try:
            from src.task4_observer import EventEmitter
            emitter = EventEmitter()
            results1 = []
            results2 = []

            def callback1(value):
                results1.append(value)

            def callback2(value):
                results2.append(value * 2)

            emitter.on("test", callback1)
            emitter.on("test", callback2)
            emitter.emit("test", 5)

            assert results1 == [5]
            assert results2 == [10]
        except ImportError:
            pytest.skip("task4_observer not yet implemented")
