"""
Task 2: Payment System - Strategy Pattern

This module implements a flexible payment processing system using the Strategy design pattern.
The Strategy pattern allows you to encapsulate different payment methods and switch between them
at runtime without modifying the PaymentProcessor code.

The pattern consists of:
- PaymentStrategy: Abstract interface for payment methods
- Concrete strategies: CreditCardPayment, PayPalPayment, CryptoPayment
- Context: PaymentProcessor that uses a strategy

This demonstrates polymorphism and the Open/Closed Principle (open for extension, closed for modification).
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """
    Abstract base class defining the interface for payment strategies.

    All payment methods must implement the process_payment method to handle
    their specific fee/discount logic.
    """

    @abstractmethod
    def process_payment(self, amount: float) -> float:
        """
        Process a payment and return the final amount after fees or discounts.

        Args:
            amount: The base payment amount in dollars

        Returns:
            The final amount after applying fees or discounts

        Raises:
            NotImplementedError: Subclasses must implement this method
        """
        # TODO: Subclasses must implement this method
        pass


class CreditCardPayment(PaymentStrategy):
    """
    Credit card payment strategy that adds a processing fee.

    This strategy represents paying by credit card, which typically incurs
    a merchant fee that is passed to the customer.
    """

    def __init__(self, fee_percentage: float):
        """
        Initialize the credit card payment strategy.

        Args:
            fee_percentage: The fee to add as a percentage (e.g., 2.5 for 2.5%)
        """
        # TODO: Store the fee percentage
        pass

    def process_payment(self, amount: float) -> float:
        """
        Process payment by adding the credit card processing fee.

        Args:
            amount: The base payment amount

        Returns:
            The amount plus the fee
        """
        # TODO: Calculate and return amount with fee applied
        pass


class PayPalPayment(PaymentStrategy):
    """
    PayPal payment strategy that adds a transaction fee.

    This strategy represents paying via PayPal, which has its own fee structure.
    """

    def __init__(self, fee_percentage: float):
        """
        Initialize the PayPal payment strategy.

        Args:
            fee_percentage: The fee to add as a percentage (e.g., 3.0 for 3%)
        """
        # TODO: Store the fee percentage
        pass

    def process_payment(self, amount: float) -> float:
        """
        Process payment by adding the PayPal transaction fee.

        Args:
            amount: The base payment amount

        Returns:
            The amount plus the fee
        """
        # TODO: Calculate and return amount with fee applied
        pass


class CryptoPayment(PaymentStrategy):
    """
    Cryptocurrency payment strategy that applies a discount.

    This strategy represents paying with cryptocurrency, which may offer
    a discount due to lower processing costs.
    """

    def __init__(self, discount_percentage: float):
        """
        Initialize the cryptocurrency payment strategy.

        Args:
            discount_percentage: The discount to apply as a percentage (e.g., 5.0 for 5% off)
        """
        # TODO: Store the discount percentage
        pass

    def process_payment(self, amount: float) -> float:
        """
        Process payment by applying a cryptocurrency discount.

        Args:
            amount: The base payment amount

        Returns:
            The amount with discount applied
        """
        # TODO: Calculate and return amount with discount applied
        pass


class PaymentProcessor:
    """
    Context class that uses a payment strategy to process payments.

    The PaymentProcessor is the context in the Strategy pattern. It delegates
    the actual payment processing to a strategy object, allowing different
    payment methods to be used interchangeably.
    """

    def __init__(self, strategy: PaymentStrategy):
        """
        Initialize the payment processor with a payment strategy.

        Args:
            strategy: A PaymentStrategy instance to use for processing
        """
        # TODO: Store the strategy
        pass

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """
        Change the payment strategy at runtime.

        This is one of the key benefits of the Strategy pattern - you can
        switch payment methods without changing the processor code.

        Args:
            strategy: A new PaymentStrategy to use
        """
        # TODO: Replace the current strategy
        pass

    def checkout(self, amount: float) -> float:
        """
        Process a payment using the current strategy.

        Args:
            amount: The base payment amount

        Returns:
            The final amount after the strategy has processed it
        """
        # TODO: Delegate to the strategy and return the result
        pass
