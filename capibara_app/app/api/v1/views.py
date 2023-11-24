from api.models import Capibara
from api.v1.serializers import CapibaraSerializer
from django.http import HttpResponse
from openpyxl import Workbook
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CapibaraXlsxView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def export_to_excel(self, capibara_queryset):
        wb = Workbook()
        ws = wb.active
        ws.title = "Capibara"
        headers = ['id', 'capibara_format', 'capibara_slang', 'capibara_phrases']
        ws.append(headers)
        for capibara in capibara_queryset:
            ws.append(
                [capibara.id, capibara.capibara_format, capibara.capibara_slang, ', '.join(capibara.capibara_phrases)]
            )
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="capibara.xlsx"'
        wb.save(response)
        return response

    def parse_capibaras(self, queryset):
        if not queryset:
            return Response({"status": "not available"})
        return self.export_to_excel(queryset)

    def get_capibara(self, capibara_id):
        capibara = Capibara.objects.filter(id=capibara_id).all()
        return self.parse_capibaras(capibara)

    def get_capibaras_over_slang(self, capibara_slang):
        capibaras = Capibara.objects.filter(capibara_slang=capibara_slang).all()
        return self.parse_capibaras(capibaras)

    def get(self, request, format=None):
        capibara_id = request.GET.get('id')
        capibara_slang = request.GET.get('capibara_slang')
        if capibara_id:
            return self.get_capibara(capibara_id)
        if capibara_slang:
            return self.get_capibaras_over_slang(capibara_slang)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CapibaraView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        if Capibara.objects.filter(id=data['id']).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        serializer = CapibaraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
