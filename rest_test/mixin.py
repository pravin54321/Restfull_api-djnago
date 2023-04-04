from django.http import HttpResponse
from django.core.serializers import serialize
import json
from django.http import JsonResponse
class SerializerMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        pdict=json.loads(json_data)
        final_list=[]
        for obj in pdict:
            final_list.append(obj['fields'])
        json_data=json.dumps(final_list)
        return json_data    
################################################################
class Json_Response_Mixin(object):
    def render_to_json_response(self,context, **kwargs):
        return JsonResponse(context,**kwargs)           