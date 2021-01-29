# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](DefaultApi.md#create_account) | **POST** /2010-04-01/Accounts.json | 
[**create_address**](DefaultApi.md#create_address) | **POST** /2010-04-01/Accounts/{AccountSid}/Addresses.json | 
[**create_application**](DefaultApi.md#create_application) | **POST** /2010-04-01/Accounts/{AccountSid}/Applications.json | 
[**create_call**](DefaultApi.md#create_call) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls.json | 
[**create_call_feedback_summary**](DefaultApi.md#create_call_feedback_summary) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/FeedbackSummary.json | 
[**create_call_recording**](DefaultApi.md#create_call_recording) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json | 
[**create_incoming_phone_number**](DefaultApi.md#create_incoming_phone_number) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json | 
[**create_incoming_phone_number_assigned_add_on**](DefaultApi.md#create_incoming_phone_number_assigned_add_on) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json | 
[**create_incoming_phone_number_local**](DefaultApi.md#create_incoming_phone_number_local) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json | 
[**create_incoming_phone_number_mobile**](DefaultApi.md#create_incoming_phone_number_mobile) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Mobile.json | 
[**create_incoming_phone_number_toll_free**](DefaultApi.md#create_incoming_phone_number_toll_free) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/TollFree.json | 
[**create_message**](DefaultApi.md#create_message) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages.json | 
[**create_message_feedback**](DefaultApi.md#create_message_feedback) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json | 
[**create_new_key**](DefaultApi.md#create_new_key) | **POST** /2010-04-01/Accounts/{AccountSid}/Keys.json | 
[**create_new_signing_key**](DefaultApi.md#create_new_signing_key) | **POST** /2010-04-01/Accounts/{AccountSid}/SigningKeys.json | 
[**create_participant**](DefaultApi.md#create_participant) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json | 
[**create_payments**](DefaultApi.md#create_payments) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json | 
[**create_queue**](DefaultApi.md#create_queue) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues.json | 
[**create_sip_auth_calls_credential_list_mapping**](DefaultApi.md#create_sip_auth_calls_credential_list_mapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings.json | 
[**create_sip_auth_calls_ip_access_control_list_mapping**](DefaultApi.md#create_sip_auth_calls_ip_access_control_list_mapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json | 
[**create_sip_auth_registrations_credential_list_mapping**](DefaultApi.md#create_sip_auth_registrations_credential_list_mapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json | 
[**create_sip_credential**](DefaultApi.md#create_sip_credential) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json | 
[**create_sip_credential_list**](DefaultApi.md#create_sip_credential_list) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json | 
[**create_sip_credential_list_mapping**](DefaultApi.md#create_sip_credential_list_mapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json | 
[**create_sip_domain**](DefaultApi.md#create_sip_domain) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json | 
[**create_sip_ip_access_control_list**](DefaultApi.md#create_sip_ip_access_control_list) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json | 
[**create_sip_ip_access_control_list_mapping**](DefaultApi.md#create_sip_ip_access_control_list_mapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json | 
[**create_sip_ip_address**](DefaultApi.md#create_sip_ip_address) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json | 
[**create_token**](DefaultApi.md#create_token) | **POST** /2010-04-01/Accounts/{AccountSid}/Tokens.json | 
[**create_usage_trigger**](DefaultApi.md#create_usage_trigger) | **POST** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json | 
[**create_validation_request**](DefaultApi.md#create_validation_request) | **POST** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json | 
[**delete_address**](DefaultApi.md#delete_address) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json | 
[**delete_application**](DefaultApi.md#delete_application) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json | 
[**delete_call**](DefaultApi.md#delete_call) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json | 
[**delete_call_feedback_summary**](DefaultApi.md#delete_call_feedback_summary) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Calls/FeedbackSummary/{Sid}.json | 
[**delete_call_recording**](DefaultApi.md#delete_call_recording) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json | 
[**delete_conference_recording**](DefaultApi.md#delete_conference_recording) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json | 
[**delete_connect_app**](DefaultApi.md#delete_connect_app) | **DELETE** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json | 
[**delete_incoming_phone_number**](DefaultApi.md#delete_incoming_phone_number) | **DELETE** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json | 
[**delete_incoming_phone_number_assigned_add_on**](DefaultApi.md#delete_incoming_phone_number_assigned_add_on) | **DELETE** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json | 
[**delete_key**](DefaultApi.md#delete_key) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Keys/{Sid}.json | 
[**delete_media**](DefaultApi.md#delete_media) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json | 
[**delete_message**](DefaultApi.md#delete_message) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json | 
[**delete_outgoing_caller_id**](DefaultApi.md#delete_outgoing_caller_id) | **DELETE** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json | 
[**delete_participant**](DefaultApi.md#delete_participant) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json | 
[**delete_queue**](DefaultApi.md#delete_queue) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json | 
[**delete_recording**](DefaultApi.md#delete_recording) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json | 
[**delete_recording_add_on_result**](DefaultApi.md#delete_recording_add_on_result) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json | 
[**delete_recording_add_on_result_payload**](DefaultApi.md#delete_recording_add_on_result_payload) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json | 
[**delete_recording_transcription**](DefaultApi.md#delete_recording_transcription) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{Sid}.json | 
[**delete_signing_key**](DefaultApi.md#delete_signing_key) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json | 
[**delete_sip_auth_calls_credential_list_mapping**](DefaultApi.md#delete_sip_auth_calls_credential_list_mapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings/{Sid}.json | 
[**delete_sip_auth_calls_ip_access_control_list_mapping**](DefaultApi.md#delete_sip_auth_calls_ip_access_control_list_mapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json | 
[**delete_sip_auth_registrations_credential_list_mapping**](DefaultApi.md#delete_sip_auth_registrations_credential_list_mapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json | 
[**delete_sip_credential**](DefaultApi.md#delete_sip_credential) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json | 
[**delete_sip_credential_list**](DefaultApi.md#delete_sip_credential_list) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json | 
[**delete_sip_credential_list_mapping**](DefaultApi.md#delete_sip_credential_list_mapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json | 
[**delete_sip_domain**](DefaultApi.md#delete_sip_domain) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json | 
[**delete_sip_ip_access_control_list**](DefaultApi.md#delete_sip_ip_access_control_list) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json | 
[**delete_sip_ip_access_control_list_mapping**](DefaultApi.md#delete_sip_ip_access_control_list_mapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json | 
[**delete_sip_ip_address**](DefaultApi.md#delete_sip_ip_address) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json | 
[**delete_transcription**](DefaultApi.md#delete_transcription) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json | 
[**delete_usage_trigger**](DefaultApi.md#delete_usage_trigger) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json | 
[**fetch_account**](DefaultApi.md#fetch_account) | **GET** /2010-04-01/Accounts/{Sid}.json | 
[**fetch_address**](DefaultApi.md#fetch_address) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json | 
[**fetch_application**](DefaultApi.md#fetch_application) | **GET** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json | 
[**fetch_authorized_connect_app**](DefaultApi.md#fetch_authorized_connect_app) | **GET** /2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps/{ConnectAppSid}.json | 
[**fetch_available_phone_number_country**](DefaultApi.md#fetch_available_phone_number_country) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json | 
[**fetch_balance**](DefaultApi.md#fetch_balance) | **GET** /2010-04-01/Accounts/{AccountSid}/Balance.json | 
[**fetch_call**](DefaultApi.md#fetch_call) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json | 
[**fetch_call_feedback**](DefaultApi.md#fetch_call_feedback) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Feedback.json | 
[**fetch_call_feedback_summary**](DefaultApi.md#fetch_call_feedback_summary) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/FeedbackSummary/{Sid}.json | 
[**fetch_call_notification**](DefaultApi.md#fetch_call_notification) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications/{Sid}.json | 
[**fetch_call_recording**](DefaultApi.md#fetch_call_recording) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json | 
[**fetch_conference**](DefaultApi.md#fetch_conference) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json | 
[**fetch_conference_recording**](DefaultApi.md#fetch_conference_recording) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json | 
[**fetch_connect_app**](DefaultApi.md#fetch_connect_app) | **GET** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json | 
[**fetch_incoming_phone_number**](DefaultApi.md#fetch_incoming_phone_number) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json | 
[**fetch_incoming_phone_number_assigned_add_on**](DefaultApi.md#fetch_incoming_phone_number_assigned_add_on) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json | 
[**fetch_incoming_phone_number_assigned_add_on_extension**](DefaultApi.md#fetch_incoming_phone_number_assigned_add_on_extension) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json | 
[**fetch_key**](DefaultApi.md#fetch_key) | **GET** /2010-04-01/Accounts/{AccountSid}/Keys/{Sid}.json | 
[**fetch_media**](DefaultApi.md#fetch_media) | **GET** /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json | 
[**fetch_member**](DefaultApi.md#fetch_member) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json | 
[**fetch_message**](DefaultApi.md#fetch_message) | **GET** /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json | 
[**fetch_notification**](DefaultApi.md#fetch_notification) | **GET** /2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json | 
[**fetch_outgoing_caller_id**](DefaultApi.md#fetch_outgoing_caller_id) | **GET** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json | 
[**fetch_participant**](DefaultApi.md#fetch_participant) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json | 
[**fetch_queue**](DefaultApi.md#fetch_queue) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json | 
[**fetch_recording**](DefaultApi.md#fetch_recording) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json | 
[**fetch_recording_add_on_result**](DefaultApi.md#fetch_recording_add_on_result) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json | 
[**fetch_recording_add_on_result_payload**](DefaultApi.md#fetch_recording_add_on_result_payload) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json | 
[**fetch_recording_transcription**](DefaultApi.md#fetch_recording_transcription) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{Sid}.json | 
[**fetch_short_code**](DefaultApi.md#fetch_short_code) | **GET** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json | 
[**fetch_signing_key**](DefaultApi.md#fetch_signing_key) | **GET** /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json | 
[**fetch_sip_auth_calls_credential_list_mapping**](DefaultApi.md#fetch_sip_auth_calls_credential_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings/{Sid}.json | 
[**fetch_sip_auth_calls_ip_access_control_list_mapping**](DefaultApi.md#fetch_sip_auth_calls_ip_access_control_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json | 
[**fetch_sip_auth_registrations_credential_list_mapping**](DefaultApi.md#fetch_sip_auth_registrations_credential_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json | 
[**fetch_sip_credential**](DefaultApi.md#fetch_sip_credential) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json | 
[**fetch_sip_credential_list**](DefaultApi.md#fetch_sip_credential_list) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json | 
[**fetch_sip_credential_list_mapping**](DefaultApi.md#fetch_sip_credential_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json | 
[**fetch_sip_domain**](DefaultApi.md#fetch_sip_domain) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json | 
[**fetch_sip_ip_access_control_list**](DefaultApi.md#fetch_sip_ip_access_control_list) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json | 
[**fetch_sip_ip_access_control_list_mapping**](DefaultApi.md#fetch_sip_ip_access_control_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json | 
[**fetch_sip_ip_address**](DefaultApi.md#fetch_sip_ip_address) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json | 
[**fetch_transcription**](DefaultApi.md#fetch_transcription) | **GET** /2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json | 
[**fetch_usage_trigger**](DefaultApi.md#fetch_usage_trigger) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json | 
[**list_account**](DefaultApi.md#list_account) | **GET** /2010-04-01/Accounts.json | 
[**list_address**](DefaultApi.md#list_address) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses.json | 
[**list_application**](DefaultApi.md#list_application) | **GET** /2010-04-01/Accounts/{AccountSid}/Applications.json | 
[**list_authorized_connect_app**](DefaultApi.md#list_authorized_connect_app) | **GET** /2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps.json | 
[**list_available_phone_number_country**](DefaultApi.md#list_available_phone_number_country) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json | 
[**list_available_phone_number_local**](DefaultApi.md#list_available_phone_number_local) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Local.json | 
[**list_available_phone_number_machine_to_machine**](DefaultApi.md#list_available_phone_number_machine_to_machine) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/MachineToMachine.json | 
[**list_available_phone_number_mobile**](DefaultApi.md#list_available_phone_number_mobile) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Mobile.json | 
[**list_available_phone_number_national**](DefaultApi.md#list_available_phone_number_national) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/National.json | 
[**list_available_phone_number_shared_cost**](DefaultApi.md#list_available_phone_number_shared_cost) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/SharedCost.json | 
[**list_available_phone_number_toll_free**](DefaultApi.md#list_available_phone_number_toll_free) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/TollFree.json | 
[**list_available_phone_number_voip**](DefaultApi.md#list_available_phone_number_voip) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Voip.json | 
[**list_call**](DefaultApi.md#list_call) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls.json | 
[**list_call_event**](DefaultApi.md#list_call_event) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Events.json | 
[**list_call_notification**](DefaultApi.md#list_call_notification) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications.json | 
[**list_call_recording**](DefaultApi.md#list_call_recording) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json | 
[**list_conference**](DefaultApi.md#list_conference) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences.json | 
[**list_conference_recording**](DefaultApi.md#list_conference_recording) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json | 
[**list_connect_app**](DefaultApi.md#list_connect_app) | **GET** /2010-04-01/Accounts/{AccountSid}/ConnectApps.json | 
[**list_dependent_phone_number**](DefaultApi.md#list_dependent_phone_number) | **GET** /2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json | 
[**list_incoming_phone_number**](DefaultApi.md#list_incoming_phone_number) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json | 
[**list_incoming_phone_number_assigned_add_on**](DefaultApi.md#list_incoming_phone_number_assigned_add_on) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json | 
[**list_incoming_phone_number_assigned_add_on_extension**](DefaultApi.md#list_incoming_phone_number_assigned_add_on_extension) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json | 
[**list_incoming_phone_number_local**](DefaultApi.md#list_incoming_phone_number_local) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json | 
[**list_incoming_phone_number_mobile**](DefaultApi.md#list_incoming_phone_number_mobile) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Mobile.json | 
[**list_incoming_phone_number_toll_free**](DefaultApi.md#list_incoming_phone_number_toll_free) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/TollFree.json | 
[**list_key**](DefaultApi.md#list_key) | **GET** /2010-04-01/Accounts/{AccountSid}/Keys.json | 
[**list_media**](DefaultApi.md#list_media) | **GET** /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media.json | 
[**list_member**](DefaultApi.md#list_member) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json | 
[**list_message**](DefaultApi.md#list_message) | **GET** /2010-04-01/Accounts/{AccountSid}/Messages.json | 
[**list_notification**](DefaultApi.md#list_notification) | **GET** /2010-04-01/Accounts/{AccountSid}/Notifications.json | 
[**list_outgoing_caller_id**](DefaultApi.md#list_outgoing_caller_id) | **GET** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json | 
[**list_participant**](DefaultApi.md#list_participant) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json | 
[**list_queue**](DefaultApi.md#list_queue) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues.json | 
[**list_recording**](DefaultApi.md#list_recording) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings.json | 
[**list_recording_add_on_result**](DefaultApi.md#list_recording_add_on_result) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json | 
[**list_recording_add_on_result_payload**](DefaultApi.md#list_recording_add_on_result_payload) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json | 
[**list_recording_transcription**](DefaultApi.md#list_recording_transcription) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions.json | 
[**list_short_code**](DefaultApi.md#list_short_code) | **GET** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json | 
[**list_signing_key**](DefaultApi.md#list_signing_key) | **GET** /2010-04-01/Accounts/{AccountSid}/SigningKeys.json | 
[**list_sip_auth_calls_credential_list_mapping**](DefaultApi.md#list_sip_auth_calls_credential_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings.json | 
[**list_sip_auth_calls_ip_access_control_list_mapping**](DefaultApi.md#list_sip_auth_calls_ip_access_control_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json | 
[**list_sip_auth_registrations_credential_list_mapping**](DefaultApi.md#list_sip_auth_registrations_credential_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json | 
[**list_sip_credential**](DefaultApi.md#list_sip_credential) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json | 
[**list_sip_credential_list**](DefaultApi.md#list_sip_credential_list) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json | 
[**list_sip_credential_list_mapping**](DefaultApi.md#list_sip_credential_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json | 
[**list_sip_domain**](DefaultApi.md#list_sip_domain) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json | 
[**list_sip_ip_access_control_list**](DefaultApi.md#list_sip_ip_access_control_list) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json | 
[**list_sip_ip_access_control_list_mapping**](DefaultApi.md#list_sip_ip_access_control_list_mapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json | 
[**list_sip_ip_address**](DefaultApi.md#list_sip_ip_address) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json | 
[**list_transcription**](DefaultApi.md#list_transcription) | **GET** /2010-04-01/Accounts/{AccountSid}/Transcriptions.json | 
[**list_usage_record**](DefaultApi.md#list_usage_record) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records.json | 
[**list_usage_record_all_time**](DefaultApi.md#list_usage_record_all_time) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/AllTime.json | 
[**list_usage_record_daily**](DefaultApi.md#list_usage_record_daily) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/Daily.json | 
[**list_usage_record_last_month**](DefaultApi.md#list_usage_record_last_month) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/LastMonth.json | 
[**list_usage_record_monthly**](DefaultApi.md#list_usage_record_monthly) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/Monthly.json | 
[**list_usage_record_this_month**](DefaultApi.md#list_usage_record_this_month) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/ThisMonth.json | 
[**list_usage_record_today**](DefaultApi.md#list_usage_record_today) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/Today.json | 
[**list_usage_record_yearly**](DefaultApi.md#list_usage_record_yearly) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/Yearly.json | 
[**list_usage_record_yesterday**](DefaultApi.md#list_usage_record_yesterday) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Records/Yesterday.json | 
[**list_usage_trigger**](DefaultApi.md#list_usage_trigger) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json | 
[**update_account**](DefaultApi.md#update_account) | **POST** /2010-04-01/Accounts/{Sid}.json | 
[**update_address**](DefaultApi.md#update_address) | **POST** /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json | 
[**update_application**](DefaultApi.md#update_application) | **POST** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json | 
[**update_call**](DefaultApi.md#update_call) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json | 
[**update_call_feedback**](DefaultApi.md#update_call_feedback) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Feedback.json | 
[**update_call_recording**](DefaultApi.md#update_call_recording) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json | 
[**update_conference**](DefaultApi.md#update_conference) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json | 
[**update_conference_recording**](DefaultApi.md#update_conference_recording) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json | 
[**update_connect_app**](DefaultApi.md#update_connect_app) | **POST** /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json | 
[**update_incoming_phone_number**](DefaultApi.md#update_incoming_phone_number) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json | 
[**update_key**](DefaultApi.md#update_key) | **POST** /2010-04-01/Accounts/{AccountSid}/Keys/{Sid}.json | 
[**update_member**](DefaultApi.md#update_member) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json | 
[**update_message**](DefaultApi.md#update_message) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json | 
[**update_outgoing_caller_id**](DefaultApi.md#update_outgoing_caller_id) | **POST** /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json | 
[**update_participant**](DefaultApi.md#update_participant) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json | 
[**update_payments**](DefaultApi.md#update_payments) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json | 
[**update_queue**](DefaultApi.md#update_queue) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json | 
[**update_short_code**](DefaultApi.md#update_short_code) | **POST** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json | 
[**update_signing_key**](DefaultApi.md#update_signing_key) | **POST** /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json | 
[**update_sip_credential**](DefaultApi.md#update_sip_credential) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json | 
[**update_sip_credential_list**](DefaultApi.md#update_sip_credential_list) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json | 
[**update_sip_domain**](DefaultApi.md#update_sip_domain) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json | 
[**update_sip_ip_access_control_list**](DefaultApi.md#update_sip_ip_access_control_list) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json | 
[**update_sip_ip_address**](DefaultApi.md#update_sip_ip_address) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json | 
[**update_usage_trigger**](DefaultApi.md#update_usage_trigger) | **POST** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json | 


# **create_account**
> ApiV2010Account create_account()



Create a new Twilio Subaccount from the account making the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account import ApiV2010Account
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    friendly_name = "friendly_name_example" # str | A human readable description of the account to create, defaults to `SubAccount Created at {YYYY-MM-DD HH:MM meridian}` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_account(friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| A human readable description of the account to create, defaults to &#x60;SubAccount Created at {YYYY-MM-DD HH:MM meridian}&#x60; | [optional]

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_address**
> ApiV2010AccountAddress create_address(account_sid, city, customer_name, iso_country, postal_code, region, street)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_address import ApiV2010AccountAddress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource.
    city = "city_example" # str | The city of the new address.
    customer_name = "customer_name_example" # str | The name to associate with the new address.
    iso_country = "iso_country_example" # str | The ISO country code of the new address.
    postal_code = "postal_code_example" # str | The postal code of the new address.
    region = "region_example" # str | The state or region of the new address.
    street = "street_example" # str | The number and street address of the new address.
    auto_correct_address = True # bool | Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide. (optional)
    emergency_enabled = True # bool | Whether to enable emergency calling on the new address. Can be: `true` or `false`. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the new address. It can be up to 64 characters long. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_address(account_sid, city, customer_name, iso_country, postal_code, region, street)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_address(account_sid, city, customer_name, iso_country, postal_code, region, street, auto_correct_address=auto_correct_address, emergency_enabled=emergency_enabled, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Address resource. |
 **city** | **str**| The city of the new address. |
 **customer_name** | **str**| The name to associate with the new address. |
 **iso_country** | **str**| The ISO country code of the new address. |
 **postal_code** | **str**| The postal code of the new address. |
 **region** | **str**| The state or region of the new address. |
 **street** | **str**| The number and street address of the new address. |
 **auto_correct_address** | **bool**| Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide. | [optional]
 **emergency_enabled** | **bool**| Whether to enable emergency calling on the new address. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the new address. It can be up to 64 characters long. | [optional]

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> ApiV2010AccountApplication create_application(account_sid)



Create a new application within your account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_application import ApiV2010AccountApplication
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    api_version = "api_version_example" # str | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is the account's default API version. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the new application. It can be up to 64 characters long. (optional)
    message_status_callback = "message_status_callback_example" # str | The URL we should call using a POST method to send message status information to your application. (optional)
    sms_fallback_method = "head" # str | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`. (optional)
    sms_status_callback = "sms_status_callback_example" # str | The URL we should call using a POST method to send status information about SMS messages sent by the application. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`. (optional)
    voice_caller_id_lookup = True # bool | Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`. (optional)
    voice_url = "voice_url_example" # str | The URL we should call when the phone number assigned to this application receives a call. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_application(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_application(account_sid, api_version=api_version, friendly_name=friendly_name, message_status_callback=message_status_callback, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_status_callback=sms_status_callback, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **api_version** | **str**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is the account&#39;s default API version. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the new application. It can be up to 64 characters long. | [optional]
 **message_status_callback** | **str**| The URL we should call using a POST method to send message status information to your application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **sms_status_callback** | **str**| The URL we should call using a POST method to send status information about SMS messages sent by the application. | [optional]
 **sms_url** | **str**| The URL we should call when the phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_url** | **str**| The URL we should call when the phone number assigned to this application receives a call. | [optional]

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_call**
> ApiV2010AccountCall create_call(account_sid, _from, to)



Create a new outgoing call to phones, SIP-enabled endpoints or Twilio Client connections

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call import ApiV2010AccountCall
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    _from = "_from_example" # str | The phone number or client identifier to use as the caller id. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the `to` parameter is a phone number, `From` must also be a phone number.
    to = "to_example" # str | The phone number, SIP address, or client identifier to call.
    application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Application resource that will handle the call, if the call will be handled by an application. (optional)
    async_amd = "async_amd_example" # str | Select whether to perform answering machine detection in the background. Default, blocks the execution of the call until Answering Machine Detection is completed. Can be: `true` or `false`. (optional)
    async_amd_status_callback = "async_amd_status_callback_example" # str | The URL that we should call using the `async_amd_status_callback_method` to notify customer application whether the call was answered by human, machine or fax. (optional)
    async_amd_status_callback_method = "head" # str | The HTTP method we should use when calling the `async_amd_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`. (optional)
    byoc = "BY62ECB020842930cc01FFCCfeEe150AC" # str | The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta) (optional)
    call_reason = "call_reason_example" # str | The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party's phone. (Branded Calls Beta) (optional)
    caller_id = "caller_id_example" # str | The phone number, SIP address, or Client identifier that made this call. Phone numbers are in [E.164 format](https://wwnw.twilio.com/docs/glossary/what-e164) (e.g., +16175551212). SIP addresses are formatted as `name@company.com`. (optional)
    fallback_method = "head" # str | The HTTP method that we should use to request the `fallback_url`. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    fallback_url = "fallback_url_example" # str | The URL that we call using the `fallback_method` if an error occurs when requesting or executing the TwiML at `url`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    machine_detection = "machine_detection_example" # str | Whether to detect if a human, answering machine, or fax has picked up the call. Can be: `Enable` or `DetectMessageEnd`. Use `Enable` if you would like us to return `AnsweredBy` as soon as the called party is identified. Use `DetectMessageEnd`, if you would like to leave a message on an answering machine. If `send_digits` is provided, this parameter is ignored. For more information, see [Answering Machine Detection](https://www.twilio.com/docs/voice/answering-machine-detection). (optional)
    machine_detection_silence_timeout = 1 # int | The number of milliseconds of initial silence after which an `unknown` AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000. (optional)
    machine_detection_speech_end_threshold = 1 # int | The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200. (optional)
    machine_detection_speech_threshold = 1 # int | The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400. (optional)
    machine_detection_timeout = 1 # int | The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with `AnsweredBy` of `unknown`. The default timeout is 30 seconds. (optional)
    method = "head" # str | The HTTP method we should use when calling the `url` parameter's value. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    record = True # bool | Whether to record the call. Can be `true` to record the phone call, or `false` to not. The default is `false`. The `recording_url` is sent to the `status_callback` URL. (optional)
    recording_channels = "recording_channels_example" # str | The number of channels in the final recording. Can be: `mono` or `dual`. The default is `mono`. `mono` records both legs of the call in a single channel of the recording file. `dual` records each leg to a separate channel of the recording file. The first channel of a dual-channel recording contains the parent call and the second channel contains the child call. (optional)
    recording_status_callback = "recording_status_callback_example" # str | The URL that we call when the recording is available to be accessed. (optional)
    recording_status_callback_event = "recording_status_callback_event_example" # [str] | The recording status events that will trigger calls to the URL specified in `recording_status_callback`. Can be: `in-progress`, `completed` and `absent`. Defaults to `completed`. Separate  multiple values with a space. (optional)
    recording_status_callback_method = "head" # str | The HTTP method we should use when calling the `recording_status_callback` URL. Can be: `GET` or `POST` and the default is `POST`. (optional)
    recording_track = "recording_track_example" # str | The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio. (optional)
    send_digits = "send_digits_example" # str | A string of keys to dial after connecting to the number, maximum of 32 digits. Valid digits in the string include: any digit (`0`-`9`), '`#`', '`*`' and '`w`', to insert a half second pause. For example, if you connected to a company phone number and wanted to pause for one second, and then dial extension 1234 followed by the pound key, the value of this parameter would be `ww1234#`. Remember to URL-encode this string, since the '`#`' character has special meaning in a URL. If both `SendDigits` and `MachineDetection` parameters are provided, then `MachineDetection` will be ignored. (optional)
    sip_auth_password = "sip_auth_password_example" # str | The password required to authenticate the user account specified in `sip_auth_username`. (optional)
    sip_auth_username = "sip_auth_username_example" # str | The username used to authenticate the caller making a SIP call. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. If no `status_callback_event` is specified, we will send the `completed` status. If an `application_sid` parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted). (optional)
    status_callback_event = "status_callback_event_example" # [str] | The call progress events that we will send to the `status_callback` URL. Can be: `initiated`, `ringing`, `answered`, and `completed`. If no event is specified, we send the `completed` status. If you want to receive multiple events, specify each one in a separate `status_callback_event` parameter. See the code sample for [monitoring call progress](https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-create-a-call-resource-and-specify-a-statuscallbackevent&code-sdk-version=json). If an `application_sid` is present, this parameter is ignored. (optional)
    status_callback_method = "head" # str | The HTTP method we should use when calling the `status_callback` URL. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    timeout = 1 # int | The integer number of seconds that we should allow the phone to ring before assuming there is no answer. The default is `60` seconds and the maximum is `600` seconds. For some call flows, we will add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as `15` seconds, to hang up before reaching an answering machine or voicemail. (optional)
    trim = "trim_example" # str | Whether to trim any leading and trailing silence from the recording. Can be: `trim-silence` or `do-not-trim` and the default is `trim-silence`. (optional)
    twiml = "twiml_example" # str | TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both `twiml` and `url` are provided then `twiml` parameter will be ignored. (optional)
    url = "url_example" # str | The absolute URL that returns the TwiML instructions for the call. We will call this URL using the `method` when the call connects. For more information, see the [Url Parameter](https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter) section in [Making Calls](https://www.twilio.com/docs/voice/make-calls). (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_call(account_sid, _from, to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_call: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_call(account_sid, _from, to, application_sid=application_sid, async_amd=async_amd, async_amd_status_callback=async_amd_status_callback, async_amd_status_callback_method=async_amd_status_callback_method, byoc=byoc, call_reason=call_reason, caller_id=caller_id, fallback_method=fallback_method, fallback_url=fallback_url, machine_detection=machine_detection, machine_detection_silence_timeout=machine_detection_silence_timeout, machine_detection_speech_end_threshold=machine_detection_speech_end_threshold, machine_detection_speech_threshold=machine_detection_speech_threshold, machine_detection_timeout=machine_detection_timeout, method=method, record=record, recording_channels=recording_channels, recording_status_callback=recording_status_callback, recording_status_callback_event=recording_status_callback_event, recording_status_callback_method=recording_status_callback_method, recording_track=recording_track, send_digits=send_digits, sip_auth_password=sip_auth_password, sip_auth_username=sip_auth_username, status_callback=status_callback, status_callback_event=status_callback_event, status_callback_method=status_callback_method, timeout=timeout, trim=trim, twiml=twiml, url=url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **_from** | **str**| The phone number or client identifier to use as the caller id. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;From&#x60; must also be a phone number. |
 **to** | **str**| The phone number, SIP address, or client identifier to call. |
 **application_sid** | **str**| The SID of the Application resource that will handle the call, if the call will be handled by an application. | [optional]
 **async_amd** | **str**| Select whether to perform answering machine detection in the background. Default, blocks the execution of the call until Answering Machine Detection is completed. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **async_amd_status_callback** | **str**| The URL that we should call using the &#x60;async_amd_status_callback_method&#x60; to notify customer application whether the call was answered by human, machine or fax. | [optional]
 **async_amd_status_callback_method** | **str**| The HTTP method we should use when calling the &#x60;async_amd_status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional]
 **byoc** | **str**| The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that &#x60;byoc&#x60; is only meaningful when &#x60;to&#x60; is a phone number; it will otherwise be ignored. (Beta) | [optional]
 **call_reason** | **str**| The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party&#39;s phone. (Branded Calls Beta) | [optional]
 **caller_id** | **str**| The phone number, SIP address, or Client identifier that made this call. Phone numbers are in [E.164 format](https://wwnw.twilio.com/docs/glossary/what-e164) (e.g., +16175551212). SIP addresses are formatted as &#x60;name@company.com&#x60;. | [optional]
 **fallback_method** | **str**| The HTTP method that we should use to request the &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **fallback_url** | **str**| The URL that we call using the &#x60;fallback_method&#x60; if an error occurs when requesting or executing the TwiML at &#x60;url&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **machine_detection** | **str**| Whether to detect if a human, answering machine, or fax has picked up the call. Can be: &#x60;Enable&#x60; or &#x60;DetectMessageEnd&#x60;. Use &#x60;Enable&#x60; if you would like us to return &#x60;AnsweredBy&#x60; as soon as the called party is identified. Use &#x60;DetectMessageEnd&#x60;, if you would like to leave a message on an answering machine. If &#x60;send_digits&#x60; is provided, this parameter is ignored. For more information, see [Answering Machine Detection](https://www.twilio.com/docs/voice/answering-machine-detection). | [optional]
 **machine_detection_silence_timeout** | **int**| The number of milliseconds of initial silence after which an &#x60;unknown&#x60; AnsweredBy result will be returned. Possible Values: 2000-10000. Default: 5000. | [optional]
 **machine_detection_speech_end_threshold** | **int**| The number of milliseconds of silence after speech activity at which point the speech activity is considered complete. Possible Values: 500-5000. Default: 1200. | [optional]
 **machine_detection_speech_threshold** | **int**| The number of milliseconds that is used as the measuring stick for the length of the speech activity, where durations lower than this value will be interpreted as a human and longer than this value as a machine. Possible Values: 1000-6000. Default: 2400. | [optional]
 **machine_detection_timeout** | **int**| The number of seconds that we should attempt to detect an answering machine before timing out and sending a voice request with &#x60;AnsweredBy&#x60; of &#x60;unknown&#x60;. The default timeout is 30 seconds. | [optional]
 **method** | **str**| The HTTP method we should use when calling the &#x60;url&#x60; parameter&#39;s value. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **record** | **bool**| Whether to record the call. Can be &#x60;true&#x60; to record the phone call, or &#x60;false&#x60; to not. The default is &#x60;false&#x60;. The &#x60;recording_url&#x60; is sent to the &#x60;status_callback&#x60; URL. | [optional]
 **recording_channels** | **str**| The number of channels in the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60;. The default is &#x60;mono&#x60;. &#x60;mono&#x60; records both legs of the call in a single channel of the recording file. &#x60;dual&#x60; records each leg to a separate channel of the recording file. The first channel of a dual-channel recording contains the parent call and the second channel contains the child call. | [optional]
 **recording_status_callback** | **str**| The URL that we call when the recording is available to be accessed. | [optional]
 **recording_status_callback_event** | **[str]**| The recording status events that will trigger calls to the URL specified in &#x60;recording_status_callback&#x60;. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60; and &#x60;absent&#x60;. Defaults to &#x60;completed&#x60;. Separate  multiple values with a space. | [optional]
 **recording_status_callback_method** | **str**| The HTTP method we should use when calling the &#x60;recording_status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional]
 **recording_track** | **str**| The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is generated from Twilio. &#x60;both&#x60; records the audio that is received and generated by Twilio. | [optional]
 **send_digits** | **str**| A string of keys to dial after connecting to the number, maximum of 32 digits. Valid digits in the string include: any digit (&#x60;0&#x60;-&#x60;9&#x60;), &#39;&#x60;#&#x60;&#39;, &#39;&#x60;*&#x60;&#39; and &#39;&#x60;w&#x60;&#39;, to insert a half second pause. For example, if you connected to a company phone number and wanted to pause for one second, and then dial extension 1234 followed by the pound key, the value of this parameter would be &#x60;ww1234#&#x60;. Remember to URL-encode this string, since the &#39;&#x60;#&#x60;&#39; character has special meaning in a URL. If both &#x60;SendDigits&#x60; and &#x60;MachineDetection&#x60; parameters are provided, then &#x60;MachineDetection&#x60; will be ignored. | [optional]
 **sip_auth_password** | **str**| The password required to authenticate the user account specified in &#x60;sip_auth_username&#x60;. | [optional]
 **sip_auth_username** | **str**| The username used to authenticate the caller making a SIP call. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. If no &#x60;status_callback_event&#x60; is specified, we will send the &#x60;completed&#x60; status. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted). | [optional]
 **status_callback_event** | **[str]**| The call progress events that we will send to the &#x60;status_callback&#x60; URL. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, and &#x60;completed&#x60;. If no event is specified, we send the &#x60;completed&#x60; status. If you want to receive multiple events, specify each one in a separate &#x60;status_callback_event&#x60; parameter. See the code sample for [monitoring call progress](https://www.twilio.com/docs/voice/api/call-resource?code-sample&#x3D;code-create-a-call-resource-and-specify-a-statuscallbackevent&amp;code-sdk-version&#x3D;json). If an &#x60;application_sid&#x60; is present, this parameter is ignored. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use when calling the &#x60;status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **timeout** | **int**| The integer number of seconds that we should allow the phone to ring before assuming there is no answer. The default is &#x60;60&#x60; seconds and the maximum is &#x60;600&#x60; seconds. For some call flows, we will add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as &#x60;15&#x60; seconds, to hang up before reaching an answering machine or voicemail. | [optional]
 **trim** | **str**| Whether to trim any leading and trailing silence from the recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and the default is &#x60;trim-silence&#x60;. | [optional]
 **twiml** | **str**| TwiML instructions for the call Twilio will use without fetching Twiml from url parameter. If both &#x60;twiml&#x60; and &#x60;url&#x60; are provided then &#x60;twiml&#x60; parameter will be ignored. | [optional]
 **url** | **str**| The absolute URL that returns the TwiML instructions for the call. We will call this URL using the &#x60;method&#x60; when the call connects. For more information, see the [Url Parameter](https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter) section in [Making Calls](https://www.twilio.com/docs/voice/make-calls). | [optional]

### Return type

[**ApiV2010AccountCall**](ApiV2010AccountCall.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_call_feedback_summary**
> ApiV2010AccountCallCallFeedbackSummary create_call_feedback_summary(account_sid, end_date, start_date)



Create a FeedbackSummary resource for a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_feedback_summary import ApiV2010AccountCallCallFeedbackSummary
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include feedback given on or before this date. Format is `YYYY-MM-DD` and specified in UTC.
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include feedback given on or after this date. Format is `YYYY-MM-DD` and specified in UTC.
    include_subaccounts = True # bool | Whether to also include Feedback resources from all subaccounts. `true` includes feedback from all subaccounts and `false`, the default, includes feedback from only the specified account. (optional)
    status_callback = "status_callback_example" # str | The URL that we will request when the feedback summary is complete. (optional)
    status_callback_method = "head" # str | The HTTP method (`GET` or `POST`) we use to make the request to the `StatusCallback` URL. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_call_feedback_summary(account_sid, end_date, start_date)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_call_feedback_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_call_feedback_summary(account_sid, end_date, start_date, include_subaccounts=include_subaccounts, status_callback=status_callback, status_callback_method=status_callback_method)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_call_feedback_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **end_date** | **datetime**| Only include feedback given on or before this date. Format is &#x60;YYYY-MM-DD&#x60; and specified in UTC. |
 **start_date** | **datetime**| Only include feedback given on or after this date. Format is &#x60;YYYY-MM-DD&#x60; and specified in UTC. |
 **include_subaccounts** | **bool**| Whether to also include Feedback resources from all subaccounts. &#x60;true&#x60; includes feedback from all subaccounts and &#x60;false&#x60;, the default, includes feedback from only the specified account. | [optional]
 **status_callback** | **str**| The URL that we will request when the feedback summary is complete. | [optional]
 **status_callback_method** | **str**| The HTTP method (&#x60;GET&#x60; or &#x60;POST&#x60;) we use to make the request to the &#x60;StatusCallback&#x60; URL. | [optional]

### Return type

[**ApiV2010AccountCallCallFeedbackSummary**](ApiV2010AccountCallCallFeedbackSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_call_recording**
> ApiV2010AccountCallCallRecording create_call_recording(account_sid, call_sid)



Create a recording for the call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_recording import ApiV2010AccountCallCallRecording
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) to associate the resource with.
    recording_channels = "recording_channels_example" # str | The number of channels used in the recording. Can be: `mono` or `dual` and the default is `mono`. `mono` records all parties of the call into one channel. `dual` records each party of a 2-party call into separate channels. (optional)
    recording_status_callback = "recording_status_callback_example" # str | The URL we should call using the `recording_status_callback_method` on each recording event specified in  `recording_status_callback_event`. For more information, see [RecordingStatusCallback parameters](https://www.twilio.com/docs/voice/api/recording#recordingstatuscallback). (optional)
    recording_status_callback_event = "recording_status_callback_event_example" # [str] | The recording status events on which we should call the `recording_status_callback` URL. Can be: `in-progress`, `completed` and `absent` and the default is `completed`. Separate multiple event values with a space. (optional)
    recording_status_callback_method = "head" # str | The HTTP method we should use to call `recording_status_callback`. Can be: `GET` or `POST` and the default is `POST`. (optional)
    recording_track = "recording_track_example" # str | The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio. (optional)
    trim = "trim_example" # str | Whether to trim any leading and trailing silence in the recording. Can be: `trim-silence` or `do-not-trim` and the default is `do-not-trim`. `trim-silence` trims the silence from the beginning and end of the recording and `do-not-trim` does not. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_call_recording(account_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_call_recording: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_call_recording(account_sid, call_sid, recording_channels=recording_channels, recording_status_callback=recording_status_callback, recording_status_callback_event=recording_status_callback_event, recording_status_callback_method=recording_status_callback_method, recording_track=recording_track, trim=trim)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_call_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **call_sid** | **str**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) to associate the resource with. |
 **recording_channels** | **str**| The number of channels used in the recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. &#x60;mono&#x60; records all parties of the call into one channel. &#x60;dual&#x60; records each party of a 2-party call into separate channels. | [optional]
 **recording_status_callback** | **str**| The URL we should call using the &#x60;recording_status_callback_method&#x60; on each recording event specified in  &#x60;recording_status_callback_event&#x60;. For more information, see [RecordingStatusCallback parameters](https://www.twilio.com/docs/voice/api/recording#recordingstatuscallback). | [optional]
 **recording_status_callback_event** | **[str]**| The recording status events on which we should call the &#x60;recording_status_callback&#x60; URL. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60; and &#x60;absent&#x60; and the default is &#x60;completed&#x60;. Separate multiple event values with a space. | [optional]
 **recording_status_callback_method** | **str**| The HTTP method we should use to call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional]
 **recording_track** | **str**| The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is generated from Twilio. &#x60;both&#x60; records the audio that is received and generated by Twilio. | [optional]
 **trim** | **str**| Whether to trim any leading and trailing silence in the recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and the default is &#x60;do-not-trim&#x60;. &#x60;trim-silence&#x60; trims the silence from the beginning and end of the recording and &#x60;do-not-trim&#x60; does not. | [optional]

### Return type

[**ApiV2010AccountCallCallRecording**](ApiV2010AccountCallCallRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incoming_phone_number**
> ApiV2010AccountIncomingPhoneNumber create_incoming_phone_number(account_sid)



Purchase a phone-number for the account.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number import ApiV2010AccountIncomingPhoneNumber
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. (optional)
    api_version = "api_version_example" # str | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`. (optional)
    area_code = "area_code_example" # str | The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an `area_code` or a `phone_number`.** (US and Canada only). (optional)
    bundle_sid = "BU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. (optional)
    emergency_address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the emergency address configuration to use for emergency calling from the new phone number. (optional)
    emergency_status = "Active" # str | The configuration status parameter that determines whether the new phone number is enabled for emergency calling. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number. (optional)
    identity_sid = "RI62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. (optional)
    phone_number = "phone_number_example" # str | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. (optional)
    sms_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application. (optional)
    sms_fallback_method = "head" # str | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the new phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    trunk_sid = "TK62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa. (optional)
    voice_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa. (optional)
    voice_caller_id_lookup = True # bool | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_receive_mode = "voice" # str | The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: `fax` or `voice` and defaults to `voice`. (optional)
    voice_url = "voice_url_example" # str | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_incoming_phone_number(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_incoming_phone_number(account_sid, address_sid=address_sid, api_version=api_version, area_code=area_code, bundle_sid=bundle_sid, emergency_address_sid=emergency_address_sid, emergency_status=emergency_status, friendly_name=friendly_name, identity_sid=identity_sid, phone_number=phone_number, sms_application_sid=sms_application_sid, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, trunk_sid=trunk_sid, voice_application_sid=voice_application_sid, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_receive_mode=voice_receive_mode, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **address_sid** | **str**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional]
 **api_version** | **str**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional]
 **area_code** | **str**| The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an &#x60;area_code&#x60; or a &#x60;phone_number&#x60;.** (US and Canada only). | [optional]
 **bundle_sid** | **str**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional]
 **emergency_address_sid** | **str**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional]
 **emergency_status** | **str**| The configuration status parameter that determines whether the new phone number is enabled for emergency calling. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number. | [optional]
 **identity_sid** | **str**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. | [optional]
 **phone_number** | **str**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. | [optional]
 **sms_application_sid** | **str**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_url** | **str**| The URL we should call when the new phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **trunk_sid** | **str**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional]
 **voice_application_sid** | **str**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_receive_mode** | **str**| The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: &#x60;fax&#x60; or &#x60;voice&#x60; and defaults to &#x60;voice&#x60;. | [optional]
 **voice_url** | **str**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional]

### Return type

[**ApiV2010AccountIncomingPhoneNumber**](ApiV2010AccountIncomingPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incoming_phone_number_assigned_add_on**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn create_incoming_phone_number_assigned_add_on(account_sid, resource_sid, installed_add_on_sid)



Assign an Add-on installation to the Number specified.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    resource_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Phone Number to assign the Add-on.
    installed_add_on_sid = "XE62ECB020842930cc01FFCCfeEe150AC" # str | The SID that identifies the Add-on installation.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_incoming_phone_number_assigned_add_on(account_sid, resource_sid, installed_add_on_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_assigned_add_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **resource_sid** | **str**| The SID of the Phone Number to assign the Add-on. |
 **installed_add_on_sid** | **str**| The SID that identifies the Add-on installation. |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incoming_phone_number_local**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal create_incoming_phone_number_local(account_sid, phone_number)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number_incoming_phone_number_local import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    phone_number = "phone_number_example" # str | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. (optional)
    api_version = "api_version_example" # str | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`. (optional)
    bundle_sid = "BU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. (optional)
    emergency_address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the emergency address configuration to use for emergency calling from the new phone number. (optional)
    emergency_status = "Active" # str | The configuration status parameter that determines whether the new phone number is enabled for emergency calling. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. (optional)
    identity_sid = "RI62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. (optional)
    sms_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application. (optional)
    sms_fallback_method = "head" # str | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the new phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    trunk_sid = "TK62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa. (optional)
    voice_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa. (optional)
    voice_caller_id_lookup = True # bool | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_receive_mode = "voice" # str | The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: `fax` or `voice` and defaults to `voice`. (optional)
    voice_url = "voice_url_example" # str | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_incoming_phone_number_local(account_sid, phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_local: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_incoming_phone_number_local(account_sid, phone_number, address_sid=address_sid, api_version=api_version, bundle_sid=bundle_sid, emergency_address_sid=emergency_address_sid, emergency_status=emergency_status, friendly_name=friendly_name, identity_sid=identity_sid, sms_application_sid=sms_application_sid, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, trunk_sid=trunk_sid, voice_application_sid=voice_application_sid, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_receive_mode=voice_receive_mode, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_local: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **phone_number** | **str**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. |
 **address_sid** | **str**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional]
 **api_version** | **str**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional]
 **bundle_sid** | **str**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional]
 **emergency_address_sid** | **str**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional]
 **emergency_status** | **str**| The configuration status parameter that determines whether the new phone number is enabled for emergency calling. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. | [optional]
 **identity_sid** | **str**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. | [optional]
 **sms_application_sid** | **str**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_url** | **str**| The URL we should call when the new phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **trunk_sid** | **str**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional]
 **voice_application_sid** | **str**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_receive_mode** | **str**| The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: &#x60;fax&#x60; or &#x60;voice&#x60; and defaults to &#x60;voice&#x60;. | [optional]
 **voice_url** | **str**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional]

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberLocal.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incoming_phone_number_mobile**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile create_incoming_phone_number_mobile(account_sid, phone_number)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number_incoming_phone_number_mobile import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    phone_number = "phone_number_example" # str | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. (optional)
    api_version = "api_version_example" # str | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`. (optional)
    bundle_sid = "BU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. (optional)
    emergency_address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the emergency address configuration to use for emergency calling from the new phone number. (optional)
    emergency_status = "Active" # str | The configuration status parameter that determines whether the new phone number is enabled for emergency calling. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, the is a formatted version of the phone number. (optional)
    identity_sid = "RI62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. (optional)
    sms_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those of the application. (optional)
    sms_fallback_method = "head" # str | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the new phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    trunk_sid = "TK62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa. (optional)
    voice_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa. (optional)
    voice_caller_id_lookup = True # bool | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_receive_mode = "voice" # str | The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: `fax` or `voice` and defaults to `voice`. (optional)
    voice_url = "voice_url_example" # str | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_incoming_phone_number_mobile(account_sid, phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_mobile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_incoming_phone_number_mobile(account_sid, phone_number, address_sid=address_sid, api_version=api_version, bundle_sid=bundle_sid, emergency_address_sid=emergency_address_sid, emergency_status=emergency_status, friendly_name=friendly_name, identity_sid=identity_sid, sms_application_sid=sms_application_sid, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, trunk_sid=trunk_sid, voice_application_sid=voice_application_sid, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_receive_mode=voice_receive_mode, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **phone_number** | **str**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. |
 **address_sid** | **str**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional]
 **api_version** | **str**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional]
 **bundle_sid** | **str**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional]
 **emergency_address_sid** | **str**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional]
 **emergency_status** | **str**| The configuration status parameter that determines whether the new phone number is enabled for emergency calling. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, the is a formatted version of the phone number. | [optional]
 **identity_sid** | **str**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. | [optional]
 **sms_application_sid** | **str**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those of the application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_url** | **str**| The URL we should call when the new phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **trunk_sid** | **str**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional]
 **voice_application_sid** | **str**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_receive_mode** | **str**| The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: &#x60;fax&#x60; or &#x60;voice&#x60; and defaults to &#x60;voice&#x60;. | [optional]
 **voice_url** | **str**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional]

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incoming_phone_number_toll_free**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree create_incoming_phone_number_toll_free(account_sid, phone_number)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number_incoming_phone_number_toll_free import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    phone_number = "phone_number_example" # str | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. (optional)
    api_version = "api_version_example" # str | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`. (optional)
    bundle_sid = "BU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. (optional)
    emergency_address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the emergency address configuration to use for emergency calling from the new phone number. (optional)
    emergency_status = "Active" # str | The configuration status parameter that determines whether the new phone number is enabled for emergency calling. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. (optional)
    identity_sid = "RI62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Identity resource that we should associate with the new phone number. Some regions require an Identity to meet local regulations. (optional)
    sms_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application. (optional)
    sms_fallback_method = "head" # str | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the new phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    trunk_sid = "TK62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa. (optional)
    voice_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa. (optional)
    voice_caller_id_lookup = True # bool | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_receive_mode = "voice" # str | The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: `fax` or `voice` and defaults to `voice`. (optional)
    voice_url = "voice_url_example" # str | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_incoming_phone_number_toll_free(account_sid, phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_toll_free: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_incoming_phone_number_toll_free(account_sid, phone_number, address_sid=address_sid, api_version=api_version, bundle_sid=bundle_sid, emergency_address_sid=emergency_address_sid, emergency_status=emergency_status, friendly_name=friendly_name, identity_sid=identity_sid, sms_application_sid=sms_application_sid, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, trunk_sid=trunk_sid, voice_application_sid=voice_application_sid, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_receive_mode=voice_receive_mode, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_incoming_phone_number_toll_free: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **phone_number** | **str**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. |
 **address_sid** | **str**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional]
 **api_version** | **str**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional]
 **bundle_sid** | **str**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional]
 **emergency_address_sid** | **str**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional]
 **emergency_status** | **str**| The configuration status parameter that determines whether the new phone number is enabled for emergency calling. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. | [optional]
 **identity_sid** | **str**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an Identity to meet local regulations. | [optional]
 **sms_application_sid** | **str**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all &#x60;sms_*_url&#x60; values and use those of the application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_url** | **str**| The URL we should call when the new phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **trunk_sid** | **str**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional]
 **voice_application_sid** | **str**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_receive_mode** | **str**| The configuration parameter for the new phone number to receive incoming voice calls or faxes. Can be: &#x60;fax&#x60; or &#x60;voice&#x60; and defaults to &#x60;voice&#x60;. | [optional]
 **voice_url** | **str**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional]

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberTollFree.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_message**
> ApiV2010AccountMessage create_message(account_sid, to)



Send a message from the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_message import ApiV2010AccountMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    to = "to_example" # str | The destination phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format for SMS/MMS or [Channel user address](https://www.twilio.com/docs/sms/channels#channel-addresses) for other 3rd-party channels.
    address_retention = "retain" # str | Determines if the address can be stored or obfuscated based on privacy settings (optional) if omitted the server will use the default value of "retain"
    application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application that should receive message status. We POST a `message_sid` parameter and a `message_status` parameter with a value of `sent` or `failed` to the [application](https://www.twilio.com/docs/usage/api/applications)'s `message_status_callback`. If a `status_callback` parameter is also passed, it will be ignored and the application's `message_status_callback` parameter will be used. (optional)
    attempt = 1 # int | Total number of attempts made ( including this ) to send out the message regardless of the provider used (optional)
    body = "body_example" # str | The text of the message you want to send. Can be up to 1,600 characters in length. (optional)
    content_retention = "retain" # str | Determines if the message content can be stored or redacted based on privacy settings (optional) if omitted the server will use the default value of "retain"
    force_delivery = True # bool | Reserved (optional)
    _from = "_from_example" # str | A Twilio phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, an [alphanumeric sender ID](https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id), or a [Channel Endpoint address](https://www.twilio.com/docs/sms/channels#channel-addresses) that is enabled for the type of message you want to send. Phone numbers or [short codes](https://www.twilio.com/docs/sms/api/short-code) purchased from Twilio also work here. You cannot, for example, spoof messages from a private cell phone number. If you are using `messaging_service_sid`, this parameter must be empty. (optional)
    max_price = 3.14 # float | The maximum total price in US dollars that you will pay for the message to be delivered. Can be a decimal value that has up to 4 decimal places. All messages are queued for delivery and the message cost is checked before the message is sent. If the cost exceeds `max_price`, the message will fail and a status of `Failed` is sent to the status callback. If `MaxPrice` is not set, the message cost is not checked. (optional)
    media_url = "media_url_example" # [str] | The URL of the media to send with the message. The media can be of type `gif`, `png`, and `jpeg` and will be formatted correctly on the recipient's device. The media size limit is 5MB for supported file types (JPEG, PNG, GIF) and 500KB for [other types](https://www.twilio.com/docs/sms/accepted-mime-types) of accepted media. To send more than one image in the message body, provide multiple `media_url` parameters in the POST request. You can include up to 10 `media_url` parameters per message. You can send images in an SMS message in only the US and Canada. (optional)
    messaging_service_sid = "MG62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services#send-a-message-with-copilot) you want to associate with the Message. Set this parameter to use the [Messaging Service Settings and Copilot Features](https://www.twilio.com/console/sms/services) you have configured and leave the `from` parameter empty. When only this parameter is set, Twilio will use your enabled Copilot Features to select the `from` phone number for delivery. (optional)
    persistent_action = "persistent_action_example" # [str] | Rich actions for Channels Messages. (optional)
    provide_feedback = True # bool | Whether to confirm delivery of the message. Set this value to `true` if you are sending messages that have a trackable user action and you intend to confirm delivery of the message using the [Message Feedback API](https://www.twilio.com/docs/sms/api/message-feedback-resource). This parameter is `false` by default. (optional)
    smart_encoded = True # bool | Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: `true` or `false`. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. If specified, we POST these message status changes to the URL: `queued`, `failed`, `sent`, `delivered`, or `undelivered`. Twilio will POST its [standard request parameters](https://www.twilio.com/docs/sms/twiml#request-parameters) as well as some additional parameters including `MessageSid`, `MessageStatus`, and `ErrorCode`. If you include this parameter with the `messaging_service_sid`, we use this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/sms/services/api). URLs must contain a valid hostname and underscores are not allowed. (optional)
    validity_period = 1 # int | How long in seconds the message can remain in our outgoing message queue. After this period elapses, the message fails and we call your status callback. Can be between 1 and the default value of 14,400 seconds. After a message has been accepted by a carrier, however, we cannot guarantee that the message will not be queued after this period. We recommend that this value be at least 5 seconds. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_message(account_sid, to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_message(account_sid, to, address_retention=address_retention, application_sid=application_sid, attempt=attempt, body=body, content_retention=content_retention, force_delivery=force_delivery, _from=_from, max_price=max_price, media_url=media_url, messaging_service_sid=messaging_service_sid, persistent_action=persistent_action, provide_feedback=provide_feedback, smart_encoded=smart_encoded, status_callback=status_callback, validity_period=validity_period)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **to** | **str**| The destination phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format for SMS/MMS or [Channel user address](https://www.twilio.com/docs/sms/channels#channel-addresses) for other 3rd-party channels. |
 **address_retention** | **str**| Determines if the address can be stored or obfuscated based on privacy settings | [optional] if omitted the server will use the default value of "retain"
 **application_sid** | **str**| The SID of the application that should receive message status. We POST a &#x60;message_sid&#x60; parameter and a &#x60;message_status&#x60; parameter with a value of &#x60;sent&#x60; or &#x60;failed&#x60; to the [application](https://www.twilio.com/docs/usage/api/applications)&#39;s &#x60;message_status_callback&#x60;. If a &#x60;status_callback&#x60; parameter is also passed, it will be ignored and the application&#39;s &#x60;message_status_callback&#x60; parameter will be used. | [optional]
 **attempt** | **int**| Total number of attempts made ( including this ) to send out the message regardless of the provider used | [optional]
 **body** | **str**| The text of the message you want to send. Can be up to 1,600 characters in length. | [optional]
 **content_retention** | **str**| Determines if the message content can be stored or redacted based on privacy settings | [optional] if omitted the server will use the default value of "retain"
 **force_delivery** | **bool**| Reserved | [optional]
 **_from** | **str**| A Twilio phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, an [alphanumeric sender ID](https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id), or a [Channel Endpoint address](https://www.twilio.com/docs/sms/channels#channel-addresses) that is enabled for the type of message you want to send. Phone numbers or [short codes](https://www.twilio.com/docs/sms/api/short-code) purchased from Twilio also work here. You cannot, for example, spoof messages from a private cell phone number. If you are using &#x60;messaging_service_sid&#x60;, this parameter must be empty. | [optional]
 **max_price** | **float**| The maximum total price in US dollars that you will pay for the message to be delivered. Can be a decimal value that has up to 4 decimal places. All messages are queued for delivery and the message cost is checked before the message is sent. If the cost exceeds &#x60;max_price&#x60;, the message will fail and a status of &#x60;Failed&#x60; is sent to the status callback. If &#x60;MaxPrice&#x60; is not set, the message cost is not checked. | [optional]
 **media_url** | **[str]**| The URL of the media to send with the message. The media can be of type &#x60;gif&#x60;, &#x60;png&#x60;, and &#x60;jpeg&#x60; and will be formatted correctly on the recipient&#39;s device. The media size limit is 5MB for supported file types (JPEG, PNG, GIF) and 500KB for [other types](https://www.twilio.com/docs/sms/accepted-mime-types) of accepted media. To send more than one image in the message body, provide multiple &#x60;media_url&#x60; parameters in the POST request. You can include up to 10 &#x60;media_url&#x60; parameters per message. You can send images in an SMS message in only the US and Canada. | [optional]
 **messaging_service_sid** | **str**| The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services#send-a-message-with-copilot) you want to associate with the Message. Set this parameter to use the [Messaging Service Settings and Copilot Features](https://www.twilio.com/console/sms/services) you have configured and leave the &#x60;from&#x60; parameter empty. When only this parameter is set, Twilio will use your enabled Copilot Features to select the &#x60;from&#x60; phone number for delivery. | [optional]
 **persistent_action** | **[str]**| Rich actions for Channels Messages. | [optional]
 **provide_feedback** | **bool**| Whether to confirm delivery of the message. Set this value to &#x60;true&#x60; if you are sending messages that have a trackable user action and you intend to confirm delivery of the message using the [Message Feedback API](https://www.twilio.com/docs/sms/api/message-feedback-resource). This parameter is &#x60;false&#x60; by default. | [optional]
 **smart_encoded** | **bool**| Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. If specified, we POST these message status changes to the URL: &#x60;queued&#x60;, &#x60;failed&#x60;, &#x60;sent&#x60;, &#x60;delivered&#x60;, or &#x60;undelivered&#x60;. Twilio will POST its [standard request parameters](https://www.twilio.com/docs/sms/twiml#request-parameters) as well as some additional parameters including &#x60;MessageSid&#x60;, &#x60;MessageStatus&#x60;, and &#x60;ErrorCode&#x60;. If you include this parameter with the &#x60;messaging_service_sid&#x60;, we use this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/sms/services/api). URLs must contain a valid hostname and underscores are not allowed. | [optional]
 **validity_period** | **int**| How long in seconds the message can remain in our outgoing message queue. After this period elapses, the message fails and we call your status callback. Can be between 1 and the default value of 14,400 seconds. After a message has been accepted by a carrier, however, we cannot guarantee that the message will not be queued after this period. We recommend that this value be at least 5 seconds. | [optional]

### Return type

[**ApiV2010AccountMessage**](ApiV2010AccountMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_message_feedback**
> ApiV2010AccountMessageMessageFeedback create_message_feedback(account_sid, message_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_message_message_feedback import ApiV2010AccountMessageMessageFeedback
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    message_sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The SID of the Message resource for which the feedback was provided.
    outcome = "confirmed" # str | Whether the feedback has arrived. Can be: `unconfirmed` or `confirmed`. If `provide_feedback`=`true` in [the initial HTTP POST](https://www.twilio.com/docs/sms/api/message-resource#create-a-message-resource), the initial value of this property is `unconfirmed`. After the message arrives, update the value to `confirmed`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_message_feedback(account_sid, message_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_message_feedback: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_message_feedback(account_sid, message_sid, outcome=outcome)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_message_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **message_sid** | **str**| The SID of the Message resource for which the feedback was provided. |
 **outcome** | **str**| Whether the feedback has arrived. Can be: &#x60;unconfirmed&#x60; or &#x60;confirmed&#x60;. If &#x60;provide_feedback&#x60;&#x3D;&#x60;true&#x60; in [the initial HTTP POST](https://www.twilio.com/docs/sms/api/message-resource#create-a-message-resource), the initial value of this property is &#x60;unconfirmed&#x60;. After the message arrives, update the value to &#x60;confirmed&#x60;. | [optional]

### Return type

[**ApiV2010AccountMessageMessageFeedback**](ApiV2010AccountMessageMessageFeedback.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_key**
> ApiV2010AccountNewKey create_new_key(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_new_key import ApiV2010AccountNewKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource.
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_new_key(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_new_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_new_key(account_sid, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_new_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource. |
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]

### Return type

[**ApiV2010AccountNewKey**](ApiV2010AccountNewKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_signing_key**
> ApiV2010AccountNewSigningKey create_new_signing_key(account_sid)



Create a new Signing Key for the account making the request.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_new_signing_key import ApiV2010AccountNewSigningKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource.
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_new_signing_key(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_new_signing_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_new_signing_key(account_sid, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_new_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource. |
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]

### Return type

[**ApiV2010AccountNewSigningKey**](ApiV2010AccountNewSigningKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_participant**
> ApiV2010AccountConferenceParticipant create_participant(account_sid, conference_sid, _from, to)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference_participant import ApiV2010AccountConferenceParticipant
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    conference_sid = "ConferenceSid_example" # str | The SID of the participant's conference.
    _from = "_from_example" # str | The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the `to` parameter is a phone number, `from` must also be a phone number. If `to` is sip address, this value of `from` should be a username portion to be used to populate the P-Asserted-Identity header that is passed to the SIP endpoint.
    to = "to_example" # str | The phone number, SIP address, or Client identifier that received this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as `sip:name@company.com`. Client identifiers are formatted `client:name`. [Custom parameters](https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters) may also be specified.
    beep = "beep_example" # str | Whether to play a notification beep to the conference when the participant joins. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`. (optional)
    byoc = "BY62ECB020842930cc01FFCCfeEe150AC" # str | The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that `byoc` is only meaningful when `to` is a phone number; it will otherwise be ignored. (Beta) (optional)
    call_reason = "call_reason_example" # str | The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party's phone. (Branded Calls Beta) (optional)
    call_sid_to_coach = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`. (optional)
    caller_id = "caller_id_example" # str | The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted `client:name`. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the `to` parameter is a phone number, `callerId` must also be a phone number. If `to` is sip address, this value of `callerId` should be a username portion to be used to populate the From header that is passed to the SIP endpoint. (optional)
    coaching = True # bool | Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined. (optional)
    conference_record = "conference_record_example" # str | Whether to record the conference the participant is joining. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`. (optional)
    conference_recording_status_callback = "conference_recording_status_callback_example" # str | The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available. (optional)
    conference_recording_status_callback_event = "conference_recording_status_callback_event_example" # [str] | The conference recording state changes that generate a call to `conference_recording_status_callback`. Can be: `in-progress`, `completed`, and `failed`. Separate multiple values with a space. The default value is `in-progress completed failed`. (optional)
    conference_recording_status_callback_method = "head" # str | The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    conference_status_callback = "conference_status_callback_example" # str | The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored. (optional)
    conference_status_callback_event = "conference_status_callback_event_example" # [str] | The conference state changes that should generate a call to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, and `speaker`. Separate multiple values with a space. Defaults to `start end`. (optional)
    conference_status_callback_method = "head" # str | The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    conference_trim = "conference_trim_example" # str | Whether to trim leading and trailing silence from your recorded conference audio files. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`. (optional)
    early_media = True # bool | Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. Can be: `true` or `false` and defaults to `true`. (optional)
    end_conference_on_exit = True # bool | Whether to end the conference when the participant leaves. Can be: `true` or `false` and defaults to `false`. (optional)
    jitter_buffer_size = "jitter_buffer_size_example" # str | Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant's audio is mixed into the conference. Can be: `off`, `small`, `medium`, and `large`. Default to `large`. (optional)
    label = "label_example" # str | A label for this participant. If one is supplied, it may subsequently be used to fetch, update or delete the participant. (optional)
    max_participants = 1 # int | The maximum number of participants in the conference. Can be a positive integer from `2` to `250`. The default value is `250`. (optional)
    muted = True # bool | Whether the agent is muted in the conference. Can be `true` or `false` and the default is `false`. (optional)
    record = True # bool | Whether to record the participant and their conferences, including the time between conferences. Can be `true` or `false` and the default is `false`. (optional)
    recording_channels = "recording_channels_example" # str | The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`. (optional)
    recording_status_callback = "recording_status_callback_example" # str | The URL that we should call using the `recording_status_callback_method` when the recording status changes. (optional)
    recording_status_callback_event = "recording_status_callback_event_example" # [str] | The recording state changes that should generate a call to `recording_status_callback`. Can be: `in-progress`, `completed`, and `failed`. Separate multiple values with a space. The default value is `in-progress completed failed`. (optional)
    recording_status_callback_method = "head" # str | The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    recording_track = "recording_track_example" # str | The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is sent from Twilio. `both` records the audio that is received and sent by Twilio. (optional)
    region = "region_example" # str | The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`. (optional)
    sip_auth_password = "sip_auth_password_example" # str | The SIP password for authentication. (optional)
    sip_auth_username = "sip_auth_username_example" # str | The SIP username used for authentication. (optional)
    start_conference_on_enter = True # bool | Whether to start the conference when the participant joins, if it has not already started. Can be: `true` or `false` and the default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_event = "status_callback_event_example" # [str] | The conference state changes that should generate a call to `status_callback`. Can be: `initiated`, `ringing`, `answered`, and `completed`. Separate multiple values with a space. The default value is `completed`. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` and `POST` and defaults to `POST`. (optional)
    timeout = 1 # int | The number of seconds that we should allow the phone to ring before assuming there is no answer. Can be an integer between `5` and `600`, inclusive. The default value is `60`. We always add a 5-second timeout buffer to outgoing calls, so  value of 10 would result in an actual timeout that was closer to 15 seconds. (optional)
    wait_method = "head" # str | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file. (optional)
    wait_url = "wait_url_example" # str | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_participant(account_sid, conference_sid, _from, to)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_participant(account_sid, conference_sid, _from, to, beep=beep, byoc=byoc, call_reason=call_reason, call_sid_to_coach=call_sid_to_coach, caller_id=caller_id, coaching=coaching, conference_record=conference_record, conference_recording_status_callback=conference_recording_status_callback, conference_recording_status_callback_event=conference_recording_status_callback_event, conference_recording_status_callback_method=conference_recording_status_callback_method, conference_status_callback=conference_status_callback, conference_status_callback_event=conference_status_callback_event, conference_status_callback_method=conference_status_callback_method, conference_trim=conference_trim, early_media=early_media, end_conference_on_exit=end_conference_on_exit, jitter_buffer_size=jitter_buffer_size, label=label, max_participants=max_participants, muted=muted, record=record, recording_channels=recording_channels, recording_status_callback=recording_status_callback, recording_status_callback_event=recording_status_callback_event, recording_status_callback_method=recording_status_callback_method, recording_track=recording_track, region=region, sip_auth_password=sip_auth_password, sip_auth_username=sip_auth_username, start_conference_on_enter=start_conference_on_enter, status_callback=status_callback, status_callback_event=status_callback_event, status_callback_method=status_callback_method, timeout=timeout, wait_method=wait_method, wait_url=wait_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **conference_sid** | **str**| The SID of the participant&#39;s conference. |
 **_from** | **str**| The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted &#x60;client:name&#x60;. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;from&#x60; must also be a phone number. If &#x60;to&#x60; is sip address, this value of &#x60;from&#x60; should be a username portion to be used to populate the P-Asserted-Identity header that is passed to the SIP endpoint. |
 **to** | **str**| The phone number, SIP address, or Client identifier that received this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). SIP addresses are formatted as &#x60;sip:name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. [Custom parameters](https://www.twilio.com/docs/voice/api/conference-participant-resource#custom-parameters) may also be specified. |
 **beep** | **str**| Whether to play a notification beep to the conference when the participant joins. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;. | [optional]
 **byoc** | **str**| The SID of a BYOC (Bring Your Own Carrier) trunk to route this call with. Note that &#x60;byoc&#x60; is only meaningful when &#x60;to&#x60; is a phone number; it will otherwise be ignored. (Beta) | [optional]
 **call_reason** | **str**| The Reason for the outgoing call. Use it to specify the purpose of the call that is presented on the called party&#39;s phone. (Branded Calls Beta) | [optional]
 **call_sid_to_coach** | **str**| The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;. | [optional]
 **caller_id** | **str**| The phone number, Client identifier, or username portion of SIP address that made this call. Phone numbers are in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (e.g., +16175551212). Client identifiers are formatted &#x60;client:name&#x60;. If using a phone number, it must be a Twilio number or a Verified [outgoing caller id](https://www.twilio.com/docs/voice/api/outgoing-caller-ids) for your account. If the &#x60;to&#x60; parameter is a phone number, &#x60;callerId&#x60; must also be a phone number. If &#x60;to&#x60; is sip address, this value of &#x60;callerId&#x60; should be a username portion to be used to populate the From header that is passed to the SIP endpoint. | [optional]
 **coaching** | **bool**| Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined. | [optional]
 **conference_record** | **str**| Whether to record the conference the participant is joining. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;. | [optional]
 **conference_recording_status_callback** | **str**| The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available. | [optional]
 **conference_recording_status_callback_event** | **[str]**| The conference recording state changes that generate a call to &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60;, and &#x60;failed&#x60;. Separate multiple values with a space. The default value is &#x60;in-progress completed failed&#x60;. | [optional]
 **conference_recording_status_callback_method** | **str**| The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **conference_status_callback** | **str**| The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored. | [optional]
 **conference_status_callback_event** | **[str]**| The conference state changes that should generate a call to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, and &#x60;speaker&#x60;. Separate multiple values with a space. Defaults to &#x60;start end&#x60;. | [optional]
 **conference_status_callback_method** | **str**| The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **conference_trim** | **str**| Whether to trim leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;. | [optional]
 **early_media** | **bool**| Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. | [optional]
 **end_conference_on_exit** | **bool**| Whether to end the conference when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **jitter_buffer_size** | **str**| Jitter buffer size for the connecting participant. Twilio will use this setting to apply Jitter Buffer before participant&#39;s audio is mixed into the conference. Can be: &#x60;off&#x60;, &#x60;small&#x60;, &#x60;medium&#x60;, and &#x60;large&#x60;. Default to &#x60;large&#x60;. | [optional]
 **label** | **str**| A label for this participant. If one is supplied, it may subsequently be used to fetch, update or delete the participant. | [optional]
 **max_participants** | **int**| The maximum number of participants in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;. | [optional]
 **muted** | **bool**| Whether the agent is muted in the conference. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **record** | **bool**| Whether to record the participant and their conferences, including the time between conferences. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **recording_channels** | **str**| The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. | [optional]
 **recording_status_callback** | **str**| The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes. | [optional]
 **recording_status_callback_event** | **[str]**| The recording state changes that should generate a call to &#x60;recording_status_callback&#x60;. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60;, and &#x60;failed&#x60;. Separate multiple values with a space. The default value is &#x60;in-progress completed failed&#x60;. | [optional]
 **recording_status_callback_method** | **str**| The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **recording_track** | **str**| The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is sent from Twilio. &#x60;both&#x60; records the audio that is received and sent by Twilio. | [optional]
 **region** | **str**| The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;. | [optional]
 **sip_auth_password** | **str**| The SIP password for authentication. | [optional]
 **sip_auth_username** | **str**| The SIP username used for authentication. | [optional]
 **start_conference_on_enter** | **bool**| Whether to start the conference when the participant joins, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_event** | **[str]**| The conference state changes that should generate a call to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, and &#x60;completed&#x60;. Separate multiple values with a space. The default value is &#x60;completed&#x60;. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; and &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **timeout** | **int**| The number of seconds that we should allow the phone to ring before assuming there is no answer. Can be an integer between &#x60;5&#x60; and &#x60;600&#x60;, inclusive. The default value is &#x60;60&#x60;. We always add a 5-second timeout buffer to outgoing calls, so  value of 10 would result in an actual timeout that was closer to 15 seconds. | [optional]
 **wait_method** | **str**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional]
 **wait_url** | **str**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional]

### Return type

[**ApiV2010AccountConferenceParticipant**](ApiV2010AccountConferenceParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payments**
> ApiV2010AccountCallPayments create_payments(account_sid, call_sid, idempotency_key, status_callback)



create an instance of payments. This will start a new payments session

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_payments import ApiV2010AccountCallPayments
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF.
    idempotency_key = "idempotency_key_example" # str | A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
    status_callback = "status_callback_example" # str | Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback)
    bank_account_type = "consumer-checking" # str | Type of bank account if payment source is ACH. One of `consumer-checking`, `consumer-savings`, or `commercial-checking`. The default value is `consumer-checking`. (optional)
    charge_amount = 3.14 # float | A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with `currency` field. Leave blank or set to 0 to tokenize. (optional)
    currency = "currency_example" # str | The currency of the `charge_amount`, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is `USD` and all values allowed from the <Pay> Connector are accepted. (optional)
    description = "description_example" # str | The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions. (optional)
    input = "input_example" # str | A list of inputs that should be accepted. Currently only `dtmf` is supported. All digits captured during a pay session are redacted from the logs. (optional)
    min_postal_code_length = 1 # int | A positive integer that is used to validate the length of the `PostalCode` inputted by the user. User must enter this many digits. (optional)
    parameter = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | A single level JSON string that is required when accepting certain information specific only to ACH payments. The information that has to be included here depends on the <Pay> Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors). (optional)
    payment_connector = "payment_connector_example" # str | This is the unique name corresponding to the Payment Gateway Connector installed in the Twilio Add-ons. Learn more about [<Pay> Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is `Default`. (optional)
    payment_method = "credit-card" # str | Type of payment being captured. One of `credit-card` or `ach-debit`. The default value is `credit-card`. (optional)
    postal_code = True # bool | Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is `true`. (optional)
    security_code = True # bool | Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is `true`. (optional)
    timeout = 1 # int | The number of seconds that <Pay> should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is `5`, maximum is `600`. (optional)
    token_type = "one-time" # str | Indicates whether the payment method should be tokenized as a `one-time` or `reusable` token. The default value is `reusable`. Do not enter a charge amount when tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized. (optional)
    valid_card_types = "valid_card_types_example" # str | Credit card types separated by space that Pay should accept. The default value is `visa mastercard amex` (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_payments(account_sid, call_sid, idempotency_key, status_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_payments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_payments(account_sid, call_sid, idempotency_key, status_callback, bank_account_type=bank_account_type, charge_amount=charge_amount, currency=currency, description=description, input=input, min_postal_code_length=min_postal_code_length, parameter=parameter, payment_connector=payment_connector, payment_method=payment_method, postal_code=postal_code, security_code=security_code, timeout=timeout, token_type=token_type, valid_card_types=valid_card_types)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **call_sid** | **str**| The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF. |
 **idempotency_key** | **str**| A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated. |
 **status_callback** | **str**| Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback) |
 **bank_account_type** | **str**| Type of bank account if payment source is ACH. One of &#x60;consumer-checking&#x60;, &#x60;consumer-savings&#x60;, or &#x60;commercial-checking&#x60;. The default value is &#x60;consumer-checking&#x60;. | [optional]
 **charge_amount** | **float**| A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with &#x60;currency&#x60; field. Leave blank or set to 0 to tokenize. | [optional]
 **currency** | **str**| The currency of the &#x60;charge_amount&#x60;, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is &#x60;USD&#x60; and all values allowed from the &lt;Pay&gt; Connector are accepted. | [optional]
 **description** | **str**| The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions. | [optional]
 **input** | **str**| A list of inputs that should be accepted. Currently only &#x60;dtmf&#x60; is supported. All digits captured during a pay session are redacted from the logs. | [optional]
 **min_postal_code_length** | **int**| A positive integer that is used to validate the length of the &#x60;PostalCode&#x60; inputted by the user. User must enter this many digits. | [optional]
 **parameter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| A single level JSON string that is required when accepting certain information specific only to ACH payments. The information that has to be included here depends on the &lt;Pay&gt; Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors). | [optional]
 **payment_connector** | **str**| This is the unique name corresponding to the Payment Gateway Connector installed in the Twilio Add-ons. Learn more about [&lt;Pay&gt; Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is &#x60;Default&#x60;. | [optional]
 **payment_method** | **str**| Type of payment being captured. One of &#x60;credit-card&#x60; or &#x60;ach-debit&#x60;. The default value is &#x60;credit-card&#x60;. | [optional]
 **postal_code** | **bool**| Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;. | [optional]
 **security_code** | **bool**| Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;. | [optional]
 **timeout** | **int**| The number of seconds that &lt;Pay&gt; should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is &#x60;5&#x60;, maximum is &#x60;600&#x60;. | [optional]
 **token_type** | **str**| Indicates whether the payment method should be tokenized as a &#x60;one-time&#x60; or &#x60;reusable&#x60; token. The default value is &#x60;reusable&#x60;. Do not enter a charge amount when tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized. | [optional]
 **valid_card_types** | **str**| Credit card types separated by space that Pay should accept. The default value is &#x60;visa mastercard amex&#x60; | [optional]

### Return type

[**ApiV2010AccountCallPayments**](ApiV2010AccountCallPayments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_queue**
> ApiV2010AccountQueue create_queue(account_sid, friendly_name)



Create a queue

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_queue import ApiV2010AccountQueue
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe this resource. It can be up to 64 characters long.
    max_size = 1 # int | The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_queue(account_sid, friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_queue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_queue(account_sid, friendly_name, max_size=max_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **friendly_name** | **str**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. |
 **max_size** | **int**| The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000. | [optional]

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_auth_calls_credential_list_mapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping create_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, credential_list_sid)



Create a new credential list mapping resource

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_credential_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that will contain the new resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the CredentialList resource to map to the SIP domain.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, credential_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_auth_calls_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **domain_sid** | **str**| The SID of the SIP domain that will contain the new resource. |
 **credential_list_sid** | **str**| The SID of the CredentialList resource to map to the SIP domain. |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_auth_calls_ip_access_control_list_mapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping create_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, ip_access_control_list_sid)



Create a new IP Access Control List mapping

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_ip_access_control_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that will contain the new resource.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the IpAccessControlList resource to map to the SIP domain.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, ip_access_control_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_auth_calls_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **domain_sid** | **str**| The SID of the SIP domain that will contain the new resource. |
 **ip_access_control_list_sid** | **str**| The SID of the IpAccessControlList resource to map to the SIP domain. |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_auth_registrations_credential_list_mapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping create_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, credential_list_sid)



Create a new credential list mapping resource

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_registrations_sip_auth_registrations_credential_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that will contain the new resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the CredentialList resource to map to the SIP domain.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, credential_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_auth_registrations_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **domain_sid** | **str**| The SID of the SIP domain that will contain the new resource. |
 **credential_list_sid** | **str**| The SID of the CredentialList resource to map to the SIP domain. |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_credential**
> ApiV2010AccountSipSipCredentialListSipCredential create_sip_credential(account_sid, credential_list_sid, password, username)



Create a new credential resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_credential_list_sip_credential import ApiV2010AccountSipSipCredentialListSipCredential
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the credential list to include the created credential.
    password = "password_example" # str | The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)
    username = "username_example" # str | The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_credential(account_sid, credential_list_sid, password, username)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **credential_list_sid** | **str**| The unique id that identifies the credential list to include the created credential. |
 **password** | **str**| The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;) |
 **username** | **str**| The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio&#39;s challenge of the initial INVITE. It can be up to 32 characters long. |

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_credential_list**
> ApiV2010AccountSipSipCredentialList create_sip_credential_list(account_sid, friendly_name)



Create a Credential List

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_credential_list import ApiV2010AccountSipSipCredentialList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    friendly_name = "friendly_name_example" # str | A human readable descriptive text that describes the CredentialList, up to 64 characters long.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_credential_list(account_sid, friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **friendly_name** | **str**| A human readable descriptive text that describes the CredentialList, up to 64 characters long. |

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_credential_list_mapping**
> ApiV2010AccountSipSipDomainSipCredentialListMapping create_sip_credential_list_mapping(account_sid, domain_sid, credential_list_sid)



Create a CredentialListMapping resource for an account.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_credential_list_mapping import ApiV2010AccountSipSipDomainSipCredentialListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_credential_list_mapping(account_sid, domain_sid, credential_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped. |
 **credential_list_sid** | **str**| A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain. |

### Return type

[**ApiV2010AccountSipSipDomainSipCredentialListMapping**](ApiV2010AccountSipSipDomainSipCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_domain**
> ApiV2010AccountSipSipDomain create_sip_domain(account_sid, domain_name)



Create a new Domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain import ApiV2010AccountSipSipDomain
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    domain_name = "domain_name_example" # str | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\"-\\\" and must end with `sip.twilio.com`.
    byoc_trunk_sid = "BY62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. (optional)
    emergency_caller_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. (optional)
    emergency_calling_enabled = True # bool | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe the resource. It can be up to 64 characters long. (optional)
    secure = True # bool | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. (optional)
    sip_registration = True # bool | Whether to allow SIP Endpoints to register with the domain to receive calls. Can be `true` or `false`. `true` allows SIP Endpoints to register with the domain to receive calls, `false` does not. (optional)
    voice_fallback_method = "head" # str | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`. (optional)
    voice_method = "head" # str | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`. (optional)
    voice_status_callback_method = "head" # str | The HTTP method we should use to call `voice_status_callback_url`. Can be: `GET` or `POST`. (optional)
    voice_status_callback_url = "voice_status_callback_url_example" # str | The URL that we should call to pass status parameters (such as call ended) to your application. (optional)
    voice_url = "voice_url_example" # str | The URL we should when the domain receives a call. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_domain(account_sid, domain_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sip_domain(account_sid, domain_name, byoc_trunk_sid=byoc_trunk_sid, emergency_caller_sid=emergency_caller_sid, emergency_calling_enabled=emergency_calling_enabled, friendly_name=friendly_name, secure=secure, sip_registration=sip_registration, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_status_callback_method=voice_status_callback_method, voice_status_callback_url=voice_status_callback_url, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **domain_name** | **str**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;. |
 **byoc_trunk_sid** | **str**| The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional]
 **emergency_caller_sid** | **str**| Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional]
 **emergency_calling_enabled** | **bool**| Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe the resource. It can be up to 64 characters long. | [optional]
 **secure** | **bool**| Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional]
 **sip_registration** | **bool**| Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not. | [optional]
 **voice_fallback_method** | **str**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_status_callback_method** | **str**| The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_status_callback_url** | **str**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional]
 **voice_url** | **str**| The URL we should when the domain receives a call. | [optional]

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_ip_access_control_list**
> ApiV2010AccountSipSipIpAccessControlList create_sip_ip_access_control_list(account_sid, friendly_name)



Create a new IpAccessControlList resource

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_ip_access_control_list import ApiV2010AccountSipSipIpAccessControlList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    friendly_name = "friendly_name_example" # str | A human readable descriptive text that describes the IpAccessControlList, up to 64 characters long.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_ip_access_control_list(account_sid, friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_ip_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **friendly_name** | **str**| A human readable descriptive text that describes the IpAccessControlList, up to 64 characters long. |

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_ip_access_control_list_mapping**
> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping create_sip_ip_access_control_list_mapping(account_sid, domain_sid, ip_access_control_list_sid)



Create a new IpAccessControlListMapping resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_ip_access_control_list_mapping import ApiV2010AccountSipSipDomainSipIpAccessControlListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP domain.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the IP access control list to map to the SIP domain.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_ip_access_control_list_mapping(account_sid, domain_sid, ip_access_control_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP domain. |
 **ip_access_control_list_sid** | **str**| The unique id of the IP access control list to map to the SIP domain. |

### Return type

[**ApiV2010AccountSipSipDomainSipIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sip_ip_address**
> ApiV2010AccountSipSipIpAccessControlListSipIpAddress create_sip_ip_address(account_sid, ip_access_control_list_sid, friendly_name, ip_address)



Create a new IpAddress resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import ApiV2010AccountSipSipIpAccessControlListSipIpAddress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The IpAccessControlList Sid with which to associate the created IpAddress resource.
    friendly_name = "friendly_name_example" # str | A human readable descriptive text for this resource, up to 64 characters long.
    ip_address = "ip_address_example" # str | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
    cidr_prefix_length = 1 # int | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sip_ip_address(account_sid, ip_access_control_list_sid, friendly_name, ip_address)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_ip_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_sip_ip_address(account_sid, ip_access_control_list_sid, friendly_name, ip_address, cidr_prefix_length=cidr_prefix_length)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_sip_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **ip_access_control_list_sid** | **str**| The IpAccessControlList Sid with which to associate the created IpAddress resource. |
 **friendly_name** | **str**| A human readable descriptive text for this resource, up to 64 characters long. |
 **ip_address** | **str**| An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. |
 **cidr_prefix_length** | **int**| An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional]

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> ApiV2010AccountToken create_token(account_sid)



Create a new token for ICE servers

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_token import ApiV2010AccountToken
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    ttl = 1 # int | The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours). (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_token(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_token(account_sid, ttl=ttl)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **ttl** | **int**| The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours). | [optional]

### Return type

[**ApiV2010AccountToken**](ApiV2010AccountToken.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_usage_trigger**
> ApiV2010AccountUsageUsageTrigger create_usage_trigger(account_sid, callback_url, trigger_value, usage_category)



Create a new UsageTrigger

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_usage_usage_trigger import ApiV2010AccountUsageUsageTrigger
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    callback_url = "callback_url_example" # str | The URL we should call using `callback_method` when the trigger fires.
    trigger_value = "trigger_value_example" # str | The usage value at which the trigger should fire.  For convenience, you can use an offset value such as `+30` to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a `+` as `%2B`.
    usage_category = "agent-conference" # str | The usage category that the trigger should watch.  Use one of the supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) for this value.
    callback_method = "head" # str | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)
    recurring = "daily" # str | The frequency of a recurring UsageTrigger.  Can be: `daily`, `monthly`, or `yearly` for recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in GMT. (optional)
    trigger_by = "count" # str | The field in the [UsageRecord](https://www.twilio.com/docs/usage/api/usage-record) resource that should fire the trigger.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).  The default is `usage`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_usage_trigger(account_sid, callback_url, trigger_value, usage_category)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_usage_trigger: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_usage_trigger(account_sid, callback_url, trigger_value, usage_category, callback_method=callback_method, friendly_name=friendly_name, recurring=recurring, trigger_by=trigger_by)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_usage_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. |
 **callback_url** | **str**| The URL we should call using &#x60;callback_method&#x60; when the trigger fires. |
 **trigger_value** | **str**| The usage value at which the trigger should fire.  For convenience, you can use an offset value such as &#x60;+30&#x60; to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a &#x60;+&#x60; as &#x60;%2B&#x60;. |
 **usage_category** | **str**| The usage category that the trigger should watch.  Use one of the supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) for this value. |
 **callback_method** | **str**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]
 **recurring** | **str**| The frequency of a recurring UsageTrigger.  Can be: &#x60;daily&#x60;, &#x60;monthly&#x60;, or &#x60;yearly&#x60; for recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in GMT. | [optional]
 **trigger_by** | **str**| The field in the [UsageRecord](https://www.twilio.com/docs/usage/api/usage-record) resource that should fire the trigger.  Can be: &#x60;count&#x60;, &#x60;usage&#x60;, or &#x60;price&#x60; as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).  The default is &#x60;usage&#x60;. | [optional]

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_validation_request**
> ApiV2010AccountValidationRequest create_validation_request(account_sid, phone_number)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_validation_request import ApiV2010AccountValidationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource.
    phone_number = "phone_number_example" # str | The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    call_delay = 1 # int | The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`. (optional)
    extension = "extension_example" # str | The digits to dial after connecting the verification call. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information about the verification process to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_validation_request(account_sid, phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_validation_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_validation_request(account_sid, phone_number, call_delay=call_delay, extension=extension, friendly_name=friendly_name, status_callback=status_callback, status_callback_method=status_callback_method)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_validation_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource. |
 **phone_number** | **str**| The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. |
 **call_delay** | **int**| The number of seconds to delay before initiating the verification call. Can be an integer between &#x60;0&#x60; and &#x60;60&#x60;, inclusive. The default is &#x60;0&#x60;. | [optional]
 **extension** | **str**| The digits to dial after connecting the verification call. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information about the verification process to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;. | [optional]

### Return type

[**ApiV2010AccountValidationRequest**](ApiV2010AccountValidationRequest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address**
> delete_address(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete.
    sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Address resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_address(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Address resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(account_sid, sid)



Delete the application by the specified application sid

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete.
    sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Application resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_application(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Application resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_call**
> delete_call(account_sid, sid)



Delete a Call record from your account. Once the record is deleted, it will no longer appear in the API and Account Portal logs.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to delete.
    sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided Call SID that uniquely identifies the Call resource to delete

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_call(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to delete. |
 **sid** | **str**| The Twilio-provided Call SID that uniquely identifies the Call resource to delete |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_call_feedback_summary**
> delete_call_feedback_summary(account_sid, sid)



Delete a FeedbackSummary resource from a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    sid = "FS62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies this resource.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_call_feedback_summary(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_call_feedback_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **sid** | **str**| A 34 character string that uniquely identifies this resource. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_call_recording**
> delete_call_recording(account_sid, call_sid, sid)



Delete a recording from your account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to delete.
    sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_call_recording(account_sid, call_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_call_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_conference_recording**
> delete_conference_recording(account_sid, conference_sid, sid)



Delete a recording from your account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to delete.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The Conference SID that identifies the conference associated with the recording to delete.
    sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Conference Recording resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_conference_recording(account_sid, conference_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_conference_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to delete. |
 **conference_sid** | **str**| The Conference SID that identifies the conference associated with the recording to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Conference Recording resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connect_app**
> delete_connect_app(account_sid, sid)



Delete an instance of a connect-app

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
    sid = "CN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_connect_app(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_connect_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_incoming_phone_number**
> delete_incoming_phone_number(account_sid, sid)



Delete a phone-numbers belonging to the account used to make the request.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to delete.
    sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_incoming_phone_number(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_incoming_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_incoming_phone_number_assigned_add_on**
> delete_incoming_phone_number_assigned_add_on(account_sid, resource_sid, sid)



Remove the assignment of an Add-on installation from the Number specified.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete.
    resource_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Phone Number to which the Add-on is assigned.
    sid = "XE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_incoming_phone_number_assigned_add_on(account_sid, resource_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_incoming_phone_number_assigned_add_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete. |
 **resource_sid** | **str**| The SID of the Phone Number to which the Add-on is assigned. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> delete_key(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to delete.
    sid = "SK62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Key resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_key(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Key resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media**
> delete_media(account_sid, message_sid, sid)



Delete media from your account. Once delete, you will no longer be billed

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to delete.
    message_sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The SID of the Message resource that this Media resource belongs to.
    sid = "ME62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Media resource to delete

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media(account_sid, message_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to delete. |
 **message_sid** | **str**| The SID of the Message resource that this Media resource belongs to. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Media resource to delete |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> delete_message(account_sid, sid)



Deletes a message record from your account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to delete.
    sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The Twilio-provided string that uniquely identifies the Message resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_message(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Message resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outgoing_caller_id**
> delete_outgoing_caller_id(account_sid, sid)



Delete the caller-id specified from the account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete.
    sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_outgoing_caller_id(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_outgoing_caller_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_participant**
> delete_participant(account_sid, conference_sid, call_sid)



Kick a participant from a given conference

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to delete.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the conference with the participants to delete.
    call_sid = "CallSid_example" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_participant(account_sid, conference_sid, call_sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to delete. |
 **conference_sid** | **str**| The SID of the conference with the participants to delete. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to delete. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_queue**
> delete_queue(account_sid, sid)



Remove an empty queue

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete.
    sid = "QU62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Queue resource to delete

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_queue(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Queue resource to delete |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(account_sid, sid)



Delete a recording from your account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete.
    sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_recording(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_add_on_result**
> delete_recording_add_on_result(account_sid, reference_sid, sid)



Delete a result and purge all associated Payloads

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to delete.
    reference_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the recording to which the result to delete belongs.
    sid = "XR62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_recording_add_on_result(account_sid, reference_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_recording_add_on_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to delete. |
 **reference_sid** | **str**| The SID of the recording to which the result to delete belongs. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_add_on_result_payload**
> delete_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid, sid)



Delete a payload from the result along with all associated Data

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete.
    reference_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs.
    add_on_result_sid = "XR62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the AddOnResult to which the payloads to delete belongs.
    sid = "XH62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_recording_add_on_result_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to delete. |
 **reference_sid** | **str**| The SID of the recording to which the AddOnResult resource that contains the payloads to delete belongs. |
 **add_on_result_sid** | **str**| The SID of the AddOnResult to which the payloads to delete belongs. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_transcription**
> delete_recording_transcription(account_sid, recording_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to delete.
    recording_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcription to delete.
    sid = "TR62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Transcription resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_recording_transcription(account_sid, recording_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_recording_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to delete. |
 **recording_sid** | **str**| The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcription to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Transcription resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_signing_key**
> delete_signing_key(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | 
    sid = "SK62ECB020842930cc01FFCCfeEe150AC" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_signing_key(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**|  |
 **sid** | **str**|  |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_auth_calls_credential_list_mapping**
> delete_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, sid)



Delete a credential list mapping from the requested domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resource to delete.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_auth_calls_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resource to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_auth_calls_ip_access_control_list_mapping**
> delete_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, sid)



Delete an IP Access Control List mapping from the requested domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resources to delete.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_auth_calls_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_auth_registrations_credential_list_mapping**
> delete_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, sid)



Delete a credential list mapping from the requested domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resources to delete.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_auth_registrations_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_credential**
> delete_sip_credential(account_sid, credential_list_sid, sid)



Delete a credential resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the credential list that contains the desired credentials.
    sid = "CR62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_credential(account_sid, credential_list_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **credential_list_sid** | **str**| The unique id that identifies the credential list that contains the desired credentials. |
 **sid** | **str**| The unique id that identifies the resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_credential_list**
> delete_sip_credential_list(account_sid, sid)



Delete a Credential List

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The credential list Sid that uniquely identifies this resource

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_credential_list(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **sid** | **str**| The credential list Sid that uniquely identifies this resource |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_credential_list_mapping**
> delete_sip_credential_list_mapping(account_sid, domain_sid, sid)



Delete a CredentialListMapping resource from an account.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_credential_list_mapping(account_sid, domain_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_domain**
> delete_sip_domain(account_sid, sid)



Delete an instance of a Domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete.
    sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the SipDomain resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_domain(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the SipDomain resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_ip_access_control_list**
> delete_sip_ip_access_control_list(account_sid, sid)



Delete an IpAccessControlList from the requested account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_ip_access_control_list(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_ip_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_ip_access_control_list_mapping**
> delete_sip_ip_access_control_list_mapping(account_sid, domain_sid, sid)



Delete an IpAccessControlListMapping resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP domain.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_ip_access_control_list_mapping(account_sid, domain_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP domain. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sip_ip_address**
> delete_sip_ip_address(account_sid, ip_access_control_list_sid, sid)



Delete an IpAddress resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The IpAccessControlList Sid that identifies the IpAddress resources to delete.
    sid = "IP62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sip_ip_address(account_sid, ip_access_control_list_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_sip_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **ip_access_control_list_sid** | **str**| The IpAccessControlList Sid that identifies the IpAddress resources to delete. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transcription**
> delete_transcription(account_sid, sid)



Delete a transcription from the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to delete.
    sid = "TR62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Transcription resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_transcription(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Transcription resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage_trigger**
> delete_usage_trigger(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete.
    sid = "UT62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_usage_trigger(account_sid, sid)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_usage_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete. |

### Return type

void (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_account**
> ApiV2010Account fetch_account(sid)



Fetch the account specified by the provided Account Sid

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account import ApiV2010Account
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The Account Sid that uniquely identifies the account to fetch

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_account(sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| The Account Sid that uniquely identifies the account to fetch |

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_address**
> ApiV2010AccountAddress fetch_address(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_address import ApiV2010AccountAddress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch.
    sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Address resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_address(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Address resource to fetch. |

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_application**
> ApiV2010AccountApplication fetch_application(account_sid, sid)



Fetch the application specified by the provided sid

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_application import ApiV2010AccountApplication
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch.
    sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Application resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_application(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Application resource to fetch. |

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_authorized_connect_app**
> ApiV2010AccountAuthorizedConnectApp fetch_authorized_connect_app(account_sid, connect_app_sid)



Fetch an instance of an authorized-connect-app

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_authorized_connect_app import ApiV2010AccountAuthorizedConnectApp
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resource to fetch.
    connect_app_sid = "CN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Connect App to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_authorized_connect_app(account_sid, connect_app_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_authorized_connect_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resource to fetch. |
 **connect_app_sid** | **str**| The SID of the Connect App to fetch. |

### Return type

[**ApiV2010AccountAuthorizedConnectApp**](ApiV2010AccountAuthorizedConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_available_phone_number_country**
> ApiV2010AccountAvailablePhoneNumberCountry fetch_available_phone_number_country(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_available_phone_number_country import ApiV2010AccountAvailablePhoneNumberCountry
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resource.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to fetch available phone number information about.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_available_phone_number_country(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_available_phone_number_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resource. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to fetch available phone number information about. |

### Return type

[**ApiV2010AccountAvailablePhoneNumberCountry**](ApiV2010AccountAvailablePhoneNumberCountry.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_balance**
> ApiV2010AccountBalance fetch_balance(account_sid)



Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately. Child accounts do not contain balance information

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_balance import ApiV2010AccountBalance
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique SID identifier of the Account.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_balance(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique SID identifier of the Account. |

### Return type

[**ApiV2010AccountBalance**](ApiV2010AccountBalance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_call**
> ApiV2010AccountCall fetch_call(account_sid, sid)



Fetch the call specified by the provided Call SID

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call import ApiV2010AccountCall
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to fetch.
    sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Call resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_call(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to fetch. |
 **sid** | **str**| The SID of the Call resource to fetch. |

### Return type

[**ApiV2010AccountCall**](ApiV2010AccountCall.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_call_feedback**
> ApiV2010AccountCallCallFeedback fetch_call_feedback(account_sid, call_sid)



Fetch a Feedback resource from a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_feedback import ApiV2010AccountCallCallFeedback
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The call sid that uniquely identifies the call

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_call_feedback(account_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_call_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **call_sid** | **str**| The call sid that uniquely identifies the call |

### Return type

[**ApiV2010AccountCallCallFeedback**](ApiV2010AccountCallCallFeedback.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_call_feedback_summary**
> ApiV2010AccountCallCallFeedbackSummary fetch_call_feedback_summary(account_sid, sid)



Fetch a FeedbackSummary resource from a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_feedback_summary import ApiV2010AccountCallCallFeedbackSummary
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    sid = "FS62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies this resource.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_call_feedback_summary(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_call_feedback_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **sid** | **str**| A 34 character string that uniquely identifies this resource. |

### Return type

[**ApiV2010AccountCallCallFeedbackSummary**](ApiV2010AccountCallCallFeedbackSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_call_notification**
> ApiV2010AccountCallCallNotificationInstance fetch_call_notification(account_sid, call_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_notification_instance import ApiV2010AccountCallCallNotificationInstance
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch.
    sid = "NO62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_call_notification(account_sid, call_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_call_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Call Notification resource to fetch. |

### Return type

[**ApiV2010AccountCallCallNotificationInstance**](ApiV2010AccountCallCallNotificationInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_call_recording**
> ApiV2010AccountCallCallRecording fetch_call_recording(account_sid, call_sid, sid)



Fetch an instance of a recording for a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_recording import ApiV2010AccountCallCallRecording
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to fetch.
    sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_call_recording(account_sid, call_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_call_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording resource to fetch. |

### Return type

[**ApiV2010AccountCallCallRecording**](ApiV2010AccountCallCallRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_conference**
> ApiV2010AccountConference fetch_conference(account_sid, sid)



Fetch an instance of a conference

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference import ApiV2010AccountConference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to fetch.
    sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Conference resource to fetch

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_conference(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Conference resource to fetch |

### Return type

[**ApiV2010AccountConference**](ApiV2010AccountConference.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_conference_recording**
> ApiV2010AccountConferenceConferenceRecording fetch_conference_recording(account_sid, conference_sid, sid)



Fetch an instance of a recording for a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference_conference_recording import ApiV2010AccountConferenceConferenceRecording
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to fetch.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The Conference SID that identifies the conference associated with the recording to fetch.
    sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_conference_recording(account_sid, conference_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_conference_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to fetch. |
 **conference_sid** | **str**| The Conference SID that identifies the conference associated with the recording to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch. |

### Return type

[**ApiV2010AccountConferenceConferenceRecording**](ApiV2010AccountConferenceConferenceRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_connect_app**
> ApiV2010AccountConnectApp fetch_connect_app(account_sid, sid)



Fetch an instance of a connect-app

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_connect_app import ApiV2010AccountConnectApp
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch.
    sid = "CN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_connect_app(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_connect_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the ConnectApp resource to fetch. |

### Return type

[**ApiV2010AccountConnectApp**](ApiV2010AccountConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_incoming_phone_number**
> ApiV2010AccountIncomingPhoneNumber fetch_incoming_phone_number(account_sid, sid)



Fetch an incoming-phone-number belonging to the account used to make the request.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number import ApiV2010AccountIncomingPhoneNumber
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to fetch.
    sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_incoming_phone_number(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_incoming_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch. |

### Return type

[**ApiV2010AccountIncomingPhoneNumber**](ApiV2010AccountIncomingPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_incoming_phone_number_assigned_add_on**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn fetch_incoming_phone_number_assigned_add_on(account_sid, resource_sid, sid)



Fetch an instance of an Add-on installation currently assigned to this Number.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
    resource_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Phone Number to which the Add-on is assigned.
    sid = "XE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_incoming_phone_number_assigned_add_on(account_sid, resource_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_incoming_phone_number_assigned_add_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch. |
 **resource_sid** | **str**| The SID of the Phone Number to which the Add-on is assigned. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the resource to fetch. |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_incoming_phone_number_assigned_add_on_extension**
> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension fetch_incoming_phone_number_assigned_add_on_extension(account_sid, resource_sid, assigned_add_on_sid, sid)



Fetch an instance of an Extension for the Assigned Add-on.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on_incoming_phone_number_assigned_add_on_extension import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
    resource_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Phone Number to which the Add-on is assigned.
    assigned_add_on_sid = "XE62ECB020842930cc01FFCCfeEe150AC" # str | The SID that uniquely identifies the assigned Add-on installation.
    sid = "XF62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_incoming_phone_number_assigned_add_on_extension(account_sid, resource_sid, assigned_add_on_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_incoming_phone_number_assigned_add_on_extension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch. |
 **resource_sid** | **str**| The SID of the Phone Number to which the Add-on is assigned. |
 **assigned_add_on_sid** | **str**| The SID that uniquely identifies the assigned Add-on installation. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the resource to fetch. |

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_key**
> ApiV2010AccountKey fetch_key(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_key import ApiV2010AccountKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resource to fetch.
    sid = "SK62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Key resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_key(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Key resource to fetch. |

### Return type

[**ApiV2010AccountKey**](ApiV2010AccountKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_media**
> ApiV2010AccountMessageMedia fetch_media(account_sid, message_sid, sid)



Fetch a single media instance belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_message_media import ApiV2010AccountMessageMedia
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to fetch.
    message_sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The SID of the Message resource that this Media resource belongs to.
    sid = "ME62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Media resource to fetch

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_media(account_sid, message_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to fetch. |
 **message_sid** | **str**| The SID of the Message resource that this Media resource belongs to. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Media resource to fetch |

### Return type

[**ApiV2010AccountMessageMedia**](ApiV2010AccountMessageMedia.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_member**
> ApiV2010AccountQueueMember fetch_member(account_sid, queue_sid, call_sid)



Fetch a specific member from the queue

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_queue_member import ApiV2010AccountQueueMember
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to fetch.
    queue_sid = "QU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Queue in which to find the members to fetch.
    call_sid = "CallSid_example" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_member(account_sid, queue_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to fetch. |
 **queue_sid** | **str**| The SID of the Queue in which to find the members to fetch. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to fetch. |

### Return type

[**ApiV2010AccountQueueMember**](ApiV2010AccountQueueMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_message**
> ApiV2010AccountMessage fetch_message(account_sid, sid)



Fetch a message belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_message import ApiV2010AccountMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resource to fetch.
    sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The Twilio-provided string that uniquely identifies the Message resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_message(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Message resource to fetch. |

### Return type

[**ApiV2010AccountMessage**](ApiV2010AccountMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_notification**
> ApiV2010AccountNotificationInstance fetch_notification(account_sid, sid)



Fetch a notification belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_notification_instance import ApiV2010AccountNotificationInstance
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource to fetch.
    sid = "NO62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Notification resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_notification(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Notification resource to fetch. |

### Return type

[**ApiV2010AccountNotificationInstance**](ApiV2010AccountNotificationInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_outgoing_caller_id**
> ApiV2010AccountOutgoingCallerId fetch_outgoing_caller_id(account_sid, sid)



Fetch an outgoing-caller-id belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_outgoing_caller_id import ApiV2010AccountOutgoingCallerId
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch.
    sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_outgoing_caller_id(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_outgoing_caller_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch. |

### Return type

[**ApiV2010AccountOutgoingCallerId**](ApiV2010AccountOutgoingCallerId.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_participant**
> ApiV2010AccountConferenceParticipant fetch_participant(account_sid, conference_sid, call_sid)



Fetch an instance of a participant

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference_participant import ApiV2010AccountConferenceParticipant
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource to fetch.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the conference with the participant to fetch.
    call_sid = "CallSid_example" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_participant(account_sid, conference_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource to fetch. |
 **conference_sid** | **str**| The SID of the conference with the participant to fetch. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to fetch. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20. |

### Return type

[**ApiV2010AccountConferenceParticipant**](ApiV2010AccountConferenceParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_queue**
> ApiV2010AccountQueue fetch_queue(account_sid, sid)



Fetch an instance of a queue identified by the QueueSid

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_queue import ApiV2010AccountQueue
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch.
    sid = "QU62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Queue resource to fetch

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_queue(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Queue resource to fetch |

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_recording**
> ApiV2010AccountRecording fetch_recording(account_sid, sid)



Fetch an instance of a recording

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_recording import ApiV2010AccountRecording
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch.
    sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_recording(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording resource to fetch. |

### Return type

[**ApiV2010AccountRecording**](ApiV2010AccountRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_recording_add_on_result**
> ApiV2010AccountRecordingRecordingAddOnResult fetch_recording_add_on_result(account_sid, reference_sid, sid)



Fetch an instance of an AddOnResult

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_recording_recording_add_on_result import ApiV2010AccountRecordingRecordingAddOnResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch.
    reference_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the recording to which the result to fetch belongs.
    sid = "XR62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_recording_add_on_result(account_sid, reference_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_recording_add_on_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch. |
 **reference_sid** | **str**| The SID of the recording to which the result to fetch belongs. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch. |

### Return type

[**ApiV2010AccountRecordingRecordingAddOnResult**](ApiV2010AccountRecordingRecordingAddOnResult.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_recording_add_on_result_payload**
> ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload fetch_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid, sid)



Fetch an instance of a result payload

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload import ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch.
    reference_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs.
    add_on_result_sid = "XR62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the AddOnResult to which the payload to fetch belongs.
    sid = "XH62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_recording_add_on_result_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch. |
 **reference_sid** | **str**| The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs. |
 **add_on_result_sid** | **str**| The SID of the AddOnResult to which the payload to fetch belongs. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch. |

### Return type

[**ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload**](ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_recording_transcription**
> ApiV2010AccountRecordingRecordingTranscription fetch_recording_transcription(account_sid, recording_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_recording_recording_transcription import ApiV2010AccountRecordingRecordingTranscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch.
    recording_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcription to fetch.
    sid = "TR62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Transcription resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_recording_transcription(account_sid, recording_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_recording_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch. |
 **recording_sid** | **str**| The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcription to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Transcription resource to fetch. |

### Return type

[**ApiV2010AccountRecordingRecordingTranscription**](ApiV2010AccountRecordingRecordingTranscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_short_code**
> ApiV2010AccountShortCode fetch_short_code(account_sid, sid)



Fetch an instance of a short code

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_short_code import ApiV2010AccountShortCode
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch.
    sid = "SC62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the ShortCode resource to fetch

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_short_code(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_short_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the ShortCode resource to fetch |

### Return type

[**ApiV2010AccountShortCode**](ApiV2010AccountShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_signing_key**
> ApiV2010AccountSigningKey fetch_signing_key(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_signing_key import ApiV2010AccountSigningKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | 
    sid = "SK62ECB020842930cc01FFCCfeEe150AC" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_signing_key(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**|  |
 **sid** | **str**|  |

### Return type

[**ApiV2010AccountSigningKey**](ApiV2010AccountSigningKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_auth_calls_credential_list_mapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping fetch_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, sid)



Fetch a specific instance of a credential list mapping

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_credential_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resource to fetch.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_auth_calls_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch. |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_auth_calls_ip_access_control_list_mapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping fetch_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, sid)



Fetch a specific instance of an IP Access Control List mapping

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_ip_access_control_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resource to fetch.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_auth_calls_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch. |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_auth_registrations_credential_list_mapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping fetch_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, sid)



Fetch a specific instance of a credential list mapping

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_registrations_sip_auth_registrations_credential_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resource to fetch.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_auth_registrations_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch. |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_credential**
> ApiV2010AccountSipSipCredentialListSipCredential fetch_sip_credential(account_sid, credential_list_sid, sid)



Fetch a single credential.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_credential_list_sip_credential import ApiV2010AccountSipSipCredentialListSipCredential
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the credential list that contains the desired credential.
    sid = "CR62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_credential(account_sid, credential_list_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **credential_list_sid** | **str**| The unique id that identifies the credential list that contains the desired credential. |
 **sid** | **str**| The unique id that identifies the resource to fetch. |

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_credential_list**
> ApiV2010AccountSipSipCredentialList fetch_sip_credential_list(account_sid, sid)



Get a Credential List

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_credential_list import ApiV2010AccountSipSipCredentialList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The credential list Sid that uniquely identifies this resource

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_credential_list(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **sid** | **str**| The credential list Sid that uniquely identifies this resource |

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_credential_list_mapping**
> ApiV2010AccountSipSipDomainSipCredentialListMapping fetch_sip_credential_list_mapping(account_sid, domain_sid, sid)



Fetch a single CredentialListMapping resource from an account.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_credential_list_mapping import ApiV2010AccountSipSipDomainSipCredentialListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_credential_list_mapping(account_sid, domain_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to fetch. |

### Return type

[**ApiV2010AccountSipSipDomainSipCredentialListMapping**](ApiV2010AccountSipSipDomainSipCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_domain**
> ApiV2010AccountSipSipDomain fetch_sip_domain(account_sid, sid)



Fetch an instance of a Domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain import ApiV2010AccountSipSipDomain
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch.
    sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_domain(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the SipDomain resource to fetch. |

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_ip_access_control_list**
> ApiV2010AccountSipSipIpAccessControlList fetch_sip_ip_access_control_list(account_sid, sid)



Fetch a specific instance of an IpAccessControlList

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_ip_access_control_list import ApiV2010AccountSipSipIpAccessControlList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_ip_access_control_list(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_ip_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to fetch. |

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_ip_access_control_list_mapping**
> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping fetch_sip_ip_access_control_list_mapping(account_sid, domain_sid, sid)



Fetch an IpAccessControlListMapping resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain_sip_ip_access_control_list_mapping import ApiV2010AccountSipSipDomainSipIpAccessControlListMapping
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP domain.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_ip_access_control_list_mapping(account_sid, domain_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP domain. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to fetch. |

### Return type

[**ApiV2010AccountSipSipDomainSipIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sip_ip_address**
> ApiV2010AccountSipSipIpAccessControlListSipIpAddress fetch_sip_ip_address(account_sid, ip_access_control_list_sid, sid)



Read one IpAddress resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import ApiV2010AccountSipSipIpAccessControlListSipIpAddress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
    sid = "IP62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the IpAddress resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_sip_ip_address(account_sid, ip_access_control_list_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_sip_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **ip_access_control_list_sid** | **str**| The IpAccessControlList Sid that identifies the IpAddress resources to fetch. |
 **sid** | **str**| A 34 character string that uniquely identifies the IpAddress resource to fetch. |

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_transcription**
> ApiV2010AccountTranscription fetch_transcription(account_sid, sid)



Fetch an instance of a Transcription

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_transcription import ApiV2010AccountTranscription
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch.
    sid = "TR62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Transcription resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_transcription(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Transcription resource to fetch. |

### Return type

[**ApiV2010AccountTranscription**](ApiV2010AccountTranscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_usage_trigger**
> ApiV2010AccountUsageUsageTrigger fetch_usage_trigger(account_sid, sid)



Fetch and instance of a usage-trigger

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_usage_usage_trigger import ApiV2010AccountUsageUsageTrigger
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch.
    sid = "UT62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.fetch_usage_trigger(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->fetch_usage_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch. |

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account**
> InlineResponse200 list_account()



Retrieves a collection of Accounts belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    friendly_name = "FriendlyName_example" # str | Only return the Account resources with friendly names that exactly match this name. (optional)
    status = "active" # str | Only return Account resources with the given status. Can be `closed`, `suspended` or `active`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_account(friendly_name=friendly_name, status=status, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **friendly_name** | **str**| Only return the Account resources with friendly names that exactly match this name. | [optional]
 **status** | **str**| Only return Account resources with the given status. Can be &#x60;closed&#x60;, &#x60;suspended&#x60; or &#x60;active&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address**
> InlineResponse2001 list_address(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read.
    customer_name = "CustomerName_example" # str | The `customer_name` of the Address resources to read. (optional)
    friendly_name = "FriendlyName_example" # str | The string that identifies the Address resources to read. (optional)
    iso_country = "IsoCountry_example" # str | The ISO country code of the Address resources to read. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_address(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_address(account_sid, customer_name=customer_name, friendly_name=friendly_name, iso_country=iso_country, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read. |
 **customer_name** | **str**| The &#x60;customer_name&#x60; of the Address resources to read. | [optional]
 **friendly_name** | **str**| The string that identifies the Address resources to read. | [optional]
 **iso_country** | **str**| The ISO country code of the Address resources to read. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application**
> InlineResponse2003 list_application(account_sid)



Retrieve a list of applications representing an application within the requesting account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read.
    friendly_name = "FriendlyName_example" # str | The string that identifies the Application resources to read. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_application(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_application(account_sid, friendly_name=friendly_name, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read. |
 **friendly_name** | **str**| The string that identifies the Application resources to read. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorized_connect_app**
> InlineResponse2004 list_authorized_connect_app(account_sid)



Retrieve a list of authorized-connect-apps belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2004 import InlineResponse2004
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_authorized_connect_app(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_authorized_connect_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_authorized_connect_app(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_authorized_connect_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_country**
> InlineResponse2005 list_available_phone_number_country(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2005 import InlineResponse2005
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resources.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_country(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_country: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_country(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the available phone number Country resources. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_local**
> InlineResponse2006 list_available_phone_number_local(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2006 import InlineResponse2006
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-number-pattern) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-character-pattern). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_local(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_local: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_local(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_local: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample&#x3D;code-find-phone-numbers-by-number-pattern) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample&#x3D;code-find-phone-numbers-by-character-pattern). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_machine_to_machine**
> InlineResponse2007 list_available_phone_number_machine_to_machine(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2007 import InlineResponse2007
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_machine_to_machine(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_machine_to_machine: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_machine_to_machine(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_machine_to_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_mobile**
> InlineResponse2008 list_available_phone_number_mobile(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2008 import InlineResponse2008
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_mobile(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_mobile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_mobile(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_national**
> InlineResponse2009 list_available_phone_number_national(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2009 import InlineResponse2009
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_national(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_national: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_national(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_national: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_shared_cost**
> InlineResponse20010 list_available_phone_number_shared_cost(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20010 import InlineResponse20010
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_shared_cost(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_shared_cost: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_shared_cost(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_shared_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_toll_free**
> InlineResponse20011 list_available_phone_number_toll_free(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20011 import InlineResponse20011
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_toll_free(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_toll_free: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_toll_free(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_toll_free: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_phone_number_voip**
> InlineResponse20012 list_available_phone_number_voip(account_sid, country_code)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20012 import InlineResponse20012
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
    country_code = "CountryCode_example" # str | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
    area_code = 1 # int | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. (optional)
    contains = "Contains_example" # str | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. (optional)
    sms_enabled = True # bool | Whether the phone numbers can receive text messages. Can be: `true` or `false`. (optional)
    mms_enabled = True # bool | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`. (optional)
    voice_enabled = True # bool | Whether the phone numbers can receive calls. Can be: `true` or `false`. (optional)
    exclude_all_address_required = True # bool | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_local_address_required = True # bool | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    exclude_foreign_address_required = True # bool | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`. (optional)
    beta = True # bool | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    near_number = "NearNumber_example" # str | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. (optional)
    near_lat_long = "NearLatLong_example" # str | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada. (optional)
    distance = 1 # int | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada. (optional)
    in_postal_code = "InPostalCode_example" # str | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_region = "InRegion_example" # str | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_rate_center = "InRateCenter_example" # str | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada. (optional)
    in_lata = "InLata_example" # str | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. (optional)
    in_locality = "InLocality_example" # str | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. (optional)
    fax_enabled = True # bool | Whether the phone numbers can receive faxes. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_available_phone_number_voip(account_sid, country_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_voip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_available_phone_number_voip(account_sid, country_code, area_code=area_code, contains=contains, sms_enabled=sms_enabled, mms_enabled=mms_enabled, voice_enabled=voice_enabled, exclude_all_address_required=exclude_all_address_required, exclude_local_address_required=exclude_local_address_required, exclude_foreign_address_required=exclude_foreign_address_required, beta=beta, near_number=near_number, near_lat_long=near_lat_long, distance=distance, in_postal_code=in_postal_code, in_region=in_region, in_rate_center=in_rate_center, in_lata=in_lata, in_locality=in_locality, fax_enabled=fax_enabled, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_available_phone_number_voip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. |
 **country_code** | **str**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. |
 **area_code** | **int**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional]
 **contains** | **str**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional]
 **sms_enabled** | **bool**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **mms_enabled** | **bool**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_enabled** | **bool**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **exclude_all_address_required** | **bool**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_local_address_required** | **bool**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **exclude_foreign_address_required** | **bool**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional]
 **beta** | **bool**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **near_number** | **str**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional]
 **near_lat_long** | **str**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional]
 **distance** | **int**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional]
 **in_postal_code** | **str**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_region** | **str**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_rate_center** | **str**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional]
 **in_lata** | **str**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional]
 **in_locality** | **str**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional]
 **fax_enabled** | **bool**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call**
> InlineResponse20013 list_call(account_sid)



Retrieves a collection of calls made to and from your account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20013 import InlineResponse20013
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to read.
    to = "To_example" # str | Only show calls made to this phone number, SIP address, Client identifier or SIM SID. (optional)
    _from = "From_example" # str | Only include calls from this phone number, SIP address, Client identifier or SIM SID. (optional)
    parent_call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | Only include calls spawned by calls with this SID. (optional)
    status = "queued" # str | The status of the calls to include. Can be: `queued`, `ringing`, `in-progress`, `canceled`, `completed`, `failed`, `busy`, or `no-answer`. (optional)
    start_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include calls that started on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read only calls that started on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read calls that started on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read calls that started on or after midnight of this date. (optional)
    start_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include calls that started on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read only calls that started on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read calls that started on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read calls that started on or after midnight of this date. (optional)
    start_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include calls that started on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read only calls that started on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read calls that started on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read calls that started on or after midnight of this date. (optional)
    end_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include calls that ended on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read only calls that ended on this date. You can also specify an inequality, such as `EndTime<=YYYY-MM-DD`, to read calls that ended on or before midnight of this date, and `EndTime>=YYYY-MM-DD` to read calls that ended on or after midnight of this date. (optional)
    end_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include calls that ended on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read only calls that ended on this date. You can also specify an inequality, such as `EndTime<=YYYY-MM-DD`, to read calls that ended on or before midnight of this date, and `EndTime>=YYYY-MM-DD` to read calls that ended on or after midnight of this date. (optional)
    end_time2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include calls that ended on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read only calls that ended on this date. You can also specify an inequality, such as `EndTime<=YYYY-MM-DD`, to read calls that ended on or before midnight of this date, and `EndTime>=YYYY-MM-DD` to read calls that ended on or after midnight of this date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_call(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_call(account_sid, to=to, _from=_from, parent_call_sid=parent_call_sid, status=status, start_time=start_time, start_time2=start_time2, start_time2=start_time2, end_time=end_time, end_time2=end_time2, end_time2=end_time2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to read. |
 **to** | **str**| Only show calls made to this phone number, SIP address, Client identifier or SIM SID. | [optional]
 **_from** | **str**| Only include calls from this phone number, SIP address, Client identifier or SIM SID. | [optional]
 **parent_call_sid** | **str**| Only include calls spawned by calls with this SID. | [optional]
 **status** | **str**| The status of the calls to include. Can be: &#x60;queued&#x60;, &#x60;ringing&#x60;, &#x60;in-progress&#x60;, &#x60;canceled&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;, &#x60;busy&#x60;, or &#x60;no-answer&#x60;. | [optional]
 **start_time** | **datetime**| Only include calls that started on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that started on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that started on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that started on or after midnight of this date. | [optional]
 **start_time2** | **datetime**| Only include calls that started on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that started on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that started on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that started on or after midnight of this date. | [optional]
 **start_time2** | **datetime**| Only include calls that started on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that started on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that started on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that started on or after midnight of this date. | [optional]
 **end_time** | **datetime**| Only include calls that ended on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that ended on this date. You can also specify an inequality, such as &#x60;EndTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that ended on or before midnight of this date, and &#x60;EndTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that ended on or after midnight of this date. | [optional]
 **end_time2** | **datetime**| Only include calls that ended on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that ended on this date. You can also specify an inequality, such as &#x60;EndTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that ended on or before midnight of this date, and &#x60;EndTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that ended on or after midnight of this date. | [optional]
 **end_time2** | **datetime**| Only include calls that ended on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read only calls that ended on this date. You can also specify an inequality, such as &#x60;EndTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read calls that ended on or before midnight of this date, and &#x60;EndTime&gt;&#x3D;YYYY-MM-DD&#x60; to read calls that ended on or after midnight of this date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_event**
> InlineResponse20014 list_call_event(account_sid, call_sid)



Retrieve a list of all events for a call.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20014 import InlineResponse20014
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique SID identifier of the Account.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The unique SID identifier of the Call.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_call_event(account_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call_event: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_call_event(account_sid, call_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique SID identifier of the Account. |
 **call_sid** | **str**| The unique SID identifier of the Call. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_notification**
> InlineResponse20015 list_call_notification(account_sid, call_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20015 import InlineResponse20015
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read.
    log = 1 # int | Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read. (optional)
    message_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date. (optional)
    message_date2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date. (optional)
    message_date2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_call_notification(account_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call_notification: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_call_notification(account_sid, call_sid, log=log, message_date=message_date, message_date2=message_date2, message_date2=message_date2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read. |
 **log** | **int**| Only read notifications of the specified log level. Can be:  &#x60;0&#x60; to read only ERROR notifications or &#x60;1&#x60; to read only WARNING notifications. By default, all notifications are read. | [optional]
 **message_date** | **datetime**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional]
 **message_date2** | **datetime**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional]
 **message_date2** | **datetime**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_call_recording**
> InlineResponse20016 list_call_recording(account_sid, call_sid)



Retrieve a list of recordings belonging to the call used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20016 import InlineResponse20016
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.
    date_created = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_call_recording(account_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call_recording: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_call_recording(account_sid, call_sid, date_created=date_created, date_created2=date_created2, date_created2=date_created2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_call_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read. |
 **date_created** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional]
 **date_created2** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional]
 **date_created2** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conference**
> InlineResponse20017 list_conference(account_sid)



Retrieve a list of conferences belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20017 import InlineResponse20017
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to read.
    date_created = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`. (optional)
    date_updated = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`. (optional)
    date_updated2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`. (optional)
    date_updated2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`. (optional)
    friendly_name = "FriendlyName_example" # str | The string that identifies the Conference resources to read. (optional)
    status = "init" # str | The status of the resources to read. Can be: `init`, `in-progress`, or `completed`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_conference(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_conference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_conference(account_sid, date_created=date_created, date_created2=date_created2, date_created2=date_created2, date_updated=date_updated, date_updated2=date_updated2, date_updated2=date_updated2, friendly_name=friendly_name, status=status, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to read. |
 **date_created** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that started on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify  conferences that started on or after midnight on a date, use &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;. | [optional]
 **date_created2** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that started on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify  conferences that started on or after midnight on a date, use &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;. | [optional]
 **date_created2** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that started on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify  conferences that started on or after midnight on a date, use &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;. | [optional]
 **date_updated** | **datetime**| The &#x60;date_updated&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that were last updated on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify conferences that were last updated on or after midnight on a given date, use  &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;. | [optional]
 **date_updated2** | **datetime**| The &#x60;date_updated&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that were last updated on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify conferences that were last updated on or after midnight on a given date, use  &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;. | [optional]
 **date_updated2** | **datetime**| The &#x60;date_updated&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. To read conferences that were last updated on or before midnight on a date, use &#x60;&lt;&#x3D;YYYY-MM-DD&#x60;, and to specify conferences that were last updated on or after midnight on a given date, use  &#x60;&gt;&#x3D;YYYY-MM-DD&#x60;. | [optional]
 **friendly_name** | **str**| The string that identifies the Conference resources to read. | [optional]
 **status** | **str**| The status of the resources to read. Can be: &#x60;init&#x60;, &#x60;in-progress&#x60;, or &#x60;completed&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conference_recording**
> InlineResponse20019 list_conference_recording(account_sid, conference_sid)



Retrieve a list of recordings belonging to the call used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20019 import InlineResponse20019
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to read.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The Conference SID that identifies the conference associated with the recording to read.
    date_created = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_conference_recording(account_sid, conference_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_conference_recording: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_conference_recording(account_sid, conference_sid, date_created=date_created, date_created2=date_created2, date_created2=date_created2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_conference_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to read. |
 **conference_sid** | **str**| The Conference SID that identifies the conference associated with the recording to read. |
 **date_created** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional]
 **date_created2** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional]
 **date_created2** | **datetime**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connect_app**
> InlineResponse20020 list_connect_app(account_sid)



Retrieve a list of connect-apps belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20020 import InlineResponse20020
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_connect_app(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_connect_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_connect_app(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_connect_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dependent_phone_number**
> InlineResponse2002 list_dependent_phone_number(account_sid, address_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DependentPhoneNumber resources to read.
    address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Address resource associated with the phone number.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_dependent_phone_number(account_sid, address_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_dependent_phone_number: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_dependent_phone_number(account_sid, address_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_dependent_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DependentPhoneNumber resources to read. |
 **address_sid** | **str**| The SID of the Address resource associated with the phone number. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_phone_number**
> InlineResponse20021 list_incoming_phone_number(account_sid)



Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20021 import InlineResponse20021
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to read.
    beta = True # bool | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    friendly_name = "FriendlyName_example" # str | A string that identifies the IncomingPhoneNumber resources to read. (optional)
    phone_number = "PhoneNumber_example" # str | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit. (optional)
    origin = "Origin_example" # str | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_incoming_phone_number(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_incoming_phone_number(account_sid, beta=beta, friendly_name=friendly_name, phone_number=phone_number, origin=origin, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resources to read. |
 **beta** | **bool**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **friendly_name** | **str**| A string that identifies the IncomingPhoneNumber resources to read. | [optional]
 **phone_number** | **str**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional]
 **origin** | **str**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_phone_number_assigned_add_on**
> InlineResponse20025 list_incoming_phone_number_assigned_add_on(account_sid, resource_sid)



Retrieve a list of Add-on installations currently assigned to this Number.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20025 import InlineResponse20025
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    resource_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Phone Number to which the Add-on is assigned.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_incoming_phone_number_assigned_add_on(account_sid, resource_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_assigned_add_on: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_incoming_phone_number_assigned_add_on(account_sid, resource_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_assigned_add_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. |
 **resource_sid** | **str**| The SID of the Phone Number to which the Add-on is assigned. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_phone_number_assigned_add_on_extension**
> InlineResponse20026 list_incoming_phone_number_assigned_add_on_extension(account_sid, resource_sid, assigned_add_on_sid)



Retrieve a list of Extensions for the Assigned Add-on.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20026 import InlineResponse20026
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    resource_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Phone Number to which the Add-on is assigned.
    assigned_add_on_sid = "XE62ECB020842930cc01FFCCfeEe150AC" # str | The SID that uniquely identifies the assigned Add-on installation.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_incoming_phone_number_assigned_add_on_extension(account_sid, resource_sid, assigned_add_on_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_assigned_add_on_extension: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_incoming_phone_number_assigned_add_on_extension(account_sid, resource_sid, assigned_add_on_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_assigned_add_on_extension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. |
 **resource_sid** | **str**| The SID of the Phone Number to which the Add-on is assigned. |
 **assigned_add_on_sid** | **str**| The SID that uniquely identifies the assigned Add-on installation. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_phone_number_local**
> InlineResponse20022 list_incoming_phone_number_local(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20022 import InlineResponse20022
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    beta = True # bool | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    friendly_name = "FriendlyName_example" # str | A string that identifies the resources to read. (optional)
    phone_number = "PhoneNumber_example" # str | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit. (optional)
    origin = "Origin_example" # str | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_incoming_phone_number_local(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_local: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_incoming_phone_number_local(account_sid, beta=beta, friendly_name=friendly_name, phone_number=phone_number, origin=origin, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_local: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. |
 **beta** | **bool**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **friendly_name** | **str**| A string that identifies the resources to read. | [optional]
 **phone_number** | **str**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional]
 **origin** | **str**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_phone_number_mobile**
> InlineResponse20023 list_incoming_phone_number_mobile(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20023 import InlineResponse20023
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    beta = True # bool | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    friendly_name = "FriendlyName_example" # str | A string that identifies the resources to read. (optional)
    phone_number = "PhoneNumber_example" # str | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit. (optional)
    origin = "Origin_example" # str | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_incoming_phone_number_mobile(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_mobile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_incoming_phone_number_mobile(account_sid, beta=beta, friendly_name=friendly_name, phone_number=phone_number, origin=origin, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_mobile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. |
 **beta** | **bool**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **friendly_name** | **str**| A string that identifies the resources to read. | [optional]
 **phone_number** | **str**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional]
 **origin** | **str**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incoming_phone_number_toll_free**
> InlineResponse20024 list_incoming_phone_number_toll_free(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20024 import InlineResponse20024
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    beta = True # bool | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`. (optional)
    friendly_name = "FriendlyName_example" # str | A string that identifies the resources to read. (optional)
    phone_number = "PhoneNumber_example" # str | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit. (optional)
    origin = "Origin_example" # str | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_incoming_phone_number_toll_free(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_toll_free: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_incoming_phone_number_toll_free(account_sid, beta=beta, friendly_name=friendly_name, phone_number=phone_number, origin=origin, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_incoming_phone_number_toll_free: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. |
 **beta** | **bool**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional]
 **friendly_name** | **str**| A string that identifies the resources to read. | [optional]
 **phone_number** | **str**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional]
 **origin** | **str**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key**
> InlineResponse20027 list_key(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20027 import InlineResponse20027
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_key(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_key(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_media**
> InlineResponse20029 list_media(account_sid, message_sid)



Retrieve a list of Media resources belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20029 import InlineResponse20029
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to read.
    message_sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The SID of the Message resource that this Media resource belongs to.
    date_created = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_media(account_sid, message_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_media: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_media(account_sid, message_sid, date_created=date_created, date_created2=date_created2, date_created2=date_created2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to read. |
 **message_sid** | **str**| The SID of the Message resource that this Media resource belongs to. |
 **date_created** | **datetime**| Only include media that was created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read media that was created on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read media that was created on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read media that was created on or after midnight of this date. | [optional]
 **date_created2** | **datetime**| Only include media that was created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read media that was created on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read media that was created on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read media that was created on or after midnight of this date. | [optional]
 **date_created2** | **datetime**| Only include media that was created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read media that was created on this date. You can also specify an inequality, such as &#x60;StartTime&lt;&#x3D;YYYY-MM-DD&#x60;, to read media that was created on or before midnight of this date, and &#x60;StartTime&gt;&#x3D;YYYY-MM-DD&#x60; to read media that was created on or after midnight of this date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member**
> InlineResponse20033 list_member(account_sid, queue_sid)



Retrieve the members of the queue

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20033 import InlineResponse20033
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to read.
    queue_sid = "QU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Queue in which to find the members
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_member(account_sid, queue_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_member(account_sid, queue_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to read. |
 **queue_sid** | **str**| The SID of the Queue in which to find the members |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_message**
> InlineResponse20028 list_message(account_sid)



Retrieve a list of messages belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20028 import InlineResponse20028
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to read.
    to = "To_example" # str | Read messages sent to only this phone number. (optional)
    _from = "From_example" # str | Read messages sent from only this phone number or alphanumeric sender ID. (optional)
    date_sent = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date. (optional)
    date_sent2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date. (optional)
    date_sent2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_message(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_message(account_sid, to=to, _from=_from, date_sent=date_sent, date_sent2=date_sent2, date_sent2=date_sent2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to read. |
 **to** | **str**| Read messages sent to only this phone number. | [optional]
 **_from** | **str**| Read messages sent from only this phone number or alphanumeric sender ID. | [optional]
 **date_sent** | **datetime**| The date of the messages to show. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT to read only messages sent on this date. For example: &#x60;2009-07-06&#x60;. You can also specify an inequality, such as &#x60;DateSent&lt;&#x3D;YYYY-MM-DD&#x60;, to read messages sent on or before midnight on a date, and &#x60;DateSent&gt;&#x3D;YYYY-MM-DD&#x60; to read messages sent on or after midnight on a date. | [optional]
 **date_sent2** | **datetime**| The date of the messages to show. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT to read only messages sent on this date. For example: &#x60;2009-07-06&#x60;. You can also specify an inequality, such as &#x60;DateSent&lt;&#x3D;YYYY-MM-DD&#x60;, to read messages sent on or before midnight on a date, and &#x60;DateSent&gt;&#x3D;YYYY-MM-DD&#x60; to read messages sent on or after midnight on a date. | [optional]
 **date_sent2** | **datetime**| The date of the messages to show. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT to read only messages sent on this date. For example: &#x60;2009-07-06&#x60;. You can also specify an inequality, such as &#x60;DateSent&lt;&#x3D;YYYY-MM-DD&#x60;, to read messages sent on or before midnight on a date, and &#x60;DateSent&gt;&#x3D;YYYY-MM-DD&#x60; to read messages sent on or after midnight on a date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification**
> InlineResponse20030 list_notification(account_sid)



Retrieve a list of notifications belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20030 import InlineResponse20030
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resources to read.
    log = 1 # int | Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read. (optional)
    message_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date. (optional)
    message_date2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date. (optional)
    message_date2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_notification(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_notification: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_notification(account_sid, log=log, message_date=message_date, message_date2=message_date2, message_date2=message_date2, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resources to read. |
 **log** | **int**| Only read notifications of the specified log level. Can be:  &#x60;0&#x60; to read only ERROR notifications or &#x60;1&#x60; to read only WARNING notifications. By default, all notifications are read. | [optional]
 **message_date** | **datetime**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional]
 **message_date2** | **datetime**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional]
 **message_date2** | **datetime**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outgoing_caller_id**
> InlineResponse20031 list_outgoing_caller_id(account_sid)



Retrieve a list of outgoing-caller-ids belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20031 import InlineResponse20031
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read.
    phone_number = "PhoneNumber_example" # str | The phone number of the OutgoingCallerId resources to read. (optional)
    friendly_name = "FriendlyName_example" # str | The string that identifies the OutgoingCallerId resources to read. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_outgoing_caller_id(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_outgoing_caller_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_outgoing_caller_id(account_sid, phone_number=phone_number, friendly_name=friendly_name, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_outgoing_caller_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read. |
 **phone_number** | **str**| The phone number of the OutgoingCallerId resources to read. | [optional]
 **friendly_name** | **str**| The string that identifies the OutgoingCallerId resources to read. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_participant**
> InlineResponse20018 list_participant(account_sid, conference_sid)



Retrieve a list of participants belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20018 import InlineResponse20018
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to read.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the conference with the participants to read.
    muted = True # bool | Whether to return only participants that are muted. Can be: `true` or `false`. (optional)
    hold = True # bool | Whether to return only participants that are on hold. Can be: `true` or `false`. (optional)
    coaching = True # bool | Whether to return only participants who are coaching another call. Can be: `true` or `false`. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_participant(account_sid, conference_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_participant(account_sid, conference_sid, muted=muted, hold=hold, coaching=coaching, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to read. |
 **conference_sid** | **str**| The SID of the conference with the participants to read. |
 **muted** | **bool**| Whether to return only participants that are muted. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **hold** | **bool**| Whether to return only participants that are on hold. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **coaching** | **bool**| Whether to return only participants who are coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_queue**
> InlineResponse20032 list_queue(account_sid)



Retrieve a list of queues belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20032 import InlineResponse20032
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_queue(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_queue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_queue(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recording**
> InlineResponse20034 list_recording(account_sid)



Retrieve a list of recordings belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20034 import InlineResponse20034
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read.
    date_created = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date. (optional)
    date_created2 = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date. (optional)
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read. (optional)
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The Conference SID that identifies the conference associated with the recording to read. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_recording(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_recording(account_sid, date_created=date_created, date_created2=date_created2, date_created2=date_created2, call_sid=call_sid, conference_sid=conference_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read. |
 **date_created** | **datetime**| Only include recordings that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read recordings that were created on this date. You can also specify an inequality, such as &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60;, to read recordings that were created on or before midnight of this date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; to read recordings that were created on or after midnight of this date. | [optional]
 **date_created2** | **datetime**| Only include recordings that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read recordings that were created on this date. You can also specify an inequality, such as &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60;, to read recordings that were created on or before midnight of this date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; to read recordings that were created on or after midnight of this date. | [optional]
 **date_created2** | **datetime**| Only include recordings that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read recordings that were created on this date. You can also specify an inequality, such as &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60;, to read recordings that were created on or before midnight of this date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; to read recordings that were created on or after midnight of this date. | [optional]
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read. | [optional]
 **conference_sid** | **str**| The Conference SID that identifies the conference associated with the recording to read. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recording_add_on_result**
> InlineResponse20036 list_recording_add_on_result(account_sid, reference_sid)



Retrieve a list of results belonging to the recording

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20036 import InlineResponse20036
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read.
    reference_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the recording to which the result to read belongs.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_recording_add_on_result(account_sid, reference_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording_add_on_result: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_recording_add_on_result(account_sid, reference_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording_add_on_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read. |
 **reference_sid** | **str**| The SID of the recording to which the result to read belongs. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recording_add_on_result_payload**
> InlineResponse20037 list_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid)



Retrieve a list of payloads belonging to the AddOnResult

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20037 import InlineResponse20037
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read.
    reference_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs.
    add_on_result_sid = "XR62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the AddOnResult to which the payloads to read belongs.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording_add_on_result_payload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_recording_add_on_result_payload(account_sid, reference_sid, add_on_result_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording_add_on_result_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read. |
 **reference_sid** | **str**| The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs. |
 **add_on_result_sid** | **str**| The SID of the AddOnResult to which the payloads to read belongs. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recording_transcription**
> InlineResponse20035 list_recording_transcription(account_sid, recording_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20035 import InlineResponse20035
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read.
    recording_sid = "RE62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcriptions to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_recording_transcription(account_sid, recording_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording_transcription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_recording_transcription(account_sid, recording_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_recording_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read. |
 **recording_sid** | **str**| The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcriptions to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_short_code**
> InlineResponse20048 list_short_code(account_sid)



Retrieve a list of short-codes belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20048 import InlineResponse20048
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read.
    friendly_name = "FriendlyName_example" # str | The string that identifies the ShortCode resources to read. (optional)
    short_code = "ShortCode_example" # str | Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_short_code(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_short_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_short_code(account_sid, friendly_name=friendly_name, short_code=short_code, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_short_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read. |
 **friendly_name** | **str**| The string that identifies the ShortCode resources to read. | [optional]
 **short_code** | **str**| Only show the ShortCode resources that match this pattern. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signing_key**
> InlineResponse20049 list_signing_key(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20049 import InlineResponse20049
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | 
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_signing_key(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_signing_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_signing_key(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**|  |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_auth_calls_credential_list_mapping**
> InlineResponse20041 list_sip_auth_calls_credential_list_mapping(account_sid, domain_sid)



Retrieve a list of credential list mappings belonging to the domain used in the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20041 import InlineResponse20041
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_auth_calls_credential_list_mapping(account_sid, domain_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_auth_calls_credential_list_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_auth_calls_credential_list_mapping(account_sid, domain_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_auth_calls_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_auth_calls_ip_access_control_list_mapping**
> InlineResponse20042 list_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid)



Retrieve a list of IP Access Control List mappings belonging to the domain used in the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20042 import InlineResponse20042
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_auth_calls_ip_access_control_list_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_auth_calls_ip_access_control_list_mapping(account_sid, domain_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_auth_calls_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_auth_registrations_credential_list_mapping**
> InlineResponse20043 list_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid)



Retrieve a list of credential list mappings belonging to the domain used in the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20043 import InlineResponse20043
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the SIP domain that contains the resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_auth_registrations_credential_list_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_auth_registrations_credential_list_mapping(account_sid, domain_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_auth_registrations_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read. |
 **domain_sid** | **str**| The SID of the SIP domain that contains the resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_credential**
> InlineResponse20039 list_sip_credential(account_sid, credential_list_sid)



Retrieve a list of credentials.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20039 import InlineResponse20039
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the credential list that contains the desired credentials.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_credential(account_sid, credential_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_credential: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_credential(account_sid, credential_list_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **credential_list_sid** | **str**| The unique id that identifies the credential list that contains the desired credentials. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_credential_list**
> InlineResponse20038 list_sip_credential_list(account_sid)



Get All Credential Lists

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20038 import InlineResponse20038
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_credential_list(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_credential_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_credential_list(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_credential_list_mapping**
> InlineResponse20044 list_sip_credential_list_mapping(account_sid, domain_sid)



Read multiple CredentialListMapping resources from an account.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20044 import InlineResponse20044
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP Domain that includes the resource to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_credential_list_mapping(account_sid, domain_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_credential_list_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_credential_list_mapping(account_sid, domain_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_credential_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_domain**
> InlineResponse20040 list_sip_domain(account_sid)



Retrieve a list of domains belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20040 import InlineResponse20040
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_domain(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_domain(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_ip_access_control_list**
> InlineResponse20046 list_sip_ip_access_control_list(account_sid)



Retrieve a list of IpAccessControlLists that belong to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20046 import InlineResponse20046
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_ip_access_control_list(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_ip_access_control_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_ip_access_control_list(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_ip_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_ip_access_control_list_mapping**
> InlineResponse20045 list_sip_ip_access_control_list_mapping(account_sid, domain_sid)



Retrieve a list of IpAccessControlListMapping resources.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20045 import InlineResponse20045
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    domain_sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the SIP domain.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_ip_access_control_list_mapping(account_sid, domain_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_ip_access_control_list_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_ip_access_control_list_mapping(account_sid, domain_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_ip_access_control_list_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **domain_sid** | **str**| A 34 character string that uniquely identifies the SIP domain. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sip_ip_address**
> InlineResponse20047 list_sip_ip_address(account_sid, ip_access_control_list_sid)



Read multiple IpAddress resources.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20047 import InlineResponse20047
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The IpAccessControlList Sid that identifies the IpAddress resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_sip_ip_address(account_sid, ip_access_control_list_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_ip_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_sip_ip_address(account_sid, ip_access_control_list_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_sip_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **ip_access_control_list_sid** | **str**| The IpAccessControlList Sid that identifies the IpAddress resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transcription**
> InlineResponse20050 list_transcription(account_sid)



Retrieve a list of transcriptions belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20050 import InlineResponse20050
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read.
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_transcription(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_transcription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_transcription(account_sid, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read. |
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record**
> InlineResponse20051 list_usage_record(account_sid)



Retrieve a list of usage-records belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20051 import InlineResponse20051
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_all_time**
> InlineResponse20052 list_usage_record_all_time(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20052 import InlineResponse20052
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_all_time(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_all_time: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_all_time(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_all_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_daily**
> InlineResponse20053 list_usage_record_daily(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20053 import InlineResponse20053
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_daily(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_daily: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_daily(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_daily: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_last_month**
> InlineResponse20054 list_usage_record_last_month(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20054 import InlineResponse20054
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_last_month(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_last_month: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_last_month(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_last_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_monthly**
> InlineResponse20055 list_usage_record_monthly(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20055 import InlineResponse20055
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_monthly(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_monthly: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_monthly(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_monthly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_this_month**
> InlineResponse20056 list_usage_record_this_month(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20056 import InlineResponse20056
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_this_month(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_this_month: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_this_month(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_this_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_today**
> InlineResponse20057 list_usage_record_today(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20057 import InlineResponse20057
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_today(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_today: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_today(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_today: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_yearly**
> InlineResponse20058 list_usage_record_yearly(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20058 import InlineResponse20058
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_yearly(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_yearly: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_yearly(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_yearly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_record_yesterday**
> InlineResponse20059 list_usage_record_yesterday(account_sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20059 import InlineResponse20059
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    category = "agent-conference" # str | The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date. (optional)
    include_subaccounts = True # bool | Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account. (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_record_yesterday(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_yesterday: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_record_yesterday(account_sid, category=category, start_date=start_date, end_date=end_date, include_subaccounts=include_subaccounts, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_record_yesterday: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read. |
 **category** | **str**| The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved. | [optional]
 **start_date** | **datetime**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date. | [optional]
 **end_date** | **datetime**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date. | [optional]
 **include_subaccounts** | **bool**| Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account. | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_trigger**
> InlineResponse20060 list_usage_trigger(account_sid)



Retrieve a list of usage-triggers belonging to the account used to make the request

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response20060 import InlineResponse20060
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read.
    recurring = "daily" # str | The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers. (optional)
    trigger_by = "count" # str | The trigger field of the UsageTriggers to read.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price). (optional)
    usage_category = "agent-conference" # str | The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories). (optional)
    page_size = 1 # int | How many resources to return in each list page. The default is 50, and the maximum is 1000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_usage_trigger(account_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_trigger: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_usage_trigger(account_sid, recurring=recurring, trigger_by=trigger_by, usage_category=usage_category, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_usage_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read. |
 **recurring** | **str**| The frequency of recurring UsageTriggers to read. Can be: &#x60;daily&#x60;, &#x60;monthly&#x60;, or &#x60;yearly&#x60; to read recurring UsageTriggers. An empty value or a value of &#x60;alltime&#x60; reads non-recurring UsageTriggers. | [optional]
 **trigger_by** | **str**| The trigger field of the UsageTriggers to read.  Can be: &#x60;count&#x60;, &#x60;usage&#x60;, or &#x60;price&#x60; as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price). | [optional]
 **usage_category** | **str**| The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories). | [optional]
 **page_size** | **int**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional]

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> ApiV2010Account update_account(sid)



Modify the properties of a given Account

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account import ApiV2010Account
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The Account Sid that uniquely identifies the account to update
    friendly_name = "friendly_name_example" # str | Update the human-readable description of this Account (optional)
    status = "active" # str | Alter the status of this account: use `closed` to irreversibly close this account, `suspended` to temporarily suspend it, or `active` to reactivate it. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_account(sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_account(sid, friendly_name=friendly_name, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| The Account Sid that uniquely identifies the account to update |
 **friendly_name** | **str**| Update the human-readable description of this Account | [optional]
 **status** | **str**| Alter the status of this account: use &#x60;closed&#x60; to irreversibly close this account, &#x60;suspended&#x60; to temporarily suspend it, or &#x60;active&#x60; to reactivate it. | [optional]

### Return type

[**ApiV2010Account**](ApiV2010Account.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> ApiV2010AccountAddress update_address(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_address import ApiV2010AccountAddress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update.
    sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Address resource to update.
    auto_correct_address = True # bool | Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide. (optional)
    city = "city_example" # str | The city of the address. (optional)
    customer_name = "customer_name_example" # str | The name to associate with the address. (optional)
    emergency_enabled = True # bool | Whether to enable emergency calling on the address. Can be: `true` or `false`. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the address. It can be up to 64 characters long. (optional)
    postal_code = "postal_code_example" # str | The postal code of the address. (optional)
    region = "region_example" # str | The state or region of the address. (optional)
    street = "street_example" # str | The number and street address of the address. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_address(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_address(account_sid, sid, auto_correct_address=auto_correct_address, city=city, customer_name=customer_name, emergency_enabled=emergency_enabled, friendly_name=friendly_name, postal_code=postal_code, region=region, street=street)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Address resource to update. |
 **auto_correct_address** | **bool**| Whether we should automatically correct the address. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If empty or &#x60;true&#x60;, we will correct the address you provide if necessary. If &#x60;false&#x60;, we won&#39;t alter the address you provide. | [optional]
 **city** | **str**| The city of the address. | [optional]
 **customer_name** | **str**| The name to associate with the address. | [optional]
 **emergency_enabled** | **bool**| Whether to enable emergency calling on the address. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the address. It can be up to 64 characters long. | [optional]
 **postal_code** | **str**| The postal code of the address. | [optional]
 **region** | **str**| The state or region of the address. | [optional]
 **street** | **str**| The number and street address of the address. | [optional]

### Return type

[**ApiV2010AccountAddress**](ApiV2010AccountAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> ApiV2010AccountApplication update_application(account_sid, sid)



Updates the application's properties

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_application import ApiV2010AccountApplication
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update.
    sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Application resource to update.
    api_version = "api_version_example" # str | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is your account's default API version. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)
    message_status_callback = "message_status_callback_example" # str | The URL we should call using a POST method to send message status information to your application. (optional)
    sms_fallback_method = "head" # str | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`. (optional)
    sms_status_callback = "sms_status_callback_example" # str | Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`. (optional)
    voice_caller_id_lookup = True # bool | Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`. (optional)
    voice_url = "voice_url_example" # str | The URL we should call when the phone number assigned to this application receives a call. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_application(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_application(account_sid, sid, api_version=api_version, friendly_name=friendly_name, message_status_callback=message_status_callback, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_status_callback=sms_status_callback, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Application resource to update. |
 **api_version** | **str**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is your account&#39;s default API version. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]
 **message_status_callback** | **str**| The URL we should call using a POST method to send message status information to your application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **sms_status_callback** | **str**| Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility. | [optional]
 **sms_url** | **str**| The URL we should call when the phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_url** | **str**| The URL we should call when the phone number assigned to this application receives a call. | [optional]

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call**
> ApiV2010AccountCall update_call(account_sid, sid)



Initiates a call redirect or terminates a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call import ApiV2010AccountCall
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to update.
    sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Call resource to update
    fallback_method = "head" # str | The HTTP method that we should use to request the `fallback_url`. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    fallback_url = "fallback_url_example" # str | The URL that we call using the `fallback_method` if an error occurs when requesting or executing the TwiML at `url`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    method = "head" # str | The HTTP method we should use when calling the `url`. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    status = "canceled" # str | The new status of the resource. Can be: `canceled` or `completed`. Specifying `canceled` will attempt to hang up calls that are queued or ringing; however, it will not affect calls already in progress. Specifying `completed` will attempt to hang up a call even if it's already in progress. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. If no `status_callback_event` is specified, we will send the `completed` status. If an `application_sid` parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted). (optional)
    status_callback_method = "head" # str | The HTTP method we should use when requesting the `status_callback` URL. Can be: `GET` or `POST` and the default is `POST`. If an `application_sid` parameter is present, this parameter is ignored. (optional)
    twiml = "twiml_example" # str | TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url parameters are mutually exclusive (optional)
    url = "url_example" # str | The absolute URL that returns the TwiML instructions for the call. We will call this URL using the `method` when the call connects. For more information, see the [Url Parameter](https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter) section in [Making Calls](https://www.twilio.com/docs/voice/make-calls). (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_call(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_call: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_call(account_sid, sid, fallback_method=fallback_method, fallback_url=fallback_url, method=method, status=status, status_callback=status_callback, status_callback_method=status_callback_method, twiml=twiml, url=url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call resource(s) to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Call resource to update |
 **fallback_method** | **str**| The HTTP method that we should use to request the &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **fallback_url** | **str**| The URL that we call using the &#x60;fallback_method&#x60; if an error occurs when requesting or executing the TwiML at &#x60;url&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **method** | **str**| The HTTP method we should use when calling the &#x60;url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **status** | **str**| The new status of the resource. Can be: &#x60;canceled&#x60; or &#x60;completed&#x60;. Specifying &#x60;canceled&#x60; will attempt to hang up calls that are queued or ringing; however, it will not affect calls already in progress. Specifying &#x60;completed&#x60; will attempt to hang up a call even if it&#39;s already in progress. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. If no &#x60;status_callback_event&#x60; is specified, we will send the &#x60;completed&#x60; status. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. URLs must contain a valid hostname (underscores are not permitted). | [optional]
 **status_callback_method** | **str**| The HTTP method we should use when requesting the &#x60;status_callback&#x60; URL. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. If an &#x60;application_sid&#x60; parameter is present, this parameter is ignored. | [optional]
 **twiml** | **str**| TwiML instructions for the call Twilio will use without fetching Twiml from url. Twiml and url parameters are mutually exclusive | [optional]
 **url** | **str**| The absolute URL that returns the TwiML instructions for the call. We will call this URL using the &#x60;method&#x60; when the call connects. For more information, see the [Url Parameter](https://www.twilio.com/docs/voice/make-calls#specify-a-url-parameter) section in [Making Calls](https://www.twilio.com/docs/voice/make-calls). | [optional]

### Return type

[**ApiV2010AccountCall**](ApiV2010AccountCall.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_feedback**
> ApiV2010AccountCallCallFeedback update_call_feedback(account_sid, call_sid, quality_score)



Update a Feedback resource for a call

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_feedback import ApiV2010AccountCallCallFeedback
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The call sid that uniquely identifies the call
    quality_score = 1 # int | The call quality expressed as an integer from `1` to `5` where `1` represents very poor call quality and `5` represents a perfect call.
    issue = "audio-latency" # [str] | One or more issues experienced during the call. The issues can be: `imperfect-audio`, `dropped-call`, `incorrect-caller-id`, `post-dial-delay`, `digits-not-captured`, `audio-latency`, `unsolicited-call`, or `one-way-audio`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_call_feedback(account_sid, call_sid, quality_score)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_call_feedback: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_call_feedback(account_sid, call_sid, quality_score, issue=issue)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_call_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **call_sid** | **str**| The call sid that uniquely identifies the call |
 **quality_score** | **int**| The call quality expressed as an integer from &#x60;1&#x60; to &#x60;5&#x60; where &#x60;1&#x60; represents very poor call quality and &#x60;5&#x60; represents a perfect call. |
 **issue** | **[str]**| One or more issues experienced during the call. The issues can be: &#x60;imperfect-audio&#x60;, &#x60;dropped-call&#x60;, &#x60;incorrect-caller-id&#x60;, &#x60;post-dial-delay&#x60;, &#x60;digits-not-captured&#x60;, &#x60;audio-latency&#x60;, &#x60;unsolicited-call&#x60;, or &#x60;one-way-audio&#x60;. | [optional]

### Return type

[**ApiV2010AccountCallCallFeedback**](ApiV2010AccountCallCallFeedback.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_recording**
> ApiV2010AccountCallCallRecording update_call_recording(account_sid, call_sid, sid, status)



Changes the status of the recording to paused, stopped, or in-progress. Note: Pass `Twilio.CURRENT` instead of recording sid to reference current active recording.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_call_recording import ApiV2010AccountCallCallRecording
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to update.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to update.
    sid = "Sid_example" # str | The Twilio-provided string that uniquely identifies the Recording resource to update.
    status = "in-progress" # str | The new status of the recording. Can be: `stopped`, `paused`, `in-progress`.
    pause_behavior = "pause_behavior_example" # str | Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_call_recording(account_sid, call_sid, sid, status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_call_recording: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_call_recording(account_sid, call_sid, sid, status, pause_behavior=pause_behavior)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_call_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to update. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Recording resource to update. |
 **status** | **str**| The new status of the recording. Can be: &#x60;stopped&#x60;, &#x60;paused&#x60;, &#x60;in-progress&#x60;. |
 **pause_behavior** | **str**| Whether to record during a pause. Can be: &#x60;skip&#x60; or &#x60;silence&#x60; and the default is &#x60;silence&#x60;. &#x60;skip&#x60; does not record during the pause period, while &#x60;silence&#x60; will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting &#x60;status&#x60; is set to &#x60;paused&#x60;. | [optional]

### Return type

[**ApiV2010AccountCallCallRecording**](ApiV2010AccountCallCallRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conference**
> ApiV2010AccountConference update_conference(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference import ApiV2010AccountConference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to update.
    sid = "Sid_example" # str | The Twilio-provided string that uniquely identifies the Conference resource to update
    announce_method = "head" # str | The HTTP method used to call `announce_url`. Can be: `GET` or `POST` and the default is `POST` (optional)
    announce_url = "announce_url_example" # str | The URL we should call to announce something into the conference. The URL can return an MP3, a WAV, or a TwiML document with `<Play>` or `<Say>`. (optional)
    status = "completed" # str | The new status of the resource. Can be:  Can be: `init`, `in-progress`, or `completed`. Specifying `completed` will end the conference and hang up all participants (optional) if omitted the server will use the default value of "completed"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_conference(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_conference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_conference(account_sid, sid, announce_method=announce_method, announce_url=announce_url, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_conference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Conference resource to update |
 **announce_method** | **str**| The HTTP method used to call &#x60;announce_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60; | [optional]
 **announce_url** | **str**| The URL we should call to announce something into the conference. The URL can return an MP3, a WAV, or a TwiML document with &#x60;&lt;Play&gt;&#x60; or &#x60;&lt;Say&gt;&#x60;. | [optional]
 **status** | **str**| The new status of the resource. Can be:  Can be: &#x60;init&#x60;, &#x60;in-progress&#x60;, or &#x60;completed&#x60;. Specifying &#x60;completed&#x60; will end the conference and hang up all participants | [optional] if omitted the server will use the default value of "completed"

### Return type

[**ApiV2010AccountConference**](ApiV2010AccountConference.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conference_recording**
> ApiV2010AccountConferenceConferenceRecording update_conference_recording(account_sid, conference_sid, sid, status)



Changes the status of the recording to paused, stopped, or in-progress. Note: To use `Twilio.CURRENT`, pass it as recording sid.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference_conference_recording import ApiV2010AccountConferenceConferenceRecording
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to update.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The Conference SID that identifies the conference associated with the recording to update.
    sid = "Sid_example" # str | The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use `Twilio.CURRENT` to reference the current active recording.
    status = "in-progress" # str | The new status of the recording. Can be: `stopped`, `paused`, `in-progress`.
    pause_behavior = "pause_behavior_example" # str | Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_conference_recording(account_sid, conference_sid, sid, status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_conference_recording: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_conference_recording(account_sid, conference_sid, sid, status, pause_behavior=pause_behavior)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_conference_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to update. |
 **conference_sid** | **str**| The Conference SID that identifies the conference associated with the recording to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use &#x60;Twilio.CURRENT&#x60; to reference the current active recording. |
 **status** | **str**| The new status of the recording. Can be: &#x60;stopped&#x60;, &#x60;paused&#x60;, &#x60;in-progress&#x60;. |
 **pause_behavior** | **str**| Whether to record during a pause. Can be: &#x60;skip&#x60; or &#x60;silence&#x60; and the default is &#x60;silence&#x60;. &#x60;skip&#x60; does not record during the pause period, while &#x60;silence&#x60; will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting &#x60;status&#x60; is set to &#x60;paused&#x60;. | [optional]

### Return type

[**ApiV2010AccountConferenceConferenceRecording**](ApiV2010AccountConferenceConferenceRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connect_app**
> ApiV2010AccountConnectApp update_connect_app(account_sid, sid)



Update a connect-app with the specified parameters

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_connect_app import ApiV2010AccountConnectApp
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update.
    sid = "CN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
    authorize_redirect_url = "authorize_redirect_url_example" # str | The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App. (optional)
    company_name = "company_name_example" # str | The company name to set for the Connect App. (optional)
    deauthorize_callback_method = "head" # str | The HTTP method to use when calling `deauthorize_callback_url`. (optional)
    deauthorize_callback_url = "deauthorize_callback_url_example" # str | The URL to call using the `deauthorize_callback_method` to de-authorize the Connect App. (optional)
    description = "description_example" # str | A description of the Connect App. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)
    homepage_url = "homepage_url_example" # str | A public URL where users can obtain more information about this Connect App. (optional)
    permissions = "get-all" # [str] | A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: `get-all` and `post-all`. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_connect_app(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_connect_app: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_connect_app(account_sid, sid, authorize_redirect_url=authorize_redirect_url, company_name=company_name, deauthorize_callback_method=deauthorize_callback_method, deauthorize_callback_url=deauthorize_callback_url, description=description, friendly_name=friendly_name, homepage_url=homepage_url, permissions=permissions)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_connect_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the ConnectApp resource to update. |
 **authorize_redirect_url** | **str**| The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App. | [optional]
 **company_name** | **str**| The company name to set for the Connect App. | [optional]
 **deauthorize_callback_method** | **str**| The HTTP method to use when calling &#x60;deauthorize_callback_url&#x60;. | [optional]
 **deauthorize_callback_url** | **str**| The URL to call using the &#x60;deauthorize_callback_method&#x60; to de-authorize the Connect App. | [optional]
 **description** | **str**| A description of the Connect App. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]
 **homepage_url** | **str**| A public URL where users can obtain more information about this Connect App. | [optional]
 **permissions** | **[str]**| A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: &#x60;get-all&#x60; and &#x60;post-all&#x60;. | [optional]

### Return type

[**ApiV2010AccountConnectApp**](ApiV2010AccountConnectApp.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_incoming_phone_number**
> ApiV2010AccountIncomingPhoneNumber update_incoming_phone_number(account_sid, sid)



Update an incoming-phone-number instance.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_incoming_phone_number import ApiV2010AccountIncomingPhoneNumber
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers).
    sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.
    account_sid2 = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers). (optional)
    address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations. (optional)
    api_version = "api_version_example" # str | The API version to use for incoming calls made to the phone number. The default is `2010-04-01`. (optional)
    bundle_sid = "BU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. (optional)
    emergency_address_sid = "AD62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the emergency address configuration to use for emergency calling from this phone number. (optional)
    emergency_status = "Active" # str | The configuration status parameter that determines whether the phone number is enabled for emergency calling. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. (optional)
    identity_sid = "RI62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations. (optional)
    sms_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application that should handle SMS messages sent to the number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application. (optional)
    sms_fallback_method = "head" # str | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when the phone number receives an incoming SMS message. (optional)
    status_callback = "status_callback_example" # str | The URL we should call using the `status_callback_method` to send status information to your application. (optional)
    status_callback_method = "head" # str | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    trunk_sid = "TK62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Trunk we should use to handle phone calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa. (optional)
    voice_application_sid = "AP62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the application we should use to handle phone calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa. (optional)
    voice_caller_id_lookup = True # bool | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`. (optional)
    voice_fallback_method = "head" # str | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`. (optional)
    voice_method = "head" # str | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    voice_receive_mode = "voice" # str | The configuration parameter for the phone number to receive incoming voice calls or faxes. Can be: `fax` or `voice` and defaults to `voice`. (optional)
    voice_url = "voice_url_example" # str | The URL that we should call to answer a call to the phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_incoming_phone_number(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_incoming_phone_number: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_incoming_phone_number(account_sid, sid, account_sid2=account_sid2, address_sid=address_sid, api_version=api_version, bundle_sid=bundle_sid, emergency_address_sid=emergency_address_sid, emergency_status=emergency_status, friendly_name=friendly_name, identity_sid=identity_sid, sms_application_sid=sms_application_sid, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, status_callback=status_callback, status_callback_method=status_callback_method, trunk_sid=trunk_sid, voice_application_sid=voice_application_sid, voice_caller_id_lookup=voice_caller_id_lookup, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_receive_mode=voice_receive_mode, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_incoming_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers). |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update. |
 **account_sid2** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IncomingPhoneNumber resource to update.  For more information, see [Exchanging Numbers Between Subaccounts](https://www.twilio.com/docs/iam/api/subaccounts#exchanging-numbers). | [optional]
 **address_sid** | **str**| The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations. | [optional]
 **api_version** | **str**| The API version to use for incoming calls made to the phone number. The default is &#x60;2010-04-01&#x60;. | [optional]
 **bundle_sid** | **str**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional]
 **emergency_address_sid** | **str**| The SID of the emergency address configuration to use for emergency calling from this phone number. | [optional]
 **emergency_status** | **str**| The configuration status parameter that determines whether the phone number is enabled for emergency calling. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number. | [optional]
 **identity_sid** | **str**| The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations. | [optional]
 **sms_application_sid** | **str**| The SID of the application that should handle SMS messages sent to the number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those set on the application. | [optional]
 **sms_fallback_method** | **str**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **sms_url** | **str**| The URL we should call when the phone number receives an incoming SMS message. | [optional]
 **status_callback** | **str**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional]
 **status_callback_method** | **str**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **trunk_sid** | **str**| The SID of the Trunk we should use to handle phone calls to the phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional]
 **voice_application_sid** | **str**| The SID of the application we should use to handle phone calls to the phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional]
 **voice_caller_id_lookup** | **bool**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **voice_fallback_method** | **str**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **voice_receive_mode** | **str**| The configuration parameter for the phone number to receive incoming voice calls or faxes. Can be: &#x60;fax&#x60; or &#x60;voice&#x60; and defaults to &#x60;voice&#x60;. | [optional]
 **voice_url** | **str**| The URL that we should call to answer a call to the phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional]

### Return type

[**ApiV2010AccountIncomingPhoneNumber**](ApiV2010AccountIncomingPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key**
> ApiV2010AccountKey update_key(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_key import ApiV2010AccountKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to update.
    sid = "SK62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Key resource to update.
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_key(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_key(account_sid, sid, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Key resources to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Key resource to update. |
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]

### Return type

[**ApiV2010AccountKey**](ApiV2010AccountKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member**
> ApiV2010AccountQueueMember update_member(account_sid, queue_sid, call_sid, url)



Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_queue_member import ApiV2010AccountQueueMember
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to update.
    queue_sid = "QU62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the Queue in which to find the members to update.
    call_sid = "CallSid_example" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update.
    url = "url_example" # str | The absolute URL of the Queue resource.
    method = "head" # str | How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_member(account_sid, queue_sid, call_sid, url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_member(account_sid, queue_sid, call_sid, url, method=method)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to update. |
 **queue_sid** | **str**| The SID of the Queue in which to find the members to update. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update. |
 **url** | **str**| The absolute URL of the Queue resource. |
 **method** | **str**| How to pass the update request data. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. &#x60;POST&#x60; sends the data as encoded form data and &#x60;GET&#x60; sends the data as query parameters. | [optional]

### Return type

[**ApiV2010AccountQueueMember**](ApiV2010AccountQueueMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message**
> ApiV2010AccountMessage update_message(account_sid, sid, body)



To redact a message-body from a post-flight message record, post to the message instance resource with an empty body

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_message import ApiV2010AccountMessage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to update.
    sid = "MM2ECB020842930cc01FFCCfeEe150AC3" # str | The Twilio-provided string that uniquely identifies the Message resource to update.
    body = "body_example" # str | The text of the message you want to send. Can be up to 1,600 characters long.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_message(account_sid, sid, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Message resource to update. |
 **body** | **str**| The text of the message you want to send. Can be up to 1,600 characters long. |

### Return type

[**ApiV2010AccountMessage**](ApiV2010AccountMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_outgoing_caller_id**
> ApiV2010AccountOutgoingCallerId update_outgoing_caller_id(account_sid, sid)



Updates the caller-id

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_outgoing_caller_id import ApiV2010AccountOutgoingCallerId
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update.
    sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_outgoing_caller_id(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_outgoing_caller_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_outgoing_caller_id(account_sid, sid, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_outgoing_caller_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update. |
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]

### Return type

[**ApiV2010AccountOutgoingCallerId**](ApiV2010AccountOutgoingCallerId.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_participant**
> ApiV2010AccountConferenceParticipant update_participant(account_sid, conference_sid, call_sid)



Update the properties of the participant

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_conference_participant import ApiV2010AccountConferenceParticipant
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to update.
    conference_sid = "CF62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the conference with the participant to update.
    call_sid = "CallSid_example" # str | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to update. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20.
    announce_method = "head" # str | The HTTP method we should use to call `announce_url`. Can be: `GET` or `POST` and defaults to `POST`. (optional)
    announce_url = "announce_url_example" # str | The URL we call using the `announce_method` for an announcement to the participant. The URL must return an MP3 file, a WAV file, or a TwiML document that contains `<Play>` or `<Say>` commands. (optional)
    beep_on_exit = True # bool | Whether to play a notification beep to the conference when the participant exits. Can be: `true` or `false`. (optional)
    call_sid_to_coach = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the participant who is being `coached`. The participant being coached is the only participant who can hear the participant who is `coaching`. (optional)
    coaching = True # bool | Whether the participant is coaching another call. Can be: `true` or `false`. If not present, defaults to `false` unless `call_sid_to_coach` is defined. If `true`, `call_sid_to_coach` must be defined. (optional)
    end_conference_on_exit = True # bool | Whether to end the conference when the participant leaves. Can be: `true` or `false` and defaults to `false`. (optional)
    hold = True # bool | Whether the participant should be on hold. Can be: `true` or `false`. `true` puts the participant on hold, and `false` lets them rejoin the conference. (optional)
    hold_method = "head" # str | The HTTP method we should use to call `hold_url`. Can be: `GET` or `POST` and the default is `GET`. (optional)
    hold_url = "hold_url_example" # str | The URL we call using the `hold_method` for  music that plays when the participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML document that contains the `<Play>`, `<Say>` or `<Redirect>` commands. (optional)
    muted = True # bool | Whether the participant should be muted. Can be `true` or `false`. `true` will mute the participant, and `false` will un-mute them. Anything value other than `true` or `false` is interpreted as `false`. (optional)
    wait_method = "head" # str | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file. (optional)
    wait_url = "wait_url_example" # str | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_participant(account_sid, conference_sid, call_sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_participant(account_sid, conference_sid, call_sid, announce_method=announce_method, announce_url=announce_url, beep_on_exit=beep_on_exit, call_sid_to_coach=call_sid_to_coach, coaching=coaching, end_conference_on_exit=end_conference_on_exit, hold=hold, hold_method=hold_method, hold_url=hold_url, muted=muted, wait_method=wait_method, wait_url=wait_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resources to update. |
 **conference_sid** | **str**| The SID of the conference with the participant to update. |
 **call_sid** | **str**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID or label of the participant to update. Non URL safe characters in a label must be percent encoded, for example, a space character is represented as %20. |
 **announce_method** | **str**| The HTTP method we should use to call &#x60;announce_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional]
 **announce_url** | **str**| The URL we call using the &#x60;announce_method&#x60; for an announcement to the participant. The URL must return an MP3 file, a WAV file, or a TwiML document that contains &#x60;&lt;Play&gt;&#x60; or &#x60;&lt;Say&gt;&#x60; commands. | [optional]
 **beep_on_exit** | **bool**| Whether to play a notification beep to the conference when the participant exits. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional]
 **call_sid_to_coach** | **str**| The SID of the participant who is being &#x60;coached&#x60;. The participant being coached is the only participant who can hear the participant who is &#x60;coaching&#x60;. | [optional]
 **coaching** | **bool**| Whether the participant is coaching another call. Can be: &#x60;true&#x60; or &#x60;false&#x60;. If not present, defaults to &#x60;false&#x60; unless &#x60;call_sid_to_coach&#x60; is defined. If &#x60;true&#x60;, &#x60;call_sid_to_coach&#x60; must be defined. | [optional]
 **end_conference_on_exit** | **bool**| Whether to end the conference when the participant leaves. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional]
 **hold** | **bool**| Whether the participant should be on hold. Can be: &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; puts the participant on hold, and &#x60;false&#x60; lets them rejoin the conference. | [optional]
 **hold_method** | **str**| The HTTP method we should use to call &#x60;hold_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;GET&#x60;. | [optional]
 **hold_url** | **str**| The URL we call using the &#x60;hold_method&#x60; for  music that plays when the participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML document that contains the &#x60;&lt;Play&gt;&#x60;, &#x60;&lt;Say&gt;&#x60; or &#x60;&lt;Redirect&gt;&#x60; commands. | [optional]
 **muted** | **bool**| Whether the participant should be muted. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; will mute the participant, and &#x60;false&#x60; will un-mute them. Anything value other than &#x60;true&#x60; or &#x60;false&#x60; is interpreted as &#x60;false&#x60;. | [optional]
 **wait_method** | **str**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional]
 **wait_url** | **str**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional]

### Return type

[**ApiV2010AccountConferenceParticipant**](ApiV2010AccountConferenceParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payments**
> ApiV2010AccountCallPayments update_payments(account_sid, call_sid, sid, idempotency_key, status_callback)



update an instance of payments with different phases of payment flows.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_call_payments import ApiV2010AccountCallPayments
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource.
    call_sid = "CA62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource.
    sid = "PK62ECB020842930cc01FFCCfeEe150AC" # str | The SID of Payments session that needs to be updated.
    idempotency_key = "idempotency_key_example" # str | A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
    status_callback = "status_callback_example" # str | Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
    capture = "payment-card-number" # str | The piece of payment information that you wish the caller to enter. Must be one of `payment-card-number`, `expiration-date`, `security-code`, `postal-code`, `bank-routing-number`, or `bank-account-number`. (optional)
    status = "complete" # str | Indicates whether the current payment session should be cancelled or completed. When `cancel` the payment session is cancelled. When `complete`, Twilio sends the payment information to the selected <Pay> connector for processing. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_payments(account_sid, call_sid, sid, idempotency_key, status_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_payments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_payments(account_sid, call_sid, sid, idempotency_key, status_callback, capture=capture, status=status)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource. |
 **call_sid** | **str**| The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource. |
 **sid** | **str**| The SID of Payments session that needs to be updated. |
 **idempotency_key** | **str**| A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated. |
 **status_callback** | **str**| Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests. |
 **capture** | **str**| The piece of payment information that you wish the caller to enter. Must be one of &#x60;payment-card-number&#x60;, &#x60;expiration-date&#x60;, &#x60;security-code&#x60;, &#x60;postal-code&#x60;, &#x60;bank-routing-number&#x60;, or &#x60;bank-account-number&#x60;. | [optional]
 **status** | **str**| Indicates whether the current payment session should be cancelled or completed. When &#x60;cancel&#x60; the payment session is cancelled. When &#x60;complete&#x60;, Twilio sends the payment information to the selected &lt;Pay&gt; connector for processing. | [optional]

### Return type

[**ApiV2010AccountCallPayments**](ApiV2010AccountCallPayments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_queue**
> ApiV2010AccountQueue update_queue(account_sid, sid)



Update the queue with the new parameters

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_queue import ApiV2010AccountQueue
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update.
    sid = "QU62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the Queue resource to update
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe this resource. It can be up to 64 characters long. (optional)
    max_size = 1 # int | The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_queue(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_queue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_queue(account_sid, sid, friendly_name=friendly_name, max_size=max_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the Queue resource to update |
 **friendly_name** | **str**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. | [optional]
 **max_size** | **int**| The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000. | [optional]

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_short_code**
> ApiV2010AccountShortCode update_short_code(account_sid, sid)



Update a short code with the following parameters

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_short_code import ApiV2010AccountShortCode
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update.
    sid = "SC62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the ShortCode resource to update
    api_version = "api_version_example" # str | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code. (optional)
    sms_fallback_method = "head" # str | The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`. (optional)
    sms_fallback_url = "sms_fallback_url_example" # str | The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`. (optional)
    sms_method = "head" # str | The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`. (optional)
    sms_url = "sms_url_example" # str | The URL we should call when receiving an incoming SMS message to this short code. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_short_code(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_short_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_short_code(account_sid, sid, api_version=api_version, friendly_name=friendly_name, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_short_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the ShortCode resource to update |
 **api_version** | **str**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the &#x60;FriendlyName&#x60; is the short code. | [optional]
 **sms_fallback_method** | **str**| The HTTP method that we should use to call the &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **sms_fallback_url** | **str**| The URL that we should call if an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional]
 **sms_method** | **str**| The HTTP method we should use when calling the &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **sms_url** | **str**| The URL we should call when receiving an incoming SMS message to this short code. | [optional]

### Return type

[**ApiV2010AccountShortCode**](ApiV2010AccountShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signing_key**
> ApiV2010AccountSigningKey update_signing_key(account_sid, sid)



### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_signing_key import ApiV2010AccountSigningKey
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | 
    sid = "SK62ECB020842930cc01FFCCfeEe150AC" # str | 
    friendly_name = "friendly_name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_signing_key(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_signing_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_signing_key(account_sid, sid, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_signing_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**|  |
 **sid** | **str**|  |
 **friendly_name** | **str**|  | [optional]

### Return type

[**ApiV2010AccountSigningKey**](ApiV2010AccountSigningKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_credential**
> ApiV2010AccountSipSipCredentialListSipCredential update_sip_credential(account_sid, credential_list_sid, sid)



Update a credential resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_credential_list_sip_credential import ApiV2010AccountSipSipCredentialListSipCredential
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    credential_list_sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the credential list that includes this credential.
    sid = "CR62ECB020842930cc01FFCCfeEe150AC" # str | The unique id that identifies the resource to update.
    password = "password_example" # str | The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`) (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sip_credential(account_sid, credential_list_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_credential: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_sip_credential(account_sid, credential_list_sid, sid, password=password)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **credential_list_sid** | **str**| The unique id that identifies the credential list that includes this credential. |
 **sid** | **str**| The unique id that identifies the resource to update. |
 **password** | **str**| The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;) | [optional]

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_credential_list**
> ApiV2010AccountSipSipCredentialList update_sip_credential_list(account_sid, sid, friendly_name)



Update a Credential List

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_credential_list import ApiV2010AccountSipSipCredentialList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the Account that is responsible for this resource.
    sid = "CL62ECB020842930cc01FFCCfeEe150AC" # str | The credential list Sid that uniquely identifies this resource
    friendly_name = "friendly_name_example" # str | A human readable descriptive text for a CredentialList, up to 64 characters long.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sip_credential_list(account_sid, sid, friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the Account that is responsible for this resource. |
 **sid** | **str**| The credential list Sid that uniquely identifies this resource |
 **friendly_name** | **str**| A human readable descriptive text for a CredentialList, up to 64 characters long. |

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_domain**
> ApiV2010AccountSipSipDomain update_sip_domain(account_sid, sid)



Update the attributes of a domain

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_domain import ApiV2010AccountSipSipDomain
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update.
    sid = "SD62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the SipDomain resource to update.
    byoc_trunk_sid = "BY62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. (optional)
    domain_name = "domain_name_example" # str | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\"-\\\" and must end with `sip.twilio.com`. (optional)
    emergency_caller_sid = "PN62ECB020842930cc01FFCCfeEe150AC" # str | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. (optional)
    emergency_calling_enabled = True # bool | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you created to describe the resource. It can be up to 64 characters long. (optional)
    secure = True # bool | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. (optional)
    sip_registration = True # bool | Whether to allow SIP Endpoints to register with the domain to receive calls. Can be `true` or `false`. `true` allows SIP Endpoints to register with the domain to receive calls, `false` does not. (optional)
    voice_fallback_method = "head" # str | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`. (optional)
    voice_fallback_url = "voice_fallback_url_example" # str | The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`. (optional)
    voice_method = "head" # str | The HTTP method we should use to call `voice_url` (optional)
    voice_status_callback_method = "head" # str | The HTTP method we should use to call `voice_status_callback_url`. Can be: `GET` or `POST`. (optional)
    voice_status_callback_url = "voice_status_callback_url_example" # str | The URL that we should call to pass status parameters (such as call ended) to your application. (optional)
    voice_url = "voice_url_example" # str | The URL we should call when the domain receives a call. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sip_domain(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_sip_domain(account_sid, sid, byoc_trunk_sid=byoc_trunk_sid, domain_name=domain_name, emergency_caller_sid=emergency_caller_sid, emergency_calling_enabled=emergency_calling_enabled, friendly_name=friendly_name, secure=secure, sip_registration=sip_registration, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_status_callback_method=voice_status_callback_method, voice_status_callback_url=voice_status_callback_url, voice_url=voice_url)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the SipDomain resource to update. |
 **byoc_trunk_sid** | **str**| The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional]
 **domain_name** | **str**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;. | [optional]
 **emergency_caller_sid** | **str**| Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional]
 **emergency_calling_enabled** | **bool**| Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional]
 **friendly_name** | **str**| A descriptive string that you created to describe the resource. It can be up to 64 characters long. | [optional]
 **secure** | **bool**| Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional]
 **sip_registration** | **bool**| Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not. | [optional]
 **voice_fallback_method** | **str**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_fallback_url** | **str**| The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;. | [optional]
 **voice_method** | **str**| The HTTP method we should use to call &#x60;voice_url&#x60; | [optional]
 **voice_status_callback_method** | **str**| The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]
 **voice_status_callback_url** | **str**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional]
 **voice_url** | **str**| The URL we should call when the domain receives a call. | [optional]

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_ip_access_control_list**
> ApiV2010AccountSipSipIpAccessControlList update_sip_ip_access_control_list(account_sid, sid, friendly_name)



Rename an IpAccessControlList

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_ip_access_control_list import ApiV2010AccountSipSipIpAccessControlList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that uniquely identifies the resource to udpate.
    friendly_name = "friendly_name_example" # str | A human readable descriptive text, up to 64 characters long.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sip_ip_access_control_list(account_sid, sid, friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_ip_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **sid** | **str**| A 34 character string that uniquely identifies the resource to udpate. |
 **friendly_name** | **str**| A human readable descriptive text, up to 64 characters long. |

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sip_ip_address**
> ApiV2010AccountSipSipIpAccessControlListSipIpAddress update_sip_ip_address(account_sid, ip_access_control_list_sid, sid)



Update an IpAddress resource.

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import ApiV2010AccountSipSipIpAccessControlListSipIpAddress
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    ip_access_control_list_sid = "AL62ECB020842930cc01FFCCfeEe150AC" # str | The IpAccessControlList Sid that identifies the IpAddress resources to update.
    sid = "IP62ECB020842930cc01FFCCfeEe150AC" # str | A 34 character string that identifies the IpAddress resource to update.
    cidr_prefix_length = 1 # int | An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. (optional)
    friendly_name = "friendly_name_example" # str | A human readable descriptive text for this resource, up to 64 characters long. (optional)
    ip_address = "ip_address_example" # str | An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sip_ip_address(account_sid, ip_access_control_list_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_ip_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_sip_ip_address(account_sid, ip_access_control_list_sid, sid, cidr_prefix_length=cidr_prefix_length, friendly_name=friendly_name, ip_address=ip_address)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_sip_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. |
 **ip_access_control_list_sid** | **str**| The IpAccessControlList Sid that identifies the IpAddress resources to update. |
 **sid** | **str**| A 34 character string that identifies the IpAddress resource to update. |
 **cidr_prefix_length** | **int**| An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used. | [optional]
 **friendly_name** | **str**| A human readable descriptive text for this resource, up to 64 characters long. | [optional]
 **ip_address** | **str**| An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today. | [optional]

### Return type

[**ApiV2010AccountSipSipIpAccessControlListSipIpAddress**](ApiV2010AccountSipSipIpAccessControlListSipIpAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_trigger**
> ApiV2010AccountUsageUsageTrigger update_usage_trigger(account_sid, sid)



Update an instance of a usage trigger

### Example

* Basic Authentication (accountSid_authToken):
```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.api_v2010_account_usage_usage_trigger import ApiV2010AccountUsageUsageTrigger
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accountSid_authToken
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account_sid = "AC62ECB020842930cc01FFCCfeEe150AC" # str | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update.
    sid = "UT62ECB020842930cc01FFCCfeEe150AC" # str | The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
    callback_method = "head" # str | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`. (optional)
    callback_url = "callback_url_example" # str | The URL we should call using `callback_method` when the trigger fires. (optional)
    friendly_name = "friendly_name_example" # str | A descriptive string that you create to describe the resource. It can be up to 64 characters long. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_usage_trigger(account_sid, sid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_usage_trigger: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_usage_trigger(account_sid, sid, callback_method=callback_method, callback_url=callback_url, friendly_name=friendly_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_usage_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_sid** | **str**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update. |
 **sid** | **str**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to update. |
 **callback_method** | **str**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional]
 **callback_url** | **str**| The URL we should call using &#x60;callback_method&#x60; when the trigger fires. | [optional]
 **friendly_name** | **str**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional]

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

