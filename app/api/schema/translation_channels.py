from app.api.schema.video_channel import VideoChannelSchemaPublic
from app.api.schema.video_stream import VideoStreamSchema
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship

from app.api.schema.base import SoftDeletionSchema


class TranslationChannelSchema(SoftDeletionSchema):
    class Meta:
        type_ = 'translation_mapping'

    id = fields.Integer(dump_only=True)
    video_stream = fields.Nested(VideoStreamSchema, dump_only=True, exclude=('video_stream',))
    channel = fields.Nested(VideoChannelSchemaPublic, dump_only=True, exclude=('streams',))
    url = fields.String()

    # # Relationships
    # video_stream_id = Relationship(
    #     related_view= 'v1.video_stream_detail',
    #     related_view_kwargs={'video_stream_id': '<video_stream.id>'},
    #     many=False,
    #     type_='video-stream',
    #     schema='VideoStreamSchema'
    # )

    # channel_id = Relationship(
    #     related_view='/video_channel_detail/{id}',
    #     related_view_kwargs={'channel_id': '<channel.id>'},
    #     many=False,
    #     type_='video-channel',
    #     schema='VideoChannelSchema'
    # )
   