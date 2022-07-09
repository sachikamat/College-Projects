from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer


from GAN.GAN_backend import run_script

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
      run_script.cleaner()
      file_serializer = FileSerializer(data=request.data)
      # print("tori   _____"+str(request.data))

      if file_serializer.is_valid():
          file_serializer.save()
          base64_data = run_script.main()
          data = {'image_base64':base64_data}
          data.update(file_serializer.data)
          return Response(data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
