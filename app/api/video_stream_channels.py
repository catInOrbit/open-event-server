from app.models.video_stream import VideoStreamChannel
from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship


class VideoStreamChannelsList(ResourceList):
    
    def query(self, view_kwargs):
        """
        Query related channels (transaltions) for specific video stream
        """
        if view_kwargs.get("video_stream_id") and view_kwargs.get("video_channel_id") :
            q_ = self.session.query(VideoStreamChannel)
            
            
            
            

    
    schema = VideoStreamChannelschema
    decorators = (jwt_optional,)
    data_layer = {
        'session': db.session,
        'model': VideoStreamChannel,
        'methods': {
            {"query": query}
        },
    }

class VideoStreamChannelsListPost(ResourceList)
