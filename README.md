CDYNE SMS Notify! Python Module
===============================

This is a spiffy drop-in Python module for interacting with the CDYNE SMS Notify! web API

[See CDYNE For More Info](https://secure.cdyne.com/products/sms-notify.aspx)

Usage
-----

Add the module somewhere where your project will be able to get at it, and use it like so.

    import sms_notify
    
    license_key = "" # Put your SMS Notify license key here
    sms = sms_notify.session(license_key)
    
    # Send a message
    phone_number = "30355512345"
    message = "This is a test message"
    sms.simple_sms_send(phone_number, message)
    
    # Get unread messages sent to the DID associated with your license key
    messages = sms.get_unread_incoming_messages()
    for message in message:
        print message