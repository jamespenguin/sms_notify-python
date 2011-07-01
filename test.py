#!/usr/bin/env python
import time
import sms_notify

def display_dictionary(dictionary):
    print
    print "-" * 50
    for key in dictionary.keys():
        print "%s => %s" % (key, dictionary[key])
    print

if __name__ == '__main__':
    license_key = ""
    phone_number = ""
    message = "Testing Testing"
    assigned_did = ""
    reference_id = "maho"
    scheduled_date_time = ""
    status_postback_url = ""
    s = sms_notify.session(license_key)

    #data = s.simple_sms_send(phone_number, message)
    #display_dictionary(data)
    #print "Sleeping for 5..."
    #time.sleep(5)
    #display_dictionary(s.get_message_status(data["MessageID"]))
    #print s.simple_sms_send_with_postback(phone_number, message, "http://google.com")

    #display_dictionary(s.get_unread_incoming_messages())
    
    display_dictionary(s.advanced_sms_send(assigned_did, message, [phone_number], reference_id,
                                           scheduled_date_time, status_postback_url))