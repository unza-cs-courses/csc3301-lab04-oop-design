"""
Task 4: Observer Pattern - Event System

This module implements an event emitter system using the Observer design pattern.
The Observer pattern allows objects to subscribe to and react to events without
tight coupling.

The Pattern:
- Subject (EventEmitter): Maintains a list of observers and notifies them of events
- Observers (Callbacks): React to events when they occur
- Decoupling: Event producers don't need to know about event consumers

Real-world analogy: A newspaper (EventEmitter) publishes articles (events),
and subscribers (callbacks) automatically receive them.
"""

from typing import Callable, Dict, List, Any


class EventEmitter:
    """
    Event emitter that implements the Observer pattern.

    This class allows registering callbacks for events and triggering those
    callbacks when events occur. It supports both repeating callbacks (on)
    and one-time callbacks (once).
    """

    def __init__(self):
        """
        Initialize an empty event emitter.

        Internally, this creates a dictionary to map event names to lists
        of callbacks.
        """
        # TODO: Initialize the internal event-to-callbacks mapping
        pass

    def on(self, event: str, callback: Callable) -> None:
        """
        Register a callback to be called whenever an event occurs.

        The same callback can be registered multiple times for different events,
        and the same event can have multiple callbacks.

        Args:
            event: The name of the event to listen for
            callback: A callable that will be invoked when the event fires

        Example:
            emitter = EventEmitter()
            def handle_login(user_id):
                print(f"User {user_id} logged in")
            emitter.on("login", handle_login)
            emitter.emit("login", user_id=123)  # Prints: User 123 logged in
        """
        # TODO: Register the callback for this event
        pass

    def off(self, event: str, callback: Callable) -> None:
        """
        Unregister a callback for an event.

        If the callback was registered multiple times, only one instance is removed.
        If the callback is not registered for this event, this does nothing.

        Args:
            event: The name of the event
            callback: The callback to remove

        Example:
            emitter.off("login", handle_login)  # Stop listening for login events
        """
        # TODO: Remove the callback from this event's callback list
        pass

    def emit(self, event: str, *args, **kwargs) -> None:
        """
        Trigger all callbacks registered for an event.

        All registered callbacks for the given event will be called with the
        provided arguments. Both positional and keyword arguments are supported.

        Args:
            event: The name of the event to emit
            *args: Positional arguments to pass to callbacks
            **kwargs: Keyword arguments to pass to callbacks

        Example:
            emitter.emit("login", 123)  # Calls with positional arg
            emitter.emit("login", user_id=123)  # Calls with keyword arg
            emitter.emit("logout", 456, "forced")  # Multiple args
        """
        # TODO: Call all callbacks registered for this event
        pass

    def once(self, event: str, callback: Callable) -> None:
        """
        Register a callback that fires only once, then removes itself.

        After the event is emitted once and the callback is called,
        the callback is automatically unregistered. Subsequent emissions
        of the event will not trigger this callback.

        Args:
            event: The name of the event
            callback: The callback to call exactly once

        Example:
            def on_first_login():
                print("Welcome!")
            emitter.once("login", on_first_login)
            emitter.emit("login")  # Prints: Welcome!
            emitter.emit("login")  # Nothing happens (callback removed)
        """
        # TODO: Create a wrapper callback that removes itself after firing
        # Hint: You'll need to wrap the callback so it unregisters itself
        pass
