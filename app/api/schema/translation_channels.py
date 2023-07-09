from app.api.schema.video_channel import VideoChannelSchemaPublic
from app.api.schema.video_stream import VideoStreamSchema
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema


# class TranslationChannelSchema(SoftDeletionSchema):
#     class Meta:
#         type_ = 'translation-channels'

#     id = fields.Integer(dump_only=True)
#     video_stream = fields.Nested(VideoStreamSchema, dump_only=True)
#     channel = fields.Nested(VideoChannelSchemaPublic, dump_only=True)
#     url = fields.String()

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

from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship


class TranslationChannelSchema(Schema):
    id = fields.Str(dump_only=True)
    video_stream_id = fields.Integer(required=True, load_only=True)
    channel_id = fields.Integer(required=True, load_only=True)
    name = fields.String(required=True)
    url = fields.String(required=True)

    video_stream = fields.Relationship(
        self_view="v1.translation_stream",
        self_view_kwargs={"translation_channel_identifier": "<identifier>"},
        related_view="v1.video_stream_detail",
        related_view_kwargs={"id": "<id>"},
        schema="VideoStreamSchema",
        type_="video_stream",
    )

    channel = fields.Relationship(
        self_view="v1.translation_channel",
        self_view_kwargs={"translation_channel_identifier": "<identifier>"},
        related_view="v1.video_channel_detail",
        related_view_kwargs={"id": "<id>"},
        schema="VideoChannelSchema",
        type_="video_channel",
    )

    class Meta:
        type_ = "translation_channel"
        strict = True