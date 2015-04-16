try:
    import json
except ImportError:
    import simplejson as json
import urllib

from error import WhitePagesError


def validate_url(result):
    if 'error' in result.keys():
        error_detail = result['error']
        raise WhitePagesError, error_detail


def url_encoder(params):
    encoded_params = urllib.urlencode(params)
    return encoded_params


def return_json(url):
    result_dict = json.load(urllib.urlopen(url))
    return result_dict


def dictIsEmpty(input_dict):
    return bool(input_dict)


def remove_blank_fields(input_dict):
    return dict((k, v) for k, v in input_dict.iteritems() if v is not None)


def add_key(request_dict, white_pages_object):
    request_dict['api_key'] = white_pages_object.__api_key
    return request_dict


def query(request_object, white_pages_object):
    url = request_object.url()
    input_dict = remove_blank_fields(request_object.to_dict)
    if dictIsEmpty(input_dict):
        error_detail = 'You have not entered any valid arguments'
        raise WhitePagesError, error_detail
    input_dict = add_key(input_dict, white_pages_object)
    url_query = url + url_encoder(input_dict)
    json_blob = return_json(url_query)
    validate_url(json_blob)
    json_result = json_blob['results']
    result = []
    for pr in json_result:
        result.append(request_object.whitePagesObject(pr))
    return result