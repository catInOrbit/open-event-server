from app.api.schema.translation_channels import TranslationChannelSchema
from app.models.translation_channels import TranslationChannel
from app.models import db
from flask_rest_jsonapi import ResourceList, ResourceRelationship,ResourceDetail

class TranslationChannelsList(ResourceList):
    
    def query(self, view_kwargs):
        """
        Query related channels (transaltions) for specific video stream
        """
        if view_kwargs.get("video_stream_id") and view_kwargs.get("video_channel_id") :
            stream_id = view_kwargs.get("video_stream_id")
            records = self.session.query(TranslationChannel).filter_by(video_stream_id=stream_id).all()
            return records
            
    schema = TranslationChannelSchema
    data_layer = {
        'session': db.session,
        'model': TranslationChannel,
        'methods': {
            "query": query
        },
    }

class TranslationChannelsListPost(ResourceList):
    schema = TranslationChannelSchema
    methods = [
        'POST',
    ]
    data_layer = {
        'session': db.session,
        'model': TranslationChannel,
        'methods': {
        }
    } 

class TranslationChannelsDetail(ResourceDetail):
    schema = TranslationChannelSchema
    data_layer = {
        'session': db.session,
        'model': TranslationChannel,
        'methods': {
        },
    }
    
class TranslationChannelsRelationship(ResourceRelationship):
    schema = TranslationChannelSchema
    data_layer = {
        'session': db.session,
        'model': TranslationChannel,
        'methods': {
        },
    }