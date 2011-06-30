#!/usr/bin/env python
#
# CDYNE SMS Notify! Python Module
# By Brandon Smith (brandon.smith@studiobebop.net)
#
import socket, httplib, urllib, urllib2
import time 
import xml.etree.ElementTree as etree

class session:
    def __init__(self, license_key):
        self.__license_key = license_key
        self.__sms_action_url = "http://sms2.cdyne.com/sms.svc"
        self.__max_retries = 5

    def __get_request(self, request):
        """
        Return contents of a given request
        """
        for i in range(0, self.__max_retries):
            try:
                return urllib2.urlopen(request).read()
            except urllib2.URLError:
                time.sleep(3)
            except httplib.BadStatusLine or httplib.InvalidURL:
                time.sleep(3)
            except socket.error or socket.timeout:
                time.sleep(3)
            except:
                import traceback
                traceback.print_exc()
                count += 1
        raise NameError("Failed to grab URL: %s", request)

    def __xml_to_dictionary(self, xml):
        boolean_keys = ["Queued", "SMSIncomingMessages", "Sent", "Cancelled"]
        root = etree.XML(xml)
        dictionary = {}
        if root is not None:
            for element in root.getchildren():
                element_name = element.tag.split("}")[1]
                element_value = element.text
                if element_name in boolean_keys:
                    if element_value == "true":
                        element_value = True
                    else:
                        element_value = False
                dictionary[element_name] = element_value
        return dictionary

    def simple_sms_send(self, phone_number, message):
        data = {"PhoneNumber": phone_number,
                "LicenseKey": self.__license_key,
                "Message": message}
        request_url = self.__sms_action_url + "/SimpleSMSSend"
        request_url += "?%s" % urllib.urlencode(data)
        response = self.__get_request(request_url)
        return self.__xml_to_dictionary(response)

    def simple_sms_send_with_postback(self, phone_number, message, postback_url):
        data = {"PhoneNumber": phone_number,
                "LicenseKey": self.__license_key,
                "Message": message,
                "SatusPostBackURL": postback_url}
        request_url = self.__sms_action_url + "/SimpleSMSSendWithPostback"
        request_url += "?%s" % urllib.urlencode(data)
        response = self.__get_request(request_url)
        return self.__xml_to_dictionary(response)

    def advanced_sms_send(self, assigned_did, message, phone_numbers, reference_id,
                          scheduled_date_time, status_postback_url):
        data = {"AssignedDID": assigned_did,
                "LicenseKey": self.__license_key,
                "Message": message,
                "PhoneNumbers": phone_numbers,
                "ReferenceID": reference_id,
                "ScheduledDateTIme": scheduled_date_time,
                "StatusPostbackURL": status_postback_url}
        request_url = self.__sms_action_url + "/AdvancedSMSSend"
        request_url += "?%s" % urllib.urlencode(data)
        response = self.__get_request(request_url)
        return self.__xml_to_dictionary(response)