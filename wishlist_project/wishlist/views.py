from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('created_at')
    serializer_class = ItemSerializer

    @action(detail=False)
    def markdown(self, request):
        items = self.get_queryset()
        markdown = "## To Do List\n\n"
        for item in items:
            checkbox = "[x]" if item.status else "[ ]"
            markdown += f"- {checkbox} {item.name}\n"
        markdown += "\n%% kanban:settings\n```\n{\"kanban-plugin\":\"list\"}\n```\n%%"
        return Response({"markdown": markdown})