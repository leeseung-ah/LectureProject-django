from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, exceptions
from . import serializers
from lectures.models import Lecture, CalculatedLecture

from django.core.files.storage import default_storage
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import boto3
from django.conf import settings

from .models import Video


class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = serializers.VideoSerializer(videos, many=True)
        return Response(serializer.data)


# 해당하는 강의의 모든 비디오를 가져오는 클래스
class LectureVideoList(APIView):
    def get(self, request, lectureId):
        lecture = Lecture.objects.get(LectureId=lectureId)
        cal_lec = CalculatedLecture.objects.get(lecture=lecture)
        videos = Video.objects.filter(calculatedLecture=cal_lec)
        serializer = serializers.VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, requset, lectureId):
        lecture = Lecture.objects.get(LectureId=lectureId)
        cal_lec = CalculatedLecture.objects.get(lecture=lecture)
        serializer = serializers.VideoSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save(calculatedLecture=cal_lec)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class oneVideo(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = serializers.VideoSerializer(video)
        return Response(serializer.data)

    def post(self, request, pk):
        video = self.get_object(pk)
        serializer = serializers.VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # video 파일을 받아서 s3에 저장하고 그 url을 db에 저장하고 videolenth를 계산해서 저장하는 클래스


class UploadVideoView(APIView):
    def post(self, request, lectureId):
        file = request.FILES.get("file")
        if file:
            lecture = Lecture.objects.get(LectureId=lectureId)
            cal_lec = CalculatedLecture.objects.get(lecture=lecture)
            # Upload the file to S3
            s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_ACCESS_KEY_ID,
            )
            file_name = default_storage.save(file.name, file)
            file_path = os.path.join(default_storage.location, file_name)
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            s3.upload_file(file_path, bucket_name, file_name)

            # Get the video URL from S3
            video_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"

            # Calculate the video length
            video_clip = VideoFileClip(file_path)
            video_length = video_clip.duration
            video_clip.close()

            # Save the video information in the database
            video = Video(
                title="Title",
                description="Description",
                videoFile=video_url,
                videoLength=video_length,
                calculatedLecture=cal_lec,
            )
            video.save()

            # Return the serialized video object
            serializer = serializers.VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "File not provided"}, status=status.HTTP_400_BAD_REQUEST
        )
